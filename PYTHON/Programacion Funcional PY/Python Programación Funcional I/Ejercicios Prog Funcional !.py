"""  ### 2.1. Función `frecuencia_letras`.

 ###  Explicación del ejercicio:

 Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

 ### Código a seguir:
 
 - **Definición de la función `frecuencia_letras`:**
  - Creamos una función llamada `frecuencia_letras` que toma una cadena de texto como parámetro y devuelve un diccionario con las frecuencias de cada letra en la cadena, ignorando los espacios.
- **Iteración sobre la cadena de texto:**
  - Iteramos sobre cada caracter en la cadena de texto utilizando un bucle `for`.
- **Ignorar los espacios:**
  - Verificamos si el caracter actual es un espacio y lo ignoramos.
- **Conteo de frecuencia de cada letra:**
  - Para cada letra en la cadena de texto, contamos su frecuencia y la almacenamos en un diccionario.

### Caso de uso:
- letras_cadena = "El patio de mi casa es particular, cuando llueve se moja como los demás"
"""

def frecuencia_letras (cadena_texto):
    diccionario ={}
    for letra in cadena_texto:
      if letra  != " ":
        if letra in diccionario:
            diccionario[letra] += 1
        else:
           diccionario[letra] = 1
    return diccionario
mi_cadena_de_texto = "hola neni"
mi_diccionario_conteo = frecuencia_letras(mi_cadena_de_texto)
print(mi_diccionario_conteo)
      
### 2.2. Función `buscar_palabra`.

### Explicación del ejercicio:

""" Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

### Código a seguir:
 
- **Definición de la función `buscar_palabra`:**
  - Creamos una función llamada `buscar_palabra` que toma dos parámetros: `lista_palabras` (una lista de palabras) y `palabra_objetivo` (la palabra que se desea buscar dentro de la lista). 
  - Inicializamos una lista vacía llamada `palabras_encontradas` para almacenar las palabras que contienen la palabra objetivo.

- **Iteración sobre la lista de palabras:**
  - Iteramos sobre cada palabra en la lista de palabras utilizando un bucle `for`.

- **Búsqueda de la palabra objetivo en cada palabra de la lista:**
  - Comprobamos si la palabra objetivo está contenida en la palabra actual utilizando el operador `in`.
  - Si la palabra objetivo está presente en la palabra actual, añadimos esa palabra a la lista `palabras_encontradas`.

- **Retorno de las palabras encontradas:**
  - Devolvemos la lista `palabras_encontradas` que contiene todas las palabras de la lista original que contienen la palabra objetivo.

### Caso de uso:
- lista_palabras = ["manzana", "banana", "naranja", "melocotón", "plátano"]
- palabra_objetivo = "na" """ 

def buscar_palabra(lista_palabras,palabra_objetivo):
    palabras_encontradas = []
    for palabra in lista_palabras: 
      if palabra_objetivo in palabra:
         palabras_encontradas.append(palabra)
    return palabras_encontradas

lista_palabras_prueba = ["manzana", "banana", "naranja", "melocotón", "plátano"]
palabra_objetivo = "na"
palabras_encontradas = buscar_palabra(lista_palabras_prueba, palabra_objetivo)
print(palabras_encontradas)

### 2.3. Función `calcular_promedio`.

### Explicación del ejercicio:

""" Escribe una función que tome una lista de números como parámetro y un valor opcional `nota_aprobado`, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que `nota_aprobado`. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

### Código a seguir:
 
- **Definición de la función:**
  - Creamos una función que toma una lista de números como parámetro y un valor opcional `nota_aprobado`, que por defecto es 5.

- **Cálculo de la media:**
  - Iteramos sobre cada número en la lista y sumamos todos los números.
  - Dividimos la suma por la cantidad de números para calcular la media.

- **Determinación del estado:**
  - Si la media es mayor o igual a `nota_aprobado`, asignamos el estado "aprobado". De lo contrario, asignamos el estado "suspenso".
- **Retorno de resultados:**
  - Devolvemos una tupla que contiene la media y el estado.

### Caso de uso:

- notas_alumnos = [6, 7, 8, 4, 5] """

def evaluación(lista_notas,nota_aprobado=5):
      for nota in  lista_notas:
        media = sum(lista_notas)/len(lista_notas)
        estado ='aprobado'if media >=nota_aprobado else 'suspendido'
      return (media,estado)
        
Notas_alumno =[6, 7, 8, 4, 5] 
Nota_final = evaluación(Notas_alumno) #si quermos cambiar la nota de aprobado, añadimos despues del 1parametro notas d alumno, el segundo que seria nota aprobado , es decir:Nota_final = evaluacion(Nota_final, nota_aprobado) podemos darle un numero dirctamente o crear una variable con el valor de aprobado que quermos q tome.
print(Nota_final)

### 2.4. Función `factorial`.

