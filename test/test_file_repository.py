# content of test_sample.py
from model import Episode
from history.historyManager import FileRepository
import os

test_history_file_location = "./history_test.txt"

def remove_file_if_exists(file_location):
    if os.path.exists(file_location):
        os.remove(file_location)
    else:
        print("The file does not exist")

remove_file_if_exists(test_history_file_location)

def test_file_repository_load_empty():
    fileRepository = FileRepository(test_history_file_location)
    loadedEpisode = fileRepository.loadHistory()

    print(loadedEpisode)
    assert [] == loadedEpisode

def test_file_repository_save_episode():
    newEpisode = Episode("A", 1, "google.com", "google.com/img")
    fileRepository = FileRepository(test_history_file_location)
    fileRepository.saveHistory(newEpisode)

    loadedEpisodes = fileRepository.loadHistory()

    assert loadedEpisodes == [newEpisode]


test_file_repository_load_empty()
test_file_repository_save_episode()
