import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import pygame
from tkinter import messagebox

from modulos.aba_login_fusion import criar_login

from modulos.aba_consulta import montar_aba_consulta
from modulos.aba_financeiro import criar_aba_financeiro
from modulos import dados_compartilhados as dc

print("Executando o main.py DENTRO da pasta modulos")

#🎵 Inicialização de sprint("Executando o main.py DENTRO da pasta modulos")om
pygame.init()
pygame.mixer.init()

# 🧩 Importações do projeto
# from modulos.aba_cadastro import montar_aba_cadastro  # ✅ certo

from modulos.audio import som_evento
from utilitarios import caminho_arquivo




def caminho_splash(nome):
    base = os.path.dirname(__file__)  # Agora que o main está na raiz, basta um nível
    return os.path.join(base, "imagensipojucao", "imagens", nome)
# 🖼️ Splash com logo
def mostrar_splash(janela):
    splash = tk.Toplevel(janela)
    splash.overrideredirect(True)
    largura, altura = 1000, 500
    x = (splash.winfo_screenwidth() - largura) // 2
    y = (splash.winfo_screenheight() - altura) // 2
    splash.geometry(f"{largura}x{altura}+{x}+{y}")

    # Obtendo o caminho da imagem através da função
    logo_splash = caminho_splash("logo_ipojucao.png")  # Passando o nome da imagem para a função

    if os.path.exists(logo_splash):
        img = Image.open(logo_splash).resize((largura, altura))
        img_tk = ImageTk.PhotoImage(img)
        label = tk.Label(splash, image=img_tk)
        label.image = img_tk  # Manter uma referência da imagem
        #label.grid(row=0, column=0, sticky="nsew")
        #label.place(x=50, y=50)  # Muda o logo para as coordenadas desejadas
   git     label.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza a imagem
        # splash.grid_rowconfigure(0, weight=1) # Use Só com .grid
        # splash.grid_columnconfigure(0, weight=1)# Use Só com .grid
    else:
        print("Imagem não encontrada:", logo_splash)  # Mensagem de erro
        tk.Label(splash, text="Ipojucão", font=("Segoe UI", 48), fg="green").grid(row=0, column=0)

        logo_splash = "caminho_invalido.png"  # Força o texto "Ipojucão" aparecer
    splash.after(5500, lambda: [splash.destroy(), iniciar_login(janela)])

    splash.after(5500, lambda: tentar_iniciar_login(janela))

    def tentar_iniciar_login(janela):
        try:
            iniciar_login(janela)
        except Exception as e:
            print("Erro ao iniciar login:", e)

def iniciar_sistema():
    janela_inicial = tk.Tk()
    janela_inicial.withdraw()
    abrir_janela_principal("Reinaldo", "Administrador")
    janela_inicial.mainloop()


