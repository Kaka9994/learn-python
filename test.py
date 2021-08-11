# -*- coding: UTF-8 -*-

import os
import re
import sys
import math
import json
import time
import zipfile
import datetime

# 添加工具类
sys.path.append(os.path.dirname(sys.argv[0]) + "/utils")
import p_utils

p_utils.s_log.zLog("哈哈 -- ")

# kk = p_utils.s_net.netGet(
#     "https://dev.jiliguala.com",
#     "api/game/resource/byGameId",
#     { "cocosEnv": "prod", "gameId": "LCDS0875" }
# )
# kk1 = json.loads(kk) if kk != None else ""

# kk = p_utils.s_filetool.loadJSON("/Users/jason/Downloads/kkk.json")

# kk = [
#     "Name\tStart\tDuration\tTime Format\tType\tDescription",
#     "标记 00\t0:00:200\t0:00.000\tdecimal\tCue\t",
#     "标记 01\t0:01:044\t0:00.000\tdecimal\tCue\t"
# ]
# p_utils.s_filetool.outputCSV(kk, "/Users/jason/Downloads/kkk.csv")

# p_utils.s_server.createHttpServer(("localhost", 8765))

# p_utils.s_log.zLog("呵呵1")

# p_utils.s_filetool.removeFile()

# open(os.path.dirname(__file__) + "/123.txt", 'a')

# a = 1
# print("呵呵")

# b = input("输入")
# print("啦啦 -- " + str(b))

# c = ("卡卡"
#      "什么")
# print(c)

# (d, e) = divmod(7, 2)
# print(d, e)

# f = open("test.sh")
# for line in f:
#     print("哈哈 -- " + line)

# arr = ["a", "b", "c"]
# for i, v in enumerate(arr):
#     print(i, v)

# o = dict(a=1)
# o["b"] = 2
# print(o)