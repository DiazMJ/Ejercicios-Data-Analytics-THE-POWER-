#Ejercicio 1: Definir una Función sin Parámetros
#Enunciado: Define una función llamada saludo que imprima en la consola el mensaje "Hola, bienvenido a R".

saludo <-function(x){
  resultado <- "Hola, bienvenido a R"
  return(resultado)
}
saludo(x)

#Ejercicio 2: Definir una Función con Parámetros y Condicionales
#Enunciado: Crea una función llamada calificar_edad que tome un parámetr numérico llamado edad y muestre en la consola si la persona es "menor de edad" o "mayor de edad".

calificar_edad <- function(edad){
  if(edad >= 18){print("eres mayor de edad")
  }else {
    print("eres menor de edad")
  }
}
calificar_edad(26)
calificar_edad(15)

#Ejercicio 3: Bucle con Operaciones Aritméticas
#Enunciado: Define una función llamada tabla_multiplicar que tome un parámetro numérico n e imprima la tabla de multiplicar del 1 al 10 de ese número.

tabla_multiplicar <- function(n){
  for (i in 1:10){
    print(i*n)}
  }
tabla_multiplicar(3)

#Ejercicio 4: Bucle con Condicionales y Operaciones con Vectores
#Enunciado: Crea una función llamada numeros_pares que tome un parámetro numérico limite e imprima los números pares hasta ese límite.

numero_pares <-function(num){
  while (contador <= num)
  resultado <- i %% 2 == 0
     <-1 contador+1
}
#no me sale

#Ejercicio 5: Bucle Anidado con Condicionales y Operaciones de Listas
#Enunciado: Define una función llamada matriz_cuadrada que tome un parámetro numérico n e imprima una matriz cuadrada de tamaño n x n donde loselementos son el resultado de la suma de sus índices de fila y columna.


matriz <-matrix(c(1,2,3,4),nrow=2,ncol = 2)
print(matriz)

#al no verlo como se hace en los microlernings no logro  desarrollar el ejercico

