def iniciar_partida ():
   tablero = [[" "  for i in range (3)] for i in range(3)]
   jugador_actual= "x"
   return tablero, jugador_actual

def imprimir_tablero(tablero):

    print('   0  1  2 ')
    print('  ---------')
    for iterador in range(len(tablero)):
        print(str(iterador)+ ' ' + ' | '.join(tablero[iterador]))
        print('  ' + ('-'*9))

def pedir_posicion():

    fila = int(input("Introduce coordenada de la fila (0, 1, 2): "))
    columna = int(input("Introduce coordenada de la columna (0, 1, 2): "))

    return fila, columna

def colocar_casilla(fila, columna, tablero, jugador_actual):

    if tablero[fila][columna] == " ":
        tablero[fila][columna] = jugador_actual
        return True
    return False

def comprobar_ganador(tablero, jugador):

    for i in range(len(tablero)):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True
        
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 -i] == jugador for i in range(3)):
        return True
        
    return False


def tablero_lleno(tablero):

    return all(all(casilla != " " for casilla in fila) for fila in tablero)


def tres_en_linea():

    tablero, jugador_actual = iniciar_partida()

    print("¡Bienvenido al Tres en línea!")

    imprimir_tablero(tablero)

    while(True):

        print(f"Turno de jugador {jugador_actual}")

        try:
            fila, columna = pedir_posicion()

            if colocar_casilla(fila, columna, tablero, jugador_actual):
                print("Has colocado tu casilla")

                imprimir_tablero(tablero)

                if comprobar_ganador(tablero, jugador_actual):
                    print(f"Gana {jugador_actual}!")
                    break

                elif tablero_lleno(tablero):
                    print("Empate")
                    break
                
                if jugador_actual == "X":
                    jugador_actual = "O"
                else:
                    jugador_actual = "X"
            else:
                print("Casilla ocupada. Reintentalo!!")
           

        except ValueError: 
            print('Tipo de dato incorrecto!! Reintentalo!!')
            
        except IndexError: 
            print('Coordenadas no validas!! Reintentalo!!')

if __name__ == "__main__":
    tres_en_linea()


   

