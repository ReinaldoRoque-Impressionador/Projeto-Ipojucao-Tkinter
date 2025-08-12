# som.py
import pygame
import threading
import os
from tkinter import ttk
som_ativo = True  # isso pode ser movido para o módulo som.py
from modulos import dados_compartilhados as dc
from modulos.utilitarios import caminho_arquivo

# ✅ Inicializa mixer uma única vez
def inicializar_audio():
    if not pygame.mixer.get_init():
        pygame.mixer.init()

# 🎵 Controlador de som global
som_ativo = True

def ativar_som():
    global som_ativo
    som_ativo = True

def desativar_som():
    global som_ativo
    som_ativo = False

def alternar_som(botao=None):
    global som_ativo
    som_ativo = not som_ativo
    if botao:
        texto = "🔈 Som Ativado" if som_ativo else "🔇 Som Desativado"
        botao.config(text=texto)

# 🔊 Toca trilha de forma assíncrona
def tocar_som(caminho, duracao=None):
    if not som_ativo:
        print("🔇 Som desativado. Trilha ignorada.")
        return
    #if os.path.exists(caminho):

    if som_ativo and os.path.exists(caminho):
        def reproduzir():
            try:
                inicializar_audio()
                pygame.mixer.music.load(caminho)
                pygame.mixer.music.play()
                if duracao:
                    pygame.time.delay(duracao * 1000)
                    pygame.mixer.music.stop()
            except Exception as e:
                print(f"Erro ao tocar som: {e}")
        threading.Thread(target=reproduzir, daemon=True).start()
    else:
        print(f"🔇 Caminho inválido ou som desativado: {caminho}")

# ⏹️ Parar trilha
def parar_som():
    if pygame.mixer.get_init():
        pygame.mixer.music.stop()


# 🔒 Modo bloqueante (espera terminar)
def tocar_som_bloqueante(caminho):
    if som_ativo and os.path.exists(caminho):
        inicializar_audio()
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

# 🎯 Som por evento
def som_evento(tipo):
    sons = {
        "login_sucesso": "sons/acesso_concedido.mp3",
        "login_falha": "sons/acesso_negado.mp3",
        "usuario_adicionado": "sons/usuario_adicionado.mp3",
        "usuario_removido": "sons/usuario_removido.mp3",
        "consulta": "sons/musica_consulta_pet.mp3",
        "relatorio": "sons/relatorio.mp3",
        "abertura": "sons/musica_abertura.mp3",
        "fechamento": "sons/musica_end_of_day.mp3",
        "mascote": "sons/bouncy_pet_intro.mp3"
    }
    caminho = sons.get(tipo)
    if caminho:
        tocar_som(caminho)

# ✨ Animação visual: fade de mensagem
def fade_label(label, janela, cor_base="#444", tempo=1000):
    def fade(passo=0):
        alpha = max(0, 1 - passo / 20)
        cinza = int(68 * alpha)
        nova_cor = f"#{cinza:02x}{cinza:02x}{cinza:02x}"
        label.config(fg=nova_cor)
        if passo < 20:
            janela.after(50, fade, passo + 1)
    janela.after(tempo, fade)

# 🐶 Mascote piscando
from PIL import Image, ImageTk, ImageEnhance

def animar_mascote(janela, caminho_img="imagens/mascote.png", x=870, y=540):
    if not os.path.exists(caminho_img):
        return
    base = Image.open(caminho_img).resize((130,130))
    img_normal = ImageTk.PhotoImage(base)
    escurecida = ImageTk.PhotoImage(ImageEnhance.Brightness(base).enhance(0.6))
    label = tk.Label(janela, image=img_normal, bg="#fff")
    label.image = img_normal
    label.place(x=x, y=y)

    def piscar(on=True):
        label.config(image=escurecida if on else img_normal)
        label.image = escurecida if on else img_normal
        janela.after(300 if on else 2400, piscar, not on)

    piscar()