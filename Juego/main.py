# Intento de juego nº1
#enconding: utf-8
#importamos la libreria de pygame y sys; y todos sus modulos.
#Importamos el archivo player con sus funcionalidades
#Importamos todas las liberias necesarias para descomprimir y decodificar el mapa.

import pygame,sys
from pygame.locals import * 

#import player

pygame.init()   #inicializamos la libreria pygame ¡¡Comando obligatorio!!


ancho_ventana=800
alto_ventana=576
ventana = pygame.display.set_mode((ancho_ventana,alto_ventana)) # Definimos las dimensiones de la ventana
pygame.display.set_caption("Goku contra los marcianos") #Colocamos el nombre a la ventana
color = pygame.Color(87,204,242) #El modulo de pygame Color va con mayuscula
clock  =pygame.time.Clock() # Controla el tiempo de la animacion



class Goku(pygame.sprite.Sprite):                               
    def __init__(self,position):  #Constructor, el init se acompaña de dos guiones bajos al principio y al final.
        self.sheet = pygame.image.load("Imagenes/gokus.png").convert_alpha()         # Cargamos la imagen completa de todos los movimientos
        self.sheet.set_clip(pygame.Rect(351,0,55,94))   #Colocamos las coordenadas para que tome la imagen que va tomar al inicio (posicion x, posicion y, ancho , alto) 
        self.image = self.sheet.subsurface (self.sheet.get_clip()) # Le decimos que tome el rectangulo de las coordenadas que le pasamos                                               
        #self.image=pygame.transform.scale(image) tendriamos que tener una variable de ancho y largo de la imagen para poder rescalarla.
        self.listaDisparo= []
        self.rect = self.image.get_rect()    #Genera un rectangulo alrededor de la imagen que nos va a permitir hacer las colisiones y moverlo.
        self.rect.topleft = position   #Guardamos en la variable position la posicion de nuestro rectangulo.    
        self.frame = 0  #Definimos este primer rectangulo como el frame 0.
        self.left_states = {0:(506,98,70,90)}   #Estado para ir a la izquierda
        self.right_states = {0: (374,105,73,80)}
        self.up_states = {0:(691,452,55,99)}
        self.down_states = {0:(175,77,46,69)}
        self.stan_parado = {0: (351,0,55,94)}
        self.stan_volar = {0: (288,0,65,101)}
        self.stan_frenar = {0: (330,106,41,72)}
        self.stan_kame = {0: (532,271,68,82)}
       
        

    def get_frame(self, frame_set):          #Obtenemos los frame y los va recorriendo segun el estado.
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
    
        
    def clip(self, clipped_rect):  #Hacemos el recorte de las imagenes y si hay varias imagenes que representan el mismo estado, se produce un loop
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
    

    def update(self,direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -=5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x +=5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5       
        if direction == 'down':
            self.clip(self.stan_volar)
            self.rect.y +=5

        if direction == 'stand_left':            #Despues de apretar cada tecla, vuelve al clip seleccionado
            self.clip(self.stan_frenar[0])
        if direction == 'stand_right':
            self.clip(self.stan_frenar[0])
        if direction == 'stand_up':
            self.clip(self.stan_volar[0])
        if direction == 'stand_down':
            self.clip(self.stan_parado[0])
        if direction == 'posicion_kame':
            self.clip(self.stan_kame[0])


        self.image = self.sheet.subsurface(self.sheet.get_clip())   #Coloca el clip en el que se quedo parado

    def handle_event (self,event):
        if event.type == pygame.KEYDOWN:        #Reacciona segun la tecla que se presione
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
            if event.key == pygame.K_s:
                self.update('posicion_kame')
            


        if event.type == pygame.KEYUP:      #Devuelve una imagen de acuerdo a la ultima tecla que levantamos.
            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
            
    def kame(self,x,y):
        miKame = Kamehameha(x,y)
        self.listaDisparo.append(miKame)



class Kamehameha(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        # Atributos
        self.imageKame = pygame.image.load('Imagenes/Kame.png')
        self.rect = self.imageKame.get_rect()
        self.velocidadKame = 3
        self.rect.top = posy
        self.rect.left = posx

    def trayectoria(self):
        self.rect.left = self.rect.left + self.velocidadKame

    def dibujar(self,superficie):
        superficie.blit(self.imageKame,self.rect)


# Editar la clase marciano, para generar los invasores
class Marciano(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        # Atributos
        # BUSCAR IMAGENES PARA EL MARCIANO ENEMIGO
        self.imageMarciano1 = pygame.image.load('Imagenes/Saibaman A1 .png')
        self.imageMarciano2 = pygame.image.load('Imagenes/Saibaman A2.png')

        self.listaImagenes = [self.imageMarciano1, self.imageMarciano2]
        self.posImagen = 0   # Para que por defecto sea la imagen 1, la que aparesca primero.

        self.imageMarciano = self.listaImagenes[self.posImagen]  
        self.rect = self.imageMarciano.get_rect()

        self.listaDisparo = []
        self.velocidad = 20
        self.rect.top = posy
        self.rect.left = posx

        self.tiempoCambio = 1  #Atributo para cambiar la imagen.


    def dibujar(self,superficie):
        self.imageMarciano = self.listaImagenes[self.posImagen]
        superficie.blit(self.imageMarciano,self.rect) 

    def comportamiento(self,tiempo):
        print(tiempo)
        if self.tiempoCambio == round (tiempo):
            self.posImagen +=1
            self.tiempoCambio +=1

            if self.posImagen > len(self.listaImagenes)-1:  #Este condicional es que para ver si llego a la ultima imagen de la lista, que se regrese.
                self.posImagen = 0

#Mi_Imagen = pygame.image.load("Imagenes/gokus.png")         #Almaceno la imagen completa en una variable
#Mi_Imagen.convert_alpha()                                   # Comando para sacar el fondo
#Mi_Imagen.set_clip(pygame.Rect(374,107,72,72))              # Marco el area que quiero recortar, pasandole las coordenadas (Pixeles ancho (x), pixelex altos(y), ancho y alto de la imagen)  
#Recorte = Mi_Imagen.subsurface(Mi_Imagen.get_clip())        #Realizo el recorte del area previamente seleccionada
#rectangulo = Recorte.get_rect()                             # Genero un rectangulo alrededor que me va a ayudar con las colisiones
#frame = 0
#La imagen de fondo
imagen_fondo = pygame.image.load("Imagenes/Fondo.jpg")  

player = Goku((56, 324))    #Posicion donde va a iniciar el personaje
kame = Kamehameha (120,359)
enemigo = Marciano(700,100)
bandera = 1

reloj = pygame.time.Clock()

#Creamos un bucle infinito donde se va a desarrolar el juego

while True:
    
    reloj.tick(60)

    #ventana.fill(color) # El comando fill permite rellenar la ventana, del color que se le mande entre parentesis
    
    kame.trayectoria()

    tiempo = pygame.time.get_ticks()/1000
    #print (tiempo)
    for evento in pygame.event.get():  #Recorremos la lista de eventos predefinida por pygame
        if evento.type == QUIT:        #Si el tipo de eventos que se desarrollo es del tipo QUIT = "Tocar la x de la ventana"
            pygame.quit() #Instruccion para detener todos los modulos de pygame             
            sys.exit()    # Instruccion para cerrar la ventana
        if evento.type == pygame.KEYDOWN:
            if evento.key == K_s:
                if bandera==1:
                    x,y = player.rect.center   
                    player.kame(x+30,y-35)

    player.handle_event(evento)          #player.handle_event(event) # Controla los eventos que se dan en el teclado
    ventana.blit(imagen_fondo,(0,0))       

    enemigo.comportamiento(tiempo)
    
                                                    
    ventana.blit(player.image,(player.rect))
    enemigo.dibujar(ventana)
    if len(player.listaDisparo)>0:
        for x in player.listaDisparo:
            x.dibujar(ventana)
            x.trayectoria()

            if x.rect.left >800:
                #bandera=1
                player.listaDisparo.remove(x)
            elif x.rect.left<400:          
                bandera=0
            elif x.rect.left<500: #Despues de que el kame supere los 500 pixeles, le va a permitir tirar otro. Si se acerca al final de la ventana, le va a permitir tirar todos los que quiera.
                bandera=1     
    #kame.dibujar(ventana)                                              #Colocar la imagen del personaje dentro de nuestra ventana
    pygame.display.update() # Comando para ir actualizando la ventana

                                       
    
