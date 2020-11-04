import random
columnas = 8
renglones = 8
tablero_secreto = []
tablero = []

def puntuacion():
    puntos = 0
    for c in range(columnas):
        for r in range(renglones):
            if tablero_secreto[c][r] == "X":
                puntos += 1
    print ("minas restantes: ", +puntos)
### contar
def contar():
    numero = 0
    if entrada_renglon > 0:
        if tablero_secreto[entrada_renglon-1][entrada_columna] == "X":
            numero += 1
            
    if entrada_renglon < 7:
        if tablero_secreto[entrada_renglon+1][entrada_columna] == "X":
            numero += 1
    
    if entrada_columna < 7:
        if tablero_secreto[entrada_renglon][entrada_columna+1] == "X":
            numero += 1
    
    if entrada_columna > 0:
        if tablero_secreto[entrada_renglon][entrada_columna-1] == "X":
            numero += 1
    
    if entrada_renglon > 0 and entrada_columna < 7:
        if tablero_secreto[entrada_renglon-1][entrada_columna+1] == "X":
            numero += 1
        
    if entrada_renglon < 7 and entrada_columna < 7:
        if tablero_secreto[entrada_renglon+1][entrada_columna+1] == "X":
            numero += 1
        
    if entrada_columna > 0 and entrada_renglon <7:
        if tablero_secreto[entrada_renglon+1][entrada_columna-1] == "X":
            numero += 1
            
    if entrada_renglon > 0 and entrada_columna > 0:
        if tablero_secreto[entrada_renglon-1][entrada_columna-1] == "X":
            numero += 1
    
    return numero

### tablero secreto
rando = ["0", "0", "0", "X"]

for r in range (renglones):
    renglon = []
    for c in range (columnas):
        aleatorio = random.choice(rando)
        renglon.append(aleatorio)
    tablero_secreto.append(renglon)
    print (renglon)
###tablero normal
def imprimir_tablero():
    for r in range (renglones):
        renglon = []
        for c in range (columnas):
            renglon.append(".")
        tablero.append(renglon)
            
    print (end  = "  ")
    for c in range (columnas):
        print (c, end = " ")
        
        
    for r in range (renglones):
        print ()
        print (r, end = " ")
        
        for c in range (columnas):
            print (tablero[r][c], end = " ")
            
    print ()        

def contar_extremo():
    tablero[entrada_renglon][entrada_columna] = numero
    
    imprimir_tablero()      

### inicia juego
imprimir_tablero()
while True:
    entrada_renglon = int(input("Disparo renglon (lineas horizontales): "))
    entrada_columna = int(input("Disparo columna (lineas verticales): "))
    tipo_disparo = input("'*' para poner una bandera (o presiona enter)")
    variable_temporal= tablero_secreto[entrada_renglon][entrada_columna]
    
    if tipo_disparo == "*":
        tablero[entrada_renglon][entrada_columna] = "*"
        tablero_secreto[entrada_renglon][entrada_columna] = "*"
        imprimir_tablero()
        
    else:    
        if variable_temporal == "X":
            tablero[entrada_renglon][entrada_columna] = "X"
            imprimir_tablero()
            print ("game over")
            puntuacion()
            break
            
            
        
        else:
            
            numero = contar()
            if numero == 0:
                contar_extremo()
            
            else:
                tablero[entrada_renglon][entrada_columna] = numero
                imprimir_tablero()
    puntuacion()