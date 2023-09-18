class Tablero:    
    def __init__(self, tabPadre):
        self.ancho = 8     # Columnas
        self.alto = 7     # Filas
        self.tablero = []

        if tabPadre == None:     # Si está vacio el tablero pasado por parámetro, inicializamos todas las posiciones a 0
            for i in range(self.alto):           
                self.tablero.append([])
                for j in range(self.ancho):
                    self.tablero[i].append(0)
        else:     # Si no está vacio, copiamos el tablero pasado como parametro al nuevo creado
            for i in range(self.alto):           
                self.tablero.append([])
                for j in range(self.ancho):
                    self.tablero[i].append(tabPadre.getCelda(i,j))          
        
    def __str__(self):    
        salida = "  0 1 2 3 4 5 6 7\n"

        for f in range(self.alto):
            salida += str(f) + " "
            for c in range(self.ancho):         
                if self.tablero[f][c] == 0:
                    salida += ". "
                elif self.tablero[f][c] == 1:
                    salida += "1 "
                elif self.tablero[f][c] == 2:
                    salida += "2 "
            salida += "\n"
        return salida
                
    def getAncho(self):     # Devuelve el ancho
        return self.ancho
    
    def getAlto(self):     # Devuelve el alto
        return self.alto
    
    def getCelda(self, fila, col):     # Devuelve una celda
        if col > 7 or fila > 6 or col < 0 or fila < 0:
            return "Fuera del tablero"
        else:
            return self.tablero[fila][col]
    
    def setCelda(self, fila, col, val):     # Modifica una celda. El valor puede ser 0,1,2
        self.tablero[fila][col]=val   
    
    # Detecta si hay 4 fichas en línea y devuelve el bando ganador, o 0 si no hay ganador todavía
    def cuatroEnRaya(self):
        i = 0     # Iterador del alto    
        fin = False
        ganador = 0
        
        while not fin and i < self.getAlto():
            j = 0     # Iterador del ancho
            while not fin and j < self.getAncho():
                casilla=self.getCelda(i,j)

                if casilla != 0:     # Si la casilla no está vacia, comprueba si las de su alrededor son del mismo tipo 
                    if (j+3) < self.getAncho():     # Búsqueda en horizontal
                        if self.getCelda(i,j+1) == casilla and self.getCelda(i,j+2) == casilla and self.getCelda(i,j+3) == casilla: 
                            ganador = casilla
                            fin = True

                    if (i+3) < self.getAlto():     # Búsqueda en vertical
                        if self.getCelda(i+1,j) == casilla and self.getCelda(i+2,j) == casilla and self.getCelda(i+3,j) == casilla: 
                            ganador = casilla
                            fin = True
                    
                    if (i+3) < self.getAlto():     # Búsqueda en diagonal
                        if (j-3) >= 0:
                            if self.getCelda(i+1,j-1) == casilla and self.getCelda(i+2,j-2) == casilla and self.getCelda(i+3,j-3) == casilla:  
                                ganador = casilla
                                fin = True
                        if (j+3) < self.getAncho():
                            if self.getCelda(i+1,j+1) == casilla and self.getCelda(i+2,j+2) == casilla and self.getCelda(i+3,j+3) == casilla:  
                                ganador = casilla
                                fin = True
                j += 1 
            i += 1
        return ganador   
    
    def horizontal(self, i, j, casilla):
        valor = 0

        if (j+1) < self.getAncho():     
            if self.getCelda(i,j+1) == casilla: 
                if self.getCelda(i,j+2) == 0 and self.getCelda(i,j+3) == casilla and self.getCelda(i+1,j+2) != 0:
                    if casilla == 2:
                        valor += 1000
                    else:
                        valor -= 1500
                elif self.getCelda(i,j+2) == 0 and self.getCelda(i+1,j+2) != 0:
                    if casilla == 2:
                        valor += 100
                    else:
                        valor -= 150
                else:
                    if casilla == 2:
                        valor += 10
                    else:
                        valor -= 15
        
        if (j-1) >= 0:
            if self.getCelda(i,j-1) == casilla: 
                if self.getCelda(i,j-2) == 0 and self.getCelda(i,j-3) == casilla and self.getCelda(i+1,j-2) != 0:
                    if casilla == 2:
                        valor += 1000
                    else:
                        valor -= 1500
                elif self.getCelda(i,j-2) == 0 and self.getCelda(i+1,j-2) != 0:
                    if casilla == 2:
                        valor += 100
                    else:
                        valor -= 150
                else:
                    if casilla == 2:
                        valor += 10
                    else:
                        valor -= 15

        if (j+2) < self.getAncho():   
            if self.getCelda(i,j+1) == casilla and self.getCelda(i,j+2) == casilla: 
                if self.getCelda(i,j+3) == 0 and self.getCelda(i+1,j+3) != 0:
                    if casilla == 2:
                        valor += 1000
                    else:
                        valor -= 1500
                else:
                    if casilla == 2:
                        valor += 100
                    else:
                        valor -= 150

        if (j-2) >= 0:
            if self.getCelda(i,j-1) == casilla and self.getCelda(i,j-2) == casilla: 
                if self.getCelda(i,j-3) == 0 and self.getCelda(i+1,j-3) != 0:
                    if casilla == 2:
                        valor += 1000
                    else:
                        valor -= 1500
                else:
                    if casilla == 2:
                        valor += 100
                    else:
                        valor -= 150

        if (j+3) < self.getAncho():   
            if self.getCelda(i,j+1) == casilla and self.getCelda(i,j+2) == casilla and self.getCelda(i,j+3) == casilla: 
                if casilla == 2:
                    valor += 10000
                else:
                    valor -= 15000
        
        return valor
    
    def vertical(self, i, j, casilla):
        valor = 0

        if (i+1) < self.getAlto():     # (i+1) mira hacia abajo. No compruebo si es 0 la tercera porque no es posible que sea 0 al ser vertical
            if self.getCelda(i+1,j) == casilla: 
                if casilla == 2:
                    valor += 10
                else:
                    valor -= 15

        if (i-1) >= 0:     #(i-1) mira hacia arriba
            if self.getCelda(i-1,j) == casilla: 
                if self.getCelda(i-2,j) == 0:
                    if casilla == 2:
                        valor += 100
                    else:
                        valor -= 150
                else:
                    if casilla == 2:
                        valor += 10
                    else:
                        valor -= 15

        if (i+2) < self.getAlto():     # Mira hacia abajo   
            if self.getCelda(i+1,j) == casilla and self.getCelda(i+2,j) == casilla: 
                if casilla == 2:
                    valor += 100
                else:
                    valor -= 150
        
        if (i-2) >= 0:     # Mira hacia arriba
            if self.getCelda(i-1,j) == casilla and self.getCelda(i-2,j) == casilla: 
                if self.getCelda(i-3,j) == 0:
                    if casilla == 2:
                        valor += 1000
                    else:
                        valor -= 1500
                else:
                    if casilla == 2:
                        valor += 100
                    else:
                        valor -= 150

        if (i+3) < self.getAlto():    
            if self.getCelda(i+1,j) == casilla and self.getCelda(i+2,j) == casilla and self.getCelda(i+3,j) == casilla: 
                if casilla == 2:
                    valor += 10000
                else:
                    valor -= 15000
        
        return valor

    def diagonal(self, i, j, casilla):
        valor = 0

        if (i+1) < self.getAlto():
            if (j+1) < self.getAncho():  
                if self.getCelda(i+1,j+1) == casilla:
                    if self.getCelda(i+2,j+2) == 0 and self.getCelda(i+3,j+3) == casilla and self.getCelda(i+3,j+2) != 0:  
                        if casilla == 2:
                            valor += 1000
                        else:
                            valor -= 1500
                    elif self.getCelda(i+2,j+2) == 0 and self.getCelda(i+3,j+2) != 0:  
                        if casilla == 2:
                            valor += 100
                        else:
                            valor -= 150
                    else:
                        if casilla == 2:
                            valor += 10
                        else:
                            valor -= 15

            if (j-1) >= 0:  
                if self.getCelda(i+1,j-1) == casilla:  
                    if self.getCelda(i+2,j-2) == 0 and self.getCelda(i+3,j-3) == casilla and self.getCelda(i+3,j-2) != 0:
                        if casilla == 2:
                            valor += 1000
                        else:
                            valor -= 1500
                    elif self.getCelda(i+2,j-2) == 0 and self.getCelda(i+3,j-2) != 0:
                        if casilla == 2:
                            valor += 100
                        else:
                            valor -= 150
                    else:
                        if casilla == 2:
                            valor += 10
                        else:
                            valor -= 15

        if (i-1) >= 0:
            if (j-1) >= 0:  
                if self.getCelda(i-1,j-1) == casilla:  
                    if self.getCelda(i-2,j-2) == 0 and self.getCelda(i-3,j-3) == casilla and self.getCelda(i-1,j-2) != 0:
                        if casilla == 2:
                            valor += 1000
                        else:
                            valor -= 1500
                    elif self.getCelda(i-2,j-2) == 0 and self.getCelda(i-1,j-2) != 0:
                        if casilla == 2:
                            valor += 100
                        else:
                            valor -= 150
                    else:
                        if casilla == 2:
                            valor += 10
                        else:
                            valor -= 15
            
            if (j+1) < self.getAncho():
                if self.getCelda(i-1,j+1) == casilla:
                    if self.getCelda(i-2,j+2) == 0 and self.getCelda(i-3,j+3) == casilla and self.getCelda(i-1,j+2) != 0:
                        if casilla == 2:
                            valor += 1000
                        else:
                            valor -= 1500
                    elif self.getCelda(i-2,j+2) == 0 and self.getCelda(i-1,j+2) != 0:
                        if casilla == 2:
                            valor += 100
                        else:
                            valor -= 150
                    else:
                        if casilla == 2:
                            valor += 10
                        else:
                            valor -= 15

        if (i+2) < self.getAlto(): 
            if (j+2) < self.getAncho():   
                if self.getCelda(i+1,j+1) == casilla and self.getCelda(i+2,j+2) == casilla:
                    if self.getCelda(i+3,j+3) == 0 and self.getCelda(i+4,j+3) != 0:  
                        if casilla == 2:
                            valor += 1000
                        else:
                            valor -= 1500
                    else:
                        if casilla == 2:
                            valor += 100
                        else:
                            valor -= 150

            if (j-2) >= 0:  
                if self.getCelda(i+1,j-1) == casilla and self.getCelda(i+2,j-2) == casilla:  
                    if self.getCelda(i+3,j-3) == 0 and self.getCelda(i+4,j-3) != 0:
                        if casilla == 2:
                            valor += 1000
                        else:
                            valor -= 1500
                    else:
                        if casilla == 2:
                            valor += 100
                        else:
                            valor -= 150

        if (i-2) >= 0:
            if (j-2) >= 0:  
                if self.getCelda(i-1,j-1) == casilla and self.getCelda(i-2,j-2) == casilla:  
                    if self.getCelda(i-3,j-3) == 0 and self.getCelda(i-2,j-3) != 0:
                        if casilla == 2:
                            valor += 1000
                        else:
                            valor -= 1500
                    else:
                        if casilla == 2:
                            valor += 100
                        else:
                            valor -= 150
            
            if (j+2) < self.getAncho():   
                if self.getCelda(i-1,j+1) == casilla and self.getCelda(i-2,j+2) == casilla:
                    if self.getCelda(i-3,j+3) == 0 and self.getCelda(i-2,j+3) != 0:  
                        if casilla == 2:
                            valor += 1000
                        else:
                            valor -= 1500
                    else:
                        if casilla == 2:
                            valor += 100
                        else:
                            valor -= 150
        
        if (i+3) < self.getAlto():    
            if (j-3) >= 0:  
                if self.getCelda(i+1,j-1) == casilla and self.getCelda(i+2,j-2) == casilla and self.getCelda(i+3,j-3) == casilla:  
                    if casilla == 2:
                        valor += 10000
                    else:
                        valor -= 15000
                                    
            if (j+3) < self.getAncho():   
                if self.getCelda(i+1,j+1) == casilla and self.getCelda(i+2,j+2) == casilla and self.getCelda(i+3,j+3) == casilla:  
                    if casilla == 2:
                        valor += 10000
                    else:
                        valor -= 15000
                        
        return valor

    # Función de evaluación   
    def evaluarJugada(self):
        i = 0      
        casilla = 0
        valor = 0

        while i < self.getAlto():
            j = 0    
            while j < self.getAncho():
                casilla = self.getCelda(i,j)
                if casilla != 0:   
                    # HORIZONTAL
                    valor += self.horizontal(i,j,casilla) 
                    
                    # VERTICAL
                    valor += self.vertical(i,j,casilla) 

                    # DIAGONAL
                    valor += self.diagonal(i,j,casilla)
                j += 1  
            i += 1
        return valor