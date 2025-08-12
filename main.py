import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import pygame

from modulos.aba_login_fusion import criar_login
from modulos.aba_consulta import montar_aba_consulta
from modulos.aba_financeiro import criar_aba_financeiro
from modulos.aba_cadastro import montar_aba_cadastro
from modulos.audio import som_evento
from modulos import dados_compartilhados as dc
from modulos.utilitarios import caminho_arquivo
from modulos.tela_principal import abrir_janela_principal


from aba_cadastro import logo_splash
from aba_login_fusion import abrir_boas_vindas
from funcoes_auxiliares import mostrar_splash

def centralizar_janela(janela, largura, altura):
    x = (janela.winfo_screenwidth() - largura) // 2
    y = (janela.winfo_screenheight() - altura) // 2
    janela.geometry(f"{largura}x{altura}+{x}+{y}")



def caminho_splash(nome):
    base = os.path.dirname(__file__)  # sobe apenas uma pasta
    return os.path.join(base, "imagensipojucao", "imagens", nome)


# def mostrar_splash(callback):
#     splash = tk.Toplevel()
#     centralizar_janela(splash, 1000, 600)
#     splash.geometry("1000x500")
#     splash.overrideredirect(True)
#
#     # Carregar imagem após criar a janela
#     imagem = Image.open(r"C:\Users\VEIRANO\PycharmProjects\ModuloTkinter\Planilha Controle Ipojucão\imagensipojucao\logo_ipojucao.png")
#     splash.img_tk = ImageTk.PhotoImage(imagem)  # Associar à janela para manter referência
#     label = tk.Label(splash, image=splash.img_tk)
#     label.place(relx=0.5, rely=0.5, anchor="center")
#
#     # Fechar splash após 3 segundos e chamar callback
#     splash.after(9000, lambda: [splash.destroy(), criar_login(janela_principal, ao_logar)])

def mostrar_splash(callback):
    splash = tk.Toplevel()
    centralizar_janela(splash, 1000, 600)
    splash.geometry("1000x500")
    splash.overrideredirect(True)

    imagem = Image.open(caminho_splash("logo_ipojucao.png"))
    splash.img_tk = ImageTk.PhotoImage(imagem)
    label = tk.Label(splash, image=splash.img_tk)
    label.place(relx=0.5, rely=0.5, anchor="center")

    splash.after(6000, lambda: [splash.destroy(), callback()])

# pasta_sons = r"C:\Users\VEIRANO\PycharmProjects\ModuloTkinter\Planilha Controle Ipojucão\sons"
# def caminho_arquivo_sons(nome_arquivo):
#     base = os.path.dirname(__file__)  # pasta do main.py
#     return os.path.join(base, "imagensipojucao", "sons", nome_arquivo)
#
# estado_musica = {"tocando": False}
# # 🎵 Inicialização de som
# pygame.init()
# pygame.mixer.init()
#
# musica = caminho_arquivo_sons("musica_abertura.mp3")
# if os.path.exists(musica):
#     pygame.mixer.music.load(musica)
#     pygame.mixer.music.play(-1)  # -1 para repetir
# else:
#     print("Arquivo de música não encontrado:", musica)
# #musica = caminho_arquivo_sons("musica_abertura.mp3")

# aqui inicio do o código original com abertura de música sem transição para telas

pasta_sons = r"C:\Users\VEIRANO\PycharmProjects\ModuloTkinter\Planilha Controle Ipojucão\sons"

def caminho_arquivo_sons(nome_arquivo):
    base = os.path.dirname(__file__)
    return os.path.join(base, "sons", nome_arquivo)

estado_musica = {"tocando": False}

# Inicialização
pygame.init()
pygame.mixer.init()

musica = caminho_arquivo_sons("musica_abertura.mp3")
if os.path.exists(musica):
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play(-1)
else:
    print("Arquivo de música não encontrado:", musica)

def tocar_musica(nome_arquivo):
    caminho_musica = os.path.join(pasta_sons, nome_arquivo)
    if os.path.exists(caminho_musica):
        pygame.mixer.music.load(caminho_musica)
        pygame.mixer.music.play()
        estado_musica["tocando"] = True
        print(f"Tocando: {nome_arquivo}")
    else:
        print("Arquivo não encontrado:", caminho_musica)

# 🎵 Funções do player
def tocar_musica(nome_arquivo):
    caminho_musica = os.path.join(pasta_sons, nome_arquivo)
    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.play()
    estado_musica["tocando"] = True
    print(f"Tocando: {nome_arquivo}")

def pausar_musica():
    if estado_musica["tocando"]:
        pygame.mixer.music.pause()
        estado_musica["tocando"] = False
        print("Pausar/Retomar")

    else:
        pygame.mixer.music.unpause()
        estado_musica["tocando"] = True
        print("Pausar/Retomar")

def parar_musica():
    pygame.mixer.music.stop()
    estado_musica["tocando"] = False
    print("Parar")

def ajustar_volume(valor):
    volume = float(valor)
    pygame.mixer.music.set_volume(volume)
    print(f"Volume ajustado para: {valor}")

def criar_player_som(pai):
    frame = tk.Frame(pai)

    # 🔘 Botões de músicas
    arquivos = [f for f in os.listdir(pasta_sons) if f.endswith(".mp3")]

    for idx, nome in enumerate(arquivos):
        botao = tk.Button(frame, text=nome, width=30,
                          command=lambda n=nome: tocar_musica(n))
        botao.grid(row=idx, column=0, padx=10, pady=5)

    botao_pausar = tk.Button(frame, text="⏸️ Pausar/Retomar", command=pausar_musica)
    botao_pausar.grid(row=0, column=1, padx=10)

    botao_parar = tk.Button(frame, text="⏹️ Parar", command=parar_musica)
    botao_parar.grid(row=1, column=1, padx=10)

    volume_label = tk.Label(frame, text="🔊 Volume")
    volume_label.grid(row=2, column=1, padx=10)

    volume_slider = tk.Scale(frame, from_=0, to=1, resolution=0.1,
                             orient=tk.HORIZONTAL, command=ajustar_volume)
    volume_slider.set(0.5)
    volume_slider.grid(row=3, column=1, padx=10)

    return frame

