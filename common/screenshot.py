# -*- coding: utf-8 -*-
import os
import subprocess
import sys

from PIL import Image
from io import StringIO

from common.auto_adb import auto_adb

SCREENSHOT_WAY = 0
adb = auto_adb()


def pull_screenshot():
    """
    获取屏幕截图，目前有 0 1 2 3 四种方法，未来添加新的平台监测方法时，
    可根据效率及适用性由高到低排序
    """
    global SCREENSHOT_WAY
    if 1 <= SCREENSHOT_WAY <= 3:
        process = subprocess.Popen(
            adb.adb_path + ' shell screencap -p',
            shell=True, stdout=subprocess.PIPE)
        binary_screenshot = process.stdout.read()
        if SCREENSHOT_WAY == 2:
            binary_screenshot = binary_screenshot.replace(b'\r\n', b'\n')
        elif SCREENSHOT_WAY == 1:
            binary_screenshot = binary_screenshot.replace(b'\r\r\n', b'\n')
        return Image.open(StringIO(binary_screenshot))
    elif SCREENSHOT_WAY == 0:
        adb.run('shell screencap -p /sdcard/screenshot.png')
        adb.run('pull /sdcard/screenshot.png .')
        return Image.open('./screenshot.png')


def check_screenshot():
    """
    检查获取截图的方式
    """
    global SCREENSHOT_WAY
    if os.path.isfile('screenshot.png'):
        try:
            os.remove('screenshot.png')
        except Exception:
            pass
    if SCREENSHOT_WAY < 0:
        print('暂不支持当前设备')
        sys.exit()
    try:
        im = pull_screenshot()
        im.load()
        im.close()
        print('采用方式 {} 获取截图'.format(SCREENSHOT_WAY))
    except Exception:
        SCREENSHOT_WAY -= 1
        check_screenshot()
