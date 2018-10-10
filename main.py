# -*- coding: utf-8 -*-
import uuid

from common.auto_adb import auto_adb
from common.config import open_accordant_config
from common.qiniu_upload import upload_to_qiniu
from common.screenshot import pull_screenshot
from common.serverchan import send_server_chan_msg

adb = auto_adb()
conf = open_accordant_config('config/default.json')


def unlock_screen():
    adb.run('shell input keyevent 26')  # press power
    adb.swipe(100, 500, 600, 500, 200)  # swipe to unlock


def start_activity():
    cmd = 'shell am start -n {activity}'.format(
        activity='com.huawei.hrandroidframe/com.huawei.hrattend.IHRPunchCardActivity',
    )
    adb.run(cmd)


def upload(localfile, key):
    upload_to_qiniu(conf['qiniu']['access_key'], conf['qiniu']['secret_key'], 'saberlion', localfile, key)


unlock_screen()
start_activity()
pull_screenshot()
key = 'screenshot{rand}.png'.format(rand=uuid.uuid1())
upload('screenshot.png', key)
content = '![pic]({url})'.format(url='http://saberlion.u.qiniudn.com/'+key)
send_server_chan_msg(conf['serverchan']['sckey'], "Test", content)
