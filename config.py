"""
Configuration and constants - PREMIUM VERSION
"""

COLORS = {
    "bg_primary": "#0a0e27",
    "bg_secondary": "#151b33",
    "bg_tertiary": "#1f2847",
    "bg_card": "#1a2332",
    "accent": "#00d4ff",
    "accent_light": "#00f0ff",
    "danger": "#ff3b30",
    "success": "#34c759",
    "text_primary": "#ffffff",
    "text_secondary": "#a0a9b8",
    "text_tertiary": "#7a8a9a",
}

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 1600

WINDOW_TITLE = "🎬 Video Feed Simulator - Premium"

FONTS = {
    "title_huge": ("Segoe UI", 36, "bold"),
    "title_large": ("Segoe UI", 28, "bold"),
    "title_medium": ("Segoe UI", 20, "bold"),
    "title_small": ("Segoe UI", 16, "bold"),
    "body_large": ("Segoe UI", 13),
    "body_medium": ("Segoe UI", 11),
    "body_small": ("Segoe UI", 9),
    "mono": ("Courier New", 10),
}

RANKING_WEIGHTS = {
    "recency": 0.35,
    "engagement": 0.35,
    "relationship": 0.20,
    "hashtag_match": 0.10,
}

MAX_ACTIVITIES_PER_USER = 100
CACHE_CAPACITY = 10
TIME_DECAY_FACTOR = 0.1
ENGAGEMENT_NORMALIZATION = 100

# Premium styling
CARD_SHADOW = True
CORNER_RADIUS = 10
PADDING = 20
BORDER_WIDTH = 1
