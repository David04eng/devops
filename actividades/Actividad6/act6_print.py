print("Hola David Espinoza, Ingrese un numero entero")

try:
    n = int(input())
    print("El numero ingresado es ", n)
    
    for number in range(n):
        print(number)
except:
    print("La entrada no es un entero")
    