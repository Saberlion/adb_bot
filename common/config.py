# -*- coding: utf-8 -*-
import json


def open_accordant_config(path):
    """
    调用配置文件
    """
    with open(path, 'r') as f:
        return json.load(f)
