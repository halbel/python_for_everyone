import socket

url=input("enter url:")
parts=url.split("/")
host=parts[2]
path='/'+'/'.join(parts[3:])
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
total_chars=0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    total_chars+=len(data)
    if total_chars<=3000:
        print(data.decode(),end='')

mysock.close()
print('calkowita liczba znakow:',total_chars)