from datetime import datetime

TOKEN = ''
students = []
name = 'Zikrulla Rakhmatov'

profMuhammadAftab = {
    "TOKEN" : "7853061299:AAHRa1YTkxENch8-Bzcrjuui7J-cxBND13I",
    "students" : ['Zikrulla Rakhmatov', 'Tolibjon']
}
profJaydipMehta = {
    'TOKEN' : '8136431001:AAFj_QR82MMDwy9Pdke0uirE_4T6C-6tqtI',
    'students' : ['Rakhmonjon', 'Adhambek']
}

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(name in profMuhammadAftab["students"])

def sendMessage(token, msg):
    print(token, msg)


match name:
    case name if name in profMuhammadAftab["students"]:
        sendMessage(profMuhammadAftab["TOKEN"], name)
    case name if name in profJaydipMehta["students"]:
        sendMessage(profJaydipMehta["TOKEN"], name)




