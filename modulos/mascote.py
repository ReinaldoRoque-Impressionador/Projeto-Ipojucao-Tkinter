# mascote.py
import tkinter as tk
from PIL import Image, ImageTk
import os

from som_expressao import som_e_expressao_acao

# mascote.py
def animar_mascote_expressivo(label_mascote, janela):
    som_e_expressao_acao("salvar", label_mascote, janela)


# 🐾 Caminhos das expressões
EXPRESSOES = {
    "feliz": "imagensipojucao/expressoes/mascote_feliz.png",
    "negativo": "imagensipojucao/expressoes/mascote_negativo.png",
    "piscando": "imagensipojucao/expressoes/mascote_piscando.png",
    "beijo": "imagensipojucao/expressoes/mascote_beijo.png",
    "anotando": "imagensipojucao/expressoes/mascote_anotando.png",
    "positivo": "imagensipojucao/expressoes/mascote_positivo.png",
    "bye": "imagensipojucao/expressoes/mascote_bye.png",
    "relatorio": "imagensipojucao/expressoes/mascote_relatorio.png",
    "triste": "imagensipojucao/expressoes/mascote_triste.png",
    "pagamento": "imagensipojucao/expressoes/mascote_pagamento.png"
}


# EXPRESSOES = {
#     "feliz": "imagens/mascote_feliz.png",
#     "negativo": "imagens/mascote_triste.png",
#     "piscando": "imagens/mascote_piscando.png",
#     "beijo": "imagens/mascote_beijo.png",
#     "anotando": "imagens/mascote_anotando.png",
#     "positivo": "imagens/mascote_positivo.png",
#     "bye": "imagens/mascote_bye.png",
#     "relatorio": "imagens/mascote_relatorio.png",
#     "triste": "imagens/mascote_triste.png",
#     "pagamento": "imagens/mascote_pagamento.png",
#
#
# }

# 🔄 Exibe o mascote com a expressão desejada
def mostrar_mascote_expressivo(janela, expressao="feliz", x=870, y=540):
    caminho = EXPRESSOES.get(expressao)
    if not caminho or not os.path.exists(caminho):
        print(f"⚠️ Expressão '{expressao}' não encontrada ou imagem ausente.")
        return

    img = Image.open(caminho).resize((130, 130))
    img_tk = ImageTk.PhotoImage(img, master=janela)

    label = tk.Label(janela, image=img_tk, bg="#fff")
    label.image = img_tk  # 🔒 mantém referência
    label.place(x=x, y=y)

# ✨ Mascote piscando em loop (opcional)
def mascote_piscante(janela, caminho_base="imagens/mascote_feliz.png", x=870, y=540):
    if not os.path.exists(caminho_base):
        return

    from PIL import ImageEnhance

    base = Image.open(caminho_base).resize((130, 130))
    normal = ImageTk.PhotoImage(base)
    escurecida = ImageTk.PhotoImage(ImageEnhance.Brightness(base).enhance(0.6))

    label = tk.Label(janela, image=normal, bg="#fff")
    label.image = normal
    label.place(x=x, y=y)

    def piscar(on=True):
        label.config(image=escurecida if on else normal)
        label.image = escurecida if on else normal
        janela.after(300 if on else 2400, piscar, not on)

    piscar()