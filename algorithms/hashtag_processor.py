"""Hashtag processing"""


class HashtagProcessor:
	"""Handle hashtag operations"""

	@staticmethod
	def filter_by_hashtags(videos, hashtags):
		"""Filter videos by hashtags"""
		filtered = []
		hashtag_set = set(hashtags)
		for video in videos:
			if set(video.hashtags) & hashtag_set:
				filtered.append(video)
		return filtered

	@staticmethod
	def get_popular_hashtags(videos, limit=10):
		"""Get trending hashtags"""
		hashtag_count = {}
		for video in videos:
			for tag in video.hashtags:
				hashtag_count[tag] = hashtag_count.get(tag, 0) + 1

		sorted_tags = sorted(hashtag_count.items(), key=lambda x: x[1], reverse=True)
		return [tag for tag, _ in sorted_tags[:limit]]
