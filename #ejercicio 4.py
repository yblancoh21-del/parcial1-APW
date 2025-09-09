#ejercicio 4 Implemente un programa que use try–except para: Pedir al usuario dos números enteros. Calcular la división entre ellos. Si el usuario ingresa un valor no numérico → mostrar "Error: Debe ingresar números enteros". Si intenta dividir entre cero → mostrar "Error: No se puede dividir entre cero".
try:
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
except ValueError:
    print("Error: Debe ingresar números enteros")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
