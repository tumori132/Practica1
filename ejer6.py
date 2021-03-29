frase = """Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple. WARCRAFT"""
#frase = frase.lower()
frase = frase.split()
listaNueva = []
for palabra in frase:
    if frase.count(palabra.lower()) == 1 and frase.count(palabra.upper()) == 0:
        listaNueva.append(palabra)
    elif frase.count(palabra.upper()) == 1 and frase.count(palabra.lower()) == 0:
        listaNueva.append(palabra)

print(listaNueva)
