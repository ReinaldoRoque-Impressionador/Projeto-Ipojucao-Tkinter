import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

from modulos.audio import tocar_musica, tocar_som_curto, parar_musica
from utilitarios import caminho_arquivo
from dados_compartilhados import usuarios, som_global_ativo

try:
    from mascote import mostrar_mascote_expressivo
except ImportError:
    mostrar_mascote_expressivo = lambda *args: None  # Fallback

# No início do arquivo, após as importações
def chamar_mascote_login(janela, erro_senha=False):
    expressao = "triste" if erro_senha else "feliz"
    mostrar_mascote_expressivo(janela, expressao=expressao)

def caminho_arquivo(nome, subpasta=None):
    raiz = os.path.dirname(os.path.dirname(__file__))  # volta para raiz do projeto
    return os.path.join(raiz, subpasta if subpasta else "", nome)



# def caminho_expressao(expressao):
#     raiz = os.path.dirname(os.path.dirname(__file__))  # raiz do projeto
#     caminho = os.path.join(raiz, "imagensipojucao", "imagens", f"mascote_{expressao}.png")
#     return caminho if os.path.exists(caminho) else None

def caminho_expressao(expressao):
    base = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base, "imagensipojucao", "expressoes", f"mascote_{expressao}.png")

    caminho_img = caminho_expressao("feliz")
    print(caminho_img, os.path.exists(caminho_img))

