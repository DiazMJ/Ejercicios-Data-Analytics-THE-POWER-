"""Datos del ejercicio"""

lista_campañas = [
    {
        'nombre': 'Rebajas de Enero',
        'presupuesto': 35000,
        'inicio': '2023-01-02',
        'fin': '2023-01-31',
        'medios': ['Publicidad en línea', 'Redes Sociales', 'Email Marketing'],
        'segmentos_objetivo': ['Clientes regulares', 'Potenciales compradores'],
        'personas_alcanzadas': 50000,
        'tasa_conversion': 0.02
    },
    {
        'nombre': 'San Valentín',
        'presupuesto': 25000,
        'inicio': '2023-02-01',
        'fin': '2023-02-14',
        'medios': ['Redes Sociales', 'Email Marketing', 'Publicidad impresa'],
        'segmentos_objetivo': ['Parejas', 'Jóvenes'],
        'personas_alcanzadas': 30000,
        'tasa_conversion': 0.05
    },
    {
        'nombre': 'Día del Padre',
        'presupuesto': 20000,
        'inicio': '2023-06-01',
        'fin': '2023-06-15',
        'medios': ['Redes Sociales', 'Colaboraciones con influencers', 'Publicidad impresa'],
        'segmentos_objetivo': ['Jóvenes', 'Familias'],
        'personas_alcanzadas': 25000,
        'tasa_conversion': 0.03
    },
    {
        'nombre': 'Día de la Madre',
        'presupuesto': 22000,
        'inicio': '2023-04-20',
        'fin': '2023-05-10',
        'medios': ['Publicidad en línea', 'Redes Sociales', 'Email Marketing'],
        'segmentos_objetivo': ['Jóvenes', 'Familias'],
        'personas_alcanzadas': 28000,
        'tasa_conversion': 0.04
    },
    {
        'nombre': 'Día del Friki',
        'presupuesto': 18000,
        'inicio': '2023-05-20',
        'fin': '2023-05-25',
        'medios': ['Publicidad en tiendas físicas', 'Redes Sociales', 'Colaboraciones con influencers'],
        'segmentos_objetivo': ['Jóvenes'],
        'personas_alcanzadas': 20000,
        'tasa_conversion': 0.05
    },
    {
        'nombre': 'Black Friday',
        'presupuesto': 50000,
        'inicio': '2023-11-21',
        'fin': '2023-11-30',
        'medios': ['Redes Sociales', 'Email Marketing', 'Publicidad en línea'],
        'segmentos_objetivo': ['Todos los compradores'],
        'personas_alcanzadas': 100000,
        'tasa_conversion': 0.03
    },
    {
        'nombre': 'Navidad',
        'presupuesto': 60000,
        'inicio': '2023-12-01',
        'fin': '2023-12-24',
        'medios': ['Publicidad en tiendas físicas', 'Redes Sociales', 'Publicidad impresa'],
        'segmentos_objetivo': ['Todos los compradores'],
        'personas_alcanzadas': 120000,
        'tasa_conversion': 0.04
    }
]

"""Ejercicio 1:
Descripción del ejercicio:
Lo primero que nos piden es que veamos el nombre de cada campaña, su presupuesto, el número de personas alcanzadas y su tasa de conversión.
Pasos a seguir:
1. **Definimos nuestra lista de elementos:**
   - Definimos una lista llamada `elementos` que contiene las claves de los datos que queremos imprimir para cada campaña, como "nombre", "presupuesto" y "personas_alcanzadas".###

2. **Recorremos Nuestra lista de campañas:**
   - Utilizamos un bucle `for` para iterar a través de cada campaña en nuestra lista `lista_campañas`.

3. **Iteramos a Través de nuestra lista de elementos:**
   - Dentro de nuestro bucle principal, empleamos otro bucle `for` para iterar a través de cada elemento en nuestra lista `elementos`.

4. **Imprimimos los elementos de la campaña:**
   - Para cada campaña y elemento, utilizamos la sintaxis `campaña[elemento]` para acceder al valor correspondiente dentro del diccionario que representa la campaña.
   - Imprimimos el nombre del elemento seguido desu valor asociado.

5. **Imprimimos una línea en blanco:**
   - Después de imprimir todos los elementos de una campaña, imprimimos una línea en blanco para separar la información de las campañas.
"""

elementos = ["nombre", "presupuesto" , "personas_alcanzadas"] #1 eleaboramos una lista con los elementos q nos pide
for campaña in lista_campañas: #2 iteramos por las campañas de nuestra lista_campañas(datos deñ ejercicio dados arriba)
  for elemento in elementos :#3 iteramos por cada elemento dentro de nuestra lista de elementos 
   print(f"{elemento}: {campaña[elemento]}") #4 Mostramos por terminal el elemento y su valor

print("\n") #5 Imprimimos una línea en blanco

