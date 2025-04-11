from abc import ABC, abstractmethod

class absnumeros(ABC):
    @abstractmethod
    def print_numeros(self):
        pass

    def __init__(self, n):
        self.n = n

class racionales_concreto(absnumeros):
    def __init__(self, n):
        super().__init__(n)

    def print_numeros(self):
        print(f"El número abstracto es: {self.n}")


