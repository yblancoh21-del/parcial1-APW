#ejemplo 5
def promedio_notas(estudiantes):
    if not estudiantes:
        return 0
    suma = sum(est["nota"] for est in estudiantes)
    return suma / len(estudiantes)
def mejor_estudiante(estudiantes):
    if not estudiantes:
        return None
    return max(estudiantes, key=lambda est: est["nota"])

def peor_estudiante(estudiantes):
    if not estudiantes:
        return None
    return min(estudiantes, key=lambda est: est["nota"])

estudiantes = []
print("sistema de gestión de estudiantes")
while True:
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    try:
        nota = float(input(f"Ingrese la nota de {nombre}: "))
        if 0 <= nota <= 100:
            estudiantes.append({"nombre": nombre, "nota": nota})
        else:
            print("Error: La nota debe estar entre 0 y 100.")
    except ValueError:
        print("Error: Debe ingresar un número válido para la nota.")
print ("reporte final")  
print(f"total de estudiantes: {len(estudiantes)}")
print(f"promedio de notas: {promedio_notas(estudiantes):.2f}")
mejor = mejor_estudiante(estudiantes)
peor = peor_estudiante(estudiantes) 
if mejor:
    print(f"mejor estudiante: {mejor['nombre']} con nota {mejor['nota']}")
if peor:
    print(f"peor estudiante: {peor['nombre']} con nota {peor['nota']}")

ordenados = sorted(estudiantes, key=lambda est: est["nota"], reverse=True)
for est in ordenados:
    print(f"{est['nombre']}: {est['nota']}")
