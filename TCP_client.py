import socket
import glob

SRV_IP = '192.168.0.108'
PORT = 50005
BUFF_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRV_IP, PORT))

for file in glob.glob("*.txt"):
    f_h = open(file, 'r')
    s.send("new ")
    s.send(file)
    s.send(" ")
    while 1:
        data = f_h.read(BUFF_SIZE)
        if not data:
            break
        s.send(data)
    f_h.close()
    print("sent file ", file)

print("exiting")
s.close()
