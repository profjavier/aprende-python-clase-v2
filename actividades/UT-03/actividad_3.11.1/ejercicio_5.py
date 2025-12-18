
roles = []

for i in range(1, 4):
    rol = input(f"Rol {i}: ")
    rol = rol.strip()
    if rol != "":
        roles.append(rol)

cadena_roles = ", ".join(roles)

print("Roles del usuario:", cadena_roles)

