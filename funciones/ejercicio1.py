def esprimo(num):
    for n in range(2, num):
        if num%n == 0:
            print("No es primo", n, "es divisor")
            return
    print("Es primo")

 

i = int(input("Ingrese un numero:"))

esprimo(i)





# def contador (i,j):
#     contador = 0
#     for numero in  range(i,j+1):   
#          contador = numero + contador

#     print(f"Resultado:{contador} ")
    


# i = int(input("Ingrese Numero de inicio:"))
# j = int(input("Ingrese Numero de fin:"))

# contador(i,j)


