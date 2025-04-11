class Numeros():

    def __init__(self,n) :
        self.n= n
    
    def print_numbers(self):
        for number in range (self.n):
            if((self.n%2)==0):
                print("el numero es ", number)
            else:
                print("el cuadrado del numero es ",pow(number,2))


class racionales (Numeros) :    
    def __init__(self, n):
        super().__init__(n) 
    
    def print_numbers(self):
       # as_integer_ratio()
       print("el numero racional es:",self.n)
       print("el numero racion en forma de fraccion es: ", self.n.as_integer_ratio())
       
    def print_hello(self):
        return "Hola David"