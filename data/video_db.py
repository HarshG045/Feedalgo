"""Video database with hashtag indexing"""

from models.video import Video


class VideoDatabase:
	"""In-memory video database with indexing"""

	def __init__(self):
		self.videos = {}
		self.by_hashtag = {}
		self.by_creator = {}
		self.by_category = {}

	def add_video(self, video):
		"""Add video - O(1)"""
		self.videos[video.id] = video

		if video.creator_id not in self.by_creator:
			self.by_creator[video.creator_id] = []
		self.by_creator[video.creator_id].append(video.id)

		if video.category not in self.by_category:
			self.by_category[video.category] = []
		self.by_category[video.category].append(video.id)

		for tag in video.hashtags:
			if tag not in self.by_hashtag:
				self.by_hashtag[tag] = []
			self.by_hashtag[tag].append(video.id)

	def get_video(self, video_id):
		return self.videos.get(video_id)

	def get_by_hashtag(self, hashtag):
		video_ids = self.by_hashtag.get(hashtag, [])
		return [self.videos[vid] for vid in video_ids if vid in self.videos]

	def get_by_creator(self, creator_id):
		video_ids = self.by_creator.get(creator_id, [])
		return [self.videos[vid] for vid in video_ids if vid in self.videos]

	def get_all(self):
		return list(self.videos.values())

	def search_by_title(self, query):
		results = []
		for video in self.videos.values():
			if query.lower() in video.title.lower():
				results.append(video)
		return results
