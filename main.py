# -*- coding: utf-8 -*-
import uuid
import time
from common.auto_adb import auto_adb
from common.config import open_accordant_config
from common.qiniu_upload import upload_to_qiniu
from common.screenshot import pull_screenshot
from common.serverchan import send_server_chan_msg

adb = auto_adb()
conf = open_accordant_config('config/default.json')


def lock_screen():
    adb.run('shell input keyevent 26')  # press power


def unlock_screen():
    adb.run('shell input keyevent 82')  # press menu
    adb.swipe(100, 500, 600, 500, 200)  # swipe to unlock


def start_activity():
    cmd = 'shell am start -n {activity}'.format(
        activity='com.huawei.hrandroidframe/com.huawei.hrattend.IHRPunchCardActivity',
    )
    adb.run(cmd)


def upload(localfile, key):
    upload_to_qiniu(conf['qiniu']['access_key'], conf['qiniu']['secret_key'], 'saberlion', localfile, key)


unlock_screen()
adb.run("shell service call connectivity 33 i32 1 s16 text")
time.sleep(5)
start_activity()
time.sleep(2)
pull_screenshot()

key = 'screenshot{rand}.png'.format(rand=uuid.uuid1())
upload('screenshot.png', key)
lock_screen()
content = '![pic]({url})'.format(url='http://saberlion.u.qiniudn.com/' + key)
send_server_chan_msg(conf['serverchan']['sckey'], "Test", content)
