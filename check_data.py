import json
import os
from data.sample_data import create_sample_videos

# Check sample.json first
json_path = os.path.join('data', 'sample.json')
with open(json_path, 'r') as f:
    data = json.load(f)

available = [v for v in data if v.get('available', False)]
print(f'📊 Sample.json Stats:')
print(f'   Total videos in JSON: {len(data)}')
print(f'   Available videos: {len(available)}')
print(f'   Categories: {set(v.get("category") for v in available)}')

# Now create videos and check for duplicates
print(f'\n🔍 Creating videos from sample_data.py...')
db = create_sample_videos()
all_videos = db.get_all()

print(f'   Total videos created: {len(all_videos)}')

# Check for duplicate IDs
video_ids = [v.id for v in all_videos]
unique_ids = set(video_ids)
print(f'   Unique video IDs: {len(unique_ids)}')

if len(video_ids) != len(unique_ids):
    print(f'   ⚠️ WARNING: Found duplicate IDs!')
    from collections import Counter
    duplicates = [id for id, count in Counter(video_ids).items() if count > 1]
    print(f'   Duplicate IDs: {duplicates}')
else:
    print(f'   ✅ All video IDs are unique!')

# Check for duplicate titles
titles = [v.title for v in all_videos]
unique_titles = set(titles)
print(f'   Unique titles: {len(unique_titles)}')

if len(titles) != len(unique_titles):
    print(f'   ⚠️ WARNING: Found duplicate titles!')
    from collections import Counter
    dup_titles = [t for t, count in Counter(titles).items() if count > 1]
    print(f'   First 3 duplicate titles: {dup_titles[:3]}')

print(f'\n📝 First 10 video IDs:')
for i in range(min(10, len(all_videos))):
    v = all_videos[i]
    print(f'   {v.id}. {v.title[:50]} (Category: {v.category})')

print(f'\n📝 Last 10 video IDs:')
for i in range(max(0, len(all_videos) - 10), len(all_videos)):
    v = all_videos[i]
    print(f'   {v.id}. {v.title[:50]} (Category: {v.category})')
