"""Video ranking algorithm - DSA O(n log n)"""

import config


class VideoRanker:
	"""DSA: Multi-factor ranking"""

	def __init__(self, current_user):
		self.current_user = current_user

	def calculate_score(self, video):
		"""Calculate relevance score - O(1)"""
		age_hours = video.get_age_hours()
		recency = 1.0 / (1 + config.TIME_DECAY_FACTOR * age_hours)

		engagement = video.likes + (video.comments * 2) + (video.shares * 3)
		engagement_norm = engagement / (engagement + config.ENGAGEMENT_NORMALIZATION)

		relationship = 2.5 if video.creator_id in self.current_user.following else 0.8

		hashtag_match = 0.0
		matching = len(set(video.hashtags) & set(self.current_user.interests))
		if matching > 0:
			hashtag_match = min(matching / 2.0, 1.0)

		return (
			recency * 0.35
			+ engagement_norm * 0.35
			+ relationship * 0.20
			+ hashtag_match * 0.10
		)

	def rank_videos(self, videos):
		"""Rank videos - O(n log n)"""
		scored = [(self.calculate_score(v), v) for v in videos]
		ranked = sorted(scored, key=lambda x: x[0], reverse=True)
		return [v for _, v in ranked]
