import act7_1_numeros
import act7_3_abstract_class

print("Ingresa un numero abstracto: ")
n = int(input())
enteros = act7_1_numeros.Numeros(n)
enteros.print_numbers()

print("Ingresa un numero: ")
q = float(input())
racionales = act7_1_numeros.racionales(q)
racionales.print_numbers()

print("Ingresa un numero para la clase abstracta: ")
m = float(input())

# Instanciar la subclase concreta de la clase abstracta 'racionales_concreto'
racionales_abs = act7_3_abstract_class.racionales_concreto(m)
racionales_abs.print_numeros()