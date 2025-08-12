from playsound import playsound
import os
import tkinter as tk
from modulos.utilitarios import caminho_arquivo
from modulos import dados_compartilhados as dc
from modulos.utilitarios import caminho_arquivo


def caminho_arquivo(nome, subpasta=""):
    caminho = os.path.join(os.getcwd(), subpasta, nome)
    return caminho

def som_evento(caminho):
    try:
        playsound(caminho)
    except:
        print(f"⚠️ Erro ao tocar som: {caminho}")

def mostrar_splash(janela):
    splash = tk.Toplevel(janela)
    splash.title("Bem-vindo")
    tk.Label(splash, text="🔷 Ipojucão Sistema", font=("Arial", 24)).pack(padx=50, pady=50)
    splash.after(2000, splash.destroy)