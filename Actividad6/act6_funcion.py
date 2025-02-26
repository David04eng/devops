def print_numbers():
    for number in range(n):
        if ((n % 2==0)):
            print("El numero ingresado es: ", number)
        else:
            print("El cuadrado del numero es: ", number ** 2)

print("Ingresa un numero")
try: 
    n = int(input())
    print("El numero que ingresaste es: ", n)
    
    print_numbers()

except:
    ("Ingresa un numero valido")