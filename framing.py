
message = input("Enter the input message : ")


message = message.replace("ESC","ESCESC")
message = message.replace('FLAG','ESCFLAG')

print(message)

asciiCode = dict({  
  'ESC': '10100011',
  'FLAG': '01111110'
})


msgBin=''
i=0
while i < len(message):
    if message.find("ESC",i) == i :
        msgBin = msgBin + "" + asciiCode['ESC']
        i = i+3
    elif message.find("FLAG",i) == i:
        msgBin = msgBin + "" + asciiCode['FLAG']
        i = i+4
    else:
        msgBin = msgBin + "" + str(bin(ord(message[i])))[2:].zfill(8)
        i = i+1

# print(msgBin)

msgBin = msgBin.replace("011111","0111110")

# print(msgBin)

frames = []
i = 0
j = 8
while j<len(msgBin):
   
    fr = msgBin[i:j]
    # fr='0111110 ' + msgBin[i:j] + ' 0111110'
    frames.append(fr)
    i = j
    j = j+8
fr = msgBin[j-8:]
# fr='0111110 ' + msgBin[j-8:] + ' 0111110'
frames.append(fr)

print(frames)

# message='0111110 ' + msgBin + ' 0111110'
# print(message)
