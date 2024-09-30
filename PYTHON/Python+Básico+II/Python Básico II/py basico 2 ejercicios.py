# DATOS DE LAS CAMPAÑAS:
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
""" ### Ejercicio 8:
### Descripción del ejercicio:
Nos piden calcular la duración en días de cada campaña publicitaria del año pasado:

### Pasos a seguir:

1. **Importamos el módulo `datetime`:**
   - Importamos la clase `datetime` del módulo `datetime` para trabajar con fechas y tiempos.

2. **Calculamos la duración de cada campaña en días:**
   - Utilizamos un bucle `for` para iterar sobre cada campaña en la lista `lista_campañas`.
   - Convertimos las fechas de inicio y fin de cada campaña de formato de cadena a objetos `datetime` utilizando la función `strptime()` de la clase `datetime`.
   - Calculamos la diferencia entre las fechas de inicio y fin para obtener la duración de la campaña en días, y almacenamos este valor en la clave `"duracion_dias"` del diccionario de cada campaña.

3. **Imprimimos la duración de cada campaña:**
   - Utilizamos otro bucle `for` para iterar sobre cada campaña en la lista `lista_campañas`.
   - Imprimimos el nombre de la campaña junto con su duración en días utilizando la función `print()`. Esto nos proporciona información sobre la duración de cada campaña en días.
---"""
from datetime import datetime as dt
for campaña in lista_campañas:
  inicio =dt.strptime(campaña['inicio'], '%Y-%m-%d')
  fin = dt.strptime(campaña['fin'],'%Y-%m-%d')
  campaña['duracion_dias'] = (fin-inicio).days
for campaña in lista_campañas:
  print(f"La duracion de cada campaña es: {campaña['nombre']}: {campaña['duracion_dias']}")

  ### Ejercicio 9:
### Descripción del ejercicio:
"""Estamos buscando la campaña más larga dentro de nuestra lista de campañas publicitarias:

### Pasos a seguir:

1. **Inicializamos una tupla para almacenar la campaña más larga:**
   - Creamos una tupla llamada `campaña_mas_larga` con dos elementos: un string vacío para almacenar el nombre de la campaña y un entero inicializado en 0 para almacenar la duración de la campaña más larga.

2. **Iteramos sobre cada campaña en la lista de campañas:**
   - Utilizamos un bucle `for` para recorrer cada campaña en la lista `lista_campañas`.

3. **Comparamos la duración de cada campaña con la campaña más larga registrada:**
   - En cada iteración, comparamos la duración de la campaña actual con la duración almacenada en `campaña_mas_larga[1]`, que representa la duración de la campaña más larga registrada hasta el momento.

4. **Actualizamos la campaña más larga si es necesario:**
   - Si la duración de la campaña actual es mayor que la duración de la campaña más larga registrada, actualizamos la tupla `campaña_mas_larga` con el nombre y la duración de la campaña actual.

5. **Imprimimos la campaña más larga encontrada:**
   - Después de completar el bucle `for`, imprimimos la tupla `campaña_mas_larga`, que contiene el nombre y la duración de la campaña más larga encontrada."""

campaña_mas_larga= ("",0)
for campaña in lista_campañas:
  if campaña['duracion_dias'] > campaña_mas_larga[1]:
    campaña_mas_larga = (campaña['nombre'],campaña['duracion_dias'])
print(f"la Campaña mas laraga es:{campaña_mas_larga}")
  


# NOS HACEN LLEGAR UNA NUEVA CAMPAÑA:
# Nuevo diccionario de campaña
nueva_campaña = {
    'nombre': 'Oferta de Verano',
    'presupuesto': 0,
    'inicio': '2024-06-01',
    'fin': '2024-08-31',
    'medios': ['Redes Sociales', 'Publicidad en línea'],
    'segmentos_objetivo': ['Familias', 'Jóvenes'],
    'personas_alcanzadas': "0",   
}
# Agregar el nuevo diccionario a la lista de campañas existente
lista_campañas.append(nueva_campaña)
print(len(lista_campañas))
### Ejercicio 10:
### Descripción del ejercicio:
"""Queremos imprimir la tasa de conversión de cada campaña en nuestra lista de campañas. Sin embargo, es posible que algunas campañas no tengan la tasa de conversión registrada.

### Pasos a seguir:

1. **Iteración sobre las Campañas:**
   - Utilizamos un bucle `for` para iterar sobre cada campaña en nuestra lista `lista_campañas`.

2. **Accedemos a la tasa de conversión:**
   - Dentro del bucle, intentamos acceder a la tasa de conversión de cada campaña.
   - Utilizamos un bloque `try-except` para manejar el posible error si no se encuentra la clave `'tasa_conversion'` en el diccionario de la campaña.

3. **Imprimimos la tasa de conversión:**
   - Si no hay errores, imprimimos la tasa de conversión de la campaña.
   - Si se produce un error `KeyError`, indicamos que la tasa de conversión no se encontró para la campaña correspondiente."""
for campaña in lista_campañas:
  try:
      tasa_conversión = campaña['tasa_conversion']
  except KeyError:
    print(f"no hay tasa de conversion para la campaña : {campaña['nombre']}")
  else :
    print(f"la tasa de conersion para la campaña{campaña['nombre']} es de {tasa_conversión}")
  
