import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

#from playsound import playsound

#import pygame
#pygame.mixer.init()



#from aba_som import musica_consulta_pet
#musica_consulta_pet()

#from aba_som import tocar_som, lightsaber_ignition_6816

# ... depois do login validado:
# tocar_som_acesso(True)  # já resolve o som de acesso positivo
# tocar_som_acesso(True)
#lightsaber_ignition_6816()

# 🎯 Dicionário de usuários simulando um “banco de dados”
usuarios = {
    "roquereinaldo@gmail.com": {"senha": "975624asa", "nome": "Reinaldo", "perfil": "Administrador"},
    "araujolindi@yahoo.com.br": {"senha": "1234", "nome": "Lindinalva", "perfil": "Administrador"},
    "cebous@hotmail.com.br": {"senha": "1234", "nome": "Raphael", "perfil": "Administrador"},
    "admin@ipojucao.com": {"senha": "1234", "nome": "Marlene", "perfil": "Administrador"},
    "anna_paula@ipojucao.com": {"senha": "1234", "nome": "Anna Paula", "perfil": "Administrador"},
    "admin@ipojucao.com": {"senha": "1234", "nome": "Qualquer", "perfil": "Administrador"},
    "wander@ipojucao.com": {"senha": "petpet", "nome": "Wander", "perfil": "Funcionário"},
}

som_global_ativo = True  # Pode ser controlado por botão global

def tocar_som_acesso(resultado=True):
    if som_global_ativo:
        som = os.path.join("sons", "acesso_concedido.mp3") if resultado else os.path.join("sons", "acesso_negado.mp3")
        if os.path.exists(som):
            #threading.Thread(target=playsound, args=(som,), daemon=True).start() # Somente se usar pacote Playsound
            tocar_som(som)
            from mascote import mostrar_mascote_expressivo

            mostrar_mascote_expressivo(janela, expressao="feliz")
            mostrar_mascote_expressivo(janela, expressao="negativo")

def criar_login(janela_principal, ao_logar_callback):
    janela_login = tk.Toplevel()
    janela_login.title("Login Ipojucão")
    janela_login.geometry("800x500")
    janela_login.resizable(False, False)

    # 🖼️ Imagem de fundo
    caminho_imagem = os.path.join("imagens", "login_fundo.png")  # nome do seu arquivo de fundo
    if os.path.exists(caminho_imagem):
        img = Image.open(caminho_imagem).resize((800, 500))
        bg = ImageTk.PhotoImage(img)
        bg_label = tk.Label(janela_login, image=bg)
        bg_label.image = bg
        bg_label.place(relwidth=1, relheight=1)

    # 📋 Campos de login
    tk.Label(janela_login, text="Email:", bg="white").place(x=260, y=180)
    email_entry = tk.Entry(janela_login, width=30)
    email_entry.place(x=330, y=180)

    tk.Label(janela_login, text="Senha:", bg="white").place(x=260, y=220)
    senha_entry = tk.Entry(janela_login, width=30, show="*")
    senha_entry.place(x=330, y=220)

    def autenticar():
        email = email_entry.get().strip()
        senha = senha_entry.get().strip()
        user = usuarios.get(email)

        if user and user["senha"] == senha:
            tocar_som_acesso(True)
            messagebox.showinfo("Bem-vindo", f"Olá, {user['nome']}!\nPerfil: {user['perfil']}")
            janela_login.destroy()
            ao_logar_callback(user["nome"], user["perfil"])
            janela_login.destroy()
        else:
            tocar_som_acesso(False)
            messagebox.showerror("Acesso negado", "Email ou senha inválidos.")

    tk.Button(janela_login, text="Entrar", command=autenticar).place(x=370, y=270)

    # (Opcional) Botão para criar novo usuário – só visível após login adm
    # (Você pode adicionar essa função mais tarde)

from mascote import mostrar_mascote_expressivo

def autenticar():
    ...
    if sucesso:
        mostrar_mascote_expressivo(janela_login, "feliz")
    else:
        mostrar_mascote_expressivo(janela_login, "negativo")

