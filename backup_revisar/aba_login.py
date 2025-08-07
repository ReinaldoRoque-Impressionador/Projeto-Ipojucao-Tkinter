# import json
# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import os
# import threading
# #from playsound import playsound
# from modulos.som import som_evento, alternar_som, animar_mascote
# from modulos.mascote import mostrar_mascote_expressivo
# from PIL import Image, ImageTk
# import os
# import tkinter as tk
# from tkinter import messagebox
# from utilitarios import caminho_arquivo
# from modulos.dados_compartilhados import usuarios
#
# logo_splash = caminho_arquivo("splash.png", subpasta=os.path.join("..", "..", "imagensipojucao"))
# som_relatorio = caminho_arquivo("relatorio_finalizado.mp3", subpasta="sons")
#
#
# from tkinter import ttk, messagebox
# from som import som_evento
# from mascote import mostrar_mascote_expressivo
#
#
# # btn_audio.config(command=lambda: alternar_som(btn_audio))
# # btn_audio.place(x=20, y=20)
#
# from som import animar_mascote
#
#
#
# #import pygame
# #pygame.mixer.init()
#
#
#
# from som import som_evento, alternar_som, tocar_som
#
# def autenticar():
#     ...
#     if sucesso:
#         som_evento("login_sucesso")
#     else:
#         som_evento("login_falha")
#
#
# #lightsaber_ignition_6816()
#
# CAMINHO_USUARIOS = "usuarios.json"
#
# def carregar_usuarios():
#     if os.path.exists(CAMINHO_USUARIOS):
#         with open(CAMINHO_USUARIOS, "r", encoding="utf-8") as f:
#             return json.load(f)
#     return {}
#
# def salvar_usuarios(usuarios):
#     with open(CAMINHO_USUARIOS, "w", encoding="utf-8") as f:
#         json.dump(usuarios, f, indent=2)
#
# # def tocar_som_acesso(resultado=True):
# #     if som_global_ativo:
# #         som = os.path.join("sons", "acesso_concedido.mp3") if resultado else os.path.join("sons", "acesso_negado.mp3")
# #         if os.path.exists(som):
# #             som_evento("login_sucesso")
# # def tocar_som_sucesso(acao):
# #     mapa = {
# #         "adicionar": "som/usuario_adicionado.mp3",
# #         "remover": "som/usuario_removido.mp3"
# #     }
#
#         #carregar_lista()
#
#     caminho = mapa.get(acao)
#     if som_global_ativo and caminho and os.path.exists(caminho):
#         tocar_som(caminho)
# #usuarios = carregar_usuarios()
#
# # 🎯 Dicionário de usuários simulando um “banco de dados”
# # usuarios = {
# #     "roquereinaldo@gmail.com": {"senha": "975624asa", "nome": "Reinaldo", "perfil": "Administrador"},
# #     "araujolindi@yahoo.com.br": {"senha": "1234", "nome": "Lindinalva", "perfil": "Administrador"},
# #     "cebous@hotmail.com.br": {"senha": "1234", "nome": "Raphael", "perfil": "Administrador"},
# #     "admin@ipojucao.com": {"senha": "1234", "nome": "Marlene", "perfil": "Administrador"},
# #     "anna_paula@ipojucao.com": {"senha": "1234", "nome": "Anna Paula", "perfil": "Administrador"},
# #     "admin@ipojucao.com": {"senha": "1234", "nome": "Qualquer", "perfil": "Administrador"},
# #     "wander@ipojucao.com": {"senha": "petpet", "nome": "Wander", "perfil": "Funcionário"},
# # }
#
# som_global_ativo = True  # Pode ser controlado por botão global
#
# # ✅ 1. Função  — interface amigável
# # Adicione este código ao seu :
#
#
# # from tkinter import ttk, messagebox
# # from som import som_evento
# # from mascote import mostrar_mascote_expressivo
#
# def gerenciar_usuarios(janela_pai):
#     janela_gerenciar = tk.Toplevel(janela_pai)
#     janela_gerenciar.title("Gerenciar Usuários")
#     janela_gerenciar.geometry("420x360")
#     janela_gerenciar.resizable(False, False)
#
#     # Campos
#     tk.Label(janela_gerenciar, text="Email:").place(x=20, y=20)
#     entrada_email = tk.Entry(janela_gerenciar, width=40)
#     entrada_email.place(x=100, y=20)
#
#     tk.Label(janela_gerenciar, text="Senha:").place(x=20, y=60)
#     entrada_senha = tk.Entry(janela_gerenciar, width=40, show="*")
#     entrada_senha.place(x=100, y=60)
#
#     tk.Label(janela_gerenciar, text="Nome:").place(x=20, y=100)
#     entrada_nome = tk.Entry(janela_gerenciar, width=40)
#     entrada_nome.place(x=100, y=100)
#
#     tk.Label(janela_gerenciar, text="Perfil:").place(x=20, y=140)
#     entrada_perfil = tk.Entry(janela_gerenciar, width=40)
#     entrada_perfil.place(x=100, y=140)
#
#     # Treeview
#     tv = ttk.Treeview(janela_gerenciar, columns=("Email", "Nome", "Perfil"), show="headings")
#     tv.heading("Email", text="Email")
#     tv.heading("Nome", text="Nome")
#     tv.heading("Perfil", text="Perfil")
#     tv.place(x=20, y=250, width=380, height=100)
#
#     def carregar_lista():
#         tv.delete(*tv.get_children())
#         for email, dados in usuarios.items():
#             tv.insert("", "end", values=(email, dados["nome"], dados["perfil"]))
#
#     carregar_lista()
#
#     # Ações
#     def adicionar():
#         email = entrada_email.get().strip()
#         senha = entrada_senha.get().strip()
#         nome = entrada_nome.get().strip()
#         perfil = entrada_perfil.get().strip()
#
#         if email and senha and nome and perfil:
#             usuarios[email] = {
#                 "senha": senha,
#                 "nome": nome,
#                 "perfil": perfil
#             }
#             salvar_usuarios(usuarios)
#             som_evento("usuario_adicionado")
#             mostrar_mascote_expressivo(janela_gerenciar, "piscando")
#             messagebox.showinfo("Usuário Adicionado", f"{nome} foi cadastrado com sucesso!")
#             carregar_lista()
#         else:
#             messagebox.showwarning("Campos Incompletos", "Preencha todos os campos.")
#
#     def remover():
#         email = entrada_email.get().strip()
#         if email in usuarios:
#             del usuarios[email]
#             salvar_usuarios(usuarios)
#             som_evento("usuario_removido")
#             mostrar_mascote_expressivo(janela_gerenciar, "negativo")
#             messagebox.showinfo("Usuário Removido", f"{email} foi removido com sucesso!")
#             carregar_lista()
#         else:
#             messagebox.showerror("Erro", "Usuário não encontrado.")
#
#     def alterar_senha():
#         email = entrada_email.get().strip()
#         nova_senha = entrada_senha.get().strip()
#
#         if email in usuarios:
#             if not nova_senha:
#                 messagebox.showwarning("Nova senha em branco", "Digite uma nova senha.")
#                 return
#
#             confirmar = messagebox.askyesno("Confirmar alteração", f"Alterar senha de {email}?")
#             if confirmar:
#                 usuarios[email]["senha"] = nova_senha
#                 salvar_usuarios(usuarios)
#                 som_evento("usuario_adicionado")  # Reaproveita som
#                 mostrar_mascote_expressivo(janela_gerenciar, "feliz")
#                 messagebox.showinfo("Senha alterada", f"Senha de {email} atualizada com sucesso!")
#                 carregar_lista()
#         else:
#             messagebox.showerror("Usuário não encontrado", f"{email} não está cadastrado.")
#
#     # Botões
#     tk.Button(janela_gerenciar, text="➕ Adicionar", command=adicionar).place(x=100, y=200)
#     tk.Button(janela_gerenciar, text="➖ Remover", command=remover).place(x=220, y=200)
#     tk.Button(janela_gerenciar, text="✏️ Alterar senha", command=alterar_senha).place(x=155, y=210)








































