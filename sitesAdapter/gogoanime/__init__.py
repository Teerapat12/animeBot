# Coded by TheSpaceCowboy
# Date: 24/11/17
# Github: https://github.com/thespacecowboy42534

#Imports
from  urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup

class Anime(): # Storing the anime data

    def __init__(self,title,link): # Intialises the anime class
        
        self.title = title # Title
        self.link = link # Link

class Episode():
    def __init__(self, name, ep, link, img):  # Intialises the anime class
        self.name = name  # Title
        self.ep = ep  # Episode
        self.link = link # Link
        self.url = "http://www3.gogoanime.tv"
        self.webName = "Gogoanime"
        self.img = img


class adapter():

    def __init__(self, epList = [],favList= ["Boruto: Naruto Next Generations","Steins;Gate 0","Boku no Hero Academia","Dorei-ku The Animation"]):
        self.name = "gogoanime"
        self.epList = epList
        self.favList = favList
        self.url = "http://www3.gogoanime.tv"  # Looks for the newest anime
        
    def crawlSite(self):
        request = Request(self.url, headers={
            'User-Agent': 'Mozilla/5.0'})  # Requests the page using a false header because scraping 403's
        client = urlopen(request)  # Opens a connection to the page
        html = client.read()  # Reads the html and stores it as html
        client.close()  # Closes connection to save memory
        return html

    def getNewest(self, n=10):
        html = self.crawlSite()

        page_soup = soup(html, "html.parser")  # Uses soup to parse the html data
        animes = page_soup.find("ul", {"class": "items"}).find_all("li")  # Finds the animes

        episodeList = []  # Placeholder for the array of animes

        for anime in animes:  # For every anime found
            ep = self.extractEpisode(anime)
            episodeList.append(ep)
            
        return episodeList  # Return the array of animes
    
    def extractEpisode(animeText):
        details = anime.findAll('p')
        name = details[0].text.replace(u'\ufeff', '')
        episode = details[1].text.replace(u'\ufeff', '').split(" ")[1]
        link = details[0].a['href']
        img = anime.find('img')['src']

        return Episode(name, episode, link, img)


