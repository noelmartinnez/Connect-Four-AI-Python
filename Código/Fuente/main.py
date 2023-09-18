import sys, pygame
from pygame.locals import *
from tablero import *
from algoritmo import *

MARGEN = 20
TAM = 60
ROJO = (255,0,0)
AZUL = (0,0,255)
AMARILLO = (255,255,0)
NEGRO = (0,0,0)
BLANCO = (255,255,255)

#Gestiona el manejo del juego, y comprueba si ha ganado un jugador u otro en cada tirada
def main():    
    pygame.init()
    reloj = pygame.time.Clock()
    screen = pygame.display.set_mode([700,620])
    pygame.display.set_caption("Practica 1")
    game_over = False
    tablero = Tablero(None)
    col = -1

    while not game_over:     #Mientras que no se haya acabado, seguimos jugando
        for event in pygame.event.get():
            if event.type == pygame.QUIT:               
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:                
                pos = pygame.mouse.get_pos()     #Obtiene la posicion donde ha pulsado la persona con el ratón  
                colDestino = (pos[0]-(2*MARGEN))//(TAM+MARGEN)     #Calcula las coordenadas matriciales                
                fila = busca(tablero,colDestino)

                if fila != -1:     #Si en la columna donde ha pulsado el jugador, hay una fila vacia entonces se coloca               
                    tablero.setCelda(fila,colDestino,1)    

                    if tablero.cuatroEnRaya() == 1:     #Llama al metodo cuatroEnRaya() que comprueba si hay 4 fichas en línea
                        game_over = True
                        print("gana persona")               
                    else:     #Si la persona no ha ganado, juega la máquina 
                        posicion = [-1,-1]
                        juega(tablero,posicion)     #El módulo juega se encarga de llamar al algoritmo MiniMax 
                        tablero.setCelda(posicion[0],posicion[1],2)    

                        if tablero.cuatroEnRaya() == 2:     #Si después de colocar la máquina ha hecho 4 en raya, terminamos la partida 
                            game_over = True         
                            print("gana máquina") 
            
        #Código de dibujo / Interfaz grafico / Limpiar pantalla
        screen.fill(NEGRO)
        pygame.draw.rect(screen,AZUL,[MARGEN,MARGEN,660,580],0)

        for fil in range(tablero.getAlto()):
            for col in range(tablero.getAncho()):
                if tablero.getCelda(fil,col) == 0: 
                    pygame.draw.ellipse(screen,BLANCO,[(TAM+MARGEN)*col+2*MARGEN,(TAM+MARGEN)*fil+2*MARGEN,TAM,TAM],0)
                elif tablero.getCelda(fil,col) == 1: 
                    pygame.draw.ellipse(screen,ROJO,[(TAM+MARGEN)*col+2*MARGEN,(TAM+MARGEN)*fil+2*MARGEN,TAM,TAM],0)
                else:
                    pygame.draw.ellipse(screen,AMARILLO,[(TAM+MARGEN)*col+2*MARGEN,(TAM+MARGEN)*fil+2*MARGEN,TAM,TAM],0)                
                        
        for col in range(tablero.getAncho()):
            pygame.draw.rect(screen,BLANCO,[(TAM+MARGEN)*col+2*MARGEN,10,TAM,10],0)
            
        #Actualizar pantalla
        pygame.display.flip()
        reloj.tick(40)

        if game_over == True: 
            pygame.time.delay(1500)     #Retardo cuando termina la partida
    
    pygame.quit()       
 
if __name__ == "__main__":
    main()