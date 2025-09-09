#ejercicio 3 
def analizar_texto(*args,**kwargs):
    contar_vocales = kwargs.get('contar_vocales', False)
    contar_palabras = kwargs.get('contar_palabras', False)
    texto_completo = ' '.join(args)
    if contar_vocales:
        vocales = 'aeiouAEIOU'
        num_vocales = sum(1 for char in texto_completo if char in vocales)
        print(f"Número de vocales: {num_vocales}")
    if contar_palabras:
        total_palabras = len(texto_completo.split())
        print(f"Número de palabras: {total_palabras}")

analizar_texto("Hola mundo", "Este es un texto de prueba", contar_vocales=True, contar_palabras=True)