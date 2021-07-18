# import requests
# from requests.api import get
# import telebot
# from vedis import Vedis
# from dateutil import parser as dparser


# db = Vedis('./db')
# bot = telebot.TeleBot("1439647072:AAEcztMUbtppCVCidGegPzs6_opr-kANfBQ")


# db['lastid'] = 754404
# def get_updates():
#     """Get a latest article from dev.to"""
#     r = requests.get("https://dev.to/api/articles/latest", params={"per_page": 1}).json()

#     id = str(r[0]["id"])
#     db['lastid'] = r[0]["id"]

#     return r, id

# last_article = db['lastid'].decode()

# interesting_tags = ["python", "golang"]

# while True:
#     body, id = get_updates()
#     print(int(id) != int(last_article))
#     # print(type(id))
#     print(last_article)

#     if int(id) != int(last_article):
#         if "discuss" in body[0]["tags"]:
#             pass
#         elif body[0]["tags"] in interesting_tags:
#             text = f"""<b>#Interesting tags</b>
# <b>{body[0]['title']}</b>\n
# {body[0]['description']}\n
# <a href="{body[0]['url']}">🔗 Link</a>"""
#         else:
#             text = f"""<b>{body[0]['title']}</b>\n
# {body[0]['description']}\n
# <a href="{body[0]['url']}">🔗 Link</a>"""
#         msg = bot.send_message("@teclightcom", text, parse_mode="html")
#         print(body[0]["id"])
