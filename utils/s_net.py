# -*- coding: UTF-8 -*-

import s_autoinstall
requests = s_autoinstall.ImportModule("requests")
s_log = s_autoinstall.ImportModule("s_log")

def netGet(host, path = None, params = None):
    '''
    net get
    :param host: 域名 str
    :param path: 路径 str
    :param params: 参数 {[key: string]: any}
    :return: 数据 str
    '''
    return httpGet(host + ('/' + path if path != None else ''), params)

def netPost(host, path = None, params = None):
    '''
    net post
    :param host: 域名 str
    :param path: 路径 str
    :param params: 参数 {[key: string]: any}
    :return: 数据 str
    '''
    return httpPost(host + ('/' + path if path != None else ''), params)

def download(url, target):
    '''
    下载
    :param url: 连接路径 str
    :param target: 目标路径 str
    :return: 是否操作成功
    '''
    s_log.zLog("download:开始请求 | " + str(url))

    # 请求
    try:
        req = requests.get(
            url = url,
            timeout = 5
        )
    except requests.exceptions.ConnectTimeout:
        s_log.zError("download:请求超时")
        return False
    except:
        s_log.zError("download:请求失败 | 异常")
        return False

    # 失败
    if req.status_code != 200:
        s_log.zError("download:请求失败 | code = " + str(req.status_code))
        return False

    # 保存文件
    open(target, 'wb').write(req.content)

    s_log.zLog("download:请求结束 | " + str(url))
    return True

def httpGet(url, params = None):
    '''
    http get
    :param url: 连接路径 str
    :param params: 参数 {[key: string]: any}
    :return: 数据 str
    '''
    url += '' if params == None else '?' + getParamsUrl(params)
    return httpRequest(url, None, True)

def httpPost(url, params = None):
    '''
    http post
    :param url: 连接路径 str
    :param params: 参数 {[key: string]: any}
    :return: 数据 str
    '''
    return httpRequest(url, params, False)

def httpRequest(url, params = None, isget = True):
    '''
    http request
    :param url: 连接路径 str
    :param params: 参数 {[key: string]: any}
    :return: 数据 str
    '''
    s_log.zLog("httpRequest:开始请求 | " + str(url))

    # 请求头
    headers = {
        "Content-Type": "application/json",
        "Authorization": ("Basic OGI5NGE1MjAxMzQxNGY2MmI1Njk4NTA0OWYxNWM3Z"
                          "GU6MzZhMzEzMGVmNzYyNDU0MDk4OTJhYTIyZDc5OWYyZjI="),
        "GGHeaderMap": ("XXB3ZNeSGVXfutsahrMz8/xIHUOzEGpkVqZWm19vew1asmpgMG"
                        "z1gDdosikPL6GcPm+bCoYmw3blhVyHvYanpy6qqXfmKeP9+nLD"
                        "1Frsp2mlDCqkZ5ZdWccdyitN0A/Ez13lxwPug5TAD8WgihnHjT"
                        "XOpcvU7WzVYVLhf9ZR8X9yA+xcrYby2l9zxxwCMe+3UXnfBsbY"
                        "DgHVGGEqg7/S8vROitYegP2hITGxTnO35aS/iAOK")
    }

    # 请求
    try:
        if isget:
            req = requests.get(
                url = url,
                headers = headers,
                timeout = 5
            )
        else:
            req = requests.post(
                url = url,
                headers = headers,
                params = params,
                timeout = 5
            )
    except requests.exceptions.ConnectTimeout:
        s_log.zError("httpRequest:请求超时")
        return None
    except:
        s_log.zError("httpRequest:请求失败 | 异常")
        return None

    # 失败
    if req.status_code != 200:
        s_log.zError("httpRequest:请求失败 | code = " + str(req.status_code))
        return None

    s_log.zLog("httpRequest:请求结束 | " + str(url))

    return req.content

def getParamsUrl(params):
    '''
    获取参数字符串
    :param params: 参数 {[key: string]: any}
    :return: 参数字符串 str
    '''
    if params == None:
        s_log.zError("getParamsUrl:无效参数 None")
        return ""

    t = type(params)
    
    if t == dict:
        paramlist = []
        for k in params:
            v = params[k]
            tt = type(v)
            vstr = v
            if tt == int or tt == float or tt == bool:
                vstr = str(v)
            elif tt == list or tt == dict:
                vstr = str(v)
            paramlist.append(str(k) + '=' + vstr)
        return '&'.join(paramlist)
    elif t == list:
        paramlist = []
        for i, v in enumerate(params):
            paramlist.append(str(i) + '=' + str(v))
        return '&'.join(paramlist)
    else:
        s_log.zError("getParamsUrl:无效参数 " + str(t))
        return ""