# 📦 IMPORTAÇÕES
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import pygame

# 🐾 INICIALIZAÇÃO DO SOM
#pygame.mixer.init()
#pygame.mixer.music.load(r"C:\Users\VEIRANO\PycharmProjects\ModuloTkinter\Planilha Controle Ipojucão\sons\bouncy_pet_intro.mp3")
#ygame.mixer.music.load("sons/bouncy_pet_intro.mp3")
#pygame.mixer.music.play(-1)

# 📇 BASE DE USUÁRIOS SIMULADA (pode ser salva em JSON depois)
usuarios = {
    "roquereinaldo@gmail.com": {"senha": "975624asa", "nome": "Reinaldo", "perfil": "Administrador"},
    "araujolindi@yahoo.com.br": {"senha": "1234", "nome": "Lindinalva", "perfil": "Administrador"},
    "cebous@hotmail.com.br": {"senha": "1234", "nome": "Raphael", "perfil": "Administrador"},
    "admin@ipojucao.com": {"senha": "1234", "nome": "Marlene", "perfil": "Administrador"},
    "anna_paula@ipojucao.com": {"senha": "1234", "nome": "Anna Paula", "perfil": "Administrador"},
    "wander@ipojucao.com": {"senha": "petpet", "nome": "Wander", "perfil": "Funcionário"},
}

som_global_ativo = True
usuario_atual = None

def mostrar_splash():
    splash = tk.Toplevel()
    splash.geometry("600x300")
    splash.title("🐾 Ipojucão")

    logo_path = os.path.join("imagens", "logo_ipojucao.png")
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).resize((600, 300))
        logo_img = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(splash, image=logo_img)
        logo_label.image = logo_img
        logo_label.pack()

    splash.after(3000, splash.destroy)  # tempo de exibição: 3 segundos
    splash.transient()
    splash.grab_set()

    mostrar_splash()
    criar_login(janela_inicial, ao_logar_callback=abrir_janela_principal)



# 🎵 FUNÇÃO DE SOM + MASCOTE
def tocar_som(caminho):
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

def tocar_som_acesso(resultado, janela_login):
    som = os.path.join("../Planilha Controle Ipojucão/sons", "acesso_concedido.mp3") if resultado else os.path.join(
        "../Planilha Controle Ipojucão/sons", "acesso_negado.mp3")
    if som_global_ativo and os.path.exists(som):
        tocar_som(som)
    try:
        from mascote import mostrar_mascote_expressivo
        expressao = "feliz" if resultado else "negativo"
        mostrar_mascote_expressivo(janela_login, expressao)
    except:
        pass  # Se mascote.py não existir, ignora


# def mostrar_splash():
#     splash = tk.Toplevel()gin
#     splash.geometry("600x300")
#     splash.title("🐾 Ipojucão")
#
#     logo_path = os.path.join("imagens", "logo_ipojucao.png")
#     if os.path.exists(logo_path):
#         logo = Image.open(logo_path).resize((600, 300))
#         logo_img = ImageTk.PhotoImage(logo)
#         logo_label = tk.Label(splash, image=logo_img)
#         logo_label.image = logo_img
#         logo_label.pack()
#
#     splash.after(3000, splash.destroy)  # tempo de exibição: 3 segundos
#     splash.transient()
#     splash.grab_set()
#
#     mostrar_splash()
#     criar_login(janela_inicial, ao_logar_callback=abrir_janela_principal)

# 🔐 FUNÇÃO PRINCIPAL DE LOGIN
def criar_login(janela_principal, ao_logar_callback):
    janela_login = tk.Toplevel(janela_principal)
    janela_login.title("Login Ipojucão")
    janela_login.geometry("800x500")
    janela_login.resizable(False, False)

    ####
    caminho_intro = os.path.join("../Planilha Controle Ipojucão/sons", "bouncy_pet_intro.mp3")
    if som_global_ativo and os.path.exists(caminho_intro):
        tocar_som(caminho_intro)

    ####

    caminho_img = os.path.join("imagens", "login_fundo.png")
    if os.path.exists(caminho_img):
        img = Image.open(caminho_img).resize((800, 500))
        bg = ImageTk.PhotoImage(img)
        fundo = tk.Label(janela_login, image=bg)
        fundo.image = bg
        fundo.place(relwidth=1, relheight=1)

    frame = tk.Frame(janela_login, bg="#ffffff", bd=2)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Email:", bg="white").grid(row=0, column=0, pady=10, padx=10)
    email_entry = tk.Entry(frame, width=30)
    email_entry.grid(row=0, column=1, pady=10)

    tk.Label(frame, text="Senha:", bg="white").grid(row=1, column=0, pady=10, padx=10)
    senha_entry = tk.Entry(frame, width=30, show="*")
    senha_entry.grid(row=1, column=1, pady=10)

    mostrar_senha = tk.BooleanVar(value=False)
    mostrar_checkbox = tk.Checkbutton(
        frame,
        text="Mostrar senha",
        variable=mostrar_senha,
        command=lambda: senha_entry.config(show="" if mostrar_senha.get() else "*"),
        bg="white"
    )
    mostrar_checkbox.grid(row=2, column=1, sticky="w")

    def autenticar():
        email = email_entry.get().strip()
        senha = senha_entry.get().strip()
        user = usuarios.get(email)
        if user and user["senha"] == senha:
            global usuario_atual
            usuario_atual = email
            tocar_som_acesso(True, janela_login)
            messagebox.showinfo("Bem-vindo", f"Olá, {user['nome']}!\nPerfil: {user['perfil']}")
            ao_logar_callback(user["nome"], user["perfil"])
            janela_login.destroy()
        else:
            tocar_som_acesso(False, janela_login)
            messagebox.showerror("Acesso negado", "Email ou senha inválidos.")

    tk.Button(frame, text="Entrar", command=autenticar, bg="#4CAF50", fg="white").grid(row=3, columnspan=2, pady=20)

