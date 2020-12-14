diccionario={
            "iperurena": {
            "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
            },
            "fmuguruza": {
            "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
            },
            "aolaizola": {
            "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
            }
            }


dic1 = {}
usuarios=[]
n1='N'
intentos=0
n=4
clave='N'

for key, value in diccionario.items():     
       usuarios.append(key)

while n1 !='ok' and  intentos<4:   
    print(f"Datos incorrectos. le quedan {n-intentos} {len(dic1)} {clave}  ") 
    user = input("Escriba el usuario:")
    password = input("Escriba contraseña:")

    if user in usuarios:       

            dic1.update(diccionario[user])  

            if len(dic1)>0:

                clave = dic1.get('password')
                if password==clave:
                    apellido = dic1.get('apellido')
                    n1 ='ok' 
                    intentos=4           
                else:
                    intentos=intentos+1
            else:                
                intentos=intentos+1
    else:  
        intentos=intentos+1


if n1 =='ok':
    print(f"El usuario es {user} {apellido}")
else:
    print(f"Datos incorrectos")

# for key, value in diccionario.items():     
#        lista.append(key)

# if user in usuarios:       

# else
#     user = input("Escriba el usuario:")
#     password = input("Escriba contraseña:")



# for key, value in diccionario.items(): 
#     if user==key:
#         dic1.update(value)
#         clave = dic1.get('password')
#         if password==clave:
#             apellido = dic1.get('apellido')
#             print(f"El usuario es {user} {apellido}  ")


# if len(dic1)>0:
#     clave = dic1.get('password')
#     if password==clave:
#         apellido = dic1.get('apellido')
#         print(f"El usuario es {user} {apellido}")


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


# print('Lista de valores ordenados por clave:', valor)
#  print(f"La Lista es  {diccionario['iperurena']['password']}  ")

    









