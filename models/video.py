"""Video model"""
from datetime import datetime, timedelta

class Video:
    def __init__(self, video_id, creator_id, creator_name, creator_avatar,
                 title, description, duration, thumbnail_emoji,
                 hashtags=None, category="general"):
        self.id = video_id
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.creator_avatar = creator_avatar
        self.title = title
        self.description = description
        self.duration = duration
        self.thumbnail_emoji = thumbnail_emoji
        self.image_url = ""  # ← NEW
        self.category = category
        self.hashtags = hashtags or []
        self.views = 0
        self.likes = 0
        self.comments = 0
        self.shares = 0
        self.bookmarks = 0
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.liked_by = set()
        self.commented_by = set()
        self.comment_list = []  # ← NEW
    
    def toggle_like(self, user_id):
        if user_id in self.liked_by:
            self.liked_by.remove(user_id)
            self.likes = max(0, self.likes - 1)
            return False
        else:
            self.liked_by.add(user_id)
            self.likes += 1
            return True
    
    def add_comment(self, user_id, text):
        self.comments += 1
        self.commented_by.add(user_id)
        self.comment_list.append({
            'user_id': user_id,
            'text': text,
            'timestamp': datetime.now()
        })
    
    def add_share(self):
        self.shares += 1
    
    def get_age_hours(self):
        delta = datetime.now() - self.created_at
        return delta.total_seconds() / 3600
    
    def get_relative_time(self):
        delta = datetime.now() - self.created_at
        seconds = delta.total_seconds()
        if seconds < 60:
            return "just now"
        elif seconds < 3600:
            return f"{int(seconds / 60)}m ago"
        elif seconds < 86400:
            return f"{int(seconds / 3600)}h ago"
        else:
            return f"{int(seconds / 86400)}d ago"
    
    def get_formatted_views(self):
        if self.views >= 1000000:
            return f"{self.views // 1000000}M"
        elif self.views >= 1000:
            return f"{self.views // 1000}K"
        return str(self.views)
