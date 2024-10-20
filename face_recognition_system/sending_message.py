import requests

class SendMessage:

    def __init__(self):
        pass

    def sendMessage(token, chat_id, msg):
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
        r = requests.get(url)
