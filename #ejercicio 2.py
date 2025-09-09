#ejercicio 2  Defina una función con parámetros por omisión llamada calcular_descuento(precio, descuento=10) que:Reciba el precio de un producto y un descuento (por defecto 10%), Retorne el precio final después del descuento, El programa debe pedir al usuario al menos 3 precios de productos y mostrar el valor total a pagar.
def calcular_descuento(precio, descuento=10): 
    precio_final = precio - (precio * descuento / 100)
    return precio_final
total_a_pagar = 0
for i in range(3):
    precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    total_a_pagar += calcular_descuento(precio)

while True:
    continuar = input("¿Desea ingresar otro producto? (s/n): ").strip().lower()
    if continuar != 's':
        break
    precio = float(input(f"Ingrese el precio del producto {i + 2}: "))
    total_a_pagar += calcular_descuento(precio)
    i += 1
    print("precio con descuento", calcular_descuento(precio))
print(f"El total a pagar es: {total_a_pagar:.2f}")
