lista =[12, 23, 5, 29, 92, 64] 
print("Lista Original:",lista)
lista2= [4, 11, 32]
numero=(lista [-1])
lista.pop() 
lista.insert(0,numero)
print("paso 1",lista)
numero=(lista [1])
lista.remove(lista [1]) 
lista.append(numero)
print("paso 2",lista)
lista.insert(0,14)
print("paso 3",lista)
suma=sum(lista)
lista.insert(-0,suma)
print("paso 4",lista)
lista.extend(lista2)
print("paso 5",lista)
for numero in  lista:
    if numero % 2 != 0:
        lista.remove(numero) 

print("paso 6",lista)
lista.sort()
print("paso 7",lista)
lista.clear() 
print("paso 8",lista)

