# -*- coding: UTF-8 -*-

import s_autoinstall
json = s_autoinstall.ImportModule("json")
httpServer = s_autoinstall.ImportModule("http.server")
socketserver = s_autoinstall.ImportModule("socketserver")
s_log = s_autoinstall.ImportModule("s_log")

# 数据
httpdata = {"kaka": "卡卡"}

# http消息监听类
class HttpResquestHandler(httpServer.BaseHTTPRequestHandler):

    def do_GET(self):
        s_log.zLog("HttpResquest.do_GET:收到请求")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(httpdata).encode())

    def do_POST(self):
        s_log.zLog("HttpResquest.do_POST:收到请求")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(httpdata).encode())

# socket消息监听类
class SocketResquestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            s_log.zLog("SocketResquestHandler.handle:卡卡 ")
            # while True:
            #     self.data=self.request.recv(1024)
            #     print("{} send:".format(self.client_address),self.data)
            #     if not self.data:
            #         print("connection lost")
            #         break
            #     self.request.sendall(self.data.upper())
        except Exception as e:
            s_log.zError("SocketResquestHandler.handle:连接断开 | " + str(e))
        finally:
            self.request.close()

    def setup(self):
        s_log.zLog("SocketResquestHandler.setup:建立连接 | " + str(self.client_address))

    def finish(self):
        s_log.zLog("SocketResquestHandler.finish:结束连接")

def createHttpServer(address):
    '''
    创建http监听
    :param address: 地址信息 (host:str, port:int)
    '''
    s_log.zLog("createHttpServer:开启http server")
    server = httpServer.HTTPServer(address, HttpResquestHandler)
    server.serve_forever()
    

def createTcpServer(address):
    '''
    创建socket监听
    :param address: 地址信息 (host:str, port:int)
    '''
    s_log.zLog("createTcpServer:开启socket server")
    server = socketserver.TCPServer(address, SocketResquestHandler)
    server.serve_forever()