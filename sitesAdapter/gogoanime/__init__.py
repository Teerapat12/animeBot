# Coded by TheSpaceCowboy
# Date: 24/11/17
# Github: https://github.com/thespacecowboy42534

#Imports
from  urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup

# Path hack.
import sys, os
sys.path.append("D:/ProjectFolder/chatbot/alertAdapter")
import lineApi


class Anime(): # Storing the anime data

    def __init__(self,title,link): # Intialises the anime class
        
        self.title = title # Title
        self.link = link # Link

class Episode():
    def __init__(self, name, ep):  # Intialises the anime class
        self.name = name  # Title
        self.ep = ep  # Link
        #self.at =


class adapter():

    def __init__(self, epList = [],favList= ["Boruto: Naruto Next Generations","Steins;Gate 0","Boku no Hero Academia","Dorei-ku The Animation"]):
        self.name = "gogoanime"
        self.epList = epList
        self.favList = favList

    def getNewest(self, n=10):
        url = "http://www3.gogoanime.tv"  # Looks for the newest anime

        request = Request(url, headers={
            'User-Agent': 'Mozilla/5.0'})  # Requests the page using a false header because scraping 403's
        client = urlopen(request)  # Opens a connection to the page
        html = client.read()  # Reads the html and stores it as html
        client.close()  # Closes connection to save memory

        page_soup = soup(html, "html.parser")  # Uses soup to parse the html data
        animes = page_soup.find("ul", {"class": "items"}).find_all("li")  # Finds the animes

        aAnimes = []  # Placeholder for the array of animes

        for anime in animes:  # For every anime found
            details = anime.findAll('p')
            name = details[0].text.replace(u'\ufeff', '')
            episode = details[1].text.replace(u'\ufeff', '').split(" ")[1]
            ep = Episode(name, episode)

            if any(ep.name == e.name and ep.ep == e.ep for e in self.epList):
                pass
            else:
                #if ep.name in self.favList: # Uncomment if only want to the notification of fav anime
                lineApi.sendMessage(ep.name+" episode "+ep.ep+" has arrived on Gogoanime")

                if any(ep.name == e.name for e in self.epList): # Already has the anime but different episode
                    self.epList = [e for e in self.epList if e.name != ep.name] # Remove the old one first then add the new one
                self.epList.append(ep)

        return self.epList  # Return the array of animes


