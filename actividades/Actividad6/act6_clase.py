class Entero:
    def __init__(self,n):
        self.n = n
  
    def print_numbers():
        for number in range(n):
            if((n%2)==0):
                print("El numero es: ", number)
            else:
                print("El cuadrado del numero es: ", number**2)
                
num = int(input())    
entero = Entero(num)
entero.print_numbers()

