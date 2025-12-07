import json
import os
from datetime import datetime, timedelta
import random
from models.video import Video
from data.video_db import VideoDatabase

def create_sample_videos():
    json_path = os.path.join(os.path.dirname(__file__), 'sample.json')
    with open(json_path, 'r') as f:
        data = json.load(f)

    db = VideoDatabase()
    vid_id = 1

    avatar_map = {
        'travel': '✈️',
        'food': '👨\u200d🍳',
        'sports': '🏅',
        'nature': '🌿',
        'cities': '🏙️',
        'people': '📸',
    }

    for card in data:
        if not card.get('available', False):
            continue

        creator_name = card['category'].capitalize() + " Creator"
        creator_avatar = avatar_map.get(card['category'], '😊')

        hashtags = card.get('tags', [])
        views = random.randint(1000, 1000000)
        likes = int(views * random.uniform(0.02, 0.08))
        comments = int(views * random.uniform(0.001, 0.005))
        shares = int(views * random.uniform(0.0005, 0.002))
        created_at = datetime.now() - timedelta(hours=random.randint(1, 720))

        video = Video(
            vid_id,
            vid_id,  # For simplicity creator_id == vid_id, or you can map creators
            creator_name,
            creator_avatar,
            card.get('title', 'No Title'),
            card.get('description', ''),
            random.randint(10, 300),
            "📹",
            hashtags,
            card.get('category', '')
        )
        video.image_url = card.get('image', '')
        video.views = views
        video.likes = likes
        video.comments = comments
        video.shares = shares
        video.created_at = created_at

        db.add_video(video)
        vid_id += 1

    return db
