import os
import importlib
import threading
import time


# Init
d = 'sitesAdapter'
moduleNames = [d + "." + o for o in os.listdir(d)
               if os.path.isdir(os.path.join(d, o)) and "__pycache__" not in o]

modules = map(importlib.import_module, moduleNames)

adapters = [m.adapter() for m in modules]

# Should check for update every n minutes
def checkUpdate():
    adapters[0].getNewest()
    # Step 1 call all the .getNewest(n) and getall the names of the movies.



    # Step 2 Check if the newest if newer than the old one.
    # Step 3 If it is, call the alertUser() function.


def startChecking():
  threading.Timer(10.0, checkUpdate).start()
  print("Checking")


while True:
    checkUpdate()
    time.sleep(180)
