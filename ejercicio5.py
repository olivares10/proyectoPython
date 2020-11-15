print ("Escribe un programa que solicite al usuario una frase. A continuación le solicitará la letra que quiere. \
 reemplazar y por qué letra deberá reemplazarse. Por último el programa mostrará el número de veces. \
 que la letra está presente en la frase y el resultado final tras reemplazarla.")

text = input("Escriba una frase:")
letra1 = input("Escriba á la letra que quiere reemplazar:")
letra2 = input("Escriba el reemplazo:")

print ("************SALIDA************")
print("{}  apariciones. {}  ". \
    format(text.count(letra1),text.replace(letra1, letra2 )))
print ("************SALIDA************")