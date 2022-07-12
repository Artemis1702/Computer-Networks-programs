import socket
import os

hIP=socket.gethostname()
port=9999
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((hIP,port))
s.listen(5)

def dwld(fileName):
    con=open(fileName,"r")
    size=os.path.getsize(fileName)
    client.send(str(size).encode('ascii'))
    l=con.read(1024)
    while l:
        client.send(l.encode('ascii'))
        l=con.read(1024)
    con.close()
    print("{} downloded".format(fileName))
    return    

def upld(fileName):
    size=int(client.recv(1024).decode('ascii'))
    con=open(fileName,'w')
    rev=0
    while rev<size:
        l=client.recv(1024).decode('ascii')
        con.write(l)
        rev+=1024
    con.close()
    print("{} file uploaded".format(fileName))
    return




while True:
    client,addr=s.accept()
    print("{} connected".format(addr))
    while True:
        cmd=client.recv(1024).decode('ascii')
        if cmd[:4]=="DWLD":
            dwld(cmd[5:])
        elif cmd[:4]=="UPLD":
            upld(cmd[5:])
        elif cmd[:4]=="QUIT":
            client.close()
            print("{} disconnected".format(addr))
            break
