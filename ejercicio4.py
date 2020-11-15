print ("Escribe un programa que solicite al usuario dos números y una frase. El primer número introducido. \
se corresponderá a la posición de inicio del substring que deberá mostrar el programa por pantalla.. \
El segundo número indicará la longitud de dicho substring.")

num1 = int(input("Escriba posición de inicio del substring:"))
num2 = int(input("Indique la longitud del substring:"))
text = input("Escriba una frase:")

print ("************SALIDA************")
print("{}  ". \
    format(text[num1:num1+num2]))
print ("************SALIDA************")