# aqui fim do código original com trilha sem transição de telas

janela_principal = tk.Toplevel()
janela_principal.title("Janela Principal")
janela_principal.geometry("600x400")

def ao_logar(nome, perfil):
    abrir_janela_principal(nome, perfil)  # ou abrir_janela_principal(nome, perfil)

player = criar_player_som(janela_principal)
player.grid(row=0, column=0, pady=10, padx=10)

print(caminho_arquivo("teste.txt"))
print("Importação funcionou!")

# Agora você pode usar a função:
musica = caminho_arquivo_sons("musica_abertura.mp3")

def caminho_pasta_sons():
    return os.path.join(os.path.dirname(__file__), "sons")

print("Mascote:", caminho_arquivo("mascote_feliz.png"))
print("Logo:", caminho_arquivo("logo_ipojucao.png"))
print("Som:", caminho_arquivo("musica_abertura.mp3", "sons"))
print(os.path.exists("caminho/para/musica_abertura.mp3"))
caminho_musica = r"C:\Users\VEIRANO\PycharmProjects\ModuloTkinter\Planilha Controle Ipojucão\sons\musica_abertura.mp3"
print(os.path.exists(caminho_musica))

# 🔼 Importações no topo

# 🔧 Inicializações e variáveis globais
pygame.mixer.init()
base_dir = os.path.dirname(os.path.abspath(__file__))
caminho_sons = os.path.join(base_dir, "sons")
estado_musica = {"tocando": False}

caminho_sons = r"C:\Users\VEIRANO\PycharmProjects\ModuloTkinter\Planilha Controle Ipojucão\sons"

# 🔐 Callback após login
def abrir_janela_principal(nome, perfil):
    janela = tk.Toplevel()
    janela.title(f"Ipojucão • Bem-vindo {nome}")
    janela.geometry("900x600")

    dc.inicializar_variaveis(janela)

    notebook = ttk.Notebook(janela)
    notebook.grid(padx=10, pady=10)

    # 📋 Aba Dados Gerais
    aba_geral = tk.Frame(notebook, bg="white")
    notebook.add(aba_geral, text="📋 Dados Gerais")
    tk.Label(aba_geral, text=f"Bem-vindo, {nome}!", font=("Segoe UI", 16), bg="white").grid(pady=20)
    tk.Label(aba_geral, text=f"Perfil: {perfil}", font=("Segoe UI", 14), bg="white").grid()

    # 🧪 Aba Formulários
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

    # ℹ️ Aba Sobre
    aba_sobre = tk.Frame(notebook, bg="white")
    notebook.add(aba_sobre, text="ℹ️ Sobre")
    tk.Label(aba_sobre, text="Sistema Ipojucão v1.0", font=("Segoe UI", 14), bg="white").grid(pady=20)
    tk.Label(aba_sobre, text="Feito com carinho por Reinaldo 🧠", bg="white").grid()

    # 💰 Aba Financeiro
    aba_financeiro = criar_aba_financeiro()
    notebook.add(aba_financeiro, text="💰 Financeiro")

    # 🐾 Aba Cadastro com scroll
    aba_cadastro = ttk.Frame(notebook)
    notebook.add(aba_cadastro, text="🐾 Cadastro")
    canvas = tk.Canvas(aba_cadastro)
    scrollbar = ttk.Scrollbar(aba_cadastro, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.grid(side="left", fill="both", expand=True)
    scrollbar.grid(side="right", fill="y")
    inner_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # Criar o notebook e posicionar
    notebook = ttk.Notebook(janela)
    notebook.grid(row=0, column=0, sticky="nsew")

    # Criar o player e posicionar abaixo
    player = criar_player_som(janela)
    player.grid(row=1, column=0, sticky="ew", pady=5)

    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    inner_frame.bind("<Configure>", ajustar_scroll)
    montar_aba_cadastro(aba_cadastro, inner_frame)

    # 🔍 Aba Consulta
    aba_consulta = montar_aba_consulta()
    notebook.add(aba_consulta, text="🔍 Consulta")

    # 📑 Aba Relatórios
    aba_relatorios = tk.Frame(notebook, bg="white")
    notebook.add(aba_relatorios, text="📑 Relatórios")
    tk.Label(aba_relatorios, text="Escolha tipo de relatório:", bg="white").grid(pady=10)
    relatorio_combo = ttk.Combobox(aba_relatorios, values=["Relatório Geral", "Relatório por Data", "Relatório Financeiro"])
    relatorio_combo.grid()
    tk.Button(aba_relatorios, text="🕵️ Visualizar", bg="#2196F3", fg="white").grid(pady=15)

    janela.mainloop()

def iniciar_login():
    janela_login = tk.Toplevel()
    centralizar_janela(janela_login, 600, 400)
    criar_login(janela_login, ao_logar_callback=abrir_janela_principal)
mostrar_splash(iniciar_login)

def iniciar_sistema():
    #mostrar_splash(iniciar_login)


# 🧭 Ponto de entrada
    if __name__ == "__main__":
        root = tk.Tk()
        root.withdraw()  # ✅ oculta a janela principal

        print("✅ Executando main.py com aba_login_fusion")

        iniciar_sistema()
        root.mainloop()

janela_principal.mainloop()
