# 👨‍💼 TELA PRINCIPAL COM BOTÕES DINÂMICOS
def abrir_janela_principal(nome, perfil):
    janela_principal = tk.Tk()
    janela_principal.title(f"Ipojucão • Bem-vindo {nome}")
    janela_principal.geometry("900x600")

    notebook = ttk.Notebook(janela_principal)
    notebook.pack(expand=True, fill='both')

    # Aba 1: Dashboard
    aba_dashboard = ttk.Frame(notebook)
    notebook.add(aba_dashboard, text="Início")

    tk.Label(aba_dashboard, text="Painel Inicial", font=("Segoe UI", 14)).pack(pady=20)

    # Aba 2: Usuários (somente administrador)

    #tk.Label(janela_principal, text=f"Bem-vindo, {nome} ({perfil})!", font=("Arial", 12)).pack(pady=10)

    if perfil == "Administrador":
        tk.Button(janela_principal, text="Novo Usuário", command=lambda: cadastro_usuario(janela_principal)).pack(pady=5)
        tk.Button(janela_principal, text="Excluir Usuário", command=lambda: excluir_usuario(janela_principal)).pack(pady=5)

    tk.Button(janela_principal, text="Sair", command=janela_principal.destroy, bg="#f44336", fg="white").pack(pady=30)

    janela_principal.mainloop()

# 🧍 CADASTRO DE USUÁRIO
def cadastro_usuario(janela_principal):
    janela_cadastro = tk.Toplevel(janela_principal)
    janela_cadastro.title("Novo Usuário")
    janela_cadastro.geometry("400x300")

    tk.Label(janela_cadastro, text="Nome:").pack(pady=5)
    nome_entry = tk.Entry(janela_cadastro)
    nome_entry.pack()

    tk.Label(janela_cadastro, text="Email:").pack(pady=5)
    email_entry = tk.Entry(janela_cadastro)
    email_entry.pack()

    tk.Label(janela_cadastro, text="Senha:").pack(pady=5)
    senha_entry = tk.Entry(janela_cadastro, show="*")
    senha_entry.pack()

    tk.Label(janela_cadastro, text="Perfil:").pack(pady=5)
    perfil_var = tk.StringVar(value="Funcionário")
    perfil_menu = tk.OptionMenu(janela_cadastro, perfil_var, "Administrador", "Funcionário")
    perfil_menu.pack()

    def salvar():
        nome = nome_entry.get().strip()
        email = email_entry.get().strip()
        senha = senha_entry.get().strip()
        perfil = perfil_var.get()
        if not nome or not email or not senha:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
            return
        if email in usuarios:
            messagebox.showerror("Duplicado", "Este email já está cadastrado.")
            return
        usuarios[email] = {"nome": nome, "senha": senha, "perfil": perfil}
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        janela_cadastro.destroy()

    tk.Button(janela_cadastro, text="Salvar", command=salvar, bg="#4CAF50", fg="white").pack(pady=20)

# ❌ EXCLUSÃO DE USUÁRIO
def excluir_usuario(janela_principal):
    janela_excluir = tk.Toplevel(janela_principal)
    janela_excluir.title("Excluir Usuário")
    janela_excluir.geometry("400x200")

    tk.Label(janela_excluir, text="Email do usuário a excluir:").pack(pady=10)
    email_entry = tk.Entry(janela_excluir)
    email_entry.pack()

    def excluir():
        email = email_entry.get().strip()
        if email in usuarios:
            confirmacao = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir {email}?")
            if confirmacao:
                del usuarios[email]
                messagebox.showinfo("Excluído", "Usuário removido com sucesso.")
                janela_excluir.destroy()
        else:
            messagebox.showerror("Não encontrado", "Usuário não localizado.")

    tk.Button(janela_excluir, text="Excluir", command=excluir, bg="#f44336", fg="white").pack(pady=20)

# 🚀 EXECUÇÃO DO PROGRAMA
janela_inicial = tk.Tk()
janela_inicial.withdraw()
criar_login(janela_inicial, ao_logar_callback=abrir_janela_principal)
janela_inicial.mainloop()