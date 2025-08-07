import pygame
import os
from tkinter import ttk

# 🔧 Inicializa o mixer apenas uma vez
pygame.mixer.init()

# 🎚️ Controle global do som
som_global_ativo = True

# 🎵 Tocar música longa (com ou sem repetição)
def tocar_musica(path, repetir=True):
    if som_global_ativo and os.path.exists(path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1 if repetir else 0)

# 🔈 Tocar efeito sonoro curto
def tocar_som_curto(path):
    if som_global_ativo and os.path.exists(path):
        som = pygame.mixer.Sound(path)
        som.play()

# ⏹️ Parar música atual
def parar_musica():
    pygame.mixer.music.stop()

# 🔇 Desativar som global
def desativar_som():
    global som_global_ativo
    som_global_ativo = False
    parar_musica()

# 🔊 Ativar som global
def ativar_som():
    global som_global_ativo
    som_global_ativo = True

def som_evento(tipo):
    sons = {
        "erro": "sons/erro.mp3",
        "login_sucesso": "sons/sucesso.mp3",
        "abertura": "sons/abertura.mp3"
    }

    caminho = sons.get(tipo)
    if caminho and som_global_ativo:
        try:
            pygame.mixer.music.load(caminho)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"🔇 Erro ao tocar som '{tipo}': {e}")