# def gerenciar_usuarios(janela_pai):
#     janela_gerenciar = tk.Toplevel(janela_pai)
#     janela_gerenciar.title("Gerenciar Usuários")
#     janela_gerenciar.geometry("420x320")
#     janela_gerenciar.resizable(False, False)
#
#     tk.Label(janela_gerenciar, text="Email:").place(x=20, y=20)
#     entrada_email = tk.Entry(janela_gerenciar, width=40)
#     entrada_email.place(x=100, y=20)
#
#     tk.Label(janela_gerenciar, text="Senha:").place(x=20, y=60)
#     entrada_senha = tk.Entry(janela_gerenciar, width=40, show="*")
#     entrada_senha.place(x=100, y=60)
#
#     tk.Label(janela_gerenciar, text="Nome:").place(x=20, y=100)
#     entrada_nome = tk.Entry(janela_gerenciar, width=40)
#     entrada_nome.place(x=100, y=100)
#
#     tk.Label(janela_gerenciar, text="Perfil:").place(x=20, y=140)
#     entrada_perfil = tk.Entry(janela_gerenciar, width=40)
#     entrada_perfil.place(x=100, y=140)
#
#     def adicionar():
#         email = entrada_email.get().strip()
#         senha = entrada_senha.get().strip()
#         nome = entrada_nome.get().strip()
#         perfil = entrada_perfil.get().strip()
#
#         carregar_lista()
#
#         if email and senha and nome and perfil:
#             usuarios[email] = {
#                 "senha": senha,
#                 "nome": nome,
#                 "perfil": perfil
#             }
#             salvar_usuarios(usuarios)
#             som_evento("usuario_adicionado")
#             messagebox.showinfo("Usuário Adicionado", f"{nome} foi cadastrado com sucesso!")
#
#             carregar_lista()
#
#         else:
#             messagebox.showwarning("Campos Incompletos", "Preencha todos os campos.")
#
#     def remover():
#         email = entrada_email.get().strip()
#         if email in usuarios:
#             del usuarios[email]
#             salvar_usuarios(usuarios)
#             tocar_som_sucesso("remover")
#             messagebox.showinfo("Usuário Removido", f"{email} foi removido com sucesso!")
#             carregar_lista()
#         else:
#             messagebox.showerror("Erro", "Usuário não encontrado.")
#
#     tk.Button(janela_gerenciar, text="➕ Adicionar", command=adicionar).place(x=100, y=200)
#     tk.Button(janela_gerenciar, text="➖ Remover", command=remover).place(x=220, y=200)
#
# # Àrvore para visualizar usuários
#     tv = ttk.Treeview(janela_gerenciar, columns=("Email", "Nome", "Perfil"), show="headings")
#     tv.heading("Email", text="Email")
#     tv.heading("Nome", text="Nome")
#     tv.heading("Perfil", text="Perfil")
#     tv.place(x=20, y=250, width=380, height=100)
#
#     carregar_lista(tv)
#
# def carregar_lista():
#     tv.delete(*tv.get_children())
#     for email, dados in usuarios.items():
#         tv.insert("", "end", values=(email, dados["nome"], dados["perfil"]))
#

