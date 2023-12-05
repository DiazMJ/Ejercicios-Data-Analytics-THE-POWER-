"""1. Ejercicio: Define una función que tome dos números y retorne su suma."""
def suma(a,b):
  return a+b
print(suma(5,7))

"""2. Ejercicio: Define una función que tome un número y retorne su factorial."""

def factorial(n):
   if n == 0:
      return 1
   else:
      return n * factorial(n - 1)
   print(factorial(5))

   
   

"""3. Ejercicio: Define una función que tome un número y determine si es primo."""

def numero_primo(x):
   if x < 2:
      return False
   for i in range(2,x):
        if x % i==0:
          return False
   return True
print(numero_primo(7))

"""4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos."""

def  sumar_lista(lista):
   return sum(lista)
print(sumar_lista([5,10,15,7]))

"""5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa."""
def texto_reverso(cadena) :
   return cadena[::-1]
print(texto_reverso('Martin'))

