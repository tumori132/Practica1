frase = input('Ingrese una frase').lower()
palabra = input('Ingrese una palabra').lower()
frase = frase.split()
for linea in frase:
    if palabra in linea:
        count = frase.count(palabra)

print(f'La cantidad de veces que esta en la frase es: {count} vez/veces')
