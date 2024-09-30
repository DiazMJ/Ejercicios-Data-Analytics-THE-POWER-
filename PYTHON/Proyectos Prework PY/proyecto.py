""" Gestor de tareas:
1 debemos definir la clase asignado a la Tarea atributo y metodos asociados:"""

class Tarea():
  def __init__ (self, descripcion,fecha_vencimiento,estado):
    self.descripcion= descripcion
    self.fecha_vencimiento= fecha_vencimiento
    self.estado= estado
    
Tareas =[]  
def añadir_tarea():
    descripcion = input("Descripcion tarea")
    fecha_vencimiento = input( "Indica fecha de vencimiento:dia/mes/año en números de dos cifras ")
    estado=input("Añade C si está completada la tarea")
    nueva_tarea = Tarea(descripcion,fecha_vencimiento,estado)
    Tarea.append(nueva_tarea)
    print("Tarea añadida")

def indexar_tarea():
    for indice, Tarearea in enumerate(Tarea):
      print(f"{indice}. Descripcion {Tarea.descripcion}. Fecha_vencimiento{Tarea.fecha_vencimiento}. Estado{Tarea.estado}")

def marcar_completada():
     print (indexar_tarea(Tarea))
     elección_tarea= input("Indica el Indice de la tarea a marcar como completada con una C ")
     while True:
      return("Tarea completada")
     else :
      return ("Formato no válido")

def ver_pendientes():
   if Tarea.estado !="C":
     print(Tareas)

#3 paso realizar el menu
def gestor_tareas_Marita():
  print("Bienvenido al Gestor de Tareas de Marita")
  while True :
    print (' Menu:')
    print('1 .Descripcion Tarea, 2. Ver tareas, 3.Marcar Tareas Completadas, 4 Ver tareas Pendientes, 5. Salir del Gestor ')

    menu =int(input('Selecciona una opcion: '))
    if menu == 5:
      print( "¿Buen trabajo, chao!")
      break
    elif menu == 1:
      añadir_tarea()
    elif menu == 2:
      indexar_tarea()
    elif menu == 3:
      marcar_completada
    elif menu == 4:
      ver_pendientes()

if __name__ == "__main__":
  gestor_tareas_Marita()







