# Program: desafio_21_tocando_musica.py
# Author: Ramon R. Valeriano
# Description:
# Updated: 24/09/2020 - 21:49

# importando a biblioteca PyGame

import pygame

pygame.init()
pygame.mixer.music.load('Arizona.mp3')
pygame.mixer.music.play()
pygame.event.wait()
