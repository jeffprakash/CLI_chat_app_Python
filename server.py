import socket
import threading

class Servernode:
    def __init__(self):
        self.node=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        port_and_ip=('127.0.0.1',12345)
        self.node.bind(port_and_ip)
        self.node.listen(5)
        self.connections,addr=self.node.accept()

    def send_sms(self,sms):
        self.connections.send(sms.encode())    


    def receive_sms(self):
        while True:
            data=self.connections.recv(1024).decode()
            print("client sent : "+data)
            

    def main(self):
      while True:
          message = input()
          self.send_sms(message)           


server=Servernode()
always_receive=threading.Thread(target=server.receive_sms)
always_receive.daemon = True
always_receive.start()
server.main()