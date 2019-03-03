#Imports
from  urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup
from model import Episode

favListDefault = ["Boruto: Naruto Next Generations", "Steins;Gate 0", "Boku no Hero Academia", "Dorei-ku The Animation"]
class adapter():
    def __init__(self, epList = [], favList=None):
        if favList is None:
            favList = favListDefault
        self.name = "gogoanime"
        self.epList = epList
        self.favList = favList
        self.url = "http://www3.gogoanime.tv"  # Looks for the newest anime

    def getNewest(self, n=10):
        html = self.crawlSite()
        episodeHtmls = self.extractEpisodesHtml(html)
        episodeList = [self.extractEpisode(episodeHtml) for episodeHtml in episodeHtmls]
        return episodeList  # Return the array of animes
        
    def crawlSite(self):
        request = Request(self.url, headers={
            'User-Agent': 'Mozilla/5.0'})  # Requests the page using a false header because scraping 403's
        client = urlopen(request)  # Opens a connection to the page
        html = client.read()  # Reads the html and stores it as html
        client.close()  # Closes connection to save memory
        return html

    def extractEpisodesHtml(self, html):
        page_soup = soup(html, "html.parser")  # Uses soup to parse the html data
        episodeHtml = page_soup.find("ul", {"class": "items"}).find_all("li")  # Finds the animes
        return episodeHtml
    
    def extractEpisode(self,episodeHtml):
        details = episodeHtml.findAll('p')
        name = details[0].text.replace(u'\ufeff', '')
        episode = details[1].text.replace(u'\ufeff', '').split(" ")[1]
        link = details[0].a['href']
        img = episodeHtml.find('img')['src']

        return Episode(name, episode, link, img)


