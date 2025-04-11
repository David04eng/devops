print ("Ingresar numero")
try:
    n=int(input())
    print("El numero ingresado es: ", n)
    
    for number in range (n):
        if ((n % 2) == 0):
            print("Residuo es:", number % 2)
            print("El numero es: ", number)
        else:
            print("El cuadrado del numero es  ", pow(number,2))
except:
    print("La entrada no es un entero")