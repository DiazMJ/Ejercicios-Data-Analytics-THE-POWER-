"""Bucles y Funciones
Planteamiento Ejercicios 2
Ejercicios nivel básico
1. Crea una función para verificar si un número es par o impar y devuelva ““Elnúmero es par” o “El número es impar” según corresponda """

def es_par(num):
  return num % 2 ==0
num= 20
if es_par(num):
  print("Es un número par.") 
else:
    print("Es un número impar.")

""" solo consigo que me imprima valor boleano el ejercicio :( )"""

"""2  Crea una función a la que pases un número como argumento, calcule el factorial
de ese número y haga print del resultado"""

def factorial(num): 
  if num == 0 or  num ==1:
    resultado = 1
  elif num > 1:
     resultado = num * factorial(num -1)
  return resultado
print ( factorial(5))


"""obviamente no doy cone el codigo :(, ya que e factorial de 5 deberia ser 120 )"""

"""3 crea una función a la que se le pase un número como argumento, calcule la
cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado
total de dígitos.
PISTA: Para convertir un número a string usa el método str(). Te recordamos que
para saber la longitud de una cadena utilizamos len()"""

def contar_digitos(numero): 
  return len(str(num))
num = 200
print("La cantidad de dígitos es:", contar_digitos(num))


"""4 Dada una lista de números, crea una función que devuelva el número máximo
de la lista."""

def funcion_maximo(lista): 
  maximo = lista[0]
  for n in lista:
   if n > maximo :
      maximo = n
  return maximo
print(funcion_maximo([5,7,8,29]))
"""1. Crea una función que, dado un número, sume los dígitos de ese número y
devuelva el resultado"""

def suma_digitos(numero): 
   numero_str =str(numero)
   suma=0
   for i in numero_str:
      suma += int(i)
      return suma
numero = 12345
resultado = suma_digitos(numero)
print(resultado)

#no logro iterar ( paracetamol y paciencia)
"""
1. Dados dos números, crea una función para encontrar el mínimo común múltiplo
(MCM) de los dos números, que se les pasarán como argumento a la función, y
devuelva el MCM.
1. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el
área de un triángulo.
pythonCopy code
def calcular_area_triangulo(base, altura): return (base * altura) / 2 base = float(inp
ut("Ingrese la base del triángulo: ")) altura = float(input("Ingrese la altura del tri
ángulo: ")) print("El área del triángulo es:", calcular_area_triangulo(base, altura))
1. Crea una función que, dado un número, verifique si un número es positivo,
negativo o cero.
pythonCopy code
def verificar_signo(num): if num > 0: return "positivo" elif num < 0: return "negativ
o"else: return "cero" num = float(input("Ingresa un número: ")) print("El número es:",
verificar_signo(num))
1. Crea una función que, dada una palabra, cuente la cantidad de letras en una
palabra.
pythonCopy code
def contar_letras(palabra): contador = 0 for letra in palabra: if letra.isalpha(): con
tador += 1 return contador palabra = input("Ingresa una palabra: ") print("La cantidad
de letras es:", contar_letras(palabra))
1. Crea una función que, dada una lista de números, convierta la lista de números
a su valor absoluto.
Planteamiento Ejercicios 4
pythonCopy code
def valor_absoluto(lista): for i in range(len(lista)): lista[i] = abs(lista[i]) return
lista numeros = [5, -12, 3, -8, 9] print("Lista con valores absolutos:", valor_absolut
o(numeros))
1. Crea una función que, dado un número, verifique si un número es primo.
pythonCopy code
def es_primo(numero): if numero <= 1: return False for i in range(2, numero): if numer
o % i == 0: return False return True num = int(input("Ingresa un número: ")) ifes_prim
o(num): print("Es un número primo.") else: print("No es un número primo.")
1. Dados dos números, crea una función para encontrar el máximo común divisor
(MCD) de esos dos números.
pythonCopy code
def mcd(a, b): while b: a, b = b, a % b return a num1 = int(input("Ingresa el primer n
úmero: ")) num2 = int(input("Ingresa el segundo número: ")) print("El MCD es:", mcd(nu
m1, num2))
"""