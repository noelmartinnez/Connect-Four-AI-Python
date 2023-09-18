from tablero import *

PROFUNDIDAD = 3     # En realidad, es esta profundidad + 1, ya que el primer nivel lo hago en juega. En profundidad 6 juega de locos (poner 5 aquí)   
ALPHA = -100000000
BETA = 100000000

# Devuelve el número de la primera fila vacia de la columna pasada como parámetro
def busca(tablero, columna):
    i = 0
    while i < tablero.getAlto() and tablero.getCelda(i,columna) == 0:          
        i += 1      
    i -= 1
   
    return i

# MAX es la maquina (suma en la funcion de evaluacion) y MIN es la persona (resta en la funcion de evaluacion)
# Esta función cambia el valor de "posición" y poner la posición que llevará a la mejor jugada
def juega(tablero, posicion):  
    mejorJugada = -100000   

    for columna in range(0,tablero.getAncho()):     
        fila = busca(tablero,columna)     # Saco la primera fila vacía de cada columna, es -1 si la columna está llena
        
        if fila != -1:
            nuevoTablero = Tablero(tablero)     # Copia del tablero actual para no trabajar sobre la partida en curso
            nuevoTablero.setCelda(fila,columna,2)     # La máquina hace su primer movimiento       
            valorJugada = V(nuevoTablero,0,False,ALPHA,BETA)    

            if valorJugada > mejorJugada:
                mejorJugada = valorJugada
                posicion[0] = fila
                posicion[1] = columna
    
#Minimax   
def V(tablero, profundidad, MAX, alpha, beta):
    if profundidad == PROFUNDIDAD:     # Nos pondriamos en los nodos hoja, y con la recursividad subimos en el árbol 
        return tablero.evaluarJugada()
    else:
        if MAX:     
            mejorValor = -1000000
            
            for columna in range(0,tablero.getAncho()):
                fila = busca(tablero,columna)
        
                if fila != -1:
                    nuevoTablero = Tablero(tablero)
                    nuevoTablero.setCelda(fila,columna,2)     
                    valor = V(nuevoTablero,profundidad+1,False,alpha,beta)
                    mejorValor = max(mejorValor,valor)  
                    alpha = max(alpha,mejorValor)
                    
                    if beta <= alpha:
                        break
                    
            return mejorValor  
        else:     
            mejorValor = 1000000
            
            for columna in range(0,tablero.getAncho()):
                fila = busca(tablero,columna)
        
                if fila != -1:
                    nuevoTablero = Tablero(tablero)
                    nuevoTablero.setCelda(fila,columna,1)     
                    valor = V(nuevoTablero,profundidad+1,True,alpha,beta)
                    mejorValor = min(mejorValor,valor)
                    beta = min(beta,mejorValor)
                    
                    if beta <= alpha:
                        break
                    
            return mejorValor