import tkinter as tk
from tkinter import ttk
from som import alternar_som, tocar_som
import pygame
som_ativo = True  # isso pode ser movido para o módulo som.py
from modulos.utilitarios import caminho_arquivo

from modulos import dados_compartilhados as dc
from modulos.utilitarios import caminho_arquivo

def salvar_cliente():
    ...
    som_e_expressao_acao("salvar")


def criar_barra_som(janela):
    trilhas = {
        "Abertura": "sons/musica_abertura.mp3",
        "Consulta PET": "sons/musica_consulta_pet.mp3",
        "Relatórios": "sons/relatorio.mp3",
        "Fechamento": "sons/musica_end_of_day.mp3",
        "Mascote": "sons/bouncy_pet_intro.mp3"
    }

# def som_e_expressao_acao(acao):
#     trilhas_acoes = {
#         "salvar": ("sons/clair_de_lune_prelude.mp3", "🐶😄"),
#         "editar": ("sons/soft_edit_tune.mp3", "🤔"),
#         "excluir": ("sons/dramatic_delete.mp3", "😲"),
#         "buscar": ("sons/search_ping.mp3", "🔍🐶")
#     }
#     som, emoji = trilhas_acoes.get(acao, (None, ""))
#     if som:
#         tocar_som(som)
#     print(f"Mascote reage: {emoji}")

def som_e_expressao_acao(acao):
    acoes = {
        "salvar": ("som/clair_de_lune_prelude.mp3", "🐶😄"),
        "editar": ("som/soft_edit_tune.mp3", "🤔"),
        "excluir": ("som/dramatic_delete.mp3", "😲"),
        "buscar": ("som/search_ping.mp3", "🔍🐶")
    }
    caminho_som, emoji = acoes.get(acao, (None, ""))
    if caminho_som:
        tocar_som(caminho_som)
    print(f"Mascote reage: {emoji}")  # Aqui pode ser substituído por função visual

    # 🎛️ Frame flutuante
    barra_som = tk.Frame(janela, bg="#f0f0f0", relief="raised", bd=2)
    barra_som.place(x=600, y=10)

    # 🔈 Botão de som
    btn_audio = ttk.Button(barra_som, text="🔈 Som Ativado")
    btn_audio.grid(row=0, column=0, padx=5)
    btn_audio.config(command=lambda: alternar_som(btn_audio))

    # 🎶 Combobox de trilhas
    trilha_var = tk.StringVar(master=janela)
    trilha_combo = ttk.Combobox(barra_som, textvariable=trilha_var, values=list(trilhas.keys()), width=20, state="readonly")
    trilha_combo.grid(row=0, column=1, padx=5)
    trilha_combo.set("Abertura")

    # ▶️ Botão para tocar trilha selecionada
    def tocar_trilha_selecionada():
        trilha_nome = trilha_var.get()
        caminho = trilhas.get(trilha_nome)
        if caminho:
            tocar_som(caminho)

    btn_play = ttk.Button(barra_som, text="▶️ Tocar", command=tocar_trilha_selecionada)
    btn_play.grid(row=0, column=2, padx=5)

    import pygame

    def parar_som():
        pygame.mixer.music.stop()

    # Alterna entre som ativado/desativado
    def alternar_som_estado(trilha_var):
        estado_atual = trilha_var.get()
        if estado_atual == "Desativado":
            trilha_var.set("Ativado")
        else:
            trilha_var.set("Desativado")
            pygame.mixer.music.stop()

    btn_parar = ttk.Button(barra_som, text="⏹️ Parar Som", command=parar_som)
    btn_parar.grid(row=0, column=3, padx=5)

import pygame

som_ativo = True  # isso pode ser movido para o módulo som.py

def tocar_som(caminho):
    if som_ativo and caminho:
        try:
            pygame.mixer.music.load(caminho)
            pygame.mixer.music.play()
        except Exception as e:
            print("Erro ao tocar som:", e)

def alternar_som(botao):
    global som_ativo
    som_ativo = not som_ativo
    estado = "Ativado" if som_ativo else "Desativado"
    botao.config(text=f"🔈 Som {estado}")
    if not som_ativo:
        pygame.mixer.music.stop()