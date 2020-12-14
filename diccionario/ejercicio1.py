
lista = [12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]
resultado = {}
for num in lista:
    resultado[num] = [lista.count(num)]
   
print(f"La Lista es  {lista}  ")
print(f"El diccionario es {resultado}  ")