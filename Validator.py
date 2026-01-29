print("Validador de Rosendo")
#REGISTRO
# Variables de Registro
user = input("Registre un usuario: ")
password = input("Registre una contraseña: ")
print("Registro Completado")

# INICIO DE SESIÓN
# Variables de Validación
re_user = input("Ingrese un usuario: ")
re_password = input("Ingrese una contraseña: ")
# Validación
while re_user != user or re_password != password:
    print("Usuario o contraseña incorrectos. Intentalo nuevamente.")
    re_user = input("Ingrese un usuario: ")
    re_password = input("Ingrese una contraseña: ")
else:
    print("Inicio de sesión exitoso")

    