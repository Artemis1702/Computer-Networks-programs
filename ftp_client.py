import socket
import os


hIP=socket.gethostname()

port=9999

def dwld(cmd):
    size=s.recv(1024)
    size=int(size.decode('ascii'))
    print("size is",size)
    f=open(cmd[5:],"w")
    rev=0
    while rev<size:
        l=s.recv(1024).decode('ascii')
        f.write(l)
        rev+=1024
    f.close()
    print("{} downloaded".format(cmd[5:]))
    return

def upld(cmd):
    fileName=cmd[5:]
    size=os.path.getsize(fileName)
    s.send(str(size).encode('ascii'))
    con=open(fileName,'r')
    l=con.read(1024).encode('ascii')
    while l:
        s.send(l)
        l=con.read(1024).encode('ascii')
    con.close()
    print("{} file uploaded".format(fileName))
    return




s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((hIP,port))
print("connected")
while True:
    cmd=input("enter the command:")
    s.send(cmd.encode('ascii'))
    if cmd[:4]=="DWLD":
        dwld(cmd)
    elif cmd[:4]=="UPLD":
        upld(cmd)
    elif cmd[:4]=="QUIT":
        print("client closed")
        s.close()
        break
