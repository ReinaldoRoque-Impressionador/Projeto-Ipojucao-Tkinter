# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# # Se 'usuarios' estiver definido em outro arquivo:
# from aba_login import usuarios  # ou o arquivo correto
# import pygame
#from audio import tocar_musica, tocar_som_curto, parar_musica
#from aba_som import som_login, som_relatorio, tocar_trilha, alternar_som_estado
#from tkinter import ttk
from modulos.utilitarios import caminho_arquivo
#
#
# usuario_atual = None
#
# def cadastro_usuario(janela_principal):
#     janela_cadastro = tk.Toplevel(janela_principal)
#     janela_cadastro.title("Novo Usuário")
#     janela_cadastro.geometry("400x300")
#     janela_cadastro.resizable(False, False)
#
#     tk.Label(janela_cadastro, text="Nome:").pack(pady=5)
#     nome_entry = tk.Entry(janela_cadastro)
#     nome_entry.pack()
#
#     tk.Label(janela_cadastro, text="Email:").pack(pady=5)
#     email_entry = tk.Entry(janela_cadastro)
#     email_entry.pack()
#
#     tk.Label(janela_cadastro, text="Senha:").pack(pady=5)
#     senha_entry = tk.Entry(janela_cadastro, show="*")
#     senha_entry.pack()
#
#     tk.Label(janela_cadastro, text="Perfil:").pack(pady=5)
#     perfil_var = tk.StringVar(value="Funcionário")
#     perfil_menu = tk.OptionMenu(janela_cadastro, perfil_var, "Administrador", "Funcionário")
#     perfil_menu.pack()
#
#     def salvar():
#         nome = nome_entry.get().strip()
#         email = email_entry.get().strip()
#         senha = senha_entry.get().strip()
#         perfil = perfil_var.get()
#
#         if not nome or not email or not senha:
#             messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
#             return
#
#         if email in usuarios:
#             messagebox.showerror("Duplicado", "Este email já está cadastrado.")
#             return
#
#         usuarios[email] = {"nome": nome, "senha": senha, "perfil": perfil}
#         messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
#         janela_cadastro.destroy()
#
#     tk.Button(janela_cadastro, text="Salvar", command=salvar, bg="#4CAF50", fg="white").pack(pady=20)
#
#     if user["perfil"] == "Administrador":
#         tk.Button(janela_principal, text="Novo Usuário", command=lambda: cadastro_usuario(janela_principal)).pack()
#         tk.Button(janela_principal, text="Excluir Usuário", command=lambda: excluir_usuario(janela_principal)).pack()

#barra_audio(frame_aba_cadastro_usuario)  # ou frame_aba_menu, frame_aba_config, etc.