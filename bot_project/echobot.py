import time
import json
import urllib
import requests

token_number="1654945708:AAFjB84JqCnBISkNne6R-IFqC3vyDifCdo8"
user_name="thunder123"
URL="https://api.telegram.org/bot{}/".format(token_number)


def get_url(url):
    file=requests.get(url)
    content=file.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js=json.loads(content)
    return js


def get_updates(offset=None):
    url=URL+"etupdates?timeout=100"
    if offset!=None:
        url+="&offset={}".format(offset)
    updates=get_json_from_url(url)
    return updates


def get_last_update_id(updates):
    updates_list = []
    for i in updates["result"]:
        updates_list.append(int(i["update_id"]))
    return max(updates_list)


def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            send_message(text, chat)
        except Exception as e:\
            print(e)


def get_last_chat_id_and_text(updates):
    num_updates=len(updates["result"])
    last_update=num_updates-1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text,chat):
    text = urllib.parse.quote_plus(text)
    url=URL+"sendMessage?text={}&chat_id={}".format(text,chat)
    get_url(url)


def main_fun():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__=='__main__':
    main_fun()