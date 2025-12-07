"""User model"""


class User:
	"""User data model"""

	def __init__(self, user_id, username, avatar):
		self.id = user_id
		self.username = username
		self.avatar = avatar

		self.followers = set()
		self.following = set()
		self.interests = []
		self.watch_history = []

	def add_follower(self, user_id):
		self.followers.add(user_id)

	def follow(self, user_id):
		self.following.add(user_id)

	def add_interest(self, hashtag):
		if hashtag not in self.interests:
			self.interests.append(hashtag)