# 🎯 2. Liberar acesso à tela de gerenciamento somente para administradores
# No seu ao_logar(nome, perfil) do main.py, adicione:




# def criar_login(janela_principal, ao_logar_callback):
#     janela_login = tk.Toplevel()
#     janela_login.title("Login Ipojucão")
#     janela_login.geometry("800x500")
#     janela_login.resizable(False, False)
#
#     # 🖼️ Imagem de fundo
#     caminho_imagem = os.path.join("imagens", "login_fundo.png")  # nome do seu arquivo de fundo
#     if os.path.exists(caminho_imagem):
#         img = Image.open(caminho_imagem).resize((800, 500))
#         bg = ImageTk.PhotoImage(img)
#         bg_label = tk.Label(janela_login, image=bg)
#         bg_label.image = bg
#         bg_label.place(relwidth=1, relheight=1)
#
# # 📋 Campos de login
# tk.Label(janela_login, text="Email:", bg="white").place(x=260, y=180)
# email_entry = tk.Entry(janela_login, width=30)
# email_entry.place(x=330, y=180)
#
# tk.Label(janela_login, text="Senha:", bg="white").place(x=260, y=220)
# senha_entry = tk.Entry(janela_login, width=30, show="*")
# senha_entry.place(x=330, y=220)
#


usuarios = carregar_usuarios()

