##EJERCICIO YA REALIZADO EN POO 1
from datetime import datetime,timedelta

class Libro:
    def __init__(self,título,autor,precio):
      """ Inicializa un libro con los atributos titulo autor precioParaqmetros(título, autor y precio) """
      self.título = título
      self.autor = autor
      self.precio = precio
      self.cantidad =0
  #Definimos métodos para la clase Libro:
    def establecer_cantidad(self):
         """ Fx para ingresar la cantidad de libros con las caracteristicas del mismo """
         """ Ingresar un número positivo """
         while True:
            try:
                cantidad = int(input(f"Ingrese la cantidad del libro con título {self.título}: ")) 
                if cantidad <0:
                    print(f"La cantidad no puede  ser negativa, por favor intentelo de nuevo")
                else :
                    # Asignamos la cantidad al atributo 'cantidad'
                    self.cantidad = cantidad #hemos introducido el atributo en la clase ibro
                    break
            except ValueError:
                print(f"Debe introdcir un numero")

             
    def info_libro(self) :
        info =""
        info += "Título:"+ self.título + "\n"
        info += "Autor:" + self.autor + "\n"
        info += "Precio:" + str(self.precio) + "\n"
        info += "Cantidad:" + str(self.cantidad) + "\n"
        return info
  
libro_1= Libro("La Comunidad del Anillo","J.R.R.Tolkien",29.99)
print(libro_1.info_libro())
libro_1.establecer_cantidad()
print(libro_1.info_libro())
""" Hacemos las subclases  `LibroFisico` y  `AudioLibro """
class LibroFísico(Libro):
    def __init__(self, título, autor, precio,categoría, peso):
        super().__init__(título,autor,precio)
        self.categoría= categoría
        self.peso= peso

    def envío(self,días_envío =5):# especificando el valor en dias de envío lo tomara por defecto, si cambia lo indicamos cuando llamemos a la fx
        hoy =datetime.now() # esta fx now() de la libreria datetime coge la fecha de ahora( hemos importado la libreria al comiemzo del codigo) 
        fecha_entrega = hoy + timedelta(days= días_envío)
        return fecha_entrega
    def info_libro(self):
        info_libro= super().info_libro()
        info_libro += "Categoría" + self.categoría +"\n"
        info_libro += "Peso" + str(self.peso )+"\n"
        info_libro += "Fecha_entrega" + str(self.envío().strftime("%Y-%m-%d")) +"\n"# llamo al metodo de envio para q me lo calcule y ademas con strftime formateo la fecha hoy que viene con segundo para q solo aparezca el años mes y dia
        return info_libro

