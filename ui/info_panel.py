"""
Premium Video information panel - CENTERED & BEAUTIFUL
"""
import tkinter as tk
import config

class InfoPanel:
    """Panel for displaying video information - Premium design"""
    
    def __init__(self, parent):
        # Main container (centered)
        container = tk.Frame(parent, bg=config.COLORS["bg_primary"])
        container.pack(fill=tk.X, pady=15, padx=20)
        
        # Card frame
        self.frame = tk.Frame(
            container,
            bg=config.COLORS["bg_card"],
            relief=tk.RAISED,
            bd=1
        )
        self.frame.pack(fill=tk.X, padx=40)
        
        # Content frame with padding
        content = tk.Frame(self.frame, bg=config.COLORS["bg_card"])
        content.pack(fill=tk.X, padx=20, pady=15)
        
        # Title (centered)
        self.title = tk.Label(
            content,
            text="",
            font=config.FONTS["title_small"],
            bg=config.COLORS["bg_card"],
            fg=config.COLORS["accent"],
            wraplength=600,
            justify=tk.CENTER
        )
        self.title.pack(fill=tk.X, pady=(0, 12))
        
        # Creator info (centered)
        creator_frame = tk.Frame(content, bg=config.COLORS["bg_card"])
        creator_frame.pack(fill=tk.X, pady=8)
        
        # Use pack with side=TOP for centering effect
        info_inner = tk.Frame(creator_frame, bg=config.COLORS["bg_card"])
        info_inner.pack()
        
        self.avatar = tk.Label(
            info_inner,
            text="",
            font=("Helvetica", 22),
            bg=config.COLORS["bg_card"]
        )
        self.avatar.pack(side=tk.LEFT, padx=5)
        
        creator_text_frame = tk.Frame(info_inner, bg=config.COLORS["bg_card"])
        creator_text_frame.pack(side=tk.LEFT, padx=5)
        
        self.creator_name = tk.Label(
            creator_text_frame,
            text="",
            font=config.FONTS["body_medium"],
            bg=config.COLORS["bg_card"],
            fg=config.COLORS["text_primary"]
        )
        self.creator_name.pack()
        
        self.time_label = tk.Label(
            creator_text_frame,
            text="",
            font=config.FONTS["body_small"],
            bg=config.COLORS["bg_card"],
            fg=config.COLORS["text_secondary"]
        )
        self.time_label.pack()
        
        # Divider line
        divider = tk.Frame(content, bg=config.COLORS["accent"], height=1)
        divider.pack(fill=tk.X, pady=10)
        
        # Stats (centered)
        self.stats = tk.Label(
            content,
            text="",
            font=config.FONTS["body_medium"],
            bg=config.COLORS["bg_card"],
            fg=config.COLORS["accent"],
            justify=tk.CENTER
        )
        self.stats.pack(fill=tk.X, pady=8)
        
        # Hashtags (centered)
        self.hashtags = tk.Label(
            content,
            text="",
            font=config.FONTS["body_small"],
            bg=config.COLORS["bg_card"],
            fg=config.COLORS["accent_light"],
            wraplength=600,
            justify=tk.CENTER
        )
        self.hashtags.pack(fill=tk.X, pady=8)
    
    def display_video(self, video):
        """Display video info"""
        self.title.config(text=video.title)
        self.avatar.config(text=video.creator_avatar)
        self.creator_name.config(text=video.creator_name)
        self.time_label.config(text=f"📅 {video.get_relative_time()}")
        
        # Format stats nicely
        stats_text = f"👁️ {video.get_formatted_views()}   ❤️ {video.likes:,}   💬 {video.comments:,}   ↗️ {video.shares}"
        self.stats.config(text=stats_text)
        
        # Hashtags
        hashtags_text = " · ".join(video.hashtags) if video.hashtags else "No hashtags"
        self.hashtags.config(text=hashtags_text)
