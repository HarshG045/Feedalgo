"""
Premium Video display panel - CENTERED & BEAUTIFUL
"""
import tkinter as tk
import config

class VideoPanel:
    """Panel for displaying video - Premium centered design"""
    
    def __init__(self, parent):
        # Outer container for centering
        outer_frame = tk.Frame(parent, bg=config.COLORS["bg_primary"])
        outer_frame.pack(fill=tk.BOTH, expand=False, pady=20, padx=20)
        
        # Inner card frame (centered)
        self.frame = tk.Frame(
            outer_frame,
            bg=config.COLORS["bg_card"],
            relief=tk.RAISED,
            bd=1
        )
        self.frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=15)
        
        # Set minimum height
        self.frame.config(height=250)
        self.frame.pack_propagate(False)
        
        # Placeholder with premium styling
        placeholder_container = tk.Frame(self.frame, bg=config.COLORS["bg_card"])
        placeholder_container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Video icon
        icon = tk.Label(
            placeholder_container,
            text="📹",
            font=("Helvetica", 60),
            bg=config.COLORS["bg_card"],
            fg=config.COLORS["accent"]
        )
        icon.pack(pady=10)
        
        # Main text
        title_text = tk.Label(
            placeholder_container,
            text="Video Section",
            font=config.FONTS["title_medium"],
            bg=config.COLORS["bg_card"],
            fg=config.COLORS["text_primary"]
        )
        title_text.pack(pady=5)
        
        # Subtitle
        subtitle = tk.Label(
            placeholder_container,
            text="Ready for video integration",
            font=config.FONTS["body_small"],
            bg=config.COLORS["bg_card"],
            fg=config.COLORS["text_secondary"]
        )
        subtitle.pack(pady=2)
        
        # Description
        description = tk.Label(
            placeholder_container,
            text="Add your video player or content here",
            font=config.FONTS["body_small"],
            bg=config.COLORS["bg_card"],
            fg=config.COLORS["text_tertiary"]
        )
        description.pack(pady=5)
    
    def display_video(self, video):
        """Display video - Currently empty"""
        pass
