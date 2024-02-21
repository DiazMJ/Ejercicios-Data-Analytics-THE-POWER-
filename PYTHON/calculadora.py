def suma(a, b):
  return a + b
def resta (a, b):
  return a-b
def division (a,b):
  if b != 0:
    return a / b
  else:
    return a
def multiplicacion(a, b):
  return a*b
def potencia (a, b):
  return a ** b
def raiz_cuadrada(a):
   if a >=0 :
    return a ** 0,5
   else:
     return (f'No calculamos raices cuadradas de numeros negativos,\njust positive my friend! ')
def porcentaje(a):
  return a/100

#2 paso realizar el menu de nuestra calculadora:
def Calculadora_Marita():
  print( "Bienvenido a la calculadora de Marita")
  while True :
    print (' Tus opciones son:')
    print('1.Suma, 2.Resta, 3.Divide, 4.Multiplica,5.Potencia, 6.Raiz Cuadrada,7.Porcentaje,8.Salir.')

    eleccion =int(input('Selecciona una opcion: '))
  
    if eleccion == 8:
      print( "adios")
      break
    if eleccion in [1,2,3,4,5] :
      a =int(input('ingresa primera cifra: '))
      b= int(input ('ingresa segunda cifra: '))
    elif eleccion in [6,7]:
      a= int(input('ingresa la cifra a operar: '))

    if eleccion == 1:
      print(suma(a,b))
    if eleccion == 2:
      print(resta(a,b))
    if eleccion == 3:
      print(division(a,b))
    if eleccion == 4 :
      print(multiplicacion(a,b))
    if eleccion == 5 :
      print(potencia(a,b))
    if eleccion ==6 :
      print(raiz_cuadrada(a))
    if eleccion == 7 :
      print(porcentaje(a))

if __name__ == "__main__":
    Calculadora_Marita()