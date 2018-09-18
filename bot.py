import requests
import datetime
import os

token = os.environ.get('TOKEN',None)
api_url = "https://api.telegram.org/bot{}/".format(token)


def get_updates(offset=None, timeout=30):
    resp = requests.get(api_url + 'getUpdates', {'timeout': timeout, 'offset': offset})
    result_json = resp.json()['result']
    return result_json

def send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    method = 'sendMessage'
    resp = requests.post(api_url + method, params)
    return resp


if __name__ == '__main__':
    new_offset = None

    while True:
        updates = get_updates(new_offset)

        for upd in updates:
            if ('new_chat_member' in upd["message"].keys()):
                send_message(upd['message']['chat']['id'],"buongiornissimo!!")


        print(updates)

        if (len(updates)>0):
            new_offset = updates[-1]['update_id'] + 1