def criar_login(janela_principal, ao_logar_callback):
    from som import som_evento, alternar_som, animar_mascote
    from mascote import mostrar_mascote_expressivo

    janela_login = tk.Toplevel(janela_principal)
    janela_login.title("Login Ipojucão")
    janela_login.geometry("800x500")
    janela_login.resizable(False, False)
    animar_mascote(janela_login)  # ✅ aqui está certo

    # 🔈 Botão de som
    btn_audio = tk.Button(janela_login, text="🔈 Som Ativado")
    btn_audio.config(command=lambda: alternar_som(btn_audio))
    btn_audio.place(x=20, y=20)

    # 🖼️ Imagem de fundo
    caminho_imagem = os.path.join("imagens", "login_fundo.png")
    if os.path.exists(caminho_imagem):
        img = Image.open(caminho_imagem).resize((800, 500))
        bg = ImageTk.PhotoImage(img)
        bg_label = tk.Label(janela_login, image=bg)
        bg_label.image = bg
        bg_label.place(relwidth=1, relheight=1)

    # 🐶 Mascote piscante
    animar_mascote(janela_login)

    # 📋 Campos de login
    tk.Label(janela_login, text="Email:", bg="white").place(x=260, y=180)
    email_entry = tk.Entry(janela_login, width=30)
    email_entry.place(x=330, y=180)

    tk.Label(janela_login, text="Senha:", bg="white").place(x=260, y=220)
    senha_entry = tk.Entry(janela_login, width=30, show="*")
    senha_entry.place(x=330, y=220)

    # 🔐 Autenticação
    def autenticar():
        email = email_entry.get().strip()
        senha = senha_entry.get().strip()
        user = usuarios.get(email)

        if user and user["senha"] == senha:
            som_evento("login_sucesso")
            mostrar_mascote_expressivo(janela_login, "feliz")
            messagebox.showinfo("Bem-vindo", f"Olá, {user['nome']}!\nPerfil: {user['perfil']}")
            janela_login.destroy()
            ao_logar_callback(user["nome"], user["perfil"])
        else:
            som_evento("login_falha")
            mostrar_mascote_expressivo(janela_login, "negativo")
            messagebox.showerror("Acesso negado", "Email ou senha inválidos.")

    # 🔘 Botão de login
    tk.Button(janela_login, text="Entrar", command=autenticar).place(x=370, y=270)

# def criar_login(janela_principal, ao_logar_callback):
#     janela_login = tk.Toplevel(janela_principal)
#     janela_login.title("Login Ipojucão")
#     janela_login.geometry("800x500")
#     animar_mascote(janela_login)
#     janela_login.resizable(False, False)
#
#     # 🔈 Botão de som
#     btn_audio = tk.Button(janela_login, text="🔈 Som Ativado")
#     btn_audio.config(command=lambda: alternar_som(btn_audio))
#     btn_audio.place(x=20, y=20)
#
#     # 🖼️ Imagem de fundo
#     caminho_imagem = os.path.join("imagens", "login_fundo.png")
#     if os.path.exists(caminho_imagem):
#         img = Image.open(caminho_imagem).resize((800, 500))
#         bg = ImageTk.PhotoImage(img)
#         bg_label = tk.Label(janela_login, image=bg)
#         bg_label.image = bg
#         bg_label.place(relwidth=1, relheight=1)
#
#     # 🐶 Mascote piscante
#     animar_mascote(janela_login)
#
#     # 📋 Campos de login
#     tk.Label(janela_login, text="Email:", bg="white").place(x=260, y=180)
#     email_entry = tk.Entry(janela_login, width=30)
#     email_entry.place(x=330, y=180)
#
#     tk.Label(janela_login, text="Senha:", bg="white").place(x=260, y=220)
#     senha_entry = tk.Entry(janela_login, width=30, show="*")
#     senha_entry.place(x=330, y=220)
#
#     # 🔐 Autenticação
#     def autenticar():
#         email = email_entry.get().strip()
#         senha = senha_entry.get().strip()
#         user = usuarios.get(email)
#
#         if user and user["senha"] == senha:
#             som_evento("login_sucesso")
#             mostrar_mascote_expressivo(janela_login, "feliz")
#             messagebox.showinfo("Bem-vindo", f"Olá, {user['nome']}!\nPerfil: {user['perfil']}")
#             janela_login.destroy()
#             ao_logar_callback(user["nome"], user["perfil"])
#         else:
#             som_evento("login_falha")
#             mostrar_mascote_expressivo(janela_login, "negativo")
#             messagebox.showerror("Acesso negado", "Email ou senha inválidos.")
#
#     # 🔘 Botão de login
#     tk.Button(janela_login, text="Entrar", command=autenticar).place(x=370, y=270)
#

