import pygame
import sys

#   Funcion primordial de Pygame, inicializa la libreria principal
#   Si no estuviera, todas las funciones derivadas de esta libreria serian tomadas como desconocidas
#   Y se omitiria cualquier informacion relacionada con ellas
pygame.init()

#   Se declara la variable ventana, con la cual se haran multiples referencias mas adelante
#   Para escribir datos en pantalla o renderizar escenas
#   Se utiliza "set_mode" para hacer que la pantalla cumpla con las medidas Alto-Ancho especificadas
ventana = pygame.display.set_mode((820,820)) 

#   Funcion de reloj, sin uso efectivo todavia
#   Se esperaba implementarlo a forma de limitar los FPS que se renderizaban
#   Pero al ser un juego sin movimiento dinamico y solo se necesita que se renderize "de un tiron"
#   Se dejo de lado, por lomenos ahora
reloj = pygame.time.Clock()

#Mensajes Personalizados

#   Medidas de la pantalla, se usan como constante para calcular la posicion de ciertos elementos en pantalla
ancho = 820
alto = 820

#   1 Blanco 2 Negro
colorJ1 = 0
colorJ2 = 0

#   1-Peon 2-Caballo 3-Alfil 4-Torre 5-Reina 6-Rey
piezaJ1 = 0
piezaJ2 = 0

#   Contador usado para saber el turno de seleccion de fichas
Contador = 1

#   Colores R,G,B para usarse despues
negro = (0,0,0)
negro_claro = (100,100,100)

blanco = (255,255,255)
blanco_oscuro = (230,230,230)

rojo = (255,0,0)
rojo_oscuro = (240,0,0)

verde = (0,255,0)
verde_oscuro = (0,240,0)

azul = (0,0,255)

botonSalir = (226,83,52)
botonSalirClaro = (215,147,131)
botonJugar = (116,226,52)
botonJugarClaro = (172,228,139)

#   Declaracion de las piezas
indicador = pygame.image.load("indicador.png")
marcador = pygame.image.load("marcador.png")
eliminado = "eliminado.png"

torre_n = "torre_negra.png"
caballo_n = "caballo_negro.png"
alfil_n  = "alfil_negro.png"
rey_n  = "reina_negra.png"
reina_n = "rey_negro.png"
peon_n = "peon_negro.png"

#   Declaracion de las piezas
torre_b = "torre_blanca.png"
caballo_b = "caballo_blanco.png"
alfil_b  = "alfil_blanco.png"
rey_b  = "reina_blanca.png"
reina_b = "rey_blanco.png"
peon_b = "peon_blanco.png"

SeleccionandoPieza = False
Turno = 1
tiempoPartida = 40 #Segundos
tiempoTurno = 5

indicesSeleccionados = []
posicionP1 = []
posicionP2 = []