### Ejercicio 11:
### Descripción del ejercicio:

"""Queremos asegurarnos de que el valor de `personas_alcanzadas` en cada campaña sea un número válido para poder realizar cálculos numéricos con él.

### Pasos a seguir:

1. **Intentamos convertir a un númer entero:**
   - Utilizamos un bloque `try` para intentar convertir el valor de `personas_alcanzadas` a un entero.
   - Iteramos sobre cada campaña en nuestra lista `lista_campañas`.
   
2. **Conversión Exitosa:**
   - Si la conversión a entero es exitosa, continuamos con las operaciones normales dentro del bucle `for`.
   
3. **Manejo de Excepción - ValueError:**
   - Si ocurre un error durante la conversión debido a que el valor no es un número válido, se levanta una excepción `ValueError`.
   - En el bloque `except ValueError`, se imprime un mensaje indicando que el valor de `personas_alcanzadas` no es un número válido."""

for campaña in lista_campañas:
  try :
    personas_alcanzadas =int(campaña['personas_alcanzadas'])
  except ValueError:
    print(f"no es un numero valido")
  else:
    print(f"{campaña['nombre']}:{personas_alcanzadas}")
### Ejercicio 12:
### Descripción del ejercicio:

"""Queremos realizar una división entre el presupuesto y la cantidad de personas alcanzadas en cada campaña. Sin embargo, puede ocurrir un error si la cantidad de personas alcanzadas es 0 o si no es un número válido

### Pasos a seguir:

1. **Iteración sobre las Campañas:**
   - Utilizamos un bucle `for` para iterar sobre cada campaña en nuestra lista `lista_campañas`.
   
2. **Intento de División:**
   - Dentro del bucle, utilizamos un bloque `try` para intentar realizar la división entre el presupuesto y la cantidad de personas alcanzadas.
   - Convertimos la cantidad de personas alcanzadas a un entero para asegurarnos de que sea un número válido y evitar posibles errores de tipo.
   
3. **Manejo de Excepciones:**
   - Si la cantidad de personas alcanzadas es 0, se levanta una excepción `ZeroDivisionError`, indicando que no se puede dividir entre 0.
   - Si la cantidad de personas alcanzadas no es un número válido, se levanta una excepción `ValueError`, indicando que el valor no es válido para realizar la división.
   - En ambos casos, se imprime un mensaje de error que indica el problema y la campaña asociada en la que ocurrió el error"""

for campaña in lista_campañas:
  try:
    presupuesto_por_alcance = int(campaña['presupuesto'])/int(campaña['personas_alcanzadas'])
  except ZeroDivisionError:
    print(f"Para la campaña {campaña['nombre']},no se puede dividir entre cero.")
  except ValueError:
    print(f"Valor erroneo,el valo de la campaña {campaña['nombre']} no es valido para ralizar divison")
 ### Ejercicio 13:
### Descripción del ejercicio:

"""Nos han pedido que implementemos un programa en Python que permita al usuario establecer una nueva contraseña segura. La contraseña debe cumplir con los siguientes criterios para ser considerada segura:

### Pasos a seguir:

1. **Requisitos de la Contraseña:**
    - Debe contener al menos una letra mayúscula.
    - Debe contener al menos una letra minúscula.
    - Debe contener al menos un dígito numérico.

2. **Flujo del Programa:**
    - El programa solicitará repetidamente al usuario que ingrese una nueva contraseña hasta que se cumplan todos los criterios de seguridad.
    - Una vez que se ingresa una contraseña que cumple con los criterios, se solicitará al usuario que la confirme.
    - Si la contraseña de confirmación coincide con la contraseña ingresada, se imprimirá un mensaje de éxito y el programa terminará.
    - Si las contraseñas no coinciden, se solicitará al usuario que ingrese la contraseña nuevamente.

3. **Detalles del Proceso:**
    - Se utiliza un bucle `while True` para mantener la solicitud de contraseña hasta que se cumplan los criterios.
    - Se verifican los caracteres de la contraseña utilizando los métodos `isupper()`, `islower()` y `isdigit()` para comprobar la presencia de letras mayúsculas, minúsculas y dígitos numéricos respectivamente.
    - Si la contraseña ingresada no cumple con los criterios, se informa al usuario sobre los requisitos de seguridad que faltan.
    - Una vez que se establece una contraseña segura, se solicita al usuario que la confirme y se comparan las contraseñas para garantizar que coincidan.

4. **Finalización del Programa:**
    - Cuando se establece una contraseña segura y se confirma correctamente, se imprime un mensaje de éxito y el programa termina su ejecución."""

while True:
    contraseña = input("Ingresa nueva contraseña: ")
    if any(letra.isupper() for letra in contraseña) and any(letra.islower() for letra in contraseña) and any(letra.isdigit() for letra in contraseña):
      confirmar_contraseña = input('confirmar contraseña: ')
      if contraseña == confirmar_contraseña:
          print("contraseña exitosa")
          break
      else:
          print('Error de contraseña vuelva a intentarlo')
    else:
      print("la contraseña debe contener minusculas, mayusculas y numeros")






