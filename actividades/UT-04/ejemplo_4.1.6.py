import getpass

USERNAME = "pepito"
PASSWORD = "1234"

username = input("Username: ").lower()
# password = input("Password: ")
# getpass no funciona en terminal del IDE
password = getpass.getpass(prompt="Password: ")
if username == USERNAME and password == PASSWORD:
    print("Acceso concedido")
else:
    print("Acceso denegado")