# modulo de Goku

import pygame
from pygame.locals import * 
import os

class Goku(pygame.sprite.Sprite):                               
    def __init__(self,position):  #Constructor, el init se acompaña de dos guiones bajos al principio y al final.
        self.sheet = pygame.image.load("Imagenes/gokus.png").convert_alpha()         # Cargamos la imagen completa de todos los movimientos
        self.sheet.set_clip(pygame.Rect(351,0,55,94))   #Colocamos las coordenadas para que tome la imagen que va tomar al inicio (posicion x, posicion y, ancho , alto) 
        self.image = self.sheet.subsurface (self.sheet.get_clip()) # Le decimos que tome el rectangulo de las coordenadas que le pasamos                                               
        #self.image=pygame.transform.scale(image) tendriamos que tener una variable de ancho y largo de la imagen para poder rescalarla.
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


        if event.type == pygame.KEYUP:      #Devuelve una imagen de acuerdo a la ultima tecla que levantamos.
            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')




