# # 📦 IMPORTAÇÕES
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import os
# import pygame
#
# from main_backup import inner_frame
# from modulos.audio import tocar_musica, tocar_som_curto, parar_musica
# from modulos.audio import ativar_som, desativar_som
# from utilitarios import caminho_arquivo
# def iniciar_login(janela):
#     from modulos.aba_login import criar_login  # ✅ Importa só na hora
#     criar_login(janela, ao_logar_callback=abrir_janela_principal)
#
# def autenticar():
#     from modulos.aba_login import criar_login
#     from modulos.aba_cadastro import montar_aba_cadastro
#     from modulos.aba_financeiro import montar_aba_financeiro
#     from modulos.aba_relatorios import montar_aba_relatorios
#     from modulos.aba_consulta import montar_aba_consulta
#     from modulos.aba_clientes import montar_aba_clientes
#     from modulos.aba_financeiro import montar_aba_financeiro
#     from modulos.aba_relatorios import montar_aba_relatorios
#
# caminho_intro = caminho_arquivo("bouncy_pet_intro.mp3", subpasta="sons")
# pygame.mixer.music.load(caminho_intro)
#
# logo_splash = caminho_arquivo("splash.png", subpasta=os.path.join("..", "..", "imagensipojucao"))
# som_relatorio = caminho_arquivo("relatorio_finalizado.mp3", subpasta="sons")
#
# #🐾 INICIALIZAÇÃO DO SOM
# pygame.mixer.init()
# pygame.mixer.music.play(-1)
#
# som_global_ativo = True
# usuario_atual = None
#
# def mostrar_splash():
#     splash = tk.Toplevel()
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
# mostrar_splash()
#
# def tocar_som_acesso(resultado, janela_login):
#     som = os.path.join("../Planilha Controle Ipojucão/sons", "acesso_concedido.mp3") if resultado else os.path.join(
#         "../Planilha Controle Ipojucão/sons", "acesso_negado.mp3")
#     if som_global_ativo and os.path.exists(som):
#         tocar_musica("sons/intro.mp3")
#         tocar_som_curto("sons/clique.mp3")
#         #tocar_som(som)
#     try:
#         from mascote import mostrar_mascote_expressivo
#         expressao = "feliz" if resultado else "negativo"
#         mostrar_mascote_expressivo(janela_login, expressao)
#     except:
#         pass  # Se mascote.py não existir, ignora
#
# # 🔐 FUNÇÃO PRINCIPAL DE LOGIN
# def criar_login(janela_principal, ao_logar_callback):
#     janela_login = tk.Toplevel(janela_principal)
#     janela_login.title("Login Ipojucão")
#     janela_login.geometry("800x500")
#     janela_login.resizable(False, False)
#
#     caminho_intro = os.path.join("../Planilha Controle Ipojucão/sons", "bouncy_pet_intro.mp3")
#     if som_global_ativo and os.path.exists(caminho_intro):
#         tocar_musica("sons/intro.mp3")
#         tocar_som_curto("sons/clique.mp3")
#         #tocar_som(caminho_intro)
#
#     caminho_img = os.path.join("imagens", "login_fundo.png")
#     if os.path.exists(caminho_img):
#         img = Image.open(caminho_img).resize((800, 500))
#         bg = ImageTk.PhotoImage(img)
#         fundo = tk.Label(janela_login, image=bg)
#         fundo.image = bg
#         fundo.place(relwidth=1, relheight=1)
#
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
#     # 🔊 Caminho do som de clique (substitua se tiver outro som)
#     som_clique = os.path.join("sons", "search_ping.mp3")
#
#     # 👁️ Controle de exibição da senha + ícones
#     mostrar_senha = tk.BooleanVar(value=False)
#
#     def alternar_senha():
#         senha_entry.config(show="" if mostrar_senha.get() else "*")
#
#         # 🖼️ Alterna ícone do botão
#         novo_icone = olho_aberto_img if mostrar_senha.get() else olho_fechado_img
#         mostrar_checkbox.config(image=novo_icone)
#         mostrar_checkbox.image = novo_icone
#
#         # 🔊 Toca som de clique
#         if som_global_ativo and os.path.exists(som_clique):
#             tocar_som(som_clique)
#
#     # 📷 Ícones do olho
#     olho_aberto_path = os.path.join("imagens", "olho_aberto.png")
#     olho_fechado_path = os.path.join("imagens", "olho_fechado.png")
#
#     if os.path.exists(olho_aberto_path) and os.path.exists(olho_fechado_path):
#         olho_aberto_img = ImageTk.PhotoImage(Image.open(olho_aberto_path).resize((50, 50)))
#         olho_fechado_img = ImageTk.PhotoImage(Image.open(olho_fechado_path).resize((30, 30)))
#     else:
#         olho_aberto_img = None
#         olho_fechado_img = None
#         print("Ícones carregados:", olho_aberto_img, olho_fechado_img)
#
#
# # 👨‍💼 TELA PRINCIPAL COM BOTÕES DINÂMICOS
# def abrir_janela_principal(nome, perfil):
#     janela_principal = tk.Tk()
#     janela_principal.title(f"Ipojucão • Bem-vindo {nome}")
#     janela_principal.geometry("900x600")
#from tkinter import ttk
print("✅ Usando ipojucao_login da pasta MODULOS")
#     notebook = ttk.Notebook(janela_principal)
#     notebook.pack(expand=True, fill='both')
#
#     # Aba 1: Dashboard
#     aba_dashboard = ttk.Frame(notebook)
#     notebook.add(aba_dashboard, text="Início")
#
#     tk.Label(aba_dashboard, text="Painel Inicial", font=("Segoe UI", 14)).pack(pady=20)
#
#     if perfil == "Administrador":
#         tk.Button(janela_principal, text="Novo Usuário", command=lambda: cadastro_usuario(janela_principal)).pack(pady=5)
#         tk.Button(janela_principal, text="Excluir Usuário", command=lambda: excluir_usuario(janela_principal)).pack(pady=5)
#
#     tk.Button(janela_principal, text="Sair", command=lambda: sair(janela_principal), bg="#f44336", fg="white").pack(pady=30)
#
#     # Aba Cadastro
#     aba_cadastro = ttk.Frame(notebook)
#     notebook.add(aba_cadastro, text="Cadastro")
#
#     # Aba Financeiro
#     aba_financeiro = ttk.Frame(notebook)
#     notebook.add(aba_financeiro, text="Financeiro")
#
#     # Aba Relatórios
#     aba_relatorios = ttk.Frame(notebook)
#     notebook.add(aba_relatorios, text="Relatórios")
#
#     montar_aba_cadastro(aba_cadastro, inner_frame)
#     montar_aba_financeiro(aba_financeiro, inner_frame)
#     montar_aba_relatorios(aba_relatorios, inner_frame)
#
#     janela_principal.mainloop()
#
# # 🧍 CADASTRO DE USUÁRIO
# def cadastro_usuario(janela_principal):
#     janela_cadastro = tk.Toplevel(janela_principal)
#     janela_cadastro.title("Novo Usuário")
#     janela_cadastro.geometry("400x300")
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
#         if not nome or not email or not senha:
#             messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
#             return
#         if email in usuarios:
#             messagebox.showerror("Duplicado", "Este email já está cadastrado.")
#             return
#         usuarios[email] = {"nome": nome, "senha": senha, "perfil": perfil}
#         messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
#         janela_cadastro.destroy()
#
#     tk.Button(janela_cadastro, text="Salvar", command=salvar, bg="#4CAF50", fg="white").pack(pady=20)
#
# # ❌ EXCLUSÃO DE USUÁRIO
# def excluir_usuario(janela_principal):
#     janela_excluir = tk.Toplevel(janela_principal)
#     janela_excluir.title("Excluir Usuário")
#     janela_excluir.geometry("400x200")
#
#     tk.Label(janela_excluir, text="Email do usuário a excluir:").pack(pady=10)
#     email_entry = tk.Entry(janela_excluir)
#     email_entry.pack()
#
#     def excluir():
#         email = email_entry.get().strip()
#         if email in usuarios:
#             confirmacao = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir {email}?")
#             if confirmacao:
#                 del usuarios[email]
#                 messagebox.showinfo("Excluído", "Usuário removido com sucesso.")
#                 janela_excluir.destroy()
#         else:
#             messagebox.showerror("Não encontrado", "Usuário não localizado.")
#
#     tk.Button(janela_excluir, text="Excluir", command=excluir, bg="#f44336", fg="white").pack(pady=20)
#
# def sair(janela_principal):
#     janela_principal.destroy()
#     abrir_boas_vindas()  # 👈 Função que recria o menu inicial
#
# #import tkinter as tk
#
# def abrir_boas_vindas():
#     janela_boas_vindas = tk.Toplevel()
#     janela_boas_vindas.title("Ipojucão • Bem-vindo!")
#     janela_boas_vindas.geometry("500x300")
#
#     tk.Label(janela_boas_vindas, text="Menu principal", font=("Segoe UI", 16)).pack(pady=20)
#
#     # Botão para abrir painel principal
#     btn_painel = tk.Button(
#         janela_boas_vindas,
#         text="📊 Acessar painel de administração",
#         bg="#4CAF50",
#         fg="white",
#         font=("Segoe UI", 12),
#         command=lambda: [janela_boas_vindas.destroy(), abrir_janela_principal("Reinaldo", "Administrador")]
#     )
#     btn_painel.pack(pady=10)
#
#     # Botão para encerrar
#     btn_sair = tk.Button(
#         janela_boas_vindas,
#         text="❌ Sair do sistema",
#         bg="#f44336",
#         fg="white",
#         font=("Segoe UI", 12),
#         command=janela_boas_vindas.destroy
#     )
#     btn_sair.pack(pady=10)
#
# def abrir_edicao_usuario():
#     janela_edicao = tk.Toplevel()
#     janela_edicao.title("Editar usuário")
#
#     def ao_fechar():
#         janela_edicao.destroy()
#         abrir_boas_vindas()  # ✅ Chama a janela de boas-vindas
#
#     janela_edicao.protocol("WM_DELETE_WINDOW", ao_fechar)
#
#     # 🚀 EXECUÇÃO DO PROGRAMA
#     janela_inicial = tk.Tk()
#     janela_inicial.withdraw()
#     criar_login(janela_inicial, ao_logar_callback=abrir_janela_principal)
#     janela_inicial.mainloop()