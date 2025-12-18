import socket
from codigos_ansi import CodigosAnsi as ca

HOST = '127.0.0.1'
# HOST = '192.168.60.78'
PORT = 65432
''' 
    socket.AF_INET  cindica IPv4 
    socket.AF_INET6  indica IPv6    
    socket.SOCK_STREAM indica TCP
    socket.SOCK_DGRAM indica UDP
'''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()   # Espera una conexion
print("Servidor esperando conexión...")

conn, addr = server.accept()
print("Conectado con:", addr)

while True:
    mensaje = conn.recv(1024).decode()
    print(ca.TEXT_ROJO, f"{mensaje:>80}",ca.RESET, sep="")

    if mensaje.lower() == "salir":
        print("Cliente se desconectó.")
        break

    respuesta = input(": ")
    conn.send(respuesta.encode())