listaIndices =  [   [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]], #0
                    [[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]], #1
                    [[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7]], #2
                    [[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7]], #3
                    [[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[4,7]], #4
                    [[5,0],[5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[5,7]], #5
                    [[6,0],[6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7]], #6
                    [[7,0],[7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7]],  #7
                ]

listaPosiciones =   [   [[31,31],  [132,31],  [232,31],  [332,31],  [432,31],  [532,31],  [631,31],  [731,31]],          #0 1 2 3 4 5 6 7
                        [[31,132], [132,132], [232,132], [332,132], [432,132], [532,132], [631,132], [731,132]],   #1
                        [[31,232], [132,232], [232,232], [332,232], [432,232], [532,232], [631,232], [731,232]],   #2
                        [[31,332], [132,332], [232,332], [332,332], [432,332], [532,332], [631,332], [731,332]],   #3
                        [[31,432], [132,432], [232,432], [332,432], [432,432], [532,432], [631,432], [731,432]],   #4
                        [[31,532], [132,532], [232,532], [332,532], [432,532], [532,532], [631,532], [731,532]],   #5
                        [[31,632], [132,632], [232,632], [332,632], [432,632], [532,632], [631,632], [731,632]],   #6
                        [[31,732], [132,732], [232,732], [332,732], [432,732], [532,732], [631,732], [731,732]],   #7
                    ]

listaColisiones =   [   [[10,10], [110,10], [210,10], [310,10], [410,10], [510,10], [610,10], [710,10]],
                        [[10,110],[110,110],[210,110],[310,110],[410,110],[510,110],[610,110],[710,110]],
                        [[10,210],[110,210],[210,210],[310,210],[410,210],[510,210],[610,210],[710,210]],
                        [[10,310],[110,310],[210,310],[310,310],[410,310],[510,310],[610,310],[710,310]],
                        [[10,410],[110,410],[210,410],[310,410],[410,410],[510,410],[610,410],[710,410]],
                        [[10,510],[110,510],[210,510],[310,510],[410,510],[510,510],[610,510],[710,510]],
                        [[10,610],[110,610],[210,610],[310,610],[410,610],[510,610],[610,610],[710,610]],
                        [[10,710],[110,710],[210,710],[310,710],[410,710],[510,710],[610,710],[710,710]],
                    ] 



#   Este metodo se utiliza en la funcion seleccionColor
#   El primero es en caso que el primer usuario elija partir con las blanca
#   El segundo es por si prefiere partir con las negras
def blanco_j1():
    global colorJ1, colorJ2
    colorJ1 = 1
    colorJ2 = 2
    #print("Color 1: ",colorJ1,"Color 2: ",colorJ2)
    seleccionPieza() 

def negro_j1():
    global colorJ1, colorJ2
    colorJ1 = 2
    colorJ2 = 1
    #print("Color 1: ",colorJ1,"Color 2: ",colorJ2)
    seleccionPieza()

#   Esta funcion se utiliza en la seleccion de piezas de cada usuario
#   Recibe como parametros el numero de jugador y la pieza que se le asignara
#   Siendo 1-Peon 2-Caballo 3-Alfil 4-Torre 5-Reina 6-Rey
def setPieza(numeroJugador,numeroPieza):
    global Contador, piezaJ1,piezaJ2
    if numeroJugador == 1:
        piezaJ1 = numeroPieza
        Contador += 1
        seleccionPieza_2()
    if numeroJugador == 2:
        piezaJ2 = numeroPieza
        iniciar_Juego()
    if numeroJugador > 2: #Modificar a futuro para ser posible jugar a tablero lleno
        print("Error: El numero de jugadores es maximo 2, revisar el codigo")        


#   Funcion rescatada de la documentacion de Pygame
#   Simplifica la creacion de titulos o cualquier elemento grafico
#   Que implique un text

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#   Esta funcion recibe los parametros necesarios para crear en pantalla un boton
#   Recibe los parametros de coordenadas y tamaños para renderizar el boton
#   Ademas como su texto, color y la accion que hara si se acciona
def crearBoton(texto,PosicionX,PosicionY,Ancho,Alto,ColorActivo,ColorInactivo,colorTexto, Accion = None, Parametro1 = None, Parametro2 = None):    
    #   La primera sirve para saber en tiempo real la posicion X e Y del mouse sobre la pantalla
    movimientoM = pygame.mouse.get_pos()
    
    #   ClickM sirve para saber si el boton del click está o no presionado, y lo almacena en la variable en tiempo real
    clickM = pygame.mouse.get_pressed()
    
    #   posx,posy,ancho,alto
    #   Basicamente chequea si la posicion del mouse esta dentro de los posiciones/limites del diseño
    #   del boton, y si lo esta, hace esto
    if PosicionX+Ancho > movimientoM[0] > PosicionX and PosicionY+Alto > movimientoM[1] > PosicionY:
        pygame.draw.rect(ventana, ColorInactivo, (PosicionX,PosicionY,Ancho,Alto))

        #Si se hace click al boton y la accion a hacerse es diferente de nulo, hace esto
        if clickM[0] == 1 and Accion != None:
            #Si los parametros 1 y 2 son iguales a nada, solamente llama a la funcion
            if Parametro1 == None and Parametro2 == None:
                Accion()
                clickM[0] = 0
            # Si alguno de los parametros es diferente a nulo, checkea cual es diferente de nulo
            # y lo ejecuta dentro de la accion (funcion)
            if Parametro1 != None or Parametro2 != None:    
                if Parametro1 != None and Parametro2 != None:
                    Accion(Parametro1,Parametro2)
                    clickM[0] = 0
                if Parametro1 != None and Parametro2 == None:
                    Accion(Parametro1)
                    clickM[0] = 0
                if Parametro1 == None and Parametro2 != None:
                    Accion(Parametro2)
                    clickM[0] = 0
            
    #Si no detecta interaccion alguna con el boton, solo lo dibuja en pantalla
    #Esta parte solamente dibuja el cuadro y sus colores
    else:
        pygame.draw.rect(ventana, ColorActivo, (PosicionX,PosicionY,Ancho,Alto))

    #En este bloque se "adjunta" el titulo o texto del boton
    textoPequeño = pygame.font.Font(None,25)
    TextSurf, textRect = text_objects(texto, textoPequeño, colorTexto)
    textRect.center = ( (PosicionX+(Ancho/2)), (PosicionY+(Alto/2)) )
    ventana.blit(TextSurf, textRect)

def menu():
          
    pygame.display.set_caption("Menu Principal")
    fondo = pygame.image.load("fondo_tablero_desenfocado.png")

    inicio = True
    while inicio == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.font.init()
        textoGrande = pygame.font.Font("times-new-roman.ttf",115)
        TextSurf,TextRect =  text_objects("Ajedrez", textoGrande, negro)
        TextRect.center = ((ancho/2),200)
        ventana.blit(fondo,(0,0))
        ventana.blit(TextSurf,TextRect)

        crearBoton("Jugar", 270, 290, 300, 100, botonJugar, botonJugarClaro, negro, seleccionColor)
        crearBoton("Salir", 270, 410, 300, 100, botonSalir, botonSalirClaro, negro, quit)

        pygame.display.update()

def seleccionColor():
    pygame.display.set_caption("Seleccion de Colores")
    fondo = pygame.image.load("fondo_tablero_desenfocado.png")

    inicio = True
    while inicio == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        
        textoGrande = pygame.font.Font("freesansbold.ttf",60)
        TextSurf,TextRect =  text_objects("Jugador 1", textoGrande, negro)
        TextRect.center = ((ancho/2),200)
        ventana.blit(fondo,(0,0))
        ventana.blit(TextSurf,TextRect)

        crearBoton("Blancas", 70, 490, 300, 150, blanco, blanco_oscuro, negro, blanco_j1)
        crearBoton("Negras", 440, 490, 300, 150, negro, negro_claro, blanco, negro_j1)

        pygame.display.update()
        reloj.tick(60)

def seleccionPieza():
    reloj.tick(200)
    global colorJ1, colorJ2, Contador
    if Contador == 1:
        if colorJ1 == 1:
            ##Seleccion J1 color blanco
            pygame.display.set_caption("Jugador 1")
            fondo = pygame.image.load("fondo_tablero_desenfocado.png")
            
            inicio = True
            while inicio == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                textoGrande = pygame.font.Font(None,60)
                TextSurf,TextRect =  text_objects("Selecciona una pieza:", textoGrande, negro)
                TextRect.center = ((ancho/2),200)
                ventana.blit(fondo,(0,0))
                ventana.blit(TextSurf,TextRect)
                
                ventana.blit(pygame.image.load(peon_b),(132,332))
                ventana.blit(pygame.image.load(caballo_b),(232,332))
                ventana.blit(pygame.image.load(alfil_b),(332,332))
                ventana.blit(pygame.image.load(torre_b),(432,332))
                ventana.blit(pygame.image.load(reina_b),(532,332))
                ventana.blit(pygame.image.load(rey_b),(632,332))
                
                #1-Peon 2-Caballo 3-Alfil 4-Torre 5-Reina 6-Rey
                crearBoton("Peon", 115, 432, 100, 30, blanco, blanco_oscuro, negro, setPieza, 1, 1)
                crearBoton("Caballo", 215, 432, 100, 30, negro, negro_claro, blanco, setPieza, 1, 2)
                crearBoton("Alfil", 315, 432, 100, 30, blanco, blanco_oscuro, negro, setPieza, 1, 3)
                crearBoton("Torre", 415, 432, 100, 30, negro, negro_claro, blanco, setPieza, 1, 4)
                crearBoton("Reina", 515, 432, 100, 30, blanco, blanco_oscuro, negro, setPieza, 1, 5)
                crearBoton("Rey", 615, 432, 100, 30, negro, negro_claro, blanco, setPieza, 1, 6)

                pygame.display.flip()
                reloj.tick(60)
        if colorJ1 == 2:
            ##Seleccion J1 y color negro
            pygame.display.set_caption("Jugador 1")
            fondo = pygame.image.load("fondo_tablero_desenfocado.png")
            
            inicio = True
            while inicio == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                pygame.font.init()
                textoGrande = pygame.font.Font(None,60)
                TextSurf,TextRect =  text_objects("Selecciona una pieza:", textoGrande, negro)
                TextRect.center = ((ancho/2),200)
                ventana.blit(fondo,(0,0))
                ventana.blit(TextSurf,TextRect)
                
                ventana.blit(pygame.image.load(peon_n),(132,332))
                ventana.blit(pygame.image.load(caballo_n),(232,332))
                ventana.blit(pygame.image.load(alfil_n),(332,332))
                ventana.blit(pygame.image.load(torre_n),(432,332))
                ventana.blit(pygame.image.load(reina_n),(532,332))
                ventana.blit(pygame.image.load(rey_n),(632,332))
                
                crearBoton("Peon", 115, 432, 100, 30, blanco, blanco_oscuro, negro, setPieza, 1, 1)
                crearBoton("Caballo", 215, 432, 100, 30, negro, negro_claro, blanco, setPieza, 1, 2)
                crearBoton("Alfil", 315, 432, 100, 30, blanco, blanco_oscuro, negro, setPieza, 1, 3)
                crearBoton("Torre", 415, 432, 100, 30, negro, negro_claro, blanco, setPieza, 1, 4)
                crearBoton("Reina", 515, 432, 100, 30, blanco, blanco_oscuro, negro, setPieza, 1, 5)
                crearBoton("Rey", 615, 432, 100, 30, negro, negro_claro, blanco, setPieza, 1, 6)

                pygame.display.flip()
                reloj.tick(60)
    pygame.display.flip()            
    if Contador == 2:            
        if colorJ2 == 1:
            ##Seleccion J2 y color blanco
            pygame.display.set_caption("Jugador 2")
            fondo = pygame.image.load("fondo_tablero_desenfocado.png")
            
            inicio = True
            while inicio == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                textoGrande = pygame.font.Font(None,60)
                TextSurf,TextRect =  text_objects("Selecciona una pieza:", textoGrande, negro)
                TextRect.center = ((ancho/2),200)
                ventana.blit(fondo,(0,0))
                ventana.blit(TextSurf,TextRect)
                
                ventana.blit(pygame.image.load(peon_b),(132,332))
                ventana.blit(pygame.image.load(caballo_b),(232,332))
                ventana.blit(pygame.image.load(alfil_b),(332,332))
                ventana.blit(pygame.image.load(torre_b),(432,332))
                ventana.blit(pygame.image.load(reina_b),(532,332))
                ventana.blit(pygame.image.load(rey_b),(632,332))
                
                crearBoton("Peon", 115, 432, 100, 30, blanco, blanco_oscuro, negro, setPieza, 2, 1)
                crearBoton("Caballo", 215, 432, 100, 30, negro, negro_claro, blanco, setPieza, 2, 2)
                crearBoton("Alfil", 315, 432, 100, 30, blanco, blanco_oscuro, negro, setPieza, 2, 3)
                crearBoton("Torre", 415, 432, 100, 30, negro, negro_claro, blanco, setPieza, 2, 4)
                crearBoton("Reina", 515, 432, 100, 30, blanco, blanco_oscuro, negro, setPieza, 2, 5)
                crearBoton("Rey", 615, 432, 100, 30, negro, negro_claro, blanco, setPieza, 2 , 6)

                pygame.display.flip()
                reloj.tick(60)
        if colorJ2 == 2:
            ##Seleccion J2 y color negro
            pygame.display.set_caption("Jugador 2")
            fondo = pygame.image.load("fondo_tablero_desenfocado.png")
            
            inicio = True
            while inicio == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                textoGrande = pygame.font.Font(None,60)
                TextSurf,TextRect =  text_objects("Selecciona una pieza:", textoGrande, negro)
                TextRect.center = ((ancho/2),200)
                ventana.blit(fondo,(0,0))
                ventana.blit(TextSurf,TextRect)
                
                ventana.blit(pygame.image.load(peon_n),(132,332))
                ventana.blit(pygame.image.load(caballo_n),(232,332))
                ventana.blit(pygame.image.load(alfil_n),(332,332))
                ventana.blit(pygame.image.load(torre_n),(432,332))
                ventana.blit(pygame.image.load(reina_n),(532,332))
                ventana.blit(pygame.image.load(rey_n),(632,332))
                
                crearBoton("Peon", 115, 432, 100, 30, blanco, blanco_oscuro, negro, setPieza, 2,1)
                crearBoton("Caballo", 215, 432, 100, 30, negro, negro_claro, blanco, setPieza, 2, 2)
                crearBoton("Alfil", 315, 432, 100, 30, blanco, blanco_oscuro, negro, setPieza, 2, 3)
                crearBoton("Torre", 415, 432, 100, 30, negro, negro_claro, blanco, setPieza, 2, 4)
                crearBoton("Reina", 515, 432, 100, 30, blanco, blanco_oscuro, negro, setPieza, 2, 5)
                crearBoton("Rey", 615, 432, 100, 30, negro, negro_claro, blanco, setPieza, 2, 6)

                pygame.display.flip()
                reloj.tick(60)

def seleccionPieza_2():
    global colorJ1,colorJ2,Contador
    if Contador == 1:
        if colorJ1 == 1:
            ##Seleccion J1 color blanco
            pygame.display.set_caption("Jugador 1")
            fondo = pygame.image.load("fondo_tablero_desenfocado.png")
            
            inicio = True
            while inicio == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                textoGrande = pygame.font.Font(None,60)
                TextSurf,TextRect =  text_objects("Selecciona una pieza:", textoGrande, negro)
                TextRect.center = ((ancho/2),200)
                ventana.blit(fondo,(0,0))
                ventana.blit(TextSurf,TextRect)
                
                ventana.blit(pygame.image.load(peon_b),(132,332))
                ventana.blit(pygame.image.load(caballo_b),(232,332))
                ventana.blit(pygame.image.load(alfil_b),(332,332))
                ventana.blit(pygame.image.load(torre_b),(432,332))
                ventana.blit(pygame.image.load(reina_b),(532,332))
                ventana.blit(pygame.image.load(rey_b),(632,332))
                
                #1-Peon 2-Caballo 3-Alfil 4-Torre 5-Reina 6-Rey
                crearBoton("Peon", 115, 532, 100, 30, blanco, blanco_oscuro, negro, setPieza, 1, 1)
                crearBoton("Caballo", 215, 532, 100, 30, negro, negro_claro, blanco, setPieza, 1, 2)
                crearBoton("Alfil", 315, 532, 100, 30, blanco, blanco_oscuro, negro, setPieza, 1, 3)
                crearBoton("Torre", 415, 532, 100, 30, negro, negro_claro, blanco, setPieza, 1, 4)
                crearBoton("Reina", 515, 532, 100, 30, blanco, blanco_oscuro, negro, setPieza, 1, 5)
                crearBoton("Rey", 615, 532, 100, 30, negro, negro_claro, blanco, setPieza, 1, 6)

                pygame.display.flip()
                reloj.tick(60)
        if colorJ1 == 2:
            ##Seleccion J1 y color negro
            pygame.display.set_caption("Jugador 1")
            fondo = pygame.image.load("fondo_tablero_desenfocado.png")
            
            inicio = True
            while inicio == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                pygame.font.init()
                textoGrande = pygame.font.Font(None,60)
                TextSurf,TextRect =  text_objects("Selecciona una pieza:", textoGrande, negro)
                TextRect.center = ((ancho/2),200)
                ventana.blit(fondo,(0,0))
                ventana.blit(TextSurf,TextRect)
                
                ventana.blit(pygame.image.load(peon_n),(132,332))
                ventana.blit(pygame.image.load(caballo_n),(232,332))
                ventana.blit(pygame.image.load(alfil_n),(332,332))
                ventana.blit(pygame.image.load(torre_n),(432,332))
                ventana.blit(pygame.image.load(reina_n),(532,332))
                ventana.blit(pygame.image.load(rey_n),(632,332))
                
                crearBoton("Peon", 115, 532, 100, 30, blanco, blanco_oscuro, negro, setPieza, 1, 1)
                crearBoton("Caballo", 215, 532, 100, 30, negro, negro_claro, blanco, setPieza, 1, 2)
                crearBoton("Alfil", 315, 532, 100, 30, blanco, blanco_oscuro, negro, setPieza, 1, 3)
                crearBoton("Torre", 415, 532, 100, 30, negro, negro_claro, blanco, setPieza, 1, 4)
                crearBoton("Reina", 515, 532, 100, 30, blanco, blanco_oscuro, negro, setPieza, 1, 5)
                crearBoton("Rey", 615, 532, 100, 30, negro, negro_claro, blanco, setPieza, 1, 6)

                pygame.display.flip()
                reloj.tick(60)
    pygame.display.flip()            
    if Contador == 2:            
        if colorJ2 == 1:
            ##Seleccion J2 y color blanco
            pygame.display.set_caption("Jugador 2")
            fondo = pygame.image.load("fondo_tablero_desenfocado.png")
            
            inicio = True
            while inicio == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                textoGrande = pygame.font.Font(None,60)
                TextSurf,TextRect =  text_objects("Selecciona una pieza:", textoGrande, negro)
                TextRect.center = ((ancho/2),200)
                ventana.blit(fondo,(0,0))
                ventana.blit(TextSurf,TextRect)
                
                ventana.blit(pygame.image.load(peon_b),(132,332))
                ventana.blit(pygame.image.load(caballo_b),(232,332))
                ventana.blit(pygame.image.load(alfil_b),(332,332))
                ventana.blit(pygame.image.load(torre_b),(432,332))
                ventana.blit(pygame.image.load(reina_b),(532,332))
                ventana.blit(pygame.image.load(rey_b),(632,332))
                
                crearBoton("Peon", 115, 532, 100, 30, blanco, blanco_oscuro, negro, setPieza, 2, 1)
                crearBoton("Caballo", 215, 532, 100, 30, negro, negro_claro, blanco, setPieza, 2, 2)
                crearBoton("Alfil", 315, 532, 100, 30, blanco, blanco_oscuro, negro, setPieza, 2, 3)
                crearBoton("Torre", 415, 532, 100, 30, negro, negro_claro, blanco, setPieza, 2, 4)
                crearBoton("Reina", 515, 532, 100, 30, blanco, blanco_oscuro, negro, setPieza, 2, 5)
                crearBoton("Rey", 615, 532, 100, 30, negro, negro_claro, blanco, setPieza, 2 , 6)

                pygame.display.flip()
                reloj.tick(60)
        if colorJ2 == 2:
            ##Seleccion J2 y color negro
            pygame.display.set_caption("Jugador 2")
            fondo = pygame.image.load("fondo_tablero_desenfocado.png")
            
            inicio = True
            while inicio == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                textoGrande = pygame.font.Font(None,60)
                TextSurf,TextRect =  text_objects("Selecciona una pieza:", textoGrande, negro)
                TextRect.center = ((ancho/2),200)
                ventana.blit(fondo,(0,0))
                ventana.blit(TextSurf,TextRect)
                
                ventana.blit(pygame.image.load(peon_n),(132,332))
                ventana.blit(pygame.image.load(caballo_n),(232,332))
                ventana.blit(pygame.image.load(alfil_n),(332,332))
                ventana.blit(pygame.image.load(torre_n),(432,332))
                ventana.blit(pygame.image.load(reina_n),(532,332))
                ventana.blit(pygame.image.load(rey_n),(632,332))
                
                crearBoton("Peon", 115, 532, 100, 30, blanco, blanco_oscuro, negro, setPieza, 2,1)
                crearBoton("Caballo", 215, 532, 100, 30, negro, negro_claro, blanco, setPieza, 2, 2)
                crearBoton("Alfil", 315, 532, 100, 30, blanco, blanco_oscuro, negro, setPieza, 2, 3)
                crearBoton("Torre", 415, 532, 100, 30, negro, negro_claro, blanco, setPieza, 2, 4)
                crearBoton("Reina", 515, 532, 100, 30, blanco, blanco_oscuro, negro, setPieza, 2, 5)
                crearBoton("Rey", 615, 532, 100, 30, negro, negro_claro, blanco, setPieza, 2, 6)

                pygame.display.flip()
                reloj.tick(60)
    pygame.display.flip()

    

def posiblesMovimientos(tipoPieza, color, listaIndice):
    Px = listaIndice[0]
    Py = listaIndice[1]
    resultados = []
    
    if tipoPieza == 1:
        if color == 1:
            limites = 7
            if(Px+1 <= 7):
                resultados.append([ Px+1,Py ])
                return resultados
            else:
                return resultados    
        if color == 2:
            limites = 7
            if(Px-1 >= 0):
                resultados.append([ Px-1,Py ])
                return resultados
            else:
                return resultados    
            
    if tipoPieza == 2:
        if (5 >= Px >= 2) and (5 >= Py >= 2): #Circulo central
            
            resultados.append([ Px-2,Py-1 ]) #Hacia arriba
            resultados.append([ Px-2,Py+1 ])

            resultados.append([ Px-1,Py-2 ]) #Hacia la izquierda
            resultados.append([ Px+1,Py-2 ])
            

            resultados.append([ Px-1,Py+2 ]) #Hacia la derecha
            resultados.append([ Px+1,Py+2 ])
            
            resultados.append([ Px+2,Py-1 ]) #Hacia abajo
            resultados.append([ Px+2,Py+1 ])
            return resultados
        if (1 >= Px >= 0 ) and (1 >= Py >= 0): #Esquina superior izquierda
            resultados.append([ Px+1,Py+2 ])
            resultados.append([ Px+2,Py+1 ])
            return resultados
        if (1 >= Px >= 0 ) and (7 >= Py >= 6): #Esquina superior derecha
            resultados.append([ Px+1,Py-2 ])
            resultados.append([ Px+2,Py-1 ])
            return resultados
        if (7 >= Px >= 6 ) and (1 >= Py >= 0): #Esquina inferior izquierda
            resultados.append([ Px-2,Py+1 ])
            resultados.append([ Px-1,Py+2 ])
            return resultados
        if (7 >= Px >= 6 ) and (7 >= Py >= 6): #Esquina inferior derecha
            resultados.append([ Px-1,Py-2 ])
            resultados.append([ Px-2,Py-1 ])
            return resultados
        if (5 >= Px >= 2 ):#Zonas laterales
            if (1 >= Py >= 0 ):#Lateral izquierda
                resultados.append([ Px-2,Py-1 ]) #Hacia arriba
                resultados.append([ Px-2,Py+1 ])

                resultados.append([ Px-1,Py+2 ]) #Hacia la derecha
                resultados.append([ Px+1,Py+2 ])
            
                resultados.append([ Px+2,Py-1 ]) #Hacia abajo
                resultados.append([ Px+2,Py+1 ])
                return resultados
            if (7 >= Py >= 6 ):#Lateral derecho
                resultados.append([ Px-2,Py-1 ]) #Hacia arriba
                resultados.append([ Px-2,Py+1 ])

                resultados.append([ Px-1,Py-2 ]) #Hacia la izquierda
                resultados.append([ Px+1,Py-2 ])

                resultados.append([ Px+2,Py-1 ]) #Hacia abajo
                resultados.append([ Px+2,Py+1 ])
                return resultados
        if (5 >= Py >= 2 ): #Zonas verticales
            if (Px == 0):
                resultados.append([ Px+2,Py-1 ]) #Hacia abajo
                resultados.append([ Px+2,Py+1 ])

                 #Hacia la derecha
                resultados.append([ Px+1,Py+2 ])

                 #Hacia la izquierda
                resultados.append([ Px+1,Py-2 ])
                return resultados
            if (Px == 1):
                resultados.append([ Px-1,Py+2 ]) #Hacia la derecha
                resultados.append([ Px+1,Py+2 ])

                resultados.append([ Px-1,Py-2 ]) #Hacia la izquierda
                resultados.append([ Px+1,Py-2 ])

                resultados.append([ Px+2,Py-1 ]) #Hacia abajo
                resultados.append([ Px+2,Py+1 ])
                return resultados
            if (Px == 6):
                resultados.append([ Px-2,Py-1 ]) #Hacia arriba
                resultados.append([ Px-2,Py+1 ])

                resultados.append([ Px-1,Py+2 ]) #Hacia la derecha
                resultados.append([ Px+1,Py+2 ])

                resultados.append([ Px-1,Py-2 ]) #Hacia la izquierda
                resultados.append([ Px+1,Py-2 ])
                return resultados
            if (Px == 7):
                resultados.append([ Px-1,Py+2 ]) #Hacia la derecha

                resultados.append([ Px-1,Py-2 ]) #Hacia la izquierda

                resultados.append([ Px-2,Py-1 ]) #Hacia arriba
                resultados.append([ Px-2,Py+1 ])
                return resultados    

    if tipoPieza == 3:
        esquinasTapadas = 0
        for acumulador in range(1,9):
            #Diagonal superior izquierda
            if (Px-acumulador >= 0) and (Py-acumulador >= 0):
                resultados.append([Px-acumulador,Py-acumulador])
            if (Px-acumulador < 0) or (Py-acumulador < 0):
                esquinasTapadas += 1
            #Diagonal superior derecha
            if (Px-acumulador >= 0) and (Py+acumulador <=7 ):
                resultados.append([Px-acumulador,Py+acumulador])
            if (Px-acumulador < 0) or (Py+acumulador > 7):
                esquinasTapadas += 1
            #Diagonal inferior izquierda
            if(Px+acumulador <= 7) and (Py-acumulador >= 0):
                resultados.append([Px+acumulador,Py-acumulador])
            if (Px+acumulador > 7) or (Py-acumulador > 7):
                esquinasTapadas += 1    
            #Diagonal inferior derecha
            if(Px+acumulador <= 7) and (Py+acumulador <= 7):
                resultados.append([Px+acumulador,Py+acumulador])
            if(Px+acumulador > 7) or (Py+acumulador > 7):
                esquinasTapadas +=1
        return resultados

    if tipoPieza == 4:
        ladoTapado = 0
        for acumulador in range(1,14):
            #Posicion vertica Sentido arriba
            if (Px-acumulador >= 0):
                resultados.append([Px-acumulador,Py])
            if (Px-acumulador < 0):
                ladoTapado += 1
            
            #Posicion vertica Sentido abajo
            if (Px+acumulador <= 7):
                resultados.append([Px+acumulador,Py])
            if (Px+acumulador > 7):
                ladoTapado += 1

            #Posicion horizonal sentido izquierda
            if (Py-acumulador >= 0):
                resultados.append([Px, Py-acumulador])
            if (Py-acumulador < 0):
                ladoTapado += 1

            #Posicion horizonal sentido derecha
            if (Py+acumulador <= 7):
                resultados.append([Px, Py+acumulador])
            if (Py+acumulador > 7):
                ladoTapado += 1    
            
        return resultados

    if tipoPieza == 5:
        esquinasTapadas = 0
        ladoTapado = 0
        for acumulador in range(1,9):
            #Diagonal superior izquierda
            if (Px-acumulador >= 0) and (Py-acumulador >= 0):
                resultados.append([Px-acumulador,Py-acumulador])
            if (Px-acumulador < 0) or (Py-acumulador < 0):
                esquinasTapadas += 1
            #Diagonal superior derecha
            if (Px-acumulador >= 0) and (Py+acumulador <=7 ):
                resultados.append([Px-acumulador,Py+acumulador])
            if (Px-acumulador < 0) or (Py+acumulador > 7):
                esquinasTapadas += 1
            #Diagonal inferior izquierda
            if(Px+acumulador <= 7) and (Py-acumulador >= 0):
                resultados.append([Px+acumulador,Py-acumulador])
            if (Px+acumulador > 7) or (Py-acumulador > 7):
                esquinasTapadas += 1    
            #Diagonal inferior derecha
            if(Px+acumulador <= 7) and (Py+acumulador <= 7):
                resultados.append([Px+acumulador,Py+acumulador])
            if(Px+acumulador > 7) or (Py+acumulador > 7):
                esquinasTapadas +=1
        for acumulador in range(1,14):
            #Posicion vertica Sentido arriba
            if (Px-acumulador >= 0):
                resultados.append([Px-acumulador,Py])
            if (Px-acumulador < 0):
                ladoTapado += 1
            
            #Posicion vertica Sentido abajo
            if (Px+acumulador <= 7):
                resultados.append([Px+acumulador,Py])
            if (Px+acumulador > 7):
                ladoTapado += 1

            #Posicion horizonal sentido izquierda
            if (Py-acumulador >= 0):
                resultados.append([Px, Py-acumulador])
            if (Py-acumulador < 0):
                ladoTapado += 1

            #Posicion horizonal sentido derecha
            if (Py+acumulador <= 7):
                resultados.append([Px, Py+acumulador])
            if (Py+acumulador > 7):
                ladoTapado += 1
        return resultados                    

    if tipoPieza == 6:
        esquinasTapadas = 0
        ladoTapado = 0
        for acumulador in range(1,2):
            #Diagonal superior izquierda
            if (Px-acumulador >= 0) and (Py-acumulador >= 0):
                resultados.append([Px-acumulador,Py-acumulador])
            if (Px-acumulador < 0) or (Py-acumulador < 0):
                esquinasTapadas += 1
            #Diagonal superior derecha
            if (Px-acumulador >= 0) and (Py+acumulador <=7 ):
                resultados.append([Px-acumulador,Py+acumulador])
            if (Px-acumulador < 0) or (Py+acumulador > 7):
                esquinasTapadas += 1
            #Diagonal inferior izquierda
            if(Px+acumulador <= 7) and (Py-acumulador >= 0):
                resultados.append([Px+acumulador,Py-acumulador])
            if (Px+acumulador > 7) or (Py-acumulador > 7):
                esquinasTapadas += 1    
            #Diagonal inferior derecha
            if(Px+acumulador <= 7) and (Py+acumulador <= 7):
                resultados.append([Px+acumulador,Py+acumulador])
            if(Px+acumulador > 7) or (Py+acumulador > 7):
                esquinasTapadas +=1
        for acumulador in range(1,2):
            #Posicion vertica Sentido arriba
            if (Px-acumulador >= 0):
                resultados.append([Px-acumulador,Py])
            if (Px-acumulador < 0):
                ladoTapado += 1
            
            #Posicion vertica Sentido abajo
            if (Px+acumulador <= 7):
                resultados.append([Px+acumulador,Py])
            if (Px+acumulador > 7):
                ladoTapado += 1

            #Posicion horizonal sentido izquierda
            if (Py-acumulador >= 0):
                resultados.append([Px, Py-acumulador])
            if (Py-acumulador < 0):
                ladoTapado += 1

            #Posicion horizonal sentido derecha
            if (Py+acumulador <= 7):
                resultados.append([Px, Py+acumulador])
            if (Py+acumulador > 7):
                ladoTapado += 1
        return resultados

def deteccionPieza(numeroJugador, tipoPieza, color, listaPixeles, listaIndice):
    global SeleccionandoPieza, indicesSeleccionados
    PosicionX = listaPixeles[0]
    PosicionY = listaPixeles[1]

    

    Ancho = 100
    Alto = 100
    
    movimientoM = pygame.mouse.get_pos()
    clickM = pygame.mouse.get_pressed()

    if PosicionX + Ancho > movimientoM[0] > PosicionX and PosicionY+Alto > movimientoM[1] > PosicionY:
        if clickM[0] == 1:#Si esta pulsando el click...
            SeleccionandoPieza = True
    if not (PosicionX + Ancho > movimientoM[0] > PosicionX and PosicionY+Alto > movimientoM[1] > PosicionY):
        if clickM[0] == 1:#Si esta pulsando el click...
            SeleccionandoPieza = False
            movs2 = posiblesMovimientos(tipoPieza, color, listaIndice)
            for cosa in movs2:
                if cosa == indicesSeleccionados:
                    return True


    if SeleccionandoPieza == True:
        movs = posiblesMovimientos(tipoPieza, color, listaIndice)
        for x in movs:
            valor1,valor2 = x[0] , x[1]
            Pix_x = listaPosiciones[valor1][valor2][0]
            Pix_y = listaPosiciones[valor1][valor2][1]
            ventana.blit(indicador,(Pix_x,Pix_y))
        pygame.display.update()

        for x in range(0,8):
            for y in range(0,8):
                Pun1 = listaColisiones[x][y][0]
                Pun2 = listaColisiones[x][y][1]
                
                if (Pun1+100 > movimientoM[0] > Pun1) and (Pun2+100 > movimientoM[1] > Pun2):
                    P1 = listaColisiones[x][y][0]
                    P2 = listaColisiones[x][y][1]
                    indicesSeleccionados = [x,y]
                    ventana.blit(marcador,(P1,P2))
                    pygame.display.update()
            

    #if SeleccionandoPieza_1 == False:
        #print("Se esta moviendo la pieza?: ", SeleccionandoPieza_1)    
def creditos():
    print("\tHecho Por C.T.L")
    sys.exit(0)

def ventanaGanador(color):
    global colorJ1, colorJ2, piezaJ1, piezaJ2, Contador, posicionP1, posicionP2

    if color == 1:
        pygame.display.set_caption("Ganador!")
        fondo = pygame.image.load("fondo_tablero_desenfocado.png")

        inicio = True
        while inicio == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.font.init()
            textoGrande = pygame.font.Font("times-new-roman.ttf",60)
            TextSurf,TextRect =  text_objects("Gano el color blanco!", textoGrande, negro)
            TextRect.center = ((ancho/2),300)
            ventana.blit(fondo,(0,0))
            ventana.blit(TextSurf,TextRect)

            colorJ1 = 0
            colorJ2 = 0
            piezaJ1 = 0
            piezaJ2 = 0
            posicionP1.clear()
            posicionP2.clear()
            Contador = 1

            crearBoton("Volver a jugar", 270, 400, 300, 100, botonJugar, botonJugarClaro, negro, seleccionColor)
            crearBoton("Salir", 270, 520, 300, 100, botonSalir, botonSalirClaro, negro, creditos)

            pygame.display.update()
    if color == 2:
        pygame.display.set_caption("Ganador!")
        fondo = pygame.image.load("fondo_tablero_desenfocado.png")

        inicio = True
        while inicio == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.font.init()
            textoGrande = pygame.font.Font("times-new-roman.ttf",60)
            TextSurf,TextRect =  text_objects("Gano el color negro!", textoGrande, negro)
            TextRect.center = ((ancho/2),300)
            ventana.blit(fondo,(0,0))
            ventana.blit(TextSurf,TextRect)

            colorJ1 = 0
            colorJ2 = 0
            piezaJ1 = 0
            piezaJ2 = 0
            posicionP1.clear()
            posicionP2.clear()
            Contador = 1

            crearBoton("Volver a jugar", 270, 400, 300, 100, botonJugar, botonJugarClaro, negro, seleccionColor)
            crearBoton("Salir", 270, 520, 300, 100, botonSalir, botonSalirClaro, negro, creditos)

            pygame.display.update()

def iniciar_Juego():
    global indicesSeleccionados, posicionP1, posicionP2
    global listaColisiones, listaIndices, listaPosiciones
    global colorJ1, colorJ2, piezaJ1, piezaJ2, Turno, eliminado
    global peon_b, caballo_b, torre_b, alfil_b, reina_b, rey_b
    global peon_n, caballo_n, torre_n, alfil_n, reina_n, rey_n
    #Creacion del tablero
    
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Ajedrez")
    fondo = pygame.image.load("fondo_tablero.png")

    #
    #   Bloque de codigo principal, se repetira siempre y cuando no se detecte que la persona cerro la ventana principal
    #   Una vez se declaran las piezas, se rellena el fondo de la pantalla, y encima se van agregando mas "capas"
    #   1a Capa: Fondo de ajedrez
    #   2a Capa: Imagenes de las piezas de ajedrez
    #   3a Capa: Botones invisibles, estos botones se mueven en conjunto con la imagen de la pieza, se usan para interactuar con el juego
    #   Si se hace click encima de la pieza, se hace click en un boton sin textura, valida en que posicion esta, y muestra sus posibles movimientos
    #   Si la persona hace click en un lugar que este habilitado para mover, se actualiza la posicion del boton y la imagen de la pieza
    #   

    class Pieza:
        color = 0
        tipo_Pieza = 0
        direccion = ""
        #  Pixeles en pantalla
        Pix_x = 0
        Pix_y = 0
        ###################################################################
        #  Posicion absoluta, se usa para saber en que cuadrante se movera
        #  Tambien se utiliza para iterar sobre otras funciones
        #  Si se cruzan estas variables con la lista "listaPosiciones"
        #  Se puede obtener el valor en pixeles de donde debera renderizarse
        #  La pieza de ajedrez
        ###################################################################
        Pos_x = 0
        Pos_y = 0
        def __init__(self, color, tipo, direccion, x, y):
            self.color = color
            self.tipo_Pieza = tipo
            self.direccion = direccion
            self.Pix_x = listaPosiciones[x][y][0]
            self.Pix_y = listaPosiciones[x][y][1]
            self.Pos_x = x
            self.Pos_y = y

        def set_imagen(self,direccion):
            self.direccion = direccion

        def get_imagen(self):
            tmp_imagen = pygame.image.load(self.direccion)
            return tmp_imagen

        def set_color(self, color):
            self.color = color

        def get_color(self):
            return self.color

        def set_tipo(self, tipo):
            self.tipo_Pieza = tipo

        def get_tipo(self):
            return self.tipo_Pieza

        def set_posicionPantalla(self, Pos_x, Pos_y):
            
            self.Pix_x = listaPosiciones[Pos_x][Pos_y][0]
            self.Pix_y = listaPosiciones[Pos_x][Pos_y][1]
            
        def get_posicionPantalla(self):
            lista = [self.Pix_x, self.Pix_y]
            return lista

        def set_posicionAbsoluta(self, Pos_X, Pos_y):
            self.Pos_x = Pos_X
            self.Pos_y = Pos_y

        def get_posicionAbsoluta(self):
            lista = [self.Pos_x, self.Pos_y]
            return lista
        def set_Eliminado(self):
            self.Pix_x = 1000
            self.Pix_y = 1000    
            self.direccion = eliminado
    
    #Color: 1 blanco 2 negro
    imagen_1 = ""
    x_1 = 0
    y_1 = 0

    imagen_2 = ""
    x_2 = 0
    y_2 = 0

    #1-Peon 2-Caballo 3-Alfil 4-Torre 5-Reina 6-Rey
    if colorJ1 == 1:
        x_1 = 0
        y_1 = 2
        if piezaJ1 == 1:
            imagen_1 = peon_b
        if piezaJ1 == 2:
            imagen_1 = caballo_b
        if piezaJ1 == 3:
            imagen_1 = alfil_b 
        if piezaJ1 == 4:
            imagen_1 = torre_b
        if piezaJ1 == 5:
            imagen_1 = reina_b
        if piezaJ1 == 6:
            imagen_1 = rey_b
    if colorJ1 == 2:
        x_1 = 7
        y_1 = 5         
        if piezaJ1 == 1:
            imagen_1 = peon_n
        if piezaJ1 == 2:
            imagen_1 = caballo_n
        if piezaJ1 == 3:
            imagen_1 = alfil_n  
        if piezaJ1 == 4:
            imagen_1 = torre_n
        if piezaJ1 == 5:
            imagen_1 = reina_n
        if piezaJ1 == 6:
            imagen_1 = rey_n

    if colorJ2 == 1:
        x_2 = 0
        y_2 = 2
        if piezaJ2 == 1:
            imagen_2 = peon_b
        if piezaJ2 == 2:
            imagen_2 = caballo_b
        if piezaJ2 == 3:
            imagen_2 = alfil_b   
        if piezaJ2 == 4:
            imagen_2 = torre_b
        if piezaJ2 == 5:
            imagen_2 = reina_b
        if piezaJ2 == 6:
            imagen_2 = rey_b
    if colorJ2 == 2:
        x_2 = 7
        y_2 = 5         
        if piezaJ2 == 1:
            imagen_2 = peon_n
        if piezaJ2 == 2:
            imagen_2 = caballo_n
        if piezaJ2 == 3:
            imagen_2 = alfil_n    
        if piezaJ2 == 4:
            imagen_2 = torre_n
        if piezaJ2 == 5:
            imagen_2 = reina_n
        if piezaJ2 == 6:
            imagen_2 = rey_n

    P_1 = Pieza(colorJ1,piezaJ1,imagen_1,x_1,y_1)               
    P_2 = Pieza(colorJ2,piezaJ2,imagen_2,x_2,y_2)

    ejecutandose = True
    while ejecutandose:
        
        #Capa inferior - Fondo
        ventana.blit(fondo,(0,0))

        ####################

        pygame.time.delay(30)
        
        for event in pygame.event.get():
            #Detecta la ventana cerrada
            if event.type == pygame.QUIT:
                ejecutandose = False
                quit()

        ####Capa intermedia
        
        ventana.blit(P_1.get_imagen(),(P_1.get_posicionPantalla()))
        ventana.blit(P_2.get_imagen(),(P_2.get_posicionPantalla()))
        Ñe = P_1.get_posicionAbsoluta()
        Ñe1, Ñe2 = Ñe[0], Ñe[1]
        posicionP1 =  [Ñe1,Ñe2]

        Ñe = P_2.get_posicionAbsoluta()
        Ñe1, Ñe2 = Ñe[0], Ñe[1]
        posicionP2 =  [Ñe1,Ñe2]
        pygame.display.update() #Actualiza la pantalla entera
        
        #####################################

        ######Seccion de actualizacion de movimiento
        if Turno == 1:
            if P_1.get_color() == 1:
                pygame.display.set_caption("Turno de: Blanco")
            if P_1.get_color() == 2:
                pygame.display.set_caption("Turno de: Negro")    
            tmp1 = deteccionPieza(1, piezaJ1, colorJ1, P_1.get_posicionPantalla(), P_1.get_posicionAbsoluta())
            if tmp1 == True:
                posicionP1 = [indicesSeleccionados[0], indicesSeleccionados[1]]
                if posicionP1 == posicionP2:
                    P_2.set_Eliminado()
                    ventanaGanador(P_1.get_color())
                    
                P_1.set_posicionPantalla(indicesSeleccionados[0], indicesSeleccionados[1])
                P_1.set_posicionAbsoluta(indicesSeleccionados[0], indicesSeleccionados[1])
                
                indicesSeleccionados.clear()
                Turno = 2
            if tmp1 == False:
                Turno = 2

        if Turno == 2:
            if P_2.get_color() == 1:
                pygame.display.set_caption("Turno de: Blanco")
            if P_2.get_color() == 2:
                pygame.display.set_caption("Turno de: Negro")    
            tmp2 = deteccionPieza(2, piezaJ2, colorJ2, P_2.get_posicionPantalla(), P_2.get_posicionAbsoluta())
            if tmp2 == True:
                posicionP2 = [indicesSeleccionados[0], indicesSeleccionados[1]]
                if posicionP2 == posicionP1:
                    P_1.set_Eliminado()
                    ventanaGanador(P_2.get_color())

                P_2.set_posicionPantalla(indicesSeleccionados[0], indicesSeleccionados[1])
                P_2.set_posicionAbsoluta(indicesSeleccionados[0], indicesSeleccionados[1])
                indicesSeleccionados.clear()
                Turno = 1
            if tmp2 == False:
                Turno = 1
    
menu()
