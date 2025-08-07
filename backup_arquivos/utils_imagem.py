from PIL import ImageTk, ImageEnhance
import tkinter as tk

def fade_in_imagem(label, imagem_pil, duracao_ms=300, passos=10):
    """
    Aplica efeito fade-in progressivamente no Label com uma imagem PIL.
    - label: widget onde a imagem será exibida
    - imagem_pil: imagem PIL já redimensionada
    """
    def animar(passo=0):
        fator = (passo + 1) / passos  # brilho gradual: 0.1 → 1.0
        enhancer = ImageEnhance.Brightness(imagem_pil)
        img_fade = enhancer.enhance(fator)
        img_tk = ImageTk.PhotoImage(img_fade)

        label.img_ref = img_tk  # mantém referência
        label.config(image=img_tk)

        if passo < passos - 1:
            label.after(int(duracao_ms / passos), animar, passo + 1)

    animar()