# -*- coding: UTF-8 -*-

import os
from importlib import import_module

def ImportModule(mName):
    '''
    导入库，自动安装
    :param mName: 模块名 str
    :return: 模块对象 any
    '''
    try:
        return import_module(mName)
    except:
        print("install module | {}".format(mName))
        os.system("python --version")
        os.system("pip -V")
        result = os.system("python -m pip install {}".format(mName))
        if result == 0:
            return import_module(mName)