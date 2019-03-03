import pickle

class HistoryManager:
	def __init__(self, repository):
		self.repository = repository

	def addEpisodeToHistory(self, episode):
		self.repository.saveHistory(episode)

	def loadHistory(self):
		return self.repository.loadHistory()

class FileRepository:
	def __init__(self, file_path):
		self.file_path = file_path
		self.episodes = self.loadHistory()

	def saveHistory(self, episode):
		self.episodes.append(episode)
		with open(self.file_path, 'wb') as handle:
			pickle.dump(self.episodes, handle)

	def loadHistory(self):
		try:
			with open(self.file_path, 'rb') as handle:
				self.episodes = pickle.load(handle)
				return self.episodes
		except:
			print("Error. Either no history or error. I'm too lazy to make check for now.")
			self.episodes = []
			return self.episodes
