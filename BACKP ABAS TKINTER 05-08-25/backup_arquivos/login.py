import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import threading
#from playsound import playsound

# import pygame
# pygame.mixer.init()



#from aba_som import musica_consulta_pet
#musica_consulta_pet()

#from aba_som import tocar_som, lightsaber_ignition_6816

# ... depois do login validado:
# tocar_som_acesso(True)  # já resolve o som de acesso positivo
# tocar_som_acesso(True)
#lightsaber_ignition_6816()
#
import tkinter as tk
from tkinter import messagebox
# from PIL import Image, ImageTk
# import os
# import pygame
#
# # Inicializa som
# pygame.mixer.init()
#
# # Banco de usuários simulado
# usuarios = {
#     "roquereinaldo@gmail.com": {"senha": "975624asa", "nome": "Reinaldo", "perfil": "Administrador"},
#     "araujolindi@yahoo.com.br": {"senha": "1234", "nome": "Lindinalva", "perfil": "Administrador"},
#     "wander@ipojucao.com": {"senha": "petpet", "nome": "Wander", "perfil": "Funcionário"},
#     "cebous@hotmail.com.br": {"senha": "1234", "nome": "Raphael", "perfil": "Administrador"},
#     "admin@ipojucao.com": {"senha": "1234", "nome": "Marlene", "perfil": "Administrador"},
#     "anna_paula@ipojucao.com": {"senha": "1234", "nome": "Anna Paula", "perfil": "Administrador"},
#     "marlene@ipojucao.com": {"senha": "1234", "nome": "Marlene", "perfil": "Administrador"},
# }
#
#
# usuario_atual = None  # Variável global para guardar quem logou
#
#
# import tkinter as tk
# from tkinter import messagebox
#
# # # Dicionário de usuários
# # usuarios = {
# #     "admin": {"senha": "123", "perfil": "Administrador"},
# #     "joao": {"senha": "abc", "perfil": "Comum"}
# # }
#
# usuario_atual = None  # Variável global para guardar quem logou
#
# def verificar_login():
#     usuario = entrada_usuario.get()
#     senha = entrada_senha.get()
#
#     if usuario in usuarios and usuarios[usuario]["senha"] == senha:
#         global usuario_atual
#         usuario_atual = usuario
#         messagebox.showinfo("Login", "Login realizado com sucesso!")
#         abrir_janela_principal()
#     else:
#         messagebox.showerror("Erro", "Usuário ou senha incorretos.")
#
# def abrir_janela_principal():
#     janela_principal = tk.Tk()
#     janela_principal.title("Sistema Principal")
#     janela_principal.geometry("400x300")
#
#     user = usuarios.get(usuario_atual)
#
#     if user and user["perfil"] == "Administrador":
#         tk.Button(janela_principal, text="Novo Usuário", command=lambda: cadastro_usuario(janela_principal)).pack(pady=5)
#         tk.Button(janela_principal, text="Excluir Usuário", command=lambda: excluir_usuario(janela_principal)).pack(pady=5)
#     else:
#         tk.Label(janela_principal, text="Bem-vindo ao sistema!").pack(pady=10)
#
#     janela_principal.mainloop()
#
# # Interface da tela de login
# janela_login = tk.Tk()
# janela_login.title("Login")
# janela_login.geometry("300x200")
#
# tk.Label(janela_login, text="Usuário").pack()
# entrada_usuario = tk.Entry(janela_login)
# entrada_usuario.pack()
#
# tk.Label(janela_login, text="Senha").pack()
# entrada_senha = tk.Entry(janela_login, show="*")
# entrada_senha.pack()
#
# tk.Button(janela_login, text="Entrar", command=verificar_login).pack(pady=10)
#
# janela_login.mainloop()
#
#
# # Ativa som global
# som_global_ativo = True
#
# def tocar_som(caminho):
#     pygame.mixer.music.load(caminho)
#     pygame.mixer.music.play()
#
# def tocar_som_acesso(resultado, janela_login):
#     som = os.path.join("sons", "acesso_concedido.mp3") if resultado else os.path.join("sons", "acesso_negado.mp3")
#     if som_global_ativo and os.path.exists(som):
#         tocar_som(som)
#     from mascote import mostrar_mascote_expressivo
#     expressao = "feliz" if resultado else "negativo"
#     mostrar_mascote_expressivo(janela_login, expressao)
#
# def criar_login(janela_principal, ao_logar_callback):
#     janela_login = tk.Toplevel(janela_principal)
#     janela_login.title("Login Ipojucão")
#     janela_login.geometry("800x500")
#     janela_login.resizable(False, False)
#
#     # Fundo estilizado
#     caminho_img = os.path.join("imagens", "login_fundo.png")
#     if os.path.exists(caminho_img):
#         img = Image.open(caminho_img).resize((800, 500))
#         bg = ImageTk.PhotoImage(img)
#         fundo = tk.Label(janela_login, image=bg)
#         fundo.image = bg
#         fundo.place(relwidth=1, relheight=1)
#
#     # Container dos campos
#     frame = tk.Frame(janela_login, bg="#ffffff", bd=2)
#     frame.place(relx=0.5, rely=0.5, anchor="center")
#
#     tk.Label(frame, text="Email:", bg="white").grid(row=0, column=0, pady=10, padx=10)
#     email_entry = tk.Entry(frame, width=30)
#     email_entry.grid(row=0, column=1, pady=10)
#
#     tk.Label(frame, text="Senha:", bg="white").grid(row=1, column=0, pady=10, padx=10)
#     senha_entry = tk.Entry(frame, width=30, show="*")
#     senha_entry.grid(row=1, column=1, pady=10)
#
#     # Variável de controle para mostrar/ocultar senha
#     mostrar_senha = tk.BooleanVar(value=False)
#
#     def alternar_senha():
#         if mostrar_senha.get():
#             senha_entry.config(show="")
#         else:
#             senha_entry.config(show="*")
#
#     # Checkbutton para mostrar senha
#     mostrar_checkbox = tk.Checkbutton(
#         frame,
#         text="Mostrar senha",
#         variable=mostrar_senha,
#         command=alternar_senha,
#         bg="white"
#     )
#     mostrar_checkbox.grid(row=3, column=1, sticky="w")
#
#
#
#
#     def autenticar():
#         email = email_entry.get().strip()
#         senha = senha_entry.get().strip()
#
#         if not email or not senha:
#             messagebox.showwarning("Campos obrigatórios", "Por favor, preencha todos os campos.")
#             return
#
#         user = usuarios.get(email)
#         if user and user["senha"] == senha:
#             tocar_som_acesso(True, janela_login)
#             messagebox.showinfo("Bem-vindo", f"Olá, {user['nome']}!\nPerfil: {user['perfil']}")
#             ao_logar_callback(user["nome"], user["perfil"])
#
#             # Se for administrador, exibe botão para cadastro
#             if user["perfil"] == "Administrador":
#                 criar_botao_novo_usuario(janela_login)
#
#             janela_login.destroy()
#         else:
#             tocar_som_acesso(False, janela_login)
#             messagebox.showerror("Acesso negado", "Email ou senha inválidos.")
#
#     def criar_botao_novo_usuario(janela):
#         botao_novo = tk.Button(janela, text="Novo Usuário", bg="#2196F3", fg="white")
#         botao_novo.place(x=680, y=450)
#
#         def acao():
#             messagebox.showinfo("Em breve", "Função de cadastro em desenvolvimento 🛠️")
#
#         botao_novo.config(command=acao)
#
#
#
#         user = usuarios.get(email)
#
#         if user and user["senha"] == senha:
#             tocar_som_acesso(True, janela_login)
#             messagebox.showinfo("Bem-vindo", f"Olá, {user['nome']}!\nPerfil: {user['perfil']}")
#             ao_logar_callback(user["nome"], user["perfil"])
#             janela_login.destroy()
#         else:
#             tocar_som_acesso(False, janela_login)
#             messagebox.showerror("Acesso negado", "Email ou senha inválidos.")
#
#     tk.Button(frame, text="Entrar", command=autenticar, bg="#4CAF50", fg="white").grid(row=2, columnspan=2, pady=20)
#
#

























