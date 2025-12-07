"""
Flask Video Feed with 500 Real Images & Working Like/Comment
"""
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import config
from models.user import User
from data.sample_data import create_sample_videos
from algorithms.ranker import VideoRanker

app = Flask(__name__)
CORS(app)

# Initialize
video_db = create_sample_videos()
current_user = User(99, "You", "😊")
user_follows = set()

current_user.interests = ["#python", "#tech", "#coding", "#travel", "#fitness", "#music"]
current_user.follow(1)
current_user.follow(2)
current_user.follow(3)
current_user.follow(4)

ranker = VideoRanker(current_user)
all_videos = video_db.get_all()
ranked_videos = ranker.rank_videos(all_videos)

@app.route('/')
def index():
    videos = []
    for v in ranked_videos:
        videos.append({
            'id': v.id,
            'creator_id': v.creator_id,
            'title': v.title,
            'creator_name': v.creator_name,
            'creator_avatar': v.creator_avatar,
            'image_url': v.image_url,
            'description': v.description,
            'views': v.get_formatted_views(),
            'likes': v.likes,
            'comments': v.comments,
            'shares': v.shares,
            'hashtags': v.hashtags,
            'category': v.category,
            'time': v.get_relative_time(),
        })
    return render_template('index.html', videos=videos, total=len(videos))

@app.route('/api/like/<int:video_id>', methods=['POST'])
def like_video(video_id):
    video = video_db.get_video(video_id)
    if video:
        is_liked = video.toggle_like(current_user.id)
        global ranked_videos
        all_vids = video_db.get_all()
        ranked_videos = ranker.rank_videos(all_vids)
        return jsonify({'success': True, 'liked': is_liked, 'likes': video.likes})
    return jsonify({'success': False}), 404

@app.route('/api/comment/<int:video_id>', methods=['POST'])
def comment_video(video_id):
    data = request.get_json()
    comment_text = data.get('text', 'Great content!')
    
    video = video_db.get_video(video_id)
    if video:
        video.add_comment(current_user.id, comment_text)
        global ranked_videos
        all_vids = video_db.get_all()
        ranked_videos = ranker.rank_videos(all_vids)
        return jsonify({'success': True, 'comments': video.comments})
    return jsonify({'success': False}), 404

@app.route('/api/share/<int:video_id>', methods=['POST'])
def share_video(video_id):
    video = video_db.get_video(video_id)
    if video:
        video.add_share()
        global ranked_videos
        all_vids = video_db.get_all()
        ranked_videos = ranker.rank_videos(all_vids)
        return jsonify({'success': True, 'shares': video.shares})
    return jsonify({'success': False}), 404

@app.route('/api/refresh', methods=['POST'])
def refresh_feed():
    global ranked_videos
    all_vids = video_db.get_all()
    ranked_videos = ranker.rank_videos(all_vids)
    return jsonify({'success': True})

@app.route('/api/follow/<int:creator_id>', methods=['POST'])
def follow_creator(creator_id):
    global ranked_videos
    if creator_id in user_follows:
        user_follows.remove(creator_id)
        current_user.following.discard(creator_id)
        following = False
    else:
        user_follows.add(creator_id)
        current_user.following.add(creator_id)
        following = True
    
    # Re-rank videos after follow/unfollow to boost creator's videos
    all_vids = video_db.get_all()
    ranked_videos = ranker.rank_videos(all_vids)

    return jsonify({'success': True, 'following': following})

@app.route('/api/videos')
def get_videos_api():
    if user_follows:
        videos_filtered = [v for v in video_db.get_all() if v.creator_id in user_follows]
        if not videos_filtered:
            videos_filtered = video_db.get_all()
    else:
        videos_filtered = video_db.get_all()

    # Serialize videos for JSON
    def serialize(v):
        return {
            'id': v.id,
            'creator_id': v.creator_id,
            'creator_name': v.creator_name,
            'creator_avatar': v.creator_avatar,
            'title': v.title,
            'description': v.description,
            'duration': v.duration,
            'thumbnail_emoji': v.thumbnail_emoji,
            'hashtags': v.hashtags,
            'category': v.category,
            'image_url': v.image_url,
            'views': v.get_formatted_views(),
            'likes': v.likes,
            'comments': v.comments,
            'shares': v.shares,
            'time': v.get_relative_time(),
            'created_at': v.created_at.isoformat() if v.created_at else None,
        }
    return jsonify([serialize(v) for v in videos_filtered])

@app.route('/api/ranked-feed')
def get_ranked_feed():
    """Get current ranked feed after interactions"""
    def serialize(v):
        return {
            'id': v.id,
            'creator_id': v.creator_id,
            'creator_name': v.creator_name,
            'creator_avatar': v.creator_avatar,
            'title': v.title,
            'description': v.description,
            'duration': v.duration,
            'thumbnail_emoji': v.thumbnail_emoji,
            'hashtags': v.hashtags,
            'category': v.category,
            'image_url': v.image_url,
            'views': v.get_formatted_views(),
            'likes': v.likes,
            'comments': v.comments,
            'shares': v.shares,
            'time': v.get_relative_time(),
            'created_at': v.created_at.isoformat() if v.created_at else None,
        }
    
    return jsonify({'success': True, 'videos': [serialize(v) for v in ranked_videos]})

@app.route('/api/shuffle', methods=['POST'])
def shuffle_and_rank():
    """Shuffle videos and re-rank by likes and follows"""
    global ranked_videos
    
    # Get all videos and re-rank them
    all_vids = video_db.get_all()
    ranked_videos = ranker.rank_videos(all_vids)
    
    # Serialize and return
    def serialize(v):
        return {
            'id': v.id,
            'creator_id': v.creator_id,
            'creator_name': v.creator_name,
            'creator_avatar': v.creator_avatar,
            'title': v.title,
            'description': v.description,
            'duration': v.duration,
            'thumbnail_emoji': v.thumbnail_emoji,
            'hashtags': v.hashtags,
            'category': v.category,
            'image_url': v.image_url,
            'views': v.get_formatted_views(),
            'likes': v.likes,
            'comments': v.comments,
            'shares': v.shares,
            'time': v.get_relative_time(),
            'created_at': v.created_at.isoformat() if v.created_at else None,
        }
    
    return jsonify({'success': True, 'videos': [serialize(v) for v in ranked_videos]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
