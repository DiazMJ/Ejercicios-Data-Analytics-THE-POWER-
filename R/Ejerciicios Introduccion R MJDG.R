# Ejercicio 1: Variables y Tipos de Datos
# Enunciado: Define una variable llamada numero con el valor 10 y otra llamada nombre con tu nombre.

numero <-10
nombre<-"María"

# Ejercicio 2: Funciones  class e is.numeric
# Utiliza las funciones class e is.numeric para determinr el tipo de dato de número:

class(numero)
is.numeric(numero)
es_numérico <-is.numeric(numero)
class(es_numérico)
# Ejercicio 3: Operaciones Aritméticas
# Enunciado: Realiza una operación aritmética que sume numero y el doble de numero 

numero + (numero * 2)

# Ejercicio 4: Vectores y Listas
# Enunciado: Crea un vector llamado edades con las de tres personas y una lista lamada informacion con el nombre y la edad de una persona

edades <- c(41,8,3)
informacion <-list(nombre="David",edad= 48)
print(informacion)

# Ejercicio 5: Funciones is.character e is.logical
#:Verifica si nombre es de tipo caracter y si es,numerico de tipo lógico.
is.character(nombre)
is.logical(es_numérico)
# Ejercicio 6: Operaciones Lógicas Enunciado: 
#Crea una variable llamada mayor_de_edad que sea TRUE si la edad de la primera persona en edades es mayor o igual a 18

mayor_de_edad <-edades[1]>=18
print(mayor_de_edad)

#Ejercicio 7: Comparaciones de Vectores
#Enunciado: Utiliza el operador %in% para verificar si el valor 30 está presenteen el vector edades .

esta_en_vector<-30 %in% edades
print(esta_en_vector)
#Ejercicio 8: Operadores de Comparación
#Enunciado: Compara si el doble de numero es mayor que edades[3] .

es_doble_es_mayor <- (numero*2)> edades[3]
print(es_doble_es_mayor)
#Ejercicio 9: Utilizar Operador Lógico
#Enunciado: Define dos variables lógicas, condicion1 y condicion2 , ambas con valor TRUE . Comprueba si ambas condiciones son verdaderas.#

condicion1<-TRUE
condicion2<-TRUE
ambas_veraderas<- condicion1 &condicion2
print(ambas_veraderas)

#Ejercicio 10: Utilizar Operador Lógico
#Enunciado: Define una variable lógica, verdadero , con valor TRUE . Comprueba que su valor NO sea verdadero.

verdadero<- TRUE
no_verdadero<-!verdadero
print(no_verdadero)
