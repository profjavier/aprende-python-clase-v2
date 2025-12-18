import socket

HOST_DESTINO = '127.0.0.1'
PORT_DESTINO = 65432
''' 
    socket.AF_INET  cindica IPv4 
    socket.AF_INET6  indica IPv6    
    socket.SOCK_STREAM indica TCP
    socket.SOCK_DGRAM indica UDP
'''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST_DESTINO, PORT_DESTINO))

while True:
    mensaje = input("Cliente: ")
    client.send(mensaje.encode())

    if mensaje.lower() == "salir":
        break

    respuesta = client.recv(1024).decode()
    print("Servidor:", respuesta)