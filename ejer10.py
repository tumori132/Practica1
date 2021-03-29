losValores = {1:["a","e","i","o","u","l","n","r","s","t"],2:["d","g"],3:["b","c","m","p"],4:["f","h","v","w","y"],5:"k",8:["j","x"],10:["q","z"]}
palabra = input("Ingrese una palabra").lower()
cont = 0
# EN PROCESO! , ME FALTA CALCULAR LA SUMA DE PUNTOS.
for char in palabra:
    lista = [char]
    cont =cont + int(list(losValores.keys())[list(losValores.values()).index(lista)])

print(f"Palabra: {palabra}")
print(f"Valor: {cont}")