###  Explicación del ejercicio:
"""
- Se crea una función que calcula el factorial de un número utilizando recursividad.
- El factorial de un número entero no negativo, denotado como `n!`, es el producto de todos los enteros positivos menores o iguales a `n`. En otras palabras, el factorial de `n` se calcula multiplicando todos los números naturales desde 1 hasta `n`. 

### Código a seguir:
 
- **Definición de la función `factorial`:**
  - Se define una función llamada `factorial` que toma un número entero positivo como argumento y devuelve el factorial de ese número.

- **Cálculo del factorial utilizando recursividad:**
  - Se implementa la lógica del cálculo del factorial utilizando recursividad.
  - Si el número es igual a 0, se devuelve 1 (por definición, el factorial de 0 es 1).
  - Si el número es mayor que 0, se multiplica el número por el factorial del número anterior.

- **Retorno del factorial calculado:**
  - Se devuelve el resultado del cálculo del factorial.

 ### Caso de uso:

 - factorial_5 = factorial(5)"""

def factorial(n):
   if n == 0:
      return 1
   else :
      return n * factorial (n-1)
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero}, es {resultado}")

### 2.5. Función `combinar_listas`.

### Explicación del ejercicio:

""" Escribe una función que tome un número arbitrario de listas como argumentos y devuelva un diccionario donde las listas originales se combinan utilizando los índices como claves.

### Código a seguir:
 
- **Definición de la función `combinar_listas`:**
  - Creamos una función llamada `combinar_listas` que toma un número arbitrario de listas como argumentos.

- **Combinación de las listas:**
  - Utilizamos la función `zip` para iterar simultáneamente sobre todas las listas.
  - La función `zip` toma elementos de todas las listas en cada iteración y los combina en tuplas.

- **Enumeración de los elementos combinados:**
  - Utilizamos la función `enumerate` para obtener el índice y los elementos combinados en cada iteración.
  - `enumerate` asigna un índice a cada iteración, comenzando desde 0.

- **Creación del diccionario combinado:**
  - Creamos un diccionario donde los índices obtenidos con `enumerate` son las claves y las listas combinadas con `zip` son los valores.

- **Retorno del diccionario combinado:**
  - Devolvemos el diccionario combinado.

### Caso de uso:

- lista1 = [1, 2, 3]
- lista2 = ['a', 'b', 'c']
- lista3 = [True, False, True]"""

def combinar_lista(*args):
   diccionario ={}
   for indice, elemento in enumerate(list(zip(*args))):
      diccionario[indice] = elemento 
   return diccionario

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista3 = [True, False, True]

mi_diccionario = combinar_lista(lista1,lista2,lista3)
print(mi_diccionario)

### 2.6. Función `area_figura`

### Explicación del ejercicio:

"""Crea una función que calcule el área de una figura geométrica según el tipo especificado.

### Código a seguir:
 
- **Definición de la función `area_figura`:**
  - Creamos una función llamada `area_figura` que toma el tipo de figura geométrica como argumento de palabra clave y los argumentos necesarios para calcular el área.

- **Cálculo del área según el tipo de figura:**
  - Utilizamos `**kwargs` para aceptar un número arbitrario de argumentos clave-valor. Esto nos permite manejar diferentes tipos de figuras geométricas sin tener que especificar todos los posibles argumentos de antemano.
  - Dependiendo del tipo de figura proporcionada, calculamos el área correspondiente utilizando los argumentos proporcionados. 
    - Si se proporcionan `base` y `altura`, asumimos que es un triángulo y calculamos el área utilizando la fórmula A = (base * altura) / 2.
    - Si se proporciona el `radio`, asumimos que es un círculo y calculamos el área utilizando la fórmula A = 3.14*r^2.
    - Si se proporciona el `lado`, asumimos que es un cuadrado y calculamos el área utilizando la fórmula A = L^2.
    - Si se proporciona un tipo de figura no soportado, la función levantará una excepción usando `raise`

- **Retorno del área calculada:**
  - Devolvemos el área calculada como resultado de la función. Esto permite al usuario utilizar la función para obtener el área de diferentes figuras geométricas, simplemente pasando los argumentos adecuados.

### Ejemplo de uso:

- area_triangulo = area_figura(base=3, altura=4)

- area_circulo = area_figura(radio=2)

- area_cuadrado = area_figura(lado=5)"""

def area_figura(**kwargs):
    if 'base' in kwargs and 'altura' in kwargs:
      base = kwargs['base']
      altura = kwargs['altura']
      area = (base * altura)/2 #calculamos el area de un triangulo
    elif 'radio' in kwargs:
      radio = kwargs['radio']
      area = 3.14 * (radio ** 2)  # Calculamos el área del círculo utilizando la fórmula A = πr^2
    elif 'lado' in kwargs:
      lado = kwargs['lado']
      area = lado ** 2 # Calculamos el área del cuadrado utilizando la fórmula A = L^2
    else:
       raise ValueError ("No se pudo determinar el tipo de figura geométrica.") 
    return area
### Ejemplo de uso:

area_triangulo = area_figura(base =3, altura =4)
print(area_triangulo)
area_circulo = area_figura(radio=2)
print(area_circulo)
area_cuadrado = area_figura(lado=5)
print(area_cuadrado)