## Ejercicio 2:
### Descripción del ejercicio:
"""Lo segundo que nos piden es que creemos un conjunto, un `set`,con todos medios donde se llevaron a cabo la campañas.

### Pasos a seguir:

1. **Definimos un conjunto de medios utilizados:**
   - Creamos un conjunto vacío llamado `medios_utilizados`, donde vamos a almacenar los medios que se han utilizado en todas las campañas. Optamos por un conjunto en lugar de una lista para garantizar que cada medio aparezca **solo una vez y evitar duplicados.**
2. **Implementamos una lista comprimida (List Comprehension):**
   - Utilizamos una lista comprimida para iterar sobre cada campaña en nuestra lista `lista_campañas`.
   - Dentro de esta lista comprimida, necesitamos un bucle anidado que itere sobre cada medio presente en la lista de medios de la campaña actual.
   - Durante cada iteración, añadimos el medio al conjunto `medios_utilizados`.
3. **Imprimimos el conjunto de medios utilizados:**

   - Una vez recopilados todos los medios únicos utilizados en las campañas, imprimimos el conjunto `medios_utilizados`."""
# creamos el set mas las iteraciones sin comprimir para entender como se hace el Comprenhension
"""medios_utilizados = set()  #aqui utilizamos set() para crear un set vacío
for campaña in lista_campañas:#aqui itero para estar en cada campaña
    for medio in campaña["medios"]: #accedo a cada medio en campaña
      medios_utilizados.add(medio)# utilizamos la fx add para añañdir en conjuntos
print(f" Los medios utilizados son : {medios_utilizados}")"""
""" list coomprehension de lo anterior"""
medios_utilizados = {medio for campaña in lista_campañas for medio in campaña["medios"]} #hemos utilizado {} xa crear el set directamente y dentro hemos hecho una comprensión: buscamos el medio por campaña y por cada medio en campaña acceder a sus "medios"
print(f"Los medios utilizados son :{medios_utilizados}") #imprimimos

### Ejercicio 3:
### Descripción del ejercicio:
""" piden que averiguemos cual es el medio más utilizado

### Pasos a seguir:

1. **Inicializamos el Diccionario de Conteo de Medios:**
   - Creamos un diccionario vacío llamado `conteo_medios` en el que almacenaremos el conteo de cada medio utilizado en las campañas. 
2. **Iteramos sobre Cada Campaña y Actualizamos el Conteo de Medios:**
   - Utilizamos un bucle `for` para iterar sobre cada campaña en la lista `lista_campañas`.
   - Dentro de este bucle, usamos otro bucle `for` para iterar sobre cada medio presente en la lista de medios de la campaña actual (`for medio in campaña['medios']`).
   - Verificamos si el medio ya está presente en el diccionario `conteo_medios`.
     - Si el medio ya está presente, incrementamos su conteo en 1.
     - Si el medio no está presente, lo agregamos al diccionario con un conteo inicial de 1.

3. **Encontramos el Medio Más Usado:**
   - Después de haber actualizado el conteo de cada medio, encontramos el medio con el conteo más alto dentro del diccionario usando la función `max()` con el argumento `key=conteo_medios.get`. Esto nos da el medio más utilizado en las campañas.

4. **Imprimimos el Resultado:**
   - Imprimimos el diccionario `conteo_medios` para mostrar el conteo de cada medio utilizado en todas las campañas.
   - Imprimimos el medio más usado en las campañas usando la variable `medio_mas_usado`.

Este código nos permite determinar qué medio fue más utilizado en las campañas publicitarias, proporcionando un análisis del uso de medios en las estrategias de publicidad del año pasado.
"""
conteo_medios= {}
for campaña in lista_campañas:
  for medio in campaña['medios']:
    if medio in conteo_medios:
      conteo_medios[medio] += 1
    else:
      conteo_medios[medio] =1
medios_mas_usados = max( conteo_medios, key= conteo_medios.get)
print( f"los medios mas usados son: {medios_mas_usados}")
print(conteo_medios)

### Ejercicio 4:
### Descripción del ejercicio:
"""Nos piden que calculemos el gasto total de todas las campañas del año pasado:

### Pasos a seguir: 

1. **Creamos la variable de gasto total:**
   - Comenzamos definiendo una variable llamada `gasto_total` en la que almacenaremos la suma de los presupuestos de todas las campañas. El valor inicial tiene que ser 0.

2. **Utilizamos un bucle `for` para sumar los presupuestos de cada campaña:**
   - Empleamos un bucle `for` para iterar a través de cada campaña en nuestra lista `lista_campañas`.
   - Durante cada iteración, sumamos el presupuesto de la campaña actual al total almacenado en la variable `gasto_total`.

3. **Imprimimos el gasto total:**
   - Una vez que hemos calculado la suma de todos los presupuestos, imprimimos el valor de `gasto_total` utilizando la función `print()`.
   - Esta impresión proporciona el gasto total de todas las campañas.

---"""
gasto_total = 0
for campaña in lista_campañas:
  gasto_total += campaña['presupuesto'] 
print(f"el gasto total de las campañasa es {gasto_total}")