class AudioLibro(Libro):
    def __init__(self, título, autor, precio, categoría, duración):
        super().__init__(título, autor, precio)
        self.categoría = categoría
        self.duración = duración

    def obtener_duración(self):
        horas = str(self.duración// 3600)
        minutos = str((self.duración % 3600) // 60) # % estamos obteniendo el resto de 360 e las hras
        segundos = str(self.duración % 60)
        duracion_formateada= horas + ":" + minutos + ":" + segundos
        return duracion_formateada
    
    def info_libro(self):
        info_libro= super().info_libro()
        info_libro += "Categoría" + self.categoría +"\n"
        info_libro += "Duración en segundos" + str(self.duración )+"\n"
        info_libro += "Duración" + self.obtener_duración() +"\n"# llamo al metodo de obtener duración formateada
        return info_libro


##EJERECIOCIO POO parte 2
##2.6 CREAMOS CLASE DE ECOMMERCE PARA SISTEMA DE COMERCIO ELECTRONICO
class ECommerce:
    def __init__(self):
        self.carrito = []
        self.inventario = {}
## 2.7 :MÉTODOS DE ITERACCION DEL TRABAJADOR CON EL ECOMMERCE 
    def agregar_al_inventario(self,producto):
        """Añade producto al inventario , que es una lista vacía,tomando el título en minúsculas como valor, y su key es producto"""
        self.inventario[producto.título.lower()]=producto
                                
    def  ver_producto (self,nombre_producto):
        """ para ver el producto y su info detallada siempre y cuando esté en el inventario"""
        nombre_producto=self.nombre_producto.strip().lower()
         # fx strip,Elimina los espacios en blanco al principio y al final del nombre y  fxlower()convierte a minúscula
        #Verificamos si está en el inventario: si True mostramos info y si False mostramos mensaje erro
        if nombre_producto in self.inventario:
            producto= self.inventario[nombre_producto] 
            print(producto.info_libro())
        else:
            print(f"El producto {nombre_producto} no está en el inventario")
    
    def ver_inventario (self):
        print('\n Iventario productos:')
        for producto in self.inventario.values(): #para cada clave valor , la clave aqui es el producto y el valor el título
            print(producto.info_libro()) #le pido que me muestre la info de cada producto que hay en el inventario{}

##2.8 METODOS DE INTERACCION DEL CLIENTE CON EL ECOMMERCE
    def agregar_al_carrito (self,nombre_producto):
        nombre_producto = nombre_producto.strip().lower() 
        if nombre_producto in self.inventario :
            producto =self.inventario[nombre_producto]
            if producto.cantidad >0:
                    self.carrito.append(producto)
                    self.inventario[nombre_producto].cantidad= -1
                    print(f"El producto: {nombre_producto} ha sido añadido al carrito con éxito")
                   
            else:
                 print(f"No hay stock del producto: {nombre_producto}")   
    def calcular_precio_total(self):
        """sumamos los precios de todos los productos que hay en el carrito"""
        precio_total= sum(producto.precio for producto in self.carrito)#
        return precio_total
    def pagar(self):
       while True:
             try:
                 monto = float(input("Ingrese el monto: "))
                 if monto > self.calcular_precio_total():
                  cambio = monto - self.calcular_precio_total()
                  print(f"¡Pago exitoso !Su cambio es:{cambio}€")
                  self.carrito=[]
                  break
                 else:
                      print("El monto ingresado no es suficiente")
             except ValueError:
               print(" el valor ingresado no es correcto")
    def ver_carrito(self): 
       if len(self.carrito)>0: 
        print("Productos del carrito")   
        for producto in self.carrito:
           print(f"\n Título: {producto.título}")
           print(f"\n Precio Total a pagar: {self.calcular_precio_total()}€")
       else:
            print("carrito vacío")
  
  ## 2.9
  ##EJEMPLOS DE USO

# Creación de instancia de ECommerce
ecommerce = ECommerce() 

# Ingreso de libros al inventario (simulado como trabajador)
# Crea un libro físico
libro1 = LibroFísico("La Comunidad del Anillo", "J.R.R Tolkien", 29.99, "Libro físico", "980 g")
# Solicita al usuario ingresar la cantidad de libros disponibles  
libro1.establecer_cantidad()  
# Agrega el libro al inventario de la tienda
ecommerce.agregar_al_inventario(libro1)  
# Crea un audiolibro
libro2 = AudioLibro("El codigo Da Vinci", "Dan Brown", 24.95, "Audio libro", 36000)
# Solicita al usuario ingresar la cantidad de audiolibros disponibles  
libro2.establecer_cantidad()  
# Agrega el audiolibro al inventario de la tienda
ecommerce.agregar_al_inventario(libro2)  

# Visualización del inventario (opcional)
ecommerce.ver_inventario()

# Simulación de la compra por parte de un cliente
print("\n¡Bienvenido a nuestra tienda en línea!")
while True:
    # Solicita al cliente que elija un producto o finalice la compra
    opcion = input("¿Qué producto deseas agregar al carrito? (Escribe 'fin' para pagar y salir): ") 
    # Verifica si el cliente ha decidido finalizar la compra 
    if opcion.lower() == "fin":  
        ecommerce.ver_carrito()
        ecommerce.pagar()
        # Sale del bucle mientras después de realizar el pago 
        break  
    else:
        # Agrega el producto seleccionado por el cliente al carrito de compras
        ecommerce.agregar_al_carrito(opcion)

# Muestra nuevamente los productos en el carrito de compras después de la compra
ecommerce.ver_carrito()  
# Muestra el inventario completo después de la compra
ecommerce.ver_inventario()  
