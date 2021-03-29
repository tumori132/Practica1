#cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no␣
#,→contener los símbolos:@ y !):")
#if len(cadena) > 10:
#print("Ingresaste más de 10 carcateres")
#cant = 0
#for car in cadena:
#if car == "@" or car == "!":
#cant = cant + 1
#if cant >= 1:
#print("Ingresaste alguno de estos símbolos: @ o !" )
#else:
#print("Ingreoo OK")
# como podemos simplificar la linea 1 y la linea 10
leer = input("Ingresa la clave (no debe contener mas de 10 caracteres, ni @ y !)")
cadena = leer
if len(cadena) > 10:
    print('Clave incorrecta')
elif '@'or '!' in cadena:
    print('Clave incorrecta')
else:
    print('Clave Correcta')