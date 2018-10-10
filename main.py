from common.auto_adb import auto_adb
from common.screenshot import check_screenshot, pull_screenshot
from qiniu import Auth

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