# 🔐 Callback após login
def abrir_janela_principal(nome, perfil):
    janela = tk.Toplevel()
    janela.title(f"Ipojucão • Bem-vindo {nome}")
    janela.geometry("900x600")

    # ✅ Inicializa variáveis globais com referência à janela
    dc.inicializar_variaveis(janela)

    notebook = ttk.Notebook(janela)
    notebook.grid(padx=10, pady=10)

    # 🧩 Aba 1 – Dados gerais
    aba_geral = tk.Frame(notebook, bg="white")
    notebook.add(aba_geral, text="📋 Dados Gerais")

    tk.Label(aba_geral, text=f"Bem-vindo, {nome}!", font=("Segoe UI", 16), bg="white").grid(pady=20)
    tk.Label(aba_geral, text=f"Perfil: {perfil}", font=("Segoe UI", 14), bg="white").grid()

    # 🧩 Aba 2 – Formulários
    aba_form = tk.Frame(notebook, bg="white")
    notebook.add(aba_form, text="🧪 Formulários")

    tk.Label(aba_form, text="Selecione uma opção:", bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")

    combo = ttk.Combobox(aba_form, values=["Item 1", "Item 2", "Item 3"], state="readonly")
    combo.grid(row=0, column=1, padx=10)

    chk_var = tk.BooleanVar(value=True)
    chk = tk.Checkbutton(aba_form, text="Ativar opção avançada", variable=chk_var, bg="white")
    chk.grid(row=1, column=0, columnspan=2, pady=10)

    btn = tk.Button(aba_form, text="Confirmar", bg="#2196F3", fg="white",
                    command=lambda: messagebox.showinfo("Confirmado", "Tudo funcionando!"))
    btn.grid(row=2, column=0, columnspan=2, pady=20)

    aba_form = tk.Frame(notebook, bg="white")


    # 🧩 Aba 3 – Sobre
    aba_sobre = tk.Frame(notebook, bg="white")
    notebook.add(aba_sobre, text="ℹ️ Sobre")

    tk.Label(aba_sobre, text="Sistema Ipojucão v1.0", font=("Segoe UI", 14), bg="white").grid(pady=20)
    tk.Label(aba_sobre, text="Feito com carinho por Reinaldo 🧠", bg="white").grid()
    # Aqui você pode adicionar suas abas e funcionalidades
    # Exemplo: notebook = ttk.Notebook(janela_principal)



    # 🧮 Aba Financeiro
    aba_financeiro = tk.Frame(notebook, bg="white")
    notebook.add(aba_financeiro, text="🧮 Financeiro")

    tk.Label(aba_financeiro, text="Resumo financeiro:", bg="white", font=("Segoe UI", 12)).grid(pady=10)
    tk.Entry(aba_financeiro, width=30).grid()
    tk.Button(aba_financeiro, text="💾 Salvar", bg="#4CAF50", fg="white").grid(pady=10)

    # 🧑‍💼 Aba Cadastro
    # aba_cadastro = tk.Frame(notebook, bg="white")
    # notebook.add(aba_cadastro, text="👤 Cadastro")
    aba_cadastro_frame = tk.Frame(notebook, bg="white")
    inner_frame = tk.Frame(aba_cadastro_frame, bg="white")
    inner_frame.grid(padx=10, pady=10)





    # tk.Label(aba_cadastro, text="Nome do usuário:", bg="white").grid(row=0, column=0, padx=10, pady=10)
    # tk.Entry(aba_cadastro, width=30).grid(row=0, column=1, padx=10)
    #
    # tk.Label(aba_cadastro, text="Perfil:", bg="white").grid(row=1, column=0, padx=10)
    # perfil_combo = ttk.Combobox(aba_cadastro, values=["Funcionário", "Administrador"])
    # perfil_combo.grid(row=1, column=1, padx=10)
    #
    # tk.Button(aba_cadastro, text="Cadastrar", bg="#4CAF50", fg="white").grid(row=2, column=0, columnspan=2, pady=15)

    from modulos.aba_cadastro import montar_aba_cadastro

    aba_cadastro = ttk.Frame(notebook)
    notebook.add(aba_cadastro, text="Cadastro")

    canvas = tk.Canvas(aba_cadastro)
    scrollbar = ttk.Scrollbar(aba_cadastro, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    inner_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    inner_frame.bind("<Configure>", ajustar_scroll)

    # Chamada da função principal
    montar_aba_cadastro(aba_cadastro, inner_frame)

    # 📑 Aba Relatórios
    aba_relatorios = tk.Frame(notebook, bg="white")
    notebook.add(aba_relatorios, text="📑 Relatórios")

    tk.Label(aba_relatorios, text="Escolha tipo de relatório:", bg="white").grid(pady=10)
    relatorio_combo = ttk.Combobox(aba_relatorios, values=["Relatório Geral", "Relatório por Data", "Relatório Financeiro"])
    relatorio_combo.grid()

    tk.Button(aba_relatorios, text="🕵️ Visualizar", bg="#2196F3", fg="white").grid(pady=15)

    notebook.add(montar_aba_cadastro(), text="🐾 Cadastro")
    notebook.add(montar_aba_consulta(), text="🔍 Consulta")
    notebook.add(criar_aba_financeiro(), text="💰 Financeiro")

#    entry_descricao = ttk.Entry(inner_frame, textvariable=dc.variaveis["var_descricao"])

    janela.mainloop()

#🚀 Início do sistema
def iniciar_login(janela):
    criar_login(janela, ao_logar_callback=abrir_janela_principal)

def iniciar_sistema():
    janela_inicial = tk.Tk()
    janela_inicial.withdraw()
    som_evento(caminho_arquivo("abertura.mp3", subpasta="sons"))
    #som_evento("abertura")
    mostrar_splash(janela_inicial)
    janela_inicial.mainloop()

# 🧭 Ponto de entrada
if __name__ == "__main__":
    print("✅ Executando main.py com aba_login_fusion")
    iniciar_sistema()











































#import tkinter as tk
# from modulos.aba_login_fusion import criar_login
# from modulos.funcoes_auxiliares import som_evento, mostrar_splash, caminho_arquivo
# from tkinter import ttk
#
# def abrir_janela_principal(nome, perfil):
#     print(f"🔓 Logado como {nome} ({perfil})")
#     janela = tk.Toplevel()
#
#     from tkinter import ttk
#     notebook = ttk.Notebook(janela)
#     notebook.pack(fill="both", expand=True)
#


#     aba = tk.Frame(notebook)
#     tk.Label(aba, text=f"Bem-vindo, {nome}! Seu perfil é: {perfil}").pack(padx=20, pady=20)
#     notebook.add(aba, text="Principal")
#
#
# def iniciar_login(janela):
#     criar_login(janela, ao_logar_callback=abrir_janela_principal)
#
#
# def iniciar_sistema():
#     janela_inicial = tk.Tk()
#     janela_inicial.withdraw()
#
#     # janela.deiconify()
#     # janela.lift()
#     # janela.focus_force()
#
#     som_evento(caminho_arquivo("abertura.mp3", subpasta="sons"))
#     mostrar_splash(janela_inicial)
#     iniciar_login(janela_inicial)
#     janela_inicial.mainloop()
#
#
# if __name__ == "__main__":
#     print("✅ Sistema inicializado com aba_login_fusion")
#     iniciar_sistema()
#
#
