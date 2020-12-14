# alumnos.index("Amaia")
diccionario={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5}
lista=[]
for key, value in diccionario.items(): 
    if not value in lista:
       lista.append(value)


print(f"La Lista es  {lista}  ")
