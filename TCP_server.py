import socket

SRV_IP = "192.168.0.108"
PORT = 50005
BUFF_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_IP, PORT))
print("listening")
s.listen(1)

conn, addr = s.accept()
print("client connected: ", addr)

pkt = bytearray()
tmp_buff = bytearray(BUFF_SIZE)

while 1:
    # read
    # parse
    # create files and write data
    print("receiving")

    n_bytes = conn.recv_into(tmp_buff, BUFF_SIZE)
    if not n_bytes:
        break
    pkt += tmp_buff[0:n_bytes]

print(pkt)
print("len", len(pkt))

# debug
f_h = open("rcv.txt", 'bw')
f_h.write(pkt)
f_h.close()
# end debug

print("End of reception")
conn.close()
