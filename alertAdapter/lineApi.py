import requests

url = 'https://notify-api.line.me/api/notify'
token = 'Fnn01pWTPEV1ZBSbcg0pddcXvrJGxOeio9w2nmBW6Oy'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

msg = 'ทดสอบภาษาไทย'

def sendMessage(msg):
    r = requests.post(url, headers=headers, data={'message': msg})
    return True


def sendImg(msg,img):
    r = requests.post(url, headers=headers, data={'message': msg,'imageFullsize':img,'imageThumbnail':img})
    return True

def sendEpisode(ep):
    sendImg(ep.name + " episode " + ep.ep + " has arrived on "+ ep.webName, ep.img)
    sendMessage(ep.url + ep.link)
