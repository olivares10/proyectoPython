num1 = int(input("Escriba un numero para multiplicarlo:"))


for numero in  [0,1,2,3,4,5,6,7,8,9,10]:
    if numero % 2 == 0:
        print("Numero par, no lo sumamos")
        continue

    print(f"{num1} * {numero} = {numero * num1}")

