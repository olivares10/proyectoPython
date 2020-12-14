
# Ctrl+K y Ctrl+C o Ctrl+U

# ejercicio2
# i = int(input("Ingrese Numero de inicio:"))
# j = int(input("Ingrese Numero de fin:"))
# contador = 0

# for numero in  range(i,j+1):
   
#    contador = numero + contador

# print(f"Resultado:{contador} ")

# ejercicio3
# i = int(input("Ingrese Numero de inicio:"))
# j = int(input("Ingrese Numero de fin:"))
# contador1 = 0
# contador2= 0

# for numero in  range(i,j+1):
#     if numero % 2 == 0:
#         contador1 = numero + contador1
#     else:
#         contador2 = numero + contador2
# print(f"Pares = {contador1}, Impares = {contador2}, Total = {contador1+contador2} ")

# ejercicio4
# usuario_v= "root"
# clave_v = "toor"
# usuario = input("Usuario: ")
# clave = input("Clave: ")

# if usuario==usuario_v and clave==clave_v:
#     print("¡Bienvenido!")
# else:
#     print("Acceso fallido")

# ejercicio5
# usuario_v= "root"
# clave_v = "toor"
# usuario = input("Usuario: ")
# clave = input("Clave: ")

# if usuario==usuario_v and clave==clave_v:
#     print("¡Bienvenido!")
# else:
#     print("Datos incorrectos. le quedan 3 intentos")
#     usuario = input("Usuario: ")
#     clave = input("Clave: ")
#     if usuario==usuario_v and clave==clave_v:
#         print("¡Bienvenido!")
#     else:
#         print("Datos incorrectos. le quedan 2 intentos")
#         usuario = input("Usuario: ")
#         clave = input("Clave: ")
#         if usuario==usuario_v and clave==clave_v:
#             print("¡Bienvenido!")
#         else:
#             print("Datos incorrectos. le quedan 1 intentos")
#             usuario = input("Usuario: ")
#             clave = input("Clave: ")
#             if usuario==usuario_v and clave==clave_v:
#                 print("¡Bienvenido!")
#             else:
#                 print("Acceso fallido")


# ejercicio6
# n1 = float(input("Escriba el primer Número: "))
# n2 = float(input("Escriba el segundo Número: "))
# n3 = float(input("Escriba el tercer Número: "))
# n4 = float(input("Escriba el cuarto Número: "))
# n5 = float(input("Escriba el quito Número: "))

# mayor=0
# for num in [n1,n2,n3,n4,n5]:
#     if num>mayor:
#         mayor=num
    
# print(f"El mayor de los numero es:{mayor} ")

# ejercicio7
numeros = []
mayor=0
n1 = input("Escriba el primer  o (“fin” para salir):")

 
while n1 !='fin':
  numeros.append(float(n1))
  n1 = input("Escriba el siguiente numero  o (“fin” para salir):")
 
if len(numeros)>0:

    print(f"El mayor de los '{len(numeros)}' numeros introducidos es:{max(numeros)} ")
    
else:
    print("No hay numeros")


