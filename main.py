"""
Video Feed Simulator - Premium Main Application
"""
import tkinter as tk
from tkinter import ttk
import config
from models.user import User
from data.video_db import VideoDatabase
from data.sample_data import create_sample_videos
from algorithms.ranker import VideoRanker
from ui.video_panel import VideoPanel
from ui.info_panel import InfoPanel
from ui.controls_panel import ControlsPanel

class VideoFeedApp:
    """Main application - Premium design"""
    
    def __init__(self, root):
        self.root = root
        self.root.title(config.WINDOW_TITLE)
        self.root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.root.configure(bg=config.COLORS["bg_primary"])
        
        # Initialize data
        self.video_db = create_sample_videos()
        self.current_user = User(99, "You", "😊")
        
        self.current_user.interests = ["#python", "#tech", "#coding", "#travel", "#fitness", "#music"]
        self.current_user.follow(1)
        self.current_user.follow(2)
        self.current_user.follow(3)
        self.current_user.follow(4)
        
        # Initialize ranker
        self.ranker = VideoRanker(self.current_user)
        
        # Get and rank videos
        all_videos = self.video_db.get_all()
        self.ranked_videos = self.ranker.rank_videos(all_videos)
        self.current_idx = 0
        self.liked_videos = set()
        
        self.create_ui()
    
    def create_ui(self):
        """Create premium UI"""
        
        main_container = tk.Frame(self.root, bg=config.COLORS["bg_primary"])
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # ===== HEADER - Premium design =====
        header = tk.Frame(main_container, bg=config.COLORS["bg_secondary"], height=120)
        header.pack(fill=tk.X, pady=0)
        header.pack_propagate(False)
        
        # Header content frame (centered)
        header_content = tk.Frame(header, bg=config.COLORS["bg_secondary"])
        header_content.pack(fill=tk.X, padx=40, pady=15)
        
        # Title and refresh on same line
        header_top = tk.Frame(header_content, bg=config.COLORS["bg_secondary"])
        header_top.pack(fill=tk.X, pady=10)
        
        title = tk.Label(
            header_top,
            text="🎬 Video Feed Simulator",
            font=config.FONTS["title_large"],
            bg=config.COLORS["bg_secondary"],
            fg=config.COLORS["accent"]
        )
        title.pack(side=tk.LEFT)
        
        refresh_btn = tk.Button(
            header_top,
            text="🔄 REFRESH",
            font=config.FONTS["body_medium"],
            bg=config.COLORS["accent"],
            fg=config.COLORS["bg_primary"],
            activebackground=config.COLORS["accent_light"],
            border=0,
            cursor="hand2",
            padx=20,
            pady=8,
            command=self.refresh_feed
        )
        refresh_btn.pack(side=tk.RIGHT)
        
        # Subtitle
        subtitle = tk.Label(
            header_content,
            text="DSA Ranking Algorithm | 100 Videos | Real-time Feed Personalization",
            font=config.FONTS["body_small"],
            bg=config.COLORS["bg_secondary"],
            fg=config.COLORS["text_secondary"]
        )
        subtitle.pack(fill=tk.X)
        
        # Divider
        divider = tk.Frame(header, bg=config.COLORS["accent"], height=2)
        divider.pack(fill=tk.X)
        
        # ===== CONTENT AREA (Scrollable) =====
        content_frame = tk.Frame(main_container, bg=config.COLORS["bg_primary"])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create canvas with scrollbar
        canvas = tk.Canvas(
            content_frame,
            bg=config.COLORS["bg_primary"],
            highlightthickness=0
        )
        scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=config.COLORS["bg_primary"])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Mousewheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create panels
        self.video_panel = VideoPanel(scrollable_frame)
        self.info_panel = InfoPanel(scrollable_frame)
        
        callbacks = {
            "like": self.like_video,
            "comment": self.comment_video,
            "share": self.share_video,
            "next": self.next_video,
            "previous": self.previous_video,
        }
        self.controls_panel = ControlsPanel(scrollable_frame, callbacks)
        
        # ===== FOOTER =====
        footer = tk.Frame(main_container, bg=config.COLORS["bg_secondary"], height=60)
        footer.pack(fill=tk.X, pady=0)
        footer.pack_propagate(False)
        
        # Footer content
        footer_content = tk.Frame(footer, bg=config.COLORS["bg_secondary"])
        footer_content.pack(expand=True, padx=40)
        
        self.footer_label = tk.Label(
            footer_content,
            text="",
            font=config.FONTS["body_small"],
            bg=config.COLORS["bg_secondary"],
            fg=config.COLORS["text_secondary"]
        )
        self.footer_label.pack()
        
        self.display_video()
    
    def display_video(self):
        """Display current video"""
        if not self.ranked_videos:
            return
        
        video = self.ranked_videos[self.current_idx % len(self.ranked_videos)]
        
        self.video_panel.display_video(video)
        self.info_panel.display_video(video)
        self.controls_panel.update_like_button(video.id in self.liked_videos)
        self.footer_label.config(
            text=f"Video {self.current_idx + 1} of {len(self.ranked_videos)} | Scroll to explore more"
        )
    
    def refresh_feed(self):
        """Re-rank and refresh the entire feed"""
        all_videos = self.video_db.get_all()
        self.ranked_videos = self.ranker.rank_videos(all_videos)
        self.current_idx = 0
        self.liked_videos.clear()
        self.display_video()
    
    def like_video(self):
        """Like current video"""
        video = self.ranked_videos[self.current_idx % len(self.ranked_videos)]
        is_liked = video.toggle_like(self.current_user.id)
        
        if is_liked:
            self.liked_videos.add(video.id)
        else:
            self.liked_videos.discard(video.id)
        
        self.display_video()
        all_videos = self.video_db.get_all()
        self.ranked_videos = self.ranker.rank_videos(all_videos)
    
    def comment_video(self):
        """Comment on video"""
        video = self.ranked_videos[self.current_idx % len(self.ranked_videos)]
        video.add_comment(self.current_user.id, "Great video!")
        self.display_video()
        all_videos = self.video_db.get_all()
        self.ranked_videos = self.ranker.rank_videos(all_videos)
    
    def share_video(self):
        """Share video"""
        video = self.ranked_videos[self.current_idx % len(self.ranked_videos)]
        video.add_share()
        self.display_video()
        all_videos = self.video_db.get_all()
        self.ranked_videos = self.ranker.rank_videos(all_videos)
    
    def next_video(self):
        """Next video"""
        self.current_idx += 1
        if self.current_idx >= len(self.ranked_videos):
            self.current_idx = 0
        self.display_video()
    
    def previous_video(self):
        """Previous video"""
        if self.current_idx > 0:
            self.current_idx -= 1
        else:
            self.current_idx = len(self.ranked_videos) - 1
        self.display_video()

def main():
    root = tk.Tk()
    app = VideoFeedApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
