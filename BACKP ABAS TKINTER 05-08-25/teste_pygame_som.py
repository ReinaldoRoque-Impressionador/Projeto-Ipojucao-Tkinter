import os
import pygame

caminho_som = os.path.join(os.getcwd(), "sons", "bouncy_pet_intro.mp3")
pygame.mixer.init()
pygame.mixer.music.load(caminho_som)
pygame.mixer.music.play(-1)