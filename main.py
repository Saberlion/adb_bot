# -*- coding: utf-8 -*-
from common.auto_adb import auto_adb
from common.screenshot import  pull_screenshot


adb = auto_adb()


def unlock_screen():
    adb.run('shell input keyevent 26')  # press power
    adb.swipe(100, 500, 600, 500)  # swipe to unlock


def start_activity():
    cmd = 'shell am start -n {activity}'.format(
        activity='com.huawei.hrandroidframe/com.huawei.hrattend.IHRPunchCardActivity',
    )
    adb.run(cmd)


start_activity()
pull_screenshot()