#        KKKKKKKKKKKKKKKKKK

# def criar_login(janela_principal, ao_logar_callback):
#     janela_login = tk.Toplevel()
#     janela_login.title("Login Ipojucão")
#     janela_login.geometry("800x500")
#     janela_login.resizable(False, False)
#     btn_audio = tk.Button(janela_login, text="🔈 Som Ativado")
#
#     from som import alternar_som
#     btn_audio = tk.Button(janela_login, text="🔈 Som Ativado")
#     btn_audio.config(command=lambda: alternar_som(btn_audio))
#     btn_audio.place(x=20, y=20)

#          KKKKKKKKKKKKKKKKKKKKKKKKK
# 🖼️ Imagem de fundo
caminho_imagem = os.path.join("imagens", "login_fundo.png")  # nome do seu arquivo de fundo
if os.path.exists(caminho_imagem):
    img = Image.open(caminho_imagem).resize((800, 500))
    bg = ImageTk.PhotoImage(img)
#    bg_label = tk.Label(janela_login, image=bg)
    bg_label.image = bg
    bg_label.place(relwidth=1, relheight=1)

# 📋 Campos de login
#tk.Label(janela_login, text="Email:", bg="white").place(x=260, y=180)
#email_entry = tk.Entry(janela_login, width=30)
#email_entry.place(x=330, y=180)

#tk.Label(janela_login, text="Senha:", bg="white").place(x=260, y=220)
#senha_entry = tk.Entry(janela_login, width=30, show="*")
#senha_entry.place(x=330, y=220)

def autenticar():
    email = email_entry.get().strip()
    senha = senha_entry.get().strip()
    user = usuarios.get(email)

    if user and user["senha"] == senha:
        tocar_som_acesso(True)
        messagebox.showinfo("Bem-vindo", f"Olá, {user['nome']}!\nPerfil: {user['perfil']}")
        janela_login.destroy()
        ao_logar_callback(user["nome"], user["perfil"])
    else:
        tocar_som_acesso(False)
        messagebox.showerror("Acesso negado", "Email ou senha inválidos.")

#tk.Button(janela_login, text="Entrar", command=autenticar).place(x=370, y=270)


#tk.Button(janela_gerenciar, text="Alterar senha", command=alterar_senha).place(x=155, y=210)

# 🔐 Função chamada após login bem-sucedido
def ao_logar(nome, perfil):
    janela.deiconify()  # Mostra a janela principal
    if perfil == "Administrador":
        gerenciar_usuarios(janela)

# 🧠 Carrega os dados dos usuários ao iniciar
usuarios = carregar_usuarios()


# def ao_logar(nome, perfil):
#     janela.deiconify()
#     if perfil == "Administrador":
#         from aba_login import gerenciar_usuarios
#         gerenciar_usuarios(janela_pai)
#
# # Carregar usuários inicialmente
# usuarios = carregar_usuarios()

# def alterar_senha():
#     email = email_entry.get().strip()  # Essas variáveis devem estar acessíveis
#     nova_senha = senha_entry.get().strip()  # O mesmo vale para elas

        # email = entrada_email.get().strip()
        # nova_senha = entrada_senha.get().strip()

# if email in usuarios:
#     if not nova_senha:
#         messagebox.showwarning("Nova senha em branco", "Digite uma nova senha.")
#     return
#
# confirmar = messagebox.askyesno("Confirmar alteração",f"Tem certeza que deseja alterar a senha de {email}?")
# if confirmar:
#     usuarios[email]["senha"] = nova_senha
#     salvar_usuarios(usuarios)
#     som_evento("usuario_adicionado")  # Reaproveita som
#     messagebox.showinfo("Senha alterada", f"Senha de {email} atualizada com sucesso!")
# else:
#     messagebox.showerror("Usuário não encontrado", f"{email} não está cadastrado.")
#
#     carregar_lista()

    # (Opcional) Botão para criar novo usuário – só visível após login adm
    # (Você pode adicionar essa função mais tarde)


#from tkinter import ttk

# def gerenciar_usuarios(janela_pai):
#     janela_gerenciar = tk.Toplevel(janela_pai)
#     janela_gerenciar.title("Gerenciar Usuários")
#     janela_gerenciar.geometry("420x320")
#     janela_gerenciar.resizable(False, False)
#
#
#
#
#
# carregar_lista()