# # 🎯 Dicionário de usuários simulando um “banco de dados”
# usuarios = {
#     "roquereinaldo@gmail.com": {"senha": "975624asa", "nome": "Reinaldo", "perfil": "Administrador"},
#     "araujolindi@yahoo.com.br": {"senha": "1234", "nome": "Lindinalva", "perfil": "Administrador"},
#     "cebous@hotmail.com.br": {"senha": "1234", "nome": "Raphael", "perfil": "Administrador"},
#     "admin@ipojucao.com": {"senha": "1234", "nome": "Marlene", "perfil": "Administrador"},
#     "anna_paula@ipojucao.com": {"senha": "1234", "nome": "Anna Paula", "perfil": "Administrador"},
#     "admin@ipojucao.com": {"senha": "1234", "nome": "Qualquer", "perfil": "Administrador"},
#     "wander@ipojucao.com": {"senha": "petpet", "nome": "Wander", "perfil": "Funcionário"},
# }
#
# som_global_ativo = True  # Pode ser controlado por botão global
#
# def tocar_som_acesso(resultado=True):
#     if som_global_ativo:
#         som = os.path.join("sons", "acesso_concedido.mp3") if resultado else os.path.join("sons", "acesso_negado.mp3")
#         if os.path.exists(som):
#             #threading.Thread(target=playsound, args=(som,), daemon=True).start() # Somente se usar pacote Playsound
#             tocar_som(som)
#             from mascote import mostrar_mascote_expressivo
#
#             mostrar_mascote_expressivo(janela, expressao="feliz")
#             mostrar_mascote_expressivo(janela, expressao="negativo")
#
# def criar_login(janela_principal, ao_logar_callback):
#     janela_login = tk.Toplevel(janela_principal)
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
#         print("🟢 Janela de login criada!")
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
#     def autenticar():
#         email = email_entry.get().strip()
#         senha = senha_entry.get().strip()
#         user = usuarios.get(email)
#
#         if user and user["senha"] == senha:
#             tocar_som_acesso(True)
#             messagebox.showinfo("Bem-vindo", f"Olá, {user['nome']}!\nPerfil: {user['perfil']}")
#             ao_logar_callback(user["nome"], user["perfil"])
#             janela_login.destroy()
#         else:
#             tocar_som_acesso(False)
#             messagebox.showerror("Acesso negado", "Email ou senha inválidos.")
#
#     tk.Button(janela_login, text="Entrar", command=autenticar).place(x=370, y=270)
#
#     # (Opcional) Botão para criar novo usuário – só visível após login adm
#     # (Você pode adicionar essa função mais tarde)
#
# from mascote import mostrar_mascote_expressivo
#
# def autenticar():
#     ...
#     if sucesso:
#         mostrar_mascote_expressivo(janela_login, "feliz")
#     else:
#         mostrar_mascote_expressivo(janela_login, "negativo")
#
