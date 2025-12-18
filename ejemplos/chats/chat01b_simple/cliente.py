import socket
from codigos_ansi import CodigosAnsi as ca

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
    # mensaje = input(": ")
    # mensaje = input(f"{ca.BG_BLANCO}{' '*80}: ")
    mensaje = input(f"{ca.BG_BLANCO}{ca.TEXT_AZUL}{' '*80}\033[1G: ")
    client.send(mensaje.encode())

    if mensaje.lower() == "salir":
        break

    respuesta = client.recv(1024).decode()
    print(ca.TEXT_ROJO, f"{mensaje:>80}",ca.RESET, sep="")
