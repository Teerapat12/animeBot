class Episode:
    def __init__(self, name, ep, link, img):  # Intialises the anime class
        self.name = name  # Title
        self.ep = ep  # Episode
        self.link = link # Link
        self.url = "http://www3.gogoanime.tv"
        self.webName = "Gogoanime"
        self.img = img

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and self.ep == other.ep
        else:
            return False
