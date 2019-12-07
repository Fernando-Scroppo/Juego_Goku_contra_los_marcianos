# Intento de juego nº1
#enconding: utf-8
#importamos la libreria de pygame y sys; y todos sus modulos.
#Importamos el archivo player con sus funcionalidades
#Importamos todas las liberias necesarias para descomprimir y decodificar el mapa.

import pygame,sys
from pygame.locals import * 

import player
pygame.init()   #inicializamos la libreria pygame ¡¡Comando obligatorio!!


ancho_ventana=600
alto_ventana=576
ventana = pygame.display.set_mode((ancho_ventana,alto_ventana)) # Definimos las dimensiones de la ventana
pygame.display.set_caption("Goku contra los marcianos") #Colocamos el nombre a la ventana
color = pygame.Color(87,204,242) #El modulo de pygame Color va con mayuscula
clock  =pygame.time.Clock() # Controla el tiempo de la animacion
player = player.Goku((56, 324))    #Posicion donde va a iniciar el personaje.

#Mi_Imagen = pygame.image.load("Imagenes/gokus.png")         #Almaceno la imagen completa en una variable
#Mi_Imagen.convert_alpha()                                   # Comando para sacar el fondo
#Mi_Imagen.set_clip(pygame.Rect(374,107,72,72))              # Marco el area que quiero recortar, pasandole las coordenadas (Pixeles ancho (x), pixelex altos(y), ancho y alto de la imagen)  
#Recorte = Mi_Imagen.subsurface(Mi_Imagen.get_clip())        #Realizo el recorte del area previamente seleccionada
#rectangulo = Recorte.get_rect()                             # Genero un rectangulo alrededor que me va a ayudar con las colisiones
#frame = 0

imagen_fondo = pygame.image.load("Imagenes/Fondo.jpg")  


#Creamos un bucle infinito donde se va a desarrolar el juego

while True:
    
    #ventana.fill(color) # El comando fill permite rellenar la ventana, del color que se le mande entre parentesis
    
    print("Bienvenido")

    for evento in pygame.event.get():  #Recorremos la lista de eventos predefinida por pygame
        if evento.type == QUIT:        #Si el tipo de eventos que se desarrollo es del tipo QUIT = "Tocar la x de la ventana"
            pygame.quit() #Instruccion para detener todos los modulos de pygame             
            sys.exit()    # Instruccion para cerrar la ventana
        
    player.handle_event(evento)
    ventana.blit(imagen_fondo,(0,0))                                                      #player.handle_event(event) # Controla los eventos que se dan en el teclado      
    ventana.blit(player.image,(player.rect))          #Colocar la imagen del personaje dentro de nuestra ventana
    pygame.display.update() # Comando para ir actualizando la ventana

                                       
    clock.tick(60)
