# tela_principal.py

import tkinter as tk
from modulos.som_expressao import som_e_expressao_acao
from PIL import Image, ImageTk
import os
from tkinter import ttk
from modulos.utilitarios import caminho_arquivo
from modulos import dados_compartilhados as dc



def caminho_imagem(nome):
    base = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base, "imagensipojucao", "imagens", nome)

def abrir_janela_principal(nome, perfil):
    janela = tk.Toplevel()
    janela.title(f"Bem-vindo, {nome} ({perfil})")
    janela.geometry("400x450")

    # 🐶 Carrega imagem inicial do mascote
    caminho_img_inicial = os.path.join(os.path.dirname(__file__), "imagens", "mascote_normal.png")
    #imagem = Image.open(caminho_img_inicial).resize((150, 150))
    imagem = Image.open(caminho_imagem("mascote_feliz.png")).resize((150, 150))
    imagem_tk = ImageTk.PhotoImage(imagem)

    print("Caminho mascote:", caminho_imagem("mascote_feliz.png"))
    print("Existe?", os.path.exists(caminho_imagem("mascote_feliz.png")))

    # 📌 Label que será atualizado com expressões
    label_mascote = tk.Label(janela, image=imagem_tk)
    label_mascote.image = imagem_tk
    label_mascote.pack(pady=10)

    # 👤 Informações do usuário
    label_usuario = tk.Label(janela, text=f"Usuário: {nome}\nPerfil: {perfil}", font=("Arial", 12))
    label_usuario.pack(pady=5)

    # 🔘 Botões para testar reações
    acoes = ["salvar", "editar", "excluir", "buscar"]
    for acao in acoes:
        botao = tk.Button(
            janela,
            text=acao.capitalize(),
            width=20,
            command=lambda ac=acao: som_e_expressao_acao(ac, label_mascote, janela)
        )
        botao.pack(pady=5)

    janela.protocol("WM_DELETE_WINDOW", janela.destroy)








# # tela_principal.py
#
# import tkinter as tk
# from modulos.som_expressao import som_e_expressao_acao
# from PIL import Image, ImageTk
# import os
# from tkinter import ttk
# from tkinter import ttk
# from modulos.utilitarios import caminho_arquivo
#
# from modulos import dados_compartilhados as dc
#
#
# def criar_interface():
#     janela = tk.Tk()
#     janela.title("Mascote Interativo")
#     janela.geometry("400x400")
#
#     # 🐶 Carrega imagem inicial do mascote
#     caminho_img_inicial = os.path.join(os.path.dirname(__file__), "imagens", "mascote_normal.png")
#     imagem = Image.open(caminho_img_inicial).resize((150, 150))
#     imagem_tk = ImageTk.PhotoImage(imagem)
#
#     # 📌 Label que será atualizado com expressões
#     label_mascote = tk.Label(janela, image=imagem_tk)
#     label_mascote.image = imagem_tk
#     label_mascote.pack(pady=10)
#
#     # 🔘 Botões para testar reações
#     acoes = ["salvar", "editar", "excluir", "buscar"]
#     for acao in acoes:
#         botao = tk.Button(
#             janela,
#             text=acao.capitalize(),
#             width=20,
#             command=lambda ac=acao: som_e_expressao_acao(ac, label_mascote, janela)
#         )
#         botao.pack(pady=5)
#
#     janela.mainloop()
#
# # 🚀 Executa a interface
# if __name__ == "__main__":
#     criar_interface()