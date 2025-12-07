"""
Premium Control buttons panel - CENTERED & BEAUTIFUL
"""
import tkinter as tk
import config

class ControlsPanel:
    """Panel with action and navigation buttons - Premium design"""
    
    def __init__(self, parent, callbacks):
        # Main container
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
        
        # Content padding
        content = tk.Frame(self.frame, bg=config.COLORS["bg_card"])
        content.pack(fill=tk.X, padx=15, pady=12)
        
        self.callbacks = callbacks
        
        # ===== ACTION BUTTONS (3 columns) =====
        actions_frame = tk.Frame(content, bg=config.COLORS["bg_card"])
        actions_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Like button
        self.like_btn = tk.Button(
            actions_frame,
            text="❤️ Like",
            font=config.FONTS["body_medium"],
            bg=config.COLORS["bg_secondary"],
            fg=config.COLORS["text_primary"],
            activebackground=config.COLORS["danger"],
            activeforeground="white",
            border=0,
            cursor="hand2",
            height=2,
            command=callbacks.get("like")
        )
        self.like_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Comment button
        comment_btn = tk.Button(
            actions_frame,
            text="💬 Comment",
            font=config.FONTS["body_medium"],
            bg=config.COLORS["bg_secondary"],
            fg=config.COLORS["text_primary"],
            activebackground=config.COLORS["accent"],
            activeforeground=config.COLORS["bg_primary"],
            border=0,
            cursor="hand2",
            height=2,
            command=callbacks.get("comment")
        )
        comment_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Share button
        share_btn = tk.Button(
            actions_frame,
            text="↗️ Share",
            font=config.FONTS["body_medium"],
            bg=config.COLORS["bg_secondary"],
            fg=config.COLORS["text_primary"],
            activebackground=config.COLORS["success"],
            activeforeground=config.COLORS["bg_primary"],
            border=0,
            cursor="hand2",
            height=2,
            command=callbacks.get("share")
        )
        share_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Divider
        divider = tk.Frame(content, bg=config.COLORS["accent"], height=1)
        divider.pack(fill=tk.X, pady=10)
        
        # ===== NAVIGATION BUTTONS (2 columns) =====
        nav_frame = tk.Frame(content, bg=config.COLORS["bg_card"])
        nav_frame.pack(fill=tk.X)
        
        # Previous button
        prev_btn = tk.Button(
            nav_frame,
            text="⬆️ Previous",
            font=config.FONTS["body_medium"],
            bg=config.COLORS["accent"],
            fg=config.COLORS["bg_primary"],
            activebackground=config.COLORS["accent_light"],
            border=0,
            cursor="hand2",
            height=2,
            command=callbacks.get("previous")
        )
        prev_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Next button
        next_btn = tk.Button(
            nav_frame,
            text="⬇️ Next",
            font=config.FONTS["body_medium"],
            bg=config.COLORS["accent"],
            fg=config.COLORS["bg_primary"],
            activebackground=config.COLORS["accent_light"],
            border=0,
            cursor="hand2",
            height=2,
            command=callbacks.get("next")
        )
        next_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
    
    def update_like_button(self, is_liked):
        """Update like button appearance"""
        if is_liked:
            self.like_btn.config(bg=config.COLORS["danger"], fg="white")
        else:
            self.like_btn.config(bg=config.COLORS["bg_secondary"], fg=config.COLORS["text_primary"])
