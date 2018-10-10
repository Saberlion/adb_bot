# -*- coding: utf-8 -*-
import requests


def send_server_chan_msg(sckey, title, desp):
    url = 'https://sc.ftqq.com/{key}.send'.format(key=sckey)
    d = {'text': title, 'desp': desp}
    r = requests.post(url, data=d)
    return r.text
