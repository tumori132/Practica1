texto = '''No te declares jamás vencido,
aunque mil veces en la lucha caigas,
que caer no es ceder si has conseguido,
levantarse de nuevo en otras tantas.
ADELANTE ESTUDIANTES ADELANTE !!!!
Con el aire cabal del vencedor,
la derrota y el triunfo son instantes,
y el laurel no es eterno en su verdor,
horizonte sonoro de clarines,
y muchedumbre de pañuelos blancos,
a tanta gloria permanente marco,
y alboroto triunfal de banderines.
No te declares jamás vencido,
aunque mil veces en la lucha caigas,
que caer no es ceder si has conseguido,
levantarse de nuevo en otras tantas,
ADELANTE ESTUDIANTES ADELANTE !!!!
con el aire cabal del vencedor,
la derrota y el triunfo son instantes,
y el laurel no es eterno en su verdor,
ADELANTE ESTUDIANTES ADELANTE !!!!
con el paso marcial animo tenso,
alta la frente, ilasado el pecho,
y la casaca bicolor triunfante !!!!!'''

charEspeciales = ''':/!,-.'"()'''
for char in texto:      # voy por palabra
    if char in charEspeciales:     # veo si hay un char especial en la palabra
        texto = texto.replace(char, " ") # reemplazo por un espacio

texto = texto.lower()
texto_mod = texto.split()
letras = '''qwertyuiopasdfghjklñzxcvbnm'''
letra = input("Ingrese una letra")
if letra in letras:
    for palabra in texto_mod:
        if palabra.startswith(letra):
            print(palabra)
else:
    print('No se ingreso una letra')