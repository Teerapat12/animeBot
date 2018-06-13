
import requests
import json

url = 'https://api.line.me/v2/bot/message/push'
#token = 'Fnn01pWTPEV1ZBSbcg0pddcXvrJGxOeio9w2nmBW6Oy'
token = 'xThFevCj5CuPYVD5cOO3dlstprs8qWE1ZJV1V3QBwdmqf1xy+/axP+tQ4ZoijT51l2buIZbVxs9RfVjkIDLT13qecRLggnkJzIWCEwEVvqqq+Ke0YbucqNYfzod1pjci38BAZEUlfdGubmhjmTS0XwdB04t89/1O/w1cDnyilFU='
headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Authorization': 'Bearer '+ token
  }
myId = "U41e301775679179f8b254b947baf9836"
msg = 'ทดสอบภาษาไทย'

def sendData(data):
    d = json.dumps({
        "to": myId,
        "messages": data
    })
    r = requests.post(url, headers=headers, data=d)  # ส่งข้อมูล

def sendMessage(msg):
    sendData([{'type':'text','text':msg}])


def sendImg(msg,img):
    sendData([{'type':'text', 'text':msg},{'type':'image','originalContentUrl': img, 'previewImageUrl':img}])


def sendEpisode(ep):
    print("HEY")
    sendImg(ep.name + " episode " + ep.ep + " has arrived on " + ep.webName, ep.img)
    sendMessage(ep.url + ep.link)
    #sendData({"type":"flex","altText":strMsg,"contents":flexMsg},{"type":"text","text":ep.url+ep.link})


def ep2Str(ep):
    return ep.name+" episode " + str(ep.ep)

def ep2Data(ep):
    print(ep.link)
    return {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": ep.img,
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
                "type": "uri",
                "uri": ep.url+ep.link
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": ep.name,
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "md",
                    "contents": [

                        {
                            "type": "text",
                            "text": "Episode "+str(ep.ep),
                            "size": "sm",
                            "color": "#999999",
                            "margin": "md",
                            "flex": 0
                        }
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "uri",
                        "label": "WATCH",
                        "uri": ep.url+ep.link
                    }
                },
                {
                    "type": "spacer",
                    "size": "sm"
                }
            ],
            "flex": 0
        }
    }