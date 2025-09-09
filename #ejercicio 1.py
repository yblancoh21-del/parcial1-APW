#ejercicio 1 Cree un programa que pida al usuario un número entero positivo y Imprima todos los números primos menores o iguales a ese número.
n = int(input("Ingrese un número entero positivo: "))
if n <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    primos = []
    for num in range(2, n + 1):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num)
            primos.append(num)
    print("Número de primos encontrados:", len(primos))