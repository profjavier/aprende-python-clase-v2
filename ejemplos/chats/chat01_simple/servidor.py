import socket

HOST = '127.0.0.1'
HOST = '127.0.0.1'
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
    print("Cliente:", mensaje)

    if mensaje.lower() == "salir":
        print("Cliente se desconectó.")
        break

    respuesta = input("Servidor: ")
    conn.send(respuesta.encode())
