import os
import importlib
import threading
import time
from alertAdapter import lineApi

# Init
d = 'sitesAdapter'
moduleNames = [d + "." + o for o in os.listdir(d)
               if os.path.isdir(os.path.join(d, o)) and "__pycache__" not in o]

modules = map(importlib.import_module, moduleNames)

adapters = [m.adapter() for m in modules]

oldEpList = []
def oldEpisodeList():
  return oldEpList # None for now. 

def isNewEpisode(episode,oldEpList):
  return not any(episode.name == e.name and episode.ep == e.ep for e in oldEpList)

def handleNewEpisode(episode):
  lineApi.sendEpisode(episode)
  oldEpList.append(episode)

# Should check for update every n minutes
def checkUpdate():
    # Step 1 call all the .getNewest(n) and getall the names of the movies.
    episodes = adapters[0].getNewest()
    # Step 2 Get the list of episode that the bot already told us.
    oldEpList = oldEpisodeList()
    # Step 3 Check if the newest if newer than the old one.
    for episode in episodes:
        if isNewEpisode(episode,oldEpList):
            handleNewEpisode(episode) 
    


def startChecking():
  threading.Timer(10.0, checkUpdate).start()
  print("Checking")


while True:
    checkUpdate()
    time.sleep(180)
