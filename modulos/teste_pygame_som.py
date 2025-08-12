import os
import pygame
import time  # ⏱️ Para controlar o tempo
from modulos.utilitarios import caminho_arquivo
from modulos import dados_compartilhados as dc

# Caminho do arquivo de som
#caminho_som = os.path.join(os.getcwd(), "sons", "bouncy_pet_intro.mp3")
caminho_som = os.path.join(os.getcwd(), "sons", "intro_musica.mp3")


# Verifica se o arquivo existe
if not os.path.isfile(caminho_som):
    print(f"⚠️ Arquivo de som não encontrado: {caminho_som}")
else:
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(caminho_som)
        pygame.mixer.music.play()
        print("🎵 Música de introdução tocando por 10 segundos...")

        time.sleep(10)  # ⏳ Aguarda 10 segundos

        #pygame.mixer.music.stop()
        pygame.mixer.music.fadeout(2000)  # 2000 ms = 2 segundos de fade
        print("⏹️ Música parada após 10 segundos.")
    except pygame.error as e:
        print(f"❌ Erro ao iniciar o mixer ou carregar o som: {e}")

        print(f"Caminho completo: {caminho_som}")
