# Coded by TheSpaceCowboy
# Date: 24/11/17
# Github: https://github.com/thespacecowboy42534

#Imports
import bs4 
from  urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
import re

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

    def __init__(self, epList= ["Boruto: Naruto Next Generations","Steins;Gate 0","Boku no Hero Academia"]):
        self.name = "gogoanime"
        self.epList = epList



    def searchResults(self, term): # Searches gogoanime for the name of the anime

        url = "http://www3.gogoanime.tv//search.html?keyword="+term # Looks for the anime by a given name

        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # Requests the page using a false header because scraping 403's
        client = urlopen(request) # Opens a connection to the page
        html = client.read() # Reads the html and stores it as html
        client.close() # Closes connection to save memory

        page_soup = soup(html,"html.parser") # Uses soup to parse the html data
        animes = page_soup.find("ul",{"class":"items"}).find_all("li") # Finds the animes

        if(len(animes) == 0 ): # If no anime are found return nothing

            return

        aAnimes = [] # Placeholder for the array of animes

        for anime in animes: # For every anime found

           aAnimes.append( Anime(anime.a["title"],"http://www3.gogoanime.tv/"+anime.a["href"].replace("/category/","")+"-episode-")) # Create an anime array

        return aAnimes # Return the array of animes

    def getDLLink(self, dlpage): # Returns the download link for the animes
        request = Request(dlpage, headers={'User-Agent': 'Mozilla/5.0'}) # Requests the page using a false header because scraping 403's
        client = urlopen(request) # Opens a connection to the page
        html = client.read() # Opens a connection to the page
        client.close() # Closes connection to save memory

        page_soup = soup(html,"html.parser") # Uses soup to parse the html data
        dl = page_soup.find("div",{"class":"download-anime"}) # Finds the animes

        if(dl is None): # If no links are found return None

            return

        href = dl.a["href"] # href is set to the download link
        return href # Return link

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

            if any(ep.name == e for e in self.epList):
                pass
                # Check if new episode or not
            else:
                print("NEW anime arrived")
                print(len(ep.name))
                print(ep.name)
                print(ep.ep)

                self.epList.append(ep)


        return aAnimes  # Return the array of animes