def criar_login(janela_principal, ao_logar_callback):
    janela_login = tk.Toplevel(janela_principal)
    janela_login.title("Login Ipojucão")
    janela_login.geometry("800x500")
    janela_login.resizable(False, False)

    chamar_mascote_login(janela_login, erro_senha=True)
    chamar_mascote_login(janela_login, erro_senha=False)



    # 🔊 Som de fundo
    intro_path = caminho_arquivo("bouncy_pet_intro.mp3", subpasta="sons")
    if som_global_ativo and os.path.exists(intro_path):
        tocar_musica("sons/intro.mp3")
        tocar_som_curto("sons/clique.mp3")

    # 🖼️ Fundo com imagem
    fundo_path = caminho_arquivo("login_fundo.png", subpasta="imagens")
    if os.path.exists(fundo_path):
        fundo_img = Image.open(fundo_path).resize((800, 500))
        bg = ImageTk.PhotoImage(fundo_img)
        fundo = tk.Label(janela_login, image=bg)
        fundo.image = bg
        fundo.place(relwidth=1, relheight=1)

    # 📦 Container central
    frame = tk.Frame(janela_login, bg="#ffffff", bd=2)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # 📧 Email
    tk.Label(frame, text="Email:", bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    email_entry = tk.Entry(frame, width=30)
    email_entry.grid(row=0, column=1, pady=10)

    # 🔒 Senha
    tk.Label(frame, text="Senha:", bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    senha_entry = tk.Entry(frame, width=30, show="*")
    senha_entry.grid(row=1, column=1, pady=10)

    # 👁️ Alternância de senha
    mostrar_senha = tk.BooleanVar(value=False)

    def alternar_senha():
        senha_entry.config(show="" if mostrar_senha.get() else "*")
        novo_icone = olho_aberto_img if mostrar_senha.get() else olho_fechado_img
        mostrar_checkbox.config(image=novo_icone)
        mostrar_checkbox.image = novo_icone
        if som_global_ativo:
            tocar_som_curto("sons/clique.mp3")

    olho_aberto_path = caminho_arquivo("olho_aberto.png", subpasta="imagens")
    olho_fechado_path = caminho_arquivo("olho_fechado.png", subpasta="imagens")
    olho_aberto_img = ImageTk.PhotoImage(Image.open(olho_aberto_path).resize((30, 30))) if os.path.exists(olho_aberto_path) else None
    olho_fechado_img = ImageTk.PhotoImage(Image.open(olho_fechado_path).resize((30, 30))) if os.path.exists(olho_fechado_path) else None

    mostrar_checkbox = tk.Checkbutton(frame, variable=mostrar_senha, command=alternar_senha,
                                      image=olho_fechado_img, bg="white")
    mostrar_checkbox.grid(row=2, column=1, sticky="w")

    # 🔐 Autenticação
    def autenticar():
        email = email_entry.get().strip()
        senha = senha_entry.get().strip()
        user = usuarios.get(email)
        if user and user["senha"] == senha:
            parar_musica()
            global usuario_atual
            usuario_atual = email
            mostrar_mascote_expressivo(janela_login, "feliz")
            messagebox.showinfo("Bem-vindo", f"Olá, {user['nome']}!\nPerfil: {user['perfil']}")
            janela_login.destroy()
            ao_logar_callback(user["nome"], user["perfil"])
        else:
            mostrar_mascote_expressivo(janela_login, "negativo")
            messagebox.showerror("Acesso negado", "Email ou senha inválidos.")

    tk.Button(frame, text="Entrar", command=autenticar, bg="#4CAF50", fg="white").grid(row=3, columnspan=2, pady=20)

#🧩 Parte 2 – Cadastro e exclusão de usuários
def cadastro_usuario(janela_principal):
    janela_cadastro = tk.Toplevel(janela_principal)
    janela_cadastro.title("Novo Usuário")
    janela_cadastro.geometry("400x300")

    labels = ["Nome:", "Email:", "Senha:", "Perfil:"]
    entries = {}
    for i, texto in enumerate(labels[:3]):
        tk.Label(janela_cadastro, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(janela_cadastro, show="*" if texto == "Senha:" else "")
        entry.grid(row=i, column=1, padx=10)
        entries[texto] = entry

    perfil_var = tk.StringVar(value="Funcionário")
    tk.Label(janela_cadastro, text="Perfil:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    perfil_menu = tk.OptionMenu(janela_cadastro, perfil_var, "Administrador", "Funcionário")
    perfil_menu.grid(row=3, column=1)

    def salvar():
        nome = entries["Nome:"].get().strip()
        email = entries["Email:"].get().strip()
        senha = entries["Senha:"].get().strip()
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

    tk.Button(janela_cadastro, text="Salvar", command=salvar, bg="#4CAF50", fg="white").grid(row=4, columnspan=2, pady=20)


def excluir_usuario(janela_principal):
    janela_excluir = tk.Toplevel(janela_principal)
    janela_excluir.title("Excluir Usuário")
    janela_excluir.geometry("400x200")

    tk.Label(janela_excluir, text="Email do usuário a excluir:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    email_entry = tk.Entry(janela_excluir)
    email_entry.grid(row=0, column=1)

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

    tk.Button(janela_excluir, text="Excluir", command=excluir, bg="#f44336", fg="white").grid(row=1, columnspan=2, pady=20)

#🧩 Parte 3 – Tela de boas-vindas e acesso ao painel
def abrir_boas_vindas():
    janela_boas_vindas = tk.Toplevel()
    janela_boas_vindas.title("Ipojucão • Bem-vindo!")
    janela_boas_vindas.geometry("500x300")

    frame = tk.Frame(janela_boas_vindas)
    frame.grid(row=0, column=0, padx=30, pady=30)

    tk.Label(frame, text="Menu principal", font=("Segoe UI", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    btn_acessar = tk.Button(
        frame,
        text="📊 Acessar painel de administração",
        bg="#4CAF50",
        fg="white",
        font=("Segoe UI", 12),
        command=lambda: [janela_boas_vindas.destroy(), abrir_janela_principal("Reinaldo", "Administrador")]
    )
    btn_acessar.grid(row=1, column=0, columnspan=2, pady=10)

    btn_sair = tk.Button(
        frame,
        text="❌ Sair do sistema",
        bg="#f44336",
        fg="white",
        font=("Segoe UI", 12),
        command=janela_boas_vindas.destroy
    )
    btn_sair.grid(row=2, column=0, columnspan=2, pady=10)