"""Ejercicio 5:
### Descripción del ejercicio:
Se nos pide calcular las conversiones de cada campaña multiplicando el número de personas alcanzadas por la tasa de conversión y luego imprimir el nombre de cada campaña junto con el número de conversiones.

### Pasos a seguir:

1. **Cálculo de las Conversiones:**
   - Iteramos a través de cada campaña en la lista `lista_campañas`.
   - Para cada campaña, calculamos las conversiones multiplicando el valor de `"personas_alcanzadas"` por el valor de `"tasa_conversion"`.
   - El resultado se almacena en la clave `"conversiones"` dentro del diccionario de cada campaña."""  
for campaña in lista_campañas:
  campaña['conversiones']=int(campaña["personas_alcanzadas"]* campaña["tasa_conversion"])
  print (f" campaña :{campaña['nombre']}:  conversiones : {campaña["conversiones"]}")

### Ejercicio 6:
### Descripción del ejercicio:
"""Nos piden que busquemos las campañas con mayor tasa de conversión

### Pasos a seguir:
1. **Inicializamos las variables:**
   - Comenzamos inicializando las variables `mayor_tasa_conversion` y `campaña_buscada`. `mayor_tasa_conversion` se utiliza para almacenar la tasa de conversión más alta encontrada hasta el momento, mientras que `campaña_buscada` guarda el nombre de la campaña (o campañas) con la tasa de conversión más alta.
   - También inicializamos la variable `indice` en 0, que usaremos para recorrer la lista de campañas.

2. **Iteramos a través de las campañas:**
   - Utilizamos un bucle `while` para recorrer la lista de campañas hasta que hayamos examinado todas las campañas.
   - Durante cada iteración, obtenemos la tasa de conversión de la campaña actual en la posición `indice` de la lista.
   
3. **Comparamos las tasas de conversión:**
   - Comparamos la tasa de conversión actual con la `mayor_tasa_conversion`.
   - Si la tasa de conversión actual es mayor que la `mayor_tasa_conversion`, actualizamos `mayor_tasa_conversion` y guardamos el nombre de la campaña en `campaña_buscada`.
   - Si la tasa de conversión actual es igual a la `mayor_tasa_conversion`, simplemente agregamos el nombre de la campaña a `campaña_buscada`.

4. **Incrementamos el índice:**
   - Incrementamos el valor de `indice` en cada iteración para pasar a la siguiente campaña en la lista.

5. **Imprimimos la campaña con la mayor tasa de conversión:**
   - Finalmente, imprimimos el nombre de la campaña (o campañas) con la mayor tasa de conversión"""
mayor_tasa_conversion = 0
campañas_buscadas= []
indice=0

while indice < len(lista_campañas):# el bucle va a estar activo mientras recorra la longitud de la lista , que es 7 campañas
   tasa_conversion_actual = lista_campañas[indice]['tasa_conversion'] #el indice es 0 porque es el valor que le dimos por lo 
   if tasa_conversion_actual > mayor_tasa_conversion:
      mayor_tasa_conversion = tasa_conversion_actual
      campañas_buscadas =  [lista_campañas[indice]['nombre']]
   elif tasa_conversion_actual == mayor_tasa_conversion:
      campañas_buscadas.append(lista_campañas[indice]['nombre'])
   indice += 1
   print(f"Las campañas buscads son: {campañas_buscadas}")

### Ejercicio 7:
### Descripción del ejercicio:
"""Queremos identificar las campañas que tienen una tasa de conversión superior a 0.03 y un presupuesto inferior a 30000.

### Pasos a seguir:

1. **Creamos una lista para almacenar las campañas seleccionadas:**
   - Inicializamos una lista llamada `campañas_seleccionadas` donde guardaremos las campañas que cumplan con las condiciones establecidas.

2. **Iteramos sobre cada campaña en la lista de campañas:**
   - Utilizamos un bucle `for` para recorrer cada campaña en la lista `lista_campañas`.

3. **Verificamos las condiciones de tasa de conversión y presupuesto:**
   - Dentro del bucle, comprobamos si la tasa de conversión de la campaña es mayor que 0.03 y si su presupuesto es inferior a 30000.
   
4. **Añadimos las campañas que cumplen las condiciones a la lista de campañas seleccionadas:**
   - Si una campaña cumple ambas condiciones, añadimos una tupla con el nombre de la campaña, su tasa de conversión y su presupuesto a la lista `campañas_seleccionadas`.


5. **Imprimimos la lista de campañas seleccionadas:**
   - Finalmente, imprimimos la lista de campañas seleccionadas que cumplen con las condiciones especificadas utilizando la función `print()`."""
campañas_seleccionadas =[]
for campaña in lista_campañas:
  if campaña["tasa_conversion"] > 0.03 and campaña['presupuesto'] < 30000 :
   campañas_seleccionadas.append((campaña['nombre'],campaña['tasa_conversion'],campaña['presupuesto']))

print(f"Las campañas seleccionadas son {campañas_seleccionadas}")

