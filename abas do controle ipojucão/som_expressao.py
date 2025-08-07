# som_expressao.py

import os
import time
import pygame
from PIL import Image, ImageTk

# Inicializa o mixer de som (caso ainda não esteja iniciado)
def inicializar_audio():
    if not pygame.mixer.get_init():
        pygame.mixer.init()

# 🎭 Função principal que toca som e troca imagens do mascote
def som_e_expressao_acao(acao, label_imagem, janela):
    inicializar_audio()

    # 💾 Caminho base das imagens
    caminho_imagens = os.path.join(os.path.dirname(__file__), "imagens")

    # 🎵 Trilha sonora associada à ação
    sons_acoes = {
        "salvar": "som/clair_de_lune_prelude.mp3",
        "editar": "som/soft_edit_tune.mp3",
        "excluir": "som/dramatic_delete.mp3",
        "buscar": "som/search_ping.mp3"
    }
    caminho_som = sons_acoes.get(acao)

    # 🐶 Imagens do mascote em diferentes expressões
    imagens_mascote = [
        "mascote_piscando.png",
        "mascote_alegre.png",
        "mascote_normal.png"
    ]

    # 🗣️ Reproduz som associado à ação
    if caminho_som and os.path.exists(caminho_som):
        try:
            pygame.mixer.music.load(caminho_som)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"[ERRO] Não foi possível tocar o som: {e}")
    else:
        print("[INFO] Nenhum som definido para esta ação.")

    # 💫 Animação rápida do mascote piscando
    for imagem_nome in imagens_mascote:
        img_path = os.path.join(caminho_imagens, imagem_nome)
        if os.path.exists(img_path):
            try:
                imagem = Image.open(img_path).resize((150, 150))
                imagem_tk = ImageTk.PhotoImage(imagem)
                label_imagem.config(image=imagem_tk)
                label_imagem.image = imagem_tk
                label_imagem.update()
                time.sleep(0.3)
            except Exception as e:
                print(f"[ERRO] Falha ao carregar imagem: {e}")
        else:
            print(f"[AVISO] Imagem '{imagem_nome}' não encontrada em /imagens")

    print(f"[MASCOTE] Reagiu à ação '{acao}' com som e expressão!")





# import pygame
# import tkinter as tk
# from PIL import Image, ImageTk
# import time
#
# # Inicializa o mixer para som
# def inicializar_audio():
#     if not pygame.mixer.get_init():
#         pygame.mixer.init()
#
# # Função principal que toca som e anima o mascote
# def som_e_expressao_acao(acao, imagem_label):
#     # Toca som
#     pygame.mixer.music.load("som_reacao.wav")
#     pygame.mixer.music.play()
#
#     # Animação piscando: troca imagens
#     imagens = ["mascote_piscando.jpg", "mascote_alegre.jpg", "mascote_normal.jpg"]
#
#     for img_path in imagens:
#         img = Image.open(img_path)
#         img = ImageTk.PhotoImage(img)
#         imagem_label.config(image=img)
#         imagem_label.image = img  # evita garbage collector
#         imagem_label.update()
#         time.sleep(0.4)
#
#     print(f"Ação '{acao}' concluída com som e piscada do mascote! 🐶🎶✨")