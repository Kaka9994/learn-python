# -*- coding: UTF-8 -*-

import s_autoinstall
re = s_autoinstall.ImportModule("re")
math = s_autoinstall.ImportModule("math")
datetime = s_autoinstall.ImportModule("datetime")
s_filetool = s_autoinstall.ImportModule("s_filetool")

class pri_Log:
    def __init__(self):
        # 限制行数
        self.__limit = 500
        # 当前文件流对象
        self.__curStream = None
        # 当前长度
        self.__curLen = 0
        # 日志队列
        self.__logQueue = []
        # 输出日志
        self.__rootPath = None

        self.__isRunning = False

    @property
    def limit(self):
        return self.__limit

    def outLog(self, s):
        '''
        输出日志
        :param s: 日志 str
        '''
        if self.__rootPath == None:
            self.__rootPath = s_filetool.getExePath()
            self.__rootPath = self.__rootPath if self.__rootPath == None else "."
        
        dateStr = self.formatDate(None, None)
        tmpStr = dateStr + "| " + s + "\n"

        print(tmpStr)
        self.__logQueue.append(tmpStr)

        self.__output()

    def formatDate(self, d = None, fmt = None):
        '''
        格式化时间
        :param d: 时间对象 datetime
        :param fmt: 格式 str
        :return: 时间字符串 str
        '''
        # 处理时间
        date = d if d != None else datetime.datetime.now()
        out = fmt if fmt != None else "yyyy-MM-dd hh:mm:ss"

        # 格式
        obj = {
            "M+": date.month,                       # 月份
            "d+": date.day,                         # 日
            "h+": date.hour,                        # 小时
            "m+": date.minute,                      # 分
            "s+": date.second,                      # 秒
            "q+": math.floor((date.month + 2) / 3), # 季度
            "S": date.microsecond                   # 毫秒
        }

        # 年
        yyyy = re.findall(r"y+", out)
        if len(yyyy) > 0:
            out = out.replace(yyyy[0], str(date.year)[4 - len(yyyy[0]):])

        for k in obj:
            tmp = re.findall(k, out)
            if len(tmp) > 0:
                out = out.replace(tmp[0], str(obj[k]) if len(tmp[0]) == 1 else str("00" + str(obj[k]))[len(str(obj[k])):])

        return out

    def __output(self):
        '''
        输出
        '''
        if self.__isRunning:
            return

        self.__isRunning = True

        def func():
            if len(self.__logQueue) <= 0:
                self.__isRunning = False
                return
            
            s = self.__logQueue.pop(0)

            try:
                # 创建流
                if self.__curStream == None:
                    filedatestr = self.formatDate(None, "yyyy-MM-dd hh·mm·ss")
                    self.__curStream = open(self.__rootPath + "/LOG " + filedatestr + ".txt", 'a')
                    self.__curLen = 0

                # 写入文件
                self.__curStream.write(s)
                self.__curLen += 1
            except:
                return

            # 文件超长，关闭文件流，下次创建新文件
            if self.limit < self.__curLen:
                self.__curStream.close()
                self.__curStream = None
                
            func()

        func()

gLog = pri_Log()

# 日志
def zLog(s):
    gLog.outLog("[LOG]   " + s)

# 警告
def zWarn(s):
    gLog.outLog("[Warn]  " + s)

# 异常
def zError(s):
    gLog.outLog("[Error] " + s)