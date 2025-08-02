#from aba_consulta import montar_aba_consulta
#import matplotlib.pyplot as plt
#from models import database, criar_app
from PIL import ImageEnhance
from som import som_evento

# 🎵 Trilha de abertura
som_evento("abertura")

import tkinter as tk
from aba_login import criar_login
from som import som_evento
from mascote import mostrar_mascote_expressivo

janela = tk.Tk()
janela.withdraw()
janela.title("Planilha Ipojucão")
janela.geometry("1000x700")
janela.configure(bg="#ffffff")

som_evento("abertura")

def ao_logar(nome, perfil):
    janela.deiconify()
    print(f"Usuário logado: {nome} - Perfil: {perfil}")

    mostrar_mascote_expressivo(janela, "feliz")
    criar_barra_som(janela)

    tk.Label(janela, text=f"🐾 Bem-vindo, {nome}!", font=("Segoe UI", 20), bg="#ffffff").place(relx=0.5, rely=0.2, anchor="center")

    if perfil == "Administrador":
        btn_gerenciar = tk.Button(janela, text="👤 Gerenciar Usuários", command=lambda: gerenciar_usuarios(janela))
        btn_gerenciar.place(x=20, y=60)

criar_login(janela, ao_logar)
janela.mainloop()

# 👤 Após login
# def ao_logar(nome, perfil):
#     janela.deiconify()
#     print(f"Usuário logado: {nome} - Perfil: {perfil}")  # ✅ Agora está dentro da função
#
#     # Mascote feliz na tela principal
#     mostrar_mascote_expressivo(janela, "feliz")
#
#     # Cria a barra de som global
#     criar_barra_som(janela)
#
#     # Se for administrador, abre gerenciador
#     if perfil == "Administrador":
#         btn_gerenciar = tk.Button(janela, text="👤 Gerenciar Usuários", command=lambda: gerenciar_usuarios(janela))
#         btn_gerenciar.place(x=20, y=60)
#
# # 🔐 Inicia processo de login
# criar_login(janela, ao_logar)
#
# # 🚀 Mantém o programa rodando
# janela.mainloop()


tk.Label(janela, text="Bem-vindo ao sistema Ipojucão!", font=("Segoe UI", 16)).pack(pady=20)

#animar_mascote(janela)

#btn_audio.config(command=lambda: alternar_som(btn_audio))

from barra_som import criar_barra_som

# def ao_logar(nome, perfil):
#     janela.deiconify()
#     criar_barra_som(janela)
#     if perfil == "Administrador":
#         from aba_login import gerenciar_usuarios
#         gerenciar_usuarios(janela)


#pygame.mixer.init()




def ao_logar(nome, perfil):
    global janela
    janela.deiconify()
    criar_barra_som(janela)
    mascote()
    #mascote_piscante()
    gerenciar_usuarios(janela)
    if perfil == "Administrador":
        print(f"Usuário logado: {nome} - Perfil: {perfil}")

        btn_gerenciar = ttk.Button(janela, text="⚙️ Gerenciar Usuários", command=lambda: gerenciar_usuarios(janela))
        btn_gerenciar.pack(pady=10)



from aba_login import gerenciar_usuarios



criar_login(janela, ao_logar)

from som import alternar_som, parar_som

def criar_barra_som(janela):
    trilhas = {
        "Abertura": "sons/musica_abertura.mp3",
        "Consulta PET": "sons/musica_consulta_pet.mp3",
        "Relatórios": "sons/relatorio.mp3",
        "Fechamento": "sons/musica_end_of_day.mp3",
        "Mascote": "sons/bouncy_pet_intro.mp3"
    }

    # 🎛️ Frame flutuante
    barra_som = tk.Frame(janela, bg="#f0f0f0", relief="raised", bd=2)
    barra_som.place(x=500, y=10)

    # 🔈 Botão de ativar/desativar som
    btn_audio = ttk.Button(barra_som, text="🔈 Som Ativado")
    btn_audio.grid(row=0, column=0, padx=5)
    btn_audio.config(command=lambda: alternar_som(btn_audio))

    # 🎶 Combobox de trilhas
    trilha_var = tk.StringVar()
    trilha_combo = ttk.Combobox(barra_som, textvariable=trilha_var, values=list(trilhas.keys()), width=20, state="readonly")
    trilha_combo.grid(row=0, column=1, padx=5)
    trilha_combo.set("Abertura")
    btn_play = ttk.Button(barra_som, text="▶️ Tocar", command=tocar_trilha_selecionada)
    btn_play.grid(row=0, column=2, padx=5)
    btn_parar = ttk.Button(barra_som, text="⏹️ Parar", command=parar_som)
    btn_parar.grid(row=0, column=3, padx=5)

# ▶️ Botão para tocar trilha selecionada
def tocar_trilha_selecionada():
    trilha_nome = trilha_var.get()
    caminho = trilhas.get(trilha_nome)
    if caminho:
        tocar_som(caminho)








janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)


# def mascote_piscante():
#     caminho_mascote = os.path.join("imagens", "mascote.png")
#     if not os.path.exists(caminho_mascote):
#         return

def mascote():
    caminho_mascote = os.path.join("imagens", "mascote.png")
    if not os.path.exists(caminho_mascote):
        return



    img_base = Image.open(caminho_mascote).resize((130, 130))
    enhancer = ImageEnhance.Brightness(img_base)
    img_normal = ImageTk.PhotoImage(img_base)
    img_piscada = ImageTk.PhotoImage(enhancer.enhance(0.6))

    mascote_label = tk.Label(janela, image=img_normal, bg="#fff")
    mascote_label.image = img_normal
    mascote_label.place(x=870, y=540)

    def piscar(on=True):
        mascote_label.config(image=img_piscada if on else img_normal)
        mascote_label.image = img_piscada if on else img_normal
        janela.after(350 if on else 2500, piscar, not on)

    piscar()


mostrar_mascote_expressivo(janela, "bye")
# 🔐 2. Ajustar chamada de login com som
# Adicione esta linha logo após  e antes do :
janela.withdraw()  # Oculta janela até login
criar_login(janela, ao_logar_callback=ao_logar)


# 🎛️ Agora vamos criar sua barra de som flutuante com controle visual!
#Essa barra será adicionada na  ou  e ficará visível sempre que desejar — com ícone animado, botão de ativar/desativar som e seleção de trilha sonora.
# 🧱 Etapa 1: Criar o widget da barra de som
def criar_barra_som(janela):
    from aba_som import alternar_som_estado

    # Frame flutuante
    barra_som = tk.Frame(janela, bg="#f0f0f0", relief="raised", bd=2)
    barra_som.place(x=600, y=10)

    # Ícone animado ou simples
    icone = tk.Label(barra_som, text="🎵", font=("Segoe UI", 18), bg="#f0f0f0")
    icone.grid(row=0, column=0, padx=5)

    # Botão Ativar/Desativar
    btn_audio = ttk.Button(barra_som, text="🔈 Som Ativado")
    btn_audio.grid(row=0, column=1, padx=5)
    btn_audio.config(command=lambda: alternar_som_estado(btn_audio))

from aba_login import criar_login

criar_login(janela, ao_logar_callback=ao_logar)

from aba_som import musica_abertura
musica_abertura()

    # Seleção de trilha
trilhas = {
    "Login": "sons/lightsaber-ignition-6816.mp3",
    "Abertura": "sons/musica_abertura.mp3",
    "Consulta PET": "sons/musica_consulta_pet.mp3",
    "Relatórios": "sons/relatorio.mp3",
    "Fechamento": "sons/musica_end_of_day.mp3"
    }

    # NA LISTA ACIMA, INCLUIR MAIS SONS CONFORME NECESSÁRIO

def tocar_musica_selecionada():
    trilha_escolhida = trilha_selecionada.get()
    caminho = trilhas.get(trilha_escolhida)
    tocar_som(caminho)

    criar_barra_som(janela)

    trilha_var = tk.StringVar()
    trilha_combo = ttk.Combobox(barra_som, textvariable=trilha_var, values=list(trilhas.keys()), width=18, state="readonly")
    trilha_combo.grid(row=0, column=2, padx=5)
    trilha_combo.set("Abertura")

    # Botão reproduzir música
    def tocar_musica_selecionada():
        caminho = trilhas.get(trilha_var.get())
        if caminho:
            tocar_som(caminho)

    btn_play = ttk.Button(barra_som, text="▶️ Tocar", command=tocar_musica_selecionada)
    btn_play.grid(row=0, column=3, padx=5)



from aba_som import tocar_som


def ao_logar(nome, perfil):
    print(f"Usuário logado: {nome} - Perfil: {perfil}")
    # Aqui você pode controlar permissões ou abrir a interface principal
    # Ex: abrir_aba_principal(perfil=perfil)

# 🎯 2. Liberar acesso à tela de gerenciamento somente para administradores
# No seu ao_logar(nome, perfil) do main.py, adicione:

def ao_logar(nome, perfil):
    janela.deiconify()
    if perfil == "Administrador":
        from aba_login import gerenciar_usuarios
        gerenciar_usuarios(janela)
        tocar_som("sons/musica_abertura.mp3")



def mostrar_splash():
    splash = tk.Toplevel()
    splash.overrideredirect(True)  # sem bordas
    largura, altura = 500, 300


    janela.withdraw()  # Esconde janela até login ser feito
    criar_login(janela, ao_logar_callback=ao_logar)
    janela.mainloop()

    # Centraliza a splash na tela
    tela_largura = splash.winfo_screenwidth()
    tela_altura = splash.winfo_screenheight()
    x = (tela_largura - largura) // 2
    y = (tela_altura - altura) // 2
    splash.geometry(f"{largura}x{altura}+{x}+{y}")

    # Carrega o logotipo
    caminho = os.path.join("imagens", "logo_ipojucao.png")
    if os.path.exists(caminho):
        img = Image.open(caminho).resize((largura, altura))
        img_tk = ImageTk.PhotoImage(img)
        label_img = tk.Label(splash, image=img_tk)
        label_img.image = img_tk  # 🔒 mantém na memória
        label_img.pack()

from aba_som import som_abertura
som_abertura()


def tocar_som_acesso(resultado=True):
    from aba_som import tocar_som
    som = os.path.join("sons", "acesso_concedido.mp3") if resultado else os.path.join("sons", "acesso_negado.mp3")
    if os.path.exists(som):
        tocar_som(som)


splash.after(3000, splash.destroy)
splash.mainloop()

mostrar_splash()


import tkinter as tk
from tkinter import ttk

btn_audio = ttk.Button(janela, text="🔈 Som Ativado")
btn_audio.config(command=lambda: alternar_audio(btn_audio))
btn_audio.place(x=880, y=10)  # Ajuste coordenadas conforme layout

# Variável global para controle do som
som_ativo = True

def tocar_som_evento(caminho):
    if som_ativo and os.path.exists(caminho):
        #threading.Thread(target=playsound, args=(caminho,), daemon=True).start() # Somente se usar pacote playsound
        tocar_som(caminho)

def alternar_audio(botao):
    global som_ativo
    som_ativo = not som_ativo
    novo_texto = "🔈 Som Ativado" if som_ativo else "🔇 Som Desativado"
    botao.config(text=novo_texto)


# Combobox para Selecionar Música

trilhas = {
    "consulta": "som/musica_consulta.mp3",
    "salvando": "som/salvando.mp3",
    "abertura": "som/musica_abertura.wav",
    "fechamento": "som/end_of_day.mp3",
    "relatorios": "som/relatorio.mp3",
    "clientes": "clair_de_lune_prelude.mp3"
}

trilha_selecionada = StringVar()
trilha_selecionada.set("Alegria leve")

combo_trilha = ttk.Combobox(janela, textvariable=trilha_selecionada, values=list(trilhas.keys()), width=25, state="readonly")
combo_trilha.place(x=680, y=10)


# E sempre que for tocar música de consulta:
caminho = trilhas.get(trilha_selecionada.get())
tocar_som_evento(caminho)


# Música Fechamento do Programa (Janela)

from aba_som import musica_end_of_day
musica_end_of_day()



def fade_out(passo=0):
    alpha = max(0, 1 - passo / 20)
    cinza = int(68 * alpha)
    cor = f"#{cinza:02x}{cinza:02x}{cinza:02x}"
    despedida.config(fg=cor)
    if passo < 20:
        janela.after(50, fade_out, passo + 1)
    else:
        janela.quit()

    janela.after(1000, fade_out)  # Espera 1s antes de começar a desaparecer


botao_fechar = tk.Button(janela, text='Fechar', command=mostrar_despedida_e_sair, borderwidth=2, relief='solid')
botao_fechar.grid(row=3, column=6, padx=6, pady=10, sticky='nsew', columnspan=4)


from tkinter import ttk
import dados_compartilhados as dc

# 🪟 Criando janela principal
janela = tk.Tk()
janela.title("Planilha Controle Ipojucão")
janela.geometry("1024x700")
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)


# ✅ 1. Mensagem de boas-vindas com fade-in
# Logo após criar a janela e antes de montar as abas, adicione:

def mostrar_mensagem_boas_vindas():
    mensagem = tk.Label(janela, text="🐾 Bem-vindo(a) ao Sistema Ipojucão!", font=("Segoe UI", 16), fg="#4CAF50")
    mensagem.place(relx=0.5, rely=0.1, anchor="center")
    mensagem.attributes = {"alpha": 0}  # controle manual do alpha

    def animar_fade_in(passo=0):
        alpha = passo / 20
        nova_cor = f"#{int(76 * alpha):02x}{int(175 * alpha):02x}{int(80 * alpha):02x}"  # gradiente de verde
        mensagem.config(fg=nova_cor)
        if passo < 20:
            janela.after(40, animar_fade_in, passo + 1)
        else:
            janela.after(2500, mensagem.destroy)

    animar_fade_in()

mostrar_mensagem_boas_vindas()
mascote()
tocar_musica_abertura()


# 📒 Criando o Notebook (abas)
notebook = ttk.Notebook(janela)
notebook.grid(row=0, column=0, sticky="nsew")

# 🧠 Inicializando variáveis globais (exemplo mínimo)
dc.var_porte = tk.StringVar(value="pequeno")
dc.var_raca = tk.StringVar()

# 🔧 Menu Diagnóstico do Sistema
from aba_diagnostico import criar_menu_diagnostico
criar_menu_diagnostico(janela, notebook)

# 🗂 Importando e montando ABAS
from aba_config import montar_aba_config
aba_config = ttk.Frame(notebook)
notebook.add(aba_config, text="⚙️ Configuração")
montar_aba_config(aba_config)

from aba_cadastro import montar_aba_cadastro
aba_cadastro = ttk.Frame(notebook)
notebook.add(aba_cadastro, text="🐶 Cadastro")
montar_aba_cadastro(aba_cadastro)

from aba_consulta import montar_aba_consulta
aba_consulta = ttk.Frame(notebook)
notebook.add(aba_consulta, text="🔍 Consulta")
montar_aba_consulta(aba_consulta)

from aba_financeiro import montar_aba_financeiro
aba_financeiro = ttk.Frame(notebook)
notebook.add(aba_financeiro, text="💰 Financeiro")
montar_aba_financeiro(aba_financeiro)

from aba_relatorio import montar_aba_relatorio
aba_relatorio = ttk.Frame(notebook)
notebook.add(aba_relatorio, text="📊 Relatórios")
montar_aba_relatorio(aba_relatorio)

# 🟢 Iniciando a aplicação


#
def montar_aba_main(aba):
    # Permitir expansão
    aba.grid_rowconfigure(0, weight=1)
    aba.grid_columnconfigure(0, weight=1)

    # Canvas + Scrollbar
    canvas = tk.Canvas(aba)
    scrollbar_y = ttk.Scrollbar(aba, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar_y.set)

    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar_y.grid(row=0, column=1, sticky="ns")

    # Frame rolável
    inner_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    inner_frame.bind("<Configure>", ajustar_scroll)

    # === A partir daqui, crie widgets dentro do inner_frame ===

    # Exemplo básico
    frame_exemplo = ttk.LabelFrame(inner_frame, text="Seção de Exemplo")
    frame_exemplo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    ttk.Label(frame_exemplo, text="Alguma informação importante").grid(row=0, column=0, sticky="w")

    # Repita quantos blocos quiser (outros frames, grids, entradas, etc.)

    # Se quiser ativar algo quando o porte mudar
    dc.var_porte.trace_add("write", lambda *args: atualizar_exemplo())

def atualizar_exemplo():
    porte = dc.var_porte.get()
    print(f"Porte selecionado na aba é: {porte}")



notebook.add(aba_config, text="Configuração")
notebook.add(aba_config, text="Configuração")

# Criando o frame principal para Serviços
frame_servicos = ttk.LabelFrame(inner_frame, text="Serviços")
frame_servicos.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

# Criando o frame principal para informações financeiras

# Criando o frame principal para Relatórios
frame_relatorios = ttk.LabelFrame(inner_frame, text="Informações Financeiras")
frame_relatorios.grid(row=8, column=4, padx=10, pady=10, sticky="nsew")


# ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO
#     AQUI ESTÃO AS VARIÁVES QUE IRÃO SALVAR TODAS AS INFORMAÇÕES INSERIDAS EM TODAS AS GUIAS,
#     PARA CADA INFORMAÇÃO INSERIDA NAS DIVERSAS GUIAS, PRECISA INCLUIR UMA tk.StringVar() PARA SALVAR NO BANCO DE DADOS
#     StringVar PARA SALVAR RADIOBUTTONS, tk.BooleanVar() PARA SALVAR CHECKBUTTONS E DateEntry PARA SALVAR DATAS.
#     ATENÇÃO, NÃO ESQUECER DE INSERIR ESSES COMANDOS PARA CADA NOVA INFORMAÇÃO INCREMENTADA NO CÓDIGO.

# Criando variáveis para entrada de dados

var_nome_pet = tk.StringVar()
var_idade_anos = tk.StringVar()
var_idade_meses = tk.StringVar()
var_descricao = tk.StringVar()  # Para os Radiobuttons
var_tipopelo = tk.StringVar()
var_check_servico1 = tk.BooleanVar() # Para os Checkbutons
var_check_servico2 = tk.BooleanVar()


# **Função única para salvar todos os dados, incluindo as datas**
def salvar_todos_dados():
    # Capturar os valores inseridos
    nome_pet = var_nome_pet.get()
    idade_anos = var_idade_anos.get()
    idade_meses = var_idade_meses.get()
    descricao_pelagem = var_descricao.get()
    servico_banho = var_check_servico1.get()
    servico_tosa = var_check_servico2.get()
    data_selecionada = data_cadastro.get_date().strftime("%Y-%m-%d")  # Formato padrão para banco

    # Conectar ao banco de dados
    conn = sqlite3.connect("petshop.db")
    cursor = conn.cursor()

    # Criar tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cadastro_pet (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade_anos TEXT,
            idade_meses TEXT,
            descricao_pelagem TEXT,
            servico_banho BOOLEAN,
            servico_tosa BOOLEAN,
            data_cadastro DATE
        )
    ''')

    # Inserir dados
    cursor.execute("INSERT INTO cadastro_pet (nome, idade_anos, idade_meses, descricao_pelagem, servico_banho, servico_tosa, data_cadastro) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (nome_pet, idade_anos, idade_meses, descricao_pelagem, servico_banho, servico_tosa, data_selecionada))

    conn.commit()
    conn.close()

    print(f"Todos os dados foram salvos com sucesso! Data: {data_selecionada}")

# Criando botão central para salvar todas as informações
btn_salvar_tudo = ttk.Button(janela, text="Salvar Tudo", command=salvar_todos_dados)
btn_salvar_tudo.grid(row=1, column=0, pady=20)


notebook.add(aba_cadastro, text="Cadastro")


# No início do seu código
var_desconto_fixo = tk.BooleanVar()
var_desconto_percentual = tk.BooleanVar()
var_status_pagamento = tk.StringVar(value="")
var_pagamento = tk.StringVar(value="")
var_condicao_pagamento = tk.StringVar(value="")
var_data_pagamento = tk.StringVar(value="")
var_calendario_cadastro = tk.StringVar(value="")
var_atualizar_pagamento = tk.StringVar(value="")
var_calendario_financeiro = tk.StringVar(value="")
# ... e outras variáveis que você deseja tornar globais.



def criar_frame_consulta(parent):
    frame_consulta = ttk.LabelFrame(parent, text="Informações Sobre o PET")
    frame_consulta.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    frame_consulta = ttk.LabelFrame(frame_consulta, text="Consultando PET")
    frame_consulta.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

notebook.add(aba_config, text="Configuração")


# Função para salvar no banco de dados
def salvar_descricao():
    descricao_selecionada = var_descricao.get()

    if descricao_selecionada:
        conn = sqlite3.connect("petshop.db")  # Conectar ao banco de dados
        cursor = conn.cursor()

        # Criar tabela se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS caracteristicas_pet (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT
            )
        ''')

        # Inserir dados
        cursor.execute("INSERT INTO caracteristicas_pet (descricao) VALUES (?)", (descricao_selecionada,))
        conn.commit()
        conn.close()

        print(f"tipopelo '{descricao_selecionada}' salva no banco de dados!")


# Botão para salvar no banco de dados
# btn_salvar = ttk.Button(frame_descricao, text="Salvar Seleção", command=salvar_descricao)
# btn_salvar.grid(row=6, column=0, pady=10, sticky="w")



# Criando um Frame para Cuidados Necessários
aba_cadastro = ttk.Frame(aba_cadastro)
aba_cadastro.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

frame_cuidados = tk.LabelFrame(aba_cadastro, text="Tipo de Pelo", borderwidth=3, relief="groove")
frame_cuidados.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

# Criando variável para os Radiobuttons
var_cuidados = tk.StringVar(value="") # Inicializa sem nenhuma seleção
#

root = tk.Tk()  # Esta linha deve ser removida se a janela principal já existir
app = App(root)
root.mainloop()  # Esta linha deve estar ao final, chamando o loop principal da janela





import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkcalendar import DateEntry
import sqlite3
import time


# Iniciando a janela

# Criando as abas
aba_principal = ttk.Notebook(janela)



# Criando aba financeira

# Função para criar uma aba com barra de rolagem
# def criar_aba_com_rolagem(parent, aba_nome):
#     # Criando um Frame para a barra de rolagem
#     scrollable_frame = ttk.Frame(parent)
#     scrollable_frame.grid(row=0, column=0, sticky="nsew")

#(aba_config, "Financeiro")


# Criando aba de serviços
aba_servicos = ttk.Frame(notebook)
notebook.add(aba_servicos, text="Serviços")

# Criando aba de relatórios
aba_relatórios = ttk.Frame(notebook)
notebook.add(aba_relatórios, text="Relatórios")

notebook.add(aba_config, text="Configuração")

aba_cadastro = ttk.Frame(notebook)
notebook.add(aba_cadastro, text="Cadastro")
#criar_aba_com_rolagem(aba_cadastro)



from dados_compartilhados import var_porte, var_raca
#aba_config = ttk.Frame(janela)
aba_config = ttk.Frame(aba_principal)
aba_principal.add(aba_config, text="Configuração")


aba_config.grid(padx=10, pady=10)  # Adicionando padding para melhor visualização
janela.geometry("1400x600")  # Ajuste o tamanho da janela conforme necessário
janela.state('zoomed')  # Abre em tela cheia

# Criando um Frame para a barra de rolagem
scrollable_frame = ttk.Frame(janela)
scrollable_frame.grid(row=0, column=0, sticky="nsew")

# Configuração da janela
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

scrollable_frame.grid_rowconfigure(0, weight=1)
scrollable_frame.grid_columnconfigure(0, weight=1)

# Criando o Canvas e as Scrollbars
canvas = tk.Canvas(scrollable_frame)
vertical_scrollbar = ttk.Scrollbar(scrollable_frame, orient="vertical", command=canvas.yview)
horizontal_scrollbar = ttk.Scrollbar(scrollable_frame, orient="horizontal", command=canvas.xview)

# Criando o Frame dentro do Canvas
inner_frame = ttk.Frame(canvas)

# Ajustando a rolagem
inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Criando a janela dentro do Canvas
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Posicionando o Canvas e as Scrollbars
canvas.grid(row=0, column=0, sticky="nsew")
vertical_scrollbar.grid(row=0, column=1, sticky="ns")
horizontal_scrollbar.grid(row=1, column=0, sticky="ew")

# Configurando as barras de rolagem
canvas.configure(yscrollcommand=vertical_scrollbar.set)
canvas.configure(xscrollcommand=horizontal_scrollbar.set)

# Garantindo que a rolagem funcione corretamente
def ajustar_tamanho_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

inner_frame.bind("<Configure>", ajustar_tamanho_canvas)

# Adicione alguns widgets ao inner_frame como exemplo
for i in range(50):
    ttk.Label(inner_frame, text=f"Item {i}").grid(row=i, column=0, sticky="w")
# Configurar a largura da coluna do inner_frame para permitir a rolagem horizontal
inner_frame.grid_columnconfigure(0, minsize=300)  # Ajuste o tamanho conforme necessário

# Definindo o tamanho do Canvas
canvas.config(height=700)  # Aumente a altura do Canvas se necessário
canvas.config(width=800) # Aumente a largura do Canvas se necessário

# Criando as abas (Notebook)
aba_config = ttk.Frame(notebook)
notebook.add(aba_config, text="Configuração")
notebook.grid(row=0, column=0, sticky='nsew')  # Use grid corretamente

# Criando aba de configuração
aba_config = ttk.Frame(notebook)
notebook.add(aba_config, text="Configuração")


base_path = "C:/Users/VEIRANO/PycharmProjects/ModuloTkinter/Planilha Controle Ipojucão/imagensipojucao"

# Dicionário para armazenar imagens dos portes
imagens_portes = {
    "pequeno": "pequeno.jpg",
    "médio": "medio.jpg",
    "grande": "grande.jpg",
    "maior": "maior.jpg"
}

# Dicionário para armazenar imagens das raças
imagens_racas = {
    'Schitzu':'schitzu.jpg','Lhasa Apso':'lhasa_apso.jpg','Maltês':'maltes.jpg','Yorkshire':'yorkshire.jpg','Dachshund':'dachshund.jpg',
    'Cavalier King Charles Spaniel':'cavalier_king_charles_spaniel.jpg','Biewer Terrier':'biewer_terrier.jpg','Bulldog Francês':'bulldog_frances.jpg',
    'Pug':'pug.jpg','Chihuahua':'chihuahua.jpg','Cocker Spaniel':'cocker_spaniel.jpg','Papillon':'papillon.jpg','Spitz Alemao':'spitz_alemao.jpg',
    'Pinscher':'pinscher.jpg','Poodle':'poodle.jpg','Jack Russell Terrier':'jack_russell_terrier.jpg','Galgo Italiano':'galgo_italiano.jpg',
    'Pequinês':'pequines.jpg','Bichon Frise':'bichon_frise.jpg','Boston Terrier':'boston_terrier.jpg','Fox Paulistinha':'fox_paulistinha.jpg',
    'American Pit Bull Terrier':'american_pit_bull_terrier.jpg','Australian Cattle Dog':'australian_cattle.jpg','Australian Shepherd':'australian_shepherd.jpg',
    'Petit Basset Griffon Vendéen':'petit_basset_griffon_vendéen.jpg','Basset Hound':'basset_hound.jpg','Bulldog Campeiro':'bulldog_campeiro.jpg','Bulldog':'bulldog.jpg',
    'Bulldog Inglês':'bulldog_ingles.jpg','Bull Terrier':'bull_terrier.jpg','Basset Fulvo':'basset_fulvo.jpg','Boxer':'boxer.jpg',
    'Clumber Spaniel':'clumber_spaniel.jpg','Cocker Americano':'cocker_americano.jpg','Cocker Inglês':'cocker_ingles.jpg',
    'Flat Coated Retriever':'flat_coated_retriever.jpg','Pastor de Shetland':'pastor_de_shetland.jpg','Pumi':'pumi.jpg',
    'Schnauzer Standard':'schnauzer_standard.jpg','Shar Pei':'shar_pei.jpg','Spaniel Bretão':'spaniel_bretao.jpg','Spaniel Francês':'spaniel_frances.jpg',
    'Spitz Japonês':'spitz_japones.jpg','Springer Spaniel':'springer_spaniel.jpg','Springer Spaniel Inglês':'springer_spaniel_ingles.jpg',
    'Terrier Tibetano':'terrier_tibetano.jpg','American Bully':'american_bully.jpg','SRD Médio':'s_r_d_medio.jpg','Dogo Argentino':'dogo_argentino.jpg',
    'Dálmata':'dalmatian.jpg','Weimaraner':'weimaraner.jpg','Mastim Tibetano':'mastim_tibetano.jpg','Leonberger':'leonberger.jpg',
    'Pastor Australiano':'pastor_australiano.jpg','Setter Irlandês':'setter_irlandes.jpg','Bulmastife':'bulmastife.jpg','Mastim Napolitano':'mastim_napolitano.jpg',
    'Dogue de Bordeaux':'dogue_de_bordeaux.jpg','Cão de Santo Humberto':'cao_de_santo_humberto.jpg','Rhodesian Ridgeback':'rhodesian_ridgeback.jpg',
    'Boiadeiro da Flandres':'boiadeiro_da_flandres.jpg','Bearded Collie':'bearded_collie.jpg','Bichon Bolonhês':'bichon_bolonhes.jpg','Basenji':'basenji.jpg',
    'Boerboel':'boerboel.jpg','Pastor do Cáucaso':'pastor_do_caucaso.jpg','Veadeiro Pampeano':'veadeiro_pampeano.jpg','Buhund Norueguês':'buhund_noruegues.jpg',
    'Basset Artesiano Normando':'basset_artesiano_normando.jpg','Braco de Auvernia':'braco_de_auvernia.jpg','Galgo Inglês':'galgo_ingles.jpg',
    'Pastor Belga':'pastor_belga.jpg','Mastiff':'mastiff.jpg','Bernese':'bernese.jpg','Akita':'akita.jpg','Bloodhound':'bloodhound.jpg','Pit Bull':'pit_bull.jpg',
    'Fila Brasileiro':'fila_brasileiro.jpg','Chow Chow':'chow_chow.jpg','Doberman':'doberman.jpg','Chip Dog':'chip_dog.jpg',
}


# ADICIONANDO CARACTERÍSTICAS DO PET
# Dicionário de características das raças
caracteristicas_racas = {
    "Chihuahua": {
        "peso": "1 a 3 kg",
        "tamanho": "15 a 23 cm",
        "pelos": "Curto",
        "temperamento": "Dócil",
        "imagem": "chihuahua.png"  # Adicione o caminho para a imagem
    },
    "Labrador": {
        "peso": "25 a 36 kg",
        "tamanho": "55 a 62 cm",
        "pelos": "Curto e grosso",
        "temperamento": "Dócil",
        "imagem": "labrador.png"
    },
    "Bulldog": {
        "peso": "18 a 25 kg",
        "tamanho": "30 a 40 cm",
        "pelos": "Curto",
        "temperamento": "Agressivo",
        "imagem": "bulldog.png"
    }
    # Adicione mais raças conforme necessário
}

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro PET SHOP")

        # Criação do Notebook para as abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=0, column=0, sticky='nsew')  # Usando grid para o Notebook

        # Criação da aba_config
        self.aba_config = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_config, text='Configuração')

        # Combobox de Raça
        self.combobox_raca = ttk.Combobox(self.aba_config, values=list(caracteristicas_racas.keys()))
        self.combobox_raca.grid(row=0, column=0, padx=10, pady=10)
        self.combobox_raca.bind("<<ComboboxSelected>>", self.atualizar_caracteristicas)

        # Campo de texto para características
        self.texto_caracteristicas = tk.Text(self.aba_config, height=10, width=50)
        self.texto_caracteristicas.grid(row=1, column=0, padx=10, pady=10)  # Mudado para row=1, column=0

        # Configuração de expansão
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def atualizar_caracteristicas(self, event):
        raca_selecionada = self.combobox_raca.get()
        if raca_selecionada in caracteristicas_racas:
            info = caracteristicas_racas[raca_selecionada]
            self.texto_caracteristicas.delete(1.0, tk.END)  # Limpa o campo de texto
            self.texto_caracteristicas.insert(tk.END, f"Peso: {info['peso']}\n")
            self.texto_caracteristicas.insert(tk.END, f"Tamanho: {info['tamanho']}\n")
            self.texto_caracteristicas.insert(tk.END, f"Pelos: {info['pelos']}\n")
            self.texto_caracteristicas.insert(tk.END, f"Temperamento: {info['temperamento']}")



# ADICIONANDO CARACTERÍSTICAS DO PET




# ""()
# var_raca = tk.StringVar()


# Funções para atualizar imagens
def update_porte_image(event=None):
    porte = var_porte.get().strip()
    image_path = os.path.join(base_path, imagens_portes.get(porte, ''))
    if os.path.exists(image_path):
        img = Image.open(image_path).resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        label_imagem.config(image=img_tk)
        label_imagem.image = img_tk
    else:
        label_imagem.config(text="Imagem do porte não encontrada", image="")
        label_imagem.image = None


# Função para atualizar a lista de raças
def atualizar_lista_racas(event=None):
    #porte = var_porte.get().strip()
    # Modificado em 24/06/2025 para compartilhar com a aba_financeiro
    #racas = list(dados_pet.get(porte, {}).get("raças", []))
    porte = var_porte.get().strip()
    racas = dados_pet.get(porte, {}).get("raças", [])
    combobox_raca["values"] = racas
    combobox_raca.set("Selecione uma raça")
    # Modificado em 24/06/2025 para compartilhar com a aba_financeiro
    print(f"Selecionado Porte: {porte}")  # Debug
    time.sleep(0.5)  # Pausa para garantir atualização

    # Modificado em 24/06/2025 para compartilhar com a aba_financeiro
    # Atualiza os valores na aba financeira
    atualizar_valores()
    # Modificado em 24/06/2025 para compartilhar com a aba_financeiro


    #racas = dados_pet.get(porte, {}).get("raças", [])
    racas = list(dados_pet.get(porte, {}).get("raças", [])) # Capitalize para correspondência
    combobox_raca["values"] = racas
    combobox_raca.set("Selecione uma raça")
    update_porte_image(event)

    if racas:
        combobox_raca.set(racas[0])  # Define a primeira raça como padrão
        update_raca_image()  # Atualiza a imagem da raça assim que uma raça é definida
    else:
        combobox_raca.set("Nenhuma raça disponível")

# Função para atualizar a imagem da raça
def update_raca_image(event=None):
    #raca = combobox_raca.get().strip()
    raca = var_raca.get().strip()
    # Modificado em 24/06/2025 para compartilhar com a aba_financeiro
    # Atualiza os valores na aba financeira
    atualizar_valores()
    # Modificado em 24/06/2025 para compartilhar com a aba_financeiro

    image_path = os.path.join(base_path, imagens_racas.get(raca, ''))
    print(f"Selecionado Raça: {raca}")  # Debug
    print(f"Imagem do porte em: {image_path}")  # Debug
    time.sleep(0.9)  # Pausa para garantir que a variável foi atualizada

    # Verifique se o nome do arquivo não está vazio
    if not imagens_racas.get(raca):
        print(f"Nome do arquivo não encontrado para a raça: {raca}")  # Debug
        time.sleep(0.9)  # Pausa para garantir que a variável foi atualizada
        label_imagem.config(text="Imagem da raça não encontrada", image="")
        time.sleep(0.5)  # Pausa para garantir que a variável foi atualizada
        label_imagem.image = None
        return

    print(f"Imagem do porte em: {image_path}")  # Debug

    if os.path.exists(image_path):
        img = Image.open(image_path).resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        label_imagem.config(image=img_tk)
        label_imagem.image = img_tk
    else:
        label_imagem.config(text="Imagem da raça não encontrada", image="")
        label_imagem.image = None
        #     except Exception as e:
        #     print(f"Erro ao carregar imagem da raça: {e}")
        # else:
        label_imagem.config(text="Imagem não encontrada", image="")
        label_imagem.image = None

# Dados centralizados (raças e preços)
dados_pet = {
    "pequeno": {
        "raças": ['Schitzu', 'Lhasa Apso', 'Maltes', 'Yorkshire', 'Dachshund', 'Cavalier King Charles Spaniel',
                  'Biewer Terrier', 'Bulldog Francês', 'Pug', 'Chihuahua', 'Cocker Spaniel', 'Papillon',
                  'Spitz Alemao', 'Pinscher', 'Poodle', 'Jack Russell Terrier', 'Galgo Italiano', 'Pequinês',
                  'Bichon Frise', 'Boston Terrier', 'Fox Paulistinha', 'Petit Basset Griffon Vendéen'],
        "preços": {"Banho": 55, "Hidratação": 20, "Desembolo": 20, "Remoção de Pelos": 20, "Corte de Unhas": 15,
                   "Escovação de Dentes": 15, "Tosa Higiênica": 20, "Tosa na Máquina": 115,
                   "Tosa na Tesoura": 125, "Leva e Trás": 10},
    },
    "médio": {
        "raças": ['American Bully', 'Australian Cattle Dog', 'Basset Hound',
                  'Bulldog Campeiro', 'Bulldog', 'Bulldog Ingles', 'Bull Terrier', 'Basset Fulvo',
                  'Boxer', 'Clumber Spaniel', 'Cocker Americano', 'Cocker Ingles', 'Flat Coated Retriever',
                  'Pastor de Shetland', 'Pumi', 'Schnauzer Standard', 'Shar Pei', 'Spaniel Bretao', 'Spaniel Frances',
                  'Spitz Japones', 'Spriger Spaniel Ingles', 'Terrier Tibetano', 'S.R.D. Médio'],
        "preços": {"Banho": 65, "Hidratação": 20, "Desembolo": 20, "Remoção de Pelos": 20, "Corte de Unhas": 15,
                   "Escovação de Dentes": 15, "Tosa Higiênica": 20, "Tosa na Máquina": 115,
              "Tosa na Tesoura": 125, "Leva e Trás": 10},
    },
    "grande": {
        "raças": ['Pastor Alemao', 'Dogue Alemao', 'Terra Nova', 'Rottweiler', 'Sao-Bernardo', 'Labrador Retriever',
                  'Golden Retriever', 'Fila brasileiro', 'Cane corso', 'Border collie', 'Boiadeiro de Berna',
                  'Akita Inu', 'Mastim Ingles', 'Husky Siberiano', 'Dogo argentino', 'Dalmata', 'Weimaraner',
                  'Bull terrier', 'Mastim tibetano', 'Leonberger', 'Pastor australiano', 'Setter irlandes',
                  'Bulmastife', 'Mastim napolitano', 'Dogue de bordeus', 'Bulmastife', 'cao de Santo Humberto',
                  'Rhodesian ridgeback', 'Boiadeiro da Flandres', 'Bearded collie', 'Bichon bolonhes', 'Basenji',
                  'Boerboel', 'Pastor do caucaso', 'Veadeiro Pampeano', 'Buhund noruegues',
                  'Basset artesiano normando', 'Braco de Auvernia', 'Galgo Ingles', 'Pastor Belga', 'Mastiff',
                  'Bernese', 'Akita', 'Bloodhound', 'Australian Shepherd'],
        "preços": {"Banho": 70, "Hidratação": 20, "Desembolo": 20, "Remoção de Pelos": 20, "Corte de Unhas": 15,
                   "Escovação de Dentes": 15, "Tosa Higiênica": 20, "Tosa na Máquina": 115,
                "Tosa na Tesoura": 125, "Leva e Trás": 10},
    },
    "maior": {
        "raças": ['American Pit Bull Terrier', 'Fila Brasileiro', 'Chow Chow', 'Doberman', 'Chip-dog', 'American Pit Bul terrier',
                  'Chow-chow'],
        "preços": {"Banho": 120, "Hidratação": 20, "Desembolo": 20, "Remoção de Pelos": 80, "Corte de Unhas": 50,
               "Escovação de Dentes": 55, "Tosa Higiênica": 75, "Tosa na Máquina": 85,
               "Tosa na Tesoura": 100, "Leva e Trás": 10},
    },
}

# Criando Combobox para seleção de porte
ttk.Label(aba_config, text="Selecione o Porte:").grid(row=0, column=0, padx=10, pady=5)
combobox_porte = ttk.Combobox(aba_config, textvariable=var_porte, values=list(dados_pet.keys()), state="readonly")
combobox_porte.grid(row=1, column=0, padx=10, pady=5)
combobox_porte.bind("<<ComboboxSelected>>", lambda event: [atualizar_lista_racas(event), update_porte_image(event)])



# Criando Combobox para seleção de raça
ttk.Label(aba_config, text="Selecione a Raça:").grid(row=0, column=1, padx=10, pady=5, sticky="w")
combobox_raca = ttk.Combobox(aba_config, textvariable=var_raca, state="readonly")
combobox_raca.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
combobox_raca.bind("<<ComboboxSelected>>", update_raca_image)


# Configurando a coluna para expandir
aba_config.grid_columnconfigure(0, weight=1)

combobox_raca.bind("<<ComboboxSelected>>", update_raca_image)



# Criando Label para exibir imagens
label_imagem = tk.Label(aba_config, text="Nenhuma imagem disponível", width=180, height=180)
label_imagem.grid(row=2, column=0, columnspan=4, padx=10, pady=10)


# Adicionando `trace_add` para ativar automaticamente a atualização da imagem e das raças
var_porte.trace_add("write", lambda *args: atualizar_lista_racas(event=None))
var_porte.trace_add("write", lambda *args: update_porte_image(event=None))


# Criando o frame principal para dados cadastrais
frame_cadastro = ttk.LabelFrame(inner_frame, text="Dados Cadastrais")
frame_cadastro.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")


# Criando o frame principal para Serviços
frame_servicos = ttk.LabelFrame(inner_frame, text="Serviços")
frame_servicos.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")


# Criando o frame principal para informações financeiras

# Criando o frame principal para Relatórios
frame_relatorios = ttk.LabelFrame(inner_frame, text="Informações Financeiras")
frame_relatorios.grid(row=8, column=4, padx=10, pady=10, sticky="nsew")


# ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO ATENÇÃO
#     AQUI ESTÃO AS VARIÁVES QUE IRÃO SALVAR TODAS AS INFORMAÇÕES INSERIDAS EM TODAS AS GUIAS,
#     PARA CADA INFORMAÇÃO INSERIDA NAS DIVERSAS GUIAS, PRECISA INCLUIR UMA tk.StringVar() PARA SALVAR NO BANCO DE DADOS
#     StringVar PARA SALVAR RADIOBUTTONS, tk.BooleanVar() PARA SALVAR CHECKBUTTONS E DateEntry PARA SALVAR DATAS.
#     ATENÇÃO, NÃO ESQUECER DE INSERIR ESSES COMANDOS PARA CADA NOVA INFORMAÇÃO INCREMENTADA NO CÓDIGO.

# Criando variáveis para entrada de dados

var_nome_pet = tk.StringVar()
var_idade_anos = tk.StringVar()
var_idade_meses = tk.StringVar()
var_descricao = tk.StringVar()  # Para os Radiobuttons
var_tipopelo = tk.StringVar()
var_check_servico1 = tk.BooleanVar() # Para os Checkbutons
var_check_servico2 = tk.BooleanVar()


# **Função única para salvar todos os dados, incluindo as datas**
def salvar_todos_dados():
    # Capturar os valores inseridos
    nome_pet = var_nome_pet.get()
    idade_anos = var_idade_anos.get()
    idade_meses = var_idade_meses.get()
    descricao_pelagem = var_descricao.get()
    servico_banho = var_check_servico1.get()
    servico_tosa = var_check_servico2.get()
    data_selecionada = data_cadastro.get_date().strftime("%Y-%m-%d")  # Formato padrão para banco

    # Conectar ao banco de dados
    conn = sqlite3.connect("petshop.db")
    cursor = conn.cursor()

    # Criar tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cadastro_pet (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade_anos TEXT,
            idade_meses TEXT,
            descricao_pelagem TEXT,
            servico_banho BOOLEAN,
            servico_tosa BOOLEAN,
            data_cadastro DATE
        )
    ''')

    # Inserir dados
    cursor.execute("INSERT INTO cadastro_pet (nome, idade_anos, idade_meses, descricao_pelagem, servico_banho, servico_tosa, data_cadastro) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (nome_pet, idade_anos, idade_meses, descricao_pelagem, servico_banho, servico_tosa, data_selecionada))

    conn.commit()
    conn.close()

    print(f"Todos os dados foram salvos com sucesso! Data: {data_selecionada}")

# Criando botão central para salvar todas as informações
btn_salvar_tudo = ttk.Button(janela, text="Salvar Tudo", command=salvar_todos_dados)
btn_salvar_tudo.grid(row=1, column=0, pady=20)


notebook.add(aba_cadastro, text="Cadastro")


# No início do seu código
var_desconto_fixo = tk.BooleanVar()
var_desconto_percentual = tk.BooleanVar()
var_status_pagamento = tk.StringVar(value="")
var_pagamento = tk.StringVar(value="")
var_condicao_pagamento = tk.StringVar(value="")
var_data_pagamento = tk.StringVar(value="")
var_calendario_cadastro = tk.StringVar(value="")
var_atualizar_pagamento = tk.StringVar(value="")
var_calendario_financeiro = tk.StringVar(value="")
# ... e outras variáveis que você deseja tornar globais.



# Função para ativar/desativar métodos de pagamento
def atualizar_pagamento():
    global var_pagamento  # Declare a variável como global
    if var_status_pagamento.get() == "pago":
        # Ativar botões de pagamento
        radiobutton_pix.config(state="normal")
        radiobutton_debito.config(state="normal")
        radiobutton_credito.config(state="normal")
        radiobutton_dinheiro.config(state="normal")
    else:
        # Resetar e desabilitar botões de pagamento
        var_pagamento.set("")
        radiobutton_pix.config(state="disabled")
        radiobutton_debito.config(state="disabled")
        radiobutton_credito.config(state="disabled")
        radiobutton_dinheiro.config(state="disabled")



# Frame para seleção de porte e raça
frame_cabecalho = ttk.LabelFrame(inner_frame, text="Seleção de Porte e Raça")
frame_cabecalho.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

# 🚀🚀🚀🚀🚀 COMBOBOX_PORTE ANTERIOR A CRIAÇÃO DE ABAS



# Criando um Frame para serviços
frame_disponiveis = ttk.LabelFrame(frame_servicos, text="Serviços Disponíveis")
frame_disponiveis.grid(row=10, column=1, padx=10, pady=5, sticky="nw")

scrollable_frame.rowconfigure(1, weight=1)  # Para o row 1 (serviços)

# Frame para Data do Serviço
frame_calendario_servico = ttk.LabelFrame(frame_servicos, text="Data do Serviço")
frame_calendario_servico.grid(row=11, column=0, padx=10, pady=10, sticky="w")
calendario_servico = DateEntry(frame_servicos, year=2025, locale='pt_br')
calendario_servico.grid(row=12, column=0 , padx=10, pady=10, sticky='nsew')


# Criando Checkbuttons para serviços
variaveis_servicos = {}
servicos_disponiveis = ["Banho", "Hidratação", "Desembolo", "Remoção de Pelos", "Corte de Unhas",
                        "Escovação de Dentes", "Tosa Higiênica", "Tosa na Máquina", "Tosa na Tesoura", "Leva e Trás"]

for i, servico in enumerate(servicos_disponiveis):
    variaveis_servicos[servico] = tk.BooleanVar()
    check_servico = ttk.Checkbutton(frame_servicos, text=servico, variable=variaveis_servicos[servico],)
    check_servico.grid(row=i, column=0, sticky="w")


scrollable_frame.rowconfigure(2, weight=1)  # Para o row 2 (abatimentos)



#Calendário Cadastrar Item
def cadastrar_item():
    data = calendario_cadastro.get_date()
    print(f"Data cadastrada  {data}")  # Substitua por lógica de salvar o item
    label_resultado.config(text=f"Data cadastrada  {data}")

# Configuração para expandir corretamente
#aba_cadastro.columnconfigure(0, weight=1)

# Frame para Data do Cadastro
frame_calendario_cadastro = ttk.LabelFrame(aba_cadastro, text="Calendario Cadastro")
frame_calendario_cadastro.grid(row=0, column=0, padx=10, pady=10, sticky="w")
calendario_cadastro = DateEntry(frame_calendario_cadastro, year=2025, locale='pt_br')
calendario_cadastro.grid(row=0, column=0 , padx=10, pady=10, sticky='nsew')

# Criando um Frame para Dados Cadastrais
# frame_cadastramento = ttk.LabelFrame(aba_cadastro, text="Dados dos Cadastrais")
# frame_cadastramento.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

def criar_frame_cadastro(parent, text="Dados Cadastrais"):
    frame_cadastro = ttk.LabelFrame(parent, )
    frame_cadastro.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    frame_cadastro = ttk.Label(aba_cadastro, "Dados Cadastrais").grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    # nome Pet
    ttk.Label(aba_cadastro, text="Nome do Pet", anchor='w').grid(row=1, column=0, padx=10, pady=5, sticky='ew')
    entry_nome = tk.Entry(frame_cadastramento)
    entry_nome.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    # idade
    ttk.Label(aba_cadastro, text="Idade Anos").grid(row=2, column=0, padx=10, pady=10, sticky='w')
    entry_idadedopetanos = ttk.Entry(aba_cadastro)
    entry_idadedopetanos.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

    ttk.Label(aba_cadastro, text="Meses").grid(row=3, column=0, padx=10, pady=5, sticky='w')
    entry_idadedopetmeses = ttk.Entry(aba_cadastro)
    entry_idadedopetmeses.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

    # Tutor 1
    ttk.LabelFrame(aba_cadastro, text="Tutor 1").grid(row=4, column=0, padx=10, pady=10, sticky='w')
    entry_tutor_1 = tk.Entry(aba_cadastro)
    entry_tutor_1.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

    # telefone1
    ttk.Label(aba_cadastro, text="Telefone Tutor 1", anchor='e').grid(row=5, column=0, padx=10, pady=5, sticky='w')
    entry_telefone_1 = tk.Entry(aba_cadastro)
    entry_telefone_1.grid(row=1, column=1, padx=10, pady=5, sticky='ew')
    # email Tutor1
    ttk.Label(aba_cadastro, text="email Tutor 1", anchor='e').grid(row=2, column=0, padx=10, pady=10, sticky='w')
    entry_email_tutor_1 = tk.Entry(aba_cadastro)
    entry_email_tutor_1.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

    #tutor 2
    # ttk.Label(aba_cadastro, text="Tutor 2", anchor='e').grid(row=3, column=0, padx=10, pady=5, sticky='ew')
    # # Campo de entrada (Entry)
    # entry_tutor_2 = tk.Entry(aba_cadastro)
    # entry_tutor_2.grid(row=7, column=1, padx=10, pady=10, sticky='ew')

    # Tutor 2
    frame_tutor2 = ttk.LabelFrame(aba_cadastro, text="Tutor 2")
    frame_tutor2.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    ttk.Label(frame_tutor2, text="Nome do Tutor").grid(row=0, column=0, padx=10, pady=5, sticky='w')
    entry_tutor_2 = tk.Entry(frame_tutor2)
    entry_tutor_2.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

    #telefone 2
    ttk.Label(frame_tutor2, text="Telefone Tutor 2", anchor='e').grid(row=1, column=1, padx=10, pady=5, sticky='ew')
    # Campo de entrada (Entry)
    entry_telefone_2 = tk.Entry(aba_cadastro)
    entry_telefone_2.grid(row=1, column=0, padx=10, pady=5, sticky='ew')
    frame_telefone_2a = ttk.LabelFrame(aba_cadastro, text="Telefone_a", borderwidth=1, relief='solid')
    entry_telefone_2a = tk.Entry(aba_cadastro)
    entry_telefone_2a.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

    #email Tutor2
    frame_email_tutor_2 = ttk.LabelFrame(aba_cadastro, text="email Tutor 2", anchor='w')
    frame_email_tutor_2.grid(row=2, column=0, padx=10, pady=5, sticky='ew')
    entry_email_tutor_2 = tk.Entry(aba_cadastro)
    entry_email_tutor_2.grid(row=10, column=0, padx=10, pady=10, sticky='nsew')

    # Criando um Frame para Endereço e Observações
    ttk.Label(aba_cadastro, text="Endereço e Observações").grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")
    #logradouro.config(height=170)  # Define a altura manualmente

    #frame_logradouro.grid_propagate(False)  # Impede que os widgets internos alterem o tamanho do frame


    #Endereço Logradouro
    ttk.Label(aba_cadastro, text="Endereço").grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
    # Campo de entrada (Entry)
    entry_enderecopet = tk.Entry(aba_cadastro)
    entry_enderecopet.grid(row=2, column=1, padx=10, pady=10, sticky='nsew', columnspan=2)
    #entry_nome.grid(row=1, column=0, columnspan=4, pady=1, sticky='nsew')

    #endereço Número
    frame_endereconumero = ttk.Label(aba_cadastro, text="Número", anchor='e')
    frame_endereconumero.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')
    # Campo de entrada (Entry)
    entry_endereconumero = tk.Entry(aba_cadastro)
    entry_endereconumero.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

    #Endereço Complemento
    frame_enderecocomplemento = ttk.Label(aba_cadastro, text="Complemento", anchor='e')
    frame_enderecocomplemento.grid(row=4, column=1, padx=10, pady=10, sticky='nsew')
    # Campo de entrada (Entry)
    entry_enderecocomplemento = tk.Entry(aba_cadastro)
    entry_enderecocomplemento.grid(row=4, column=2, padx=10, pady=10, sticky='nsew')



    # frame_recomendacoes = ttk.Label(aba_cadastro, text="Recomendações", borderwidth=1, relief='solid')
    # frame_recomendacoes.grid(row=20, column=0, columnspan=2, padx=10, pady=5, sticky="w")
    #
    # # Observações sobre o PET
    # frame_recomendacoes = ttk.Label(aba_cadastro, text="Recomendações Sobre o pet", borderwidth=1, relief='solid' )
    # frame_recomendacoes.grid(row=21, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
    # Campo de entrada (Entry)
    campo_observacoes = tk.Text(aba_cadastro, width=80, height=12, borderwidth=2, relief='solid' )
    campo_observacoes.grid(row=30, column=0, columnspan=2, padx=10, pady=10)

    # Configuração para expandir corretamente
    janela.columnconfigure(0, weight=1)
    janela.rowconfigure(0, weight=1)
    aba_cadastro.columnconfigure(1, weight=1)
#=

# entry_recomendacoes = tk.Entry(frame_recomendacoes)
# entry_recomendacoes.grid(row=0, column=3, padx=10, pady=10, sticky='nsew', columnspan=3)

# #Criando um Frame para Endereço e Observações
# frame_recomendacoes = ttk.LabelFrame(inner_frame, text="Recomendações Sobre o PET")
# frame_cadastro.grid(row=2, column=5, columnspan=6, padx=10, pady=5, sticky="nsew")
# label_relatorio = tk.Label(frame_relatorio, text="Recomendações", borderwidth=1, relief='solid' )
# #Campo para exibir o relatório
# campo_observacoes = tk.Text(frame_cadastro, width=50, height=10, borderwidth=2, relief='solid' )
# campo_observacoes.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

#RELATÓRIOS:

# Definindo variáveis globais
combobox_item = None
combobox_item1 = None
combobox_item2 = None
calendario_inicial = None
calendario_final = None


item= {
    "Relatórios": {
        "Serviços": ['Banho', 'Hidratação', 'Desembolo', 'Remoção Pelos', 'Corte Unhas', 'Escovação Dentes', 'Tosa Higiênica', 'Tosa Máquina', 'Tosa Tesoura', 'Leva Trás']}}
                  #

item1= {
    "Relatórios": {
        "Cadastro": ['Cadastrado Desde', 'Nome Pet', 'Idade', 'Tutor 1', 'Tutor 2', 'Telefone Tutor 1', 'email Tutor 1',
                  'Telefone Tutor 2', 'email Tutor 2', 'Endereço', 'Número', 'Complemento', 'Recomendações']}}

item2= {
    "Relatórios": {
        "Pagamentos": ['Condições Pagamento', 'Abatimentos', 'Status Pagamento', 'Data Pagamento', 'Forma Pagamento']}}






# Frame para combobox item
frame_data_pagamento = ttk.LabelFrame(inner_frame, text="Data do Pagamento")
frame_data_pagamento.grid(row=9, column=1, padx=10, pady=10, sticky="w")

#combobox_item = ttk.LabelFrame(inner_frame, text="Item para Relatório")
combobox_item = ttk.Combobox(frame_relatorios, values=item["Relatórios"]["Serviços"])
combobox_item.grid(row=10, column=1, padx=10, pady=10, sticky="nsew")
combobox_item.bind("<<ComboboxSelected>>", lambda event: [atualizar_item(event)])  # Atualiza raças e imagem ao selecionar porte])  # Atualiza raças e imagem ao selecionar porte


#combobox_item1 = ttk.LabelFrame(inner_frame, text="Item para Relatório")
combobox_item1 = ttk.Combobox(frame_relatorios, values=item1["Relatórios"]["Cadastro"])
combobox_item1.grid(row=11, column=2, padx=10, pady=10, sticky="nsew")
combobox_item1.bind("<<ComboboxSelected>>", lambda event: [atualizar_item1(event),])  # Atualiza raças e imagem ao selecionar porte])  # Atualiza raças e imagem ao selecionar porte


#combobox_item = ttk.LabelFrame(inner_frame, text="Item para Relatório")
combobox_item2 = ttk.Combobox(frame_relatorios, values=item2["Relatórios"]["Pagamentos"])
combobox_item2.grid(row=12, column=3, padx=10, pady=10, sticky="nsew")
combobox_item2.bind("<<ComboboxSelected>>", lambda event: [atualizar_item2(event)])  # Atualiza raças e imagem ao selecionar porte])  # Atualiza raças e imagem ao selecionar porte
# combobox_porte = ttk.Combobox(inner_frame, values=list(dados_pet.keys()))
# combobox_porte.grid(row=0, column=0, padx=10, pady=5)
#combobox_porte.bind("<<ComboboxSelected>>", atualizar_lista_racas)  # Atualiza raças ao selecionar porte


#scrollable_frame.rowconfigure(0, weight=1)  # Para o row 0 (combobox)


# combobox_item = ttk.LabelFrame(inner_frame, text="Calendario Cadastro")
# combobox_item = ttk.Combobox(inner_frame, values=list(dados_pet.keys()))
# combobox_item.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")
# scrollable_frame.rowconfigure(0, weight=1)  # Para o row 0 (combobox)



# Função única para gerar relatórios
def gerar_relatorio(event=None):
    global calendario_inicial, calendario_final


    # Captura das datas e do item selecionado
    date_inicial = calendario_inicial.get_date()
    data_final = calendario_final.get_date()
    item_selecionado = None # Definido à seguir

    # Verifica qual combobox está sendo utilizado
    if combobox_item.get():
        item_selecionado = combobox_item.get()
        relatorio_texto = f"Relatório do item {item_selecionado}\nOcorrências simuladas: {item['Relatórios']['Serviços']}"
    elif combobox_item1.get():
        item_selecionado = combobox_item1.get()
        relatorio_texto = f"Relatório do item {item_selecionado}\nOcorrências simuladas: {item1['Relatórios']['Cadastro']}"
    elif combobox_item2.get():
        item_selecionado = combobox_item2.get()
        relatorio_texto = f"Relatório do item {item_selecionado}\nOcorrências simuladas:{item2['Relatórios']['Pagamentos']}"
    else:
        relatotio_texto = "Por favor, selecione um item para pesquisa!"

        # Exibir o relatório no campo de texto
    campo_relatorio.delete('1.0', 'end')
    campo_relatorio.insert('1.0', relatorio_texto)



def gerar_relatorio():
    # Capturar as datas e o item selecionado
    global calendario_inicial, calendario_final, combobox_item

    data_inicial = calendario_inicial.get_date()
    data_final = calendario_final.get_date()
    item_selecionado = combobox_item.get()


    # Verificar se o item foi selecionado e as datas estão corretas
    if not item_selecionado:
        relatorio_texto = "Por favor, selecione um item para a pesquisa!\n"
    elif not data_inicial or not data_final:
        relatorio_texto = "Por favor, selecione a datas inicial e final!\n"
    else:
        # Criar o texto do relatório
        relatorio_texto = f"Relatório do item  {item_selecionado}\n"
        relatorio_texto += f"Data inicial  {data_inicial}\n"
        relatorio_texto += f"Data final  {data_final}\n"
        relatorio_texto += f"Ocorrências simuladas: ['Banho', 'Hidratação', 'Desembolo', 'Remoção Pelos', 'Corte Unhas', 'Escovação Dentes', 'Tosa Higiênica', 'Tosa Máquina', 'Tosa Tesoura', 'Leva Trás']"

def gerar_relatorio():
    # Capturar as datas e o item selecionado
    global calendario_inicial, calendario_final, combobox_item1

    data_inicial = calendario_inicial.get_date()
    data_final = calendario_final.get_date()
    item_selecionado = combobox_item1.get()


    # Verificar se o item foi selecionado e as datas estão corretas
    if not item_selecionado:
        relatorio_texto = "Por favor, selecione um item para a pesquisa!\n"
    elif not data_inicial or not data_final:
        relatorio_texto = "Por favor, selecione a datas inicial e final!\n"
    else:
        # Criar o texto do relatório
        relatorio_texto = f"Relatório do item  {item_selecionado}\n"
        relatorio_texto += f"Data inicial  {data_inicial}\n"
        relatorio_texto += f"Data final  {data_final}\n"
        relatorio_texto += f"Ocorrências simuladas: ['Cadastrado Desde', 'Nome Pet', 'Idade', 'Tutor 1', 'Tutor 2', 'Telefone Tutor 1', 'email Tutor 1',                 'Telefone Tutor 2', 'email Tutor 2', 'Endereço', 'Número', 'Complemento', 'Recomendações']"



def gerar_relatorio():
    # Capturar as datas e o item selecionado
    global calendario_inicial, calendario_final, combobox_item2

    data_inicial = calendario_inicial.get_date()
    data_final = calendario_final.get_date()
    item_selecionado = combobox_item2.get()


    # Verificar se o item foi selecionado e as datas estão corretas
    if not item_selecionado:
        relatorio_texto = "Por favor, selecione um item para a pesquisa!\n"
    elif not data_inicial or not data_final:
        relatorio_texto = "Por favor, selecione a datas inicial e final!\n"
    else:
        # Criar o texto do relatório
        relatorio_texto = f"Relatório do item  {item_selecionado}\n"
        relatorio_texto += f"Data inicial  {data_inicial}\n"
        relatorio_texto += f"Data final  {data_final}\n"
        relatorio_texto += f"Ocorrências simuladas: ['Condições Pagamento', 'Abatimentos', 'Status Pagamento', 'Data Pagamento', 'Forma Pagamento']"



def update_porte_item1(event=None):
    global combobox_item1
    porte = combobox_item1.get().strip()

def gerar_relatorio():
    # Capturar as datas e o item selecionado
    global calendario_inicial, calendario_final, combobox_item

    data_inicial = calendario_inicial.get_date()
    data_final = calendario_final.get_date()
    item_selecionado = combobox_item.get()


    # Verificar se o item foi selecionado e as datas estão corretas
    if not item_selecionado:
        relatorio_texto = "Por favor, selecione um item para a pesquisa!\n"
    elif not data_inicial or not data_final:
        relatorio_texto = "Por favor, selecione a datas inicial e final!\n"
    else:
        # Criar o texto do relatório
        relatorio_texto = f"Relatório do item  {item_selecionado}\n"
        relatorio_texto += f"Data inicial  {data_inicial}\n"
        relatorio_texto += f"Data final  {data_final}\n"
        relatorio_texto += f"Ocorrências simuladas: ['Porte', 'Raça', 'Serviço', 'Condições Pagamento', 'Abatimentos', 'Status Pagamento', 'Data Pagamento', 'Forma Pagamento', 'Cadastrado Desde', 'Nome Pet', 'Idade', 'Tutor 1', 'Tutor 2', 'Telefone 1', 'Telefone 2', 'Endereço', 'Poodle', 'Recomendações', 'Em Aberto-Total', 'Pago-Total', 'Em Aberto-Individual', 'Pago-Individual']"

        # Exibir o relatório no campo de texto
    campo_relatorio.delete('1.0', 'end')
    campo_relatorio.insert('1.0', relatorio_texto)

# Configuração de Calendários
frame_calendario_inicial = ttk.LabelFrame(frame_relatorios, text="Data Inicial-Relatório")
frame_calendario_inicial.grid(row=2, column=3, padx=10, pady=10, sticky="w")
date_inicial = DateEntry(frame_relatorios, year=2025, locale='pt_br')
date_inicial.grid(row=3, column=3 , padx=10, pady=10, sticky='nsew')

frame_calendario_final = ttk.LabelFrame(inner_frame, text="Data Final-Relatório")
frame_calendario_final.grid(row=2, column=4, padx=10, pady=10, sticky="w")
date_final = DateEntry(frame_relatorios, year=2025, locale='pt_br')
date_final.grid(row=3, column=5 , padx=10, pady=10, sticky='nsew')

def limpar_relatorio():
    campo_relatorio.delete('1.0', 'end')

#Botão para limpar o relatório exibido
botao_limpar = ttk.Button(inner_frame, text="Limpar Relatório", command=limpar_relatorio)
botao_limpar.grid(row=5, column=4, pady=6)


# Criando um Frame para Relatório
frame_relatorio = ttk.LabelFrame(inner_frame, text="Relatórios-(Cadastro, Serviços, Controle Pagamentos)")
frame_relatorio.grid(row=3, column=5, columnspan=2, padx=10, pady=5, sticky="w")
label_relatorio = tk.Label(frame_relatorio, text="Recomendações", borderwidth=1, relief='solid' )

# Campo para exibir o relatório
campo_relatorio = tk.Text(frame_relatorio, width=50, height=5, borderwidth=2, relief='solid')
campo_relatorio.grid(row=4, column=5, columnspan=2, padx=10, pady=10)



# Botão para gerar relatório
botao_gerar = ttk.Button(inner_frame, text="Gerar Relatório", command=gerar_relatorio)
botao_gerar.grid(row=3, column=4, pady=6)
#
# Botão para limpar o relatório exibido
botao_limpar = ttk.Button(inner_frame, text="Limpar Relatório", command=limpar_relatorio)
botao_limpar.grid(row=6, column=4, pady=6)

botao_fechar = tk.Button(text='Fechar', command=janela.quit, borderwidth=2, relief='solid')
botao_fechar.grid(row=3, column=6, padx=6, pady=10, sticky='nsew', columnspan=4)


# FINANCEIRO FINANCEIRO FINANCEIRO



# CONSULTA CONSULTA CONSULTA

def criar_frame_consulta(parent):
    frame_consulta = ttk.LabelFrame(parent, text="Informações Sobre o PET")
    frame_consulta.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    frame_consulta = ttk.LabelFrame(frame_consulta, text="Consultando PET")
    frame_consulta.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")



# Criando um Frame para Dados Cadastrais
frame_cadastramento = tk.LabelFrame(aba_cadastro, text="Dados Cadastrais", borderwidth=3, relief='groove')
frame_cadastramento.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Nome do Pet
ttk.Label(frame_cadastramento, text="Nome do Pet:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nome_pet = ttk.Entry(frame_cadastramento)
entry_nome_pet.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Idade
ttk.Label(frame_cadastramento, text="Idade (Anos):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_idade_anos = ttk.Entry(frame_cadastramento)
entry_idade_anos.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

ttk.Label(frame_cadastramento, text="Idade (Meses):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_idade_meses = ttk.Entry(frame_cadastramento)
entry_idade_meses.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Criando um Frame para Endereço e Observações
frame_endereco = tk.LabelFrame(aba_cadastro, text="Endereço e Observações", borderwidth=3, relief='groove')
frame_endereco.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")

ttk.Label(frame_endereco, text="Endereço:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_expande = ttk.Entry(frame_endereco)
entry_expande.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

# aumentando o tamanho do entry configurando columnconfigure(1, weight=1)
frame_endereco.columnconfigure(1, weight=2)

# Configura as colunas do frame_endereco para expansão
# for col in range(2):
#     frame_endereco.columnconfigure(col, weight=1)



ttk.Label(frame_endereco, text="Número:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_fixo = ttk.Entry(frame_endereco)
entry_fixo.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Endereço Complemento
ttk.Label(frame_endereco, text="Complemento").grid(row=2, column=0, padx=10, pady=10, sticky='nsew')     # Campo de entrada (Entry)
entry_enderecocomplemento = ttk.Entry(frame_endereco)
entry_enderecocomplemento.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky='ew')




# Criando um Frame para Dados Cadastrais
frame_tutor = tk.LabelFrame(aba_cadastro, text="Dados dos Tutores", borderwidth=3, relief='groove')
frame_tutor.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

# Tutor 1
ttk.Label(frame_tutor, text="NOME Tutor 1:").grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
entry_tutor_1 = tk.Entry(frame_tutor)
entry_tutor_1.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

# telefone1
ttk.Label(frame_tutor, text="Telefone Tutor 1").grid(row=4, column=0, padx=10, pady=10, sticky='e')
entry_telefone_1 = tk.Entry(frame_tutor)
entry_telefone_1.grid(row=4, column=1, padx=10, pady=10, sticky='nsew')

# email Tutor1
ttk.Label(frame_tutor, text="email Tutor 1").grid(row=5, column=0, padx=10, pady=10, sticky='e')
entry_email_tutor_1 = tk.Entry(frame_tutor)
entry_email_tutor_1.grid(row=5, column=1, padx=10, pady=10, sticky='nsew')

# tutor 2
ttk.Label(frame_tutor, text="NOME Tutor 2:").grid(row=6, column=0, padx=10, pady=10, sticky='nsew')

# Campo de entrada (Entry)
entry_tutor_2 = tk.Entry(frame_tutor)
entry_tutor_2.grid(row=6, column=1, padx=10, pady=10, sticky='nsew')

# telefone 2
ttk.Label(frame_tutor, text="Telefone Tutor 2").grid(row=7, column=0, padx=10, pady=10, sticky='nsew')
# Campo de entrada (Entry)
entry_telefone_2 = tk.Entry(frame_tutor)
entry_telefone_2.grid(row=7, column=1, padx=10, pady=10, sticky='nsew')
ttk.LabelFrame(frame_tutor, text="Telefone_a")
entry_telefone_2a = tk.Entry(inner_frame)
entry_telefone_2a.grid(row=8, column=0, padx=10, pady=10, sticky='nsew')

# email Tutor2
ttk.Label(frame_tutor, text="email Tutor 2").grid(row=9, column=0, padx=10, pady=10, sticky='e')
entry_email_tutor_2 = tk.Entry(frame_tutor)
entry_email_tutor_2.grid(row=9, column=1, padx=10, pady=10, sticky='nsew')



# Criando um Frame para tipopelo e Características
aba_cadastro = ttk.Frame(aba_cadastro)
aba_cadastro.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

frame_descricao = tk.LabelFrame(aba_cadastro, text=" Tamanho e Características - Pelagem ", borderwidth=3, relief="groove")
frame_descricao.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

# Criando variável para os Radiobuttons
var_descricao = tk.StringVar(value="") # Inicializa sem nenhuma seleção


# Botões de Características - Pelagem (inicialmente desabilitados)
radiobutton_curta = tk.Radiobutton(frame_descricao, text="Curta", variable=var_descricao, value="Curta")
radiobutton_curta.grid(row=2, column=0, sticky="w")

radiobutton_mediana = tk.Radiobutton(frame_descricao, text="Mediana", variable=var_descricao, value="Mediana")
radiobutton_mediana.grid(row=3, column=0, sticky="w")

radiobutton_longa = tk.Radiobutton(frame_descricao, text="Longa", variable=var_descricao, value="Longa")
radiobutton_longa.grid(row=4, column=0, sticky="w")

# Função para ativar/desativar Radiobuttons
def atualizar_descricao():
    global var_descricao  # Declare a variável como global
    if var_descricao.get() in ["Curta", "Mediana", "Longa"]:
        # Ativar botões de pagamento
        radiobutton_curta.config(state="normal")
        radiobutton_mediana.config(state="normal")
        radiobutton_longa.config(state="normal")
    else:
        # Resetar e desabilitar botões de pagamento
        var_descricao.set("") # Ressetar seleção
        radiobutton_curta.config(state="disabled")
        radiobutton_mediana.config(state="disabled")
        radiobutton_longa.config(state="disabled")

# Botão para testar ativação dos Radiobuttons
# btn_ativar = ttk.Button(frame_descricao, text="Ativar Seleção", command=atualizar_descricao)
# btn_ativar.grid(row=5, column=0, pady=10, sticky="w")


# Função para salvar no banco de dados
def salvar_descricao():
    descricao_selecionada = var_descricao.get()

    if descricao_selecionada:
        conn = sqlite3.connect("petshop.db")  # Conectar ao banco de dados
        cursor = conn.cursor()

        # Criar tabela se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS caracteristicas_pet (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT
            )
        ''')

        # Inserir dados
        cursor.execute("INSERT INTO caracteristicas_pet (descricao) VALUES (?)", (descricao_selecionada,))
        conn.commit()
        conn.close()

        print(f"tipopelo '{descricao_selecionada}' salva no banco de dados!")


# Criando um Frame para Tipos de Pelos
aba_cadastro = ttk.Frame(aba_cadastro)
aba_cadastro.grid(row=4, column=0, padx=10, pady=5, sticky="w")

frame_tipopelo = tk.LabelFrame(aba_cadastro, text="Tipo de Pelo", borderwidth=3, relief="groove")
frame_tipopelo.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

# Criando variável para os Radiobuttons
var_tipopelo = tk.StringVar(value="") # Inicializa sem nenhuma seleção


# Botões de forma de pagamento (inicialmente desabilitados)
radiobutton_grosso = tk.Radiobutton(frame_tipopelo, text="Grosso Espesso", variable=var_tipopelo, value="Grosso Espesso")
radiobutton_grosso.grid(row=0, column=0, sticky="w")

radiobutton_fino = tk.Radiobutton(frame_tipopelo, text="Fino Suave", variable=var_tipopelo, value="Fino Suave")
radiobutton_fino.grid(row=1, column=0, sticky="w")


# Função para ativar/desativar Radiobuttons
def atualizar_tipopelo():
    global var_tipopelo  # Declare a variável como global
    if var_tipopelo.get() in ["Grosso", "Fino"]:
        # Ativar botões de pagamento
        radiobutton_grosso.config(state="normal")
        radiobutton_fino.config(state="normal")

    else:
        # Resetar e desabilitar botões de pagamento
        var_tipopelo.set("") # Ressetar seleção
        radiobutton_grosso.config(state="disabled")
        radiobutton_fino.config(state="disabled")

# Botão para testar ativação dos Radiobuttons
# btn_ativar = ttk.Button(frame_tipopelo, text="Ativar Seleção", command=atualizar_tipopelo)
# btn_ativar.grid(row=4, column=3, pady=10, sticky="w")


# Função para salvar no banco de dados
def salvar_tipopelo():
    tipopelo_selecionada = var_tipopelo.get()

    if tipopelo_selecionada:
        conn = sqlite3.connect("petshop.db")  # Conectar ao banco de dados
        cursor = conn.cursor()

        # Criar tabela se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS caracteristicas_pet (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT
            )
        ''')

        # Inserir dados
        cursor.execute("INSERT INTO caracteristicas_pet (descricao) VALUES (?)", (tipopelo_selecionada,))
        conn.commit()
        conn.close()

        print(f"tipopelo '{tipopelo_selecionada}' salva no banco de dados!")


# tempo previsto para para execução
# Criando um Frame para Tempo de Execução
frame_tempo = tk.LabelFrame(aba_cadastro, text="Tempo de Execução", borderwidth=3, relief='groove')
frame_tempo.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")


# Ajustando colunas para melhor organização
frame_tempo.grid_columnconfigure(0, weight=1)
frame_tempo.grid_columnconfigure(1, weight=1)


# Frame de Tempo de Execução
ttk.Label(frame_tempo, text="Duração do Serviço:").grid(row=0, column=0, padx=5, pady=2, sticky='w')
entry_duracao = tk.Entry(frame_tempo)
entry_duracao.grid(row=0, column=1, sticky="ew", padx=5, pady=2)

# Tempo Banho
ttk.Label(frame_tempo, text="Tempo Banho:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
entry_banho = tk.Entry(frame_tempo)
entry_banho.grid(row=1, column=1, sticky="ew", padx=5, pady=2)


# Tempo Secagem
ttk.Label(frame_tempo, text="Tempo Secagem:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
entry_secagem = tk.Entry(frame_tempo)
entry_secagem.grid(row=2, column=1, sticky="ew", padx=5, pady=2)


# Hidratação
ttk.Label(frame_tempo, text="Tempo T. Hidratação:").grid(row=3, column=0, sticky="w", padx=5, pady=2)
entry_hidratacao = tk.Entry(frame_tempo)
entry_hidratacao.grid(row=3, column=1, sticky="ew", padx=5, pady=2)


# Tempo Desembolo
ttk.Label(frame_tempo, text="Tempo T. Desembolo:").grid(row=4, column=0, sticky="w", padx=5, pady=2)
entry_desembolo = tk.Entry(frame_tempo)
entry_desembolo.grid(row=4, column=1, sticky="ew", padx=5, pady=2)


# Tempo Tosa Higiênica
ttk.Label(frame_tempo, text="Tempo T. Higiênica:").grid(row=5, column=0, sticky="w", padx=5, pady=2)
entry_higienica = tk.Entry(frame_tempo)
entry_higienica.grid(row=5, column=1, sticky="ew", padx=5, pady=2)

# Tempo Tosa Máquina
ttk.Label(frame_tempo, text="Tempo T. Máquina:").grid(row=6, column=0, sticky="w", padx=5, pady=2)
entry_maquina = tk.Entry(frame_tempo)
entry_maquina.grid(row=6, column=1, sticky="ew", padx=5, pady=2)



# Tempo Tosa Tesoura
ttk.Label(frame_tempo, text="Tempo T. Tesoura:").grid(row=7, column=0, sticky="w", padx=5, pady=2)
entry_tesoura = tk.Entry(frame_tempo)
entry_tesoura.grid(row=7, column=1, sticky="ew", padx=5, pady=2)



# TEMPO TOTAL ATENDIMENTO
ttk.Label(frame_tempo, text="Tempo Total Atendimento:").grid(row=8, column=0, sticky="w", padx=5, pady=2)
entry_total = tk.Entry(frame_tempo)
entry_total.grid(row=8, column=1, sticky="ew", padx=5, pady=2)


# Criando um Frame para Cuidados Necessários
aba_cadastro = ttk.Frame(aba_cadastro)
aba_cadastro.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

frame_cuidados = tk.LabelFrame(aba_cadastro, text="Tipo de Pelo", borderwidth=3, relief="groove")
frame_cuidados.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

# Criando variável para os Radiobuttons
var_cuidados = tk.StringVar(value="") # Inicializa sem nenhuma seleção


# Usando a instância existente de root
root = tk.Tk()  # Esta linha deve ser removida se a janela principal já existir
app = App(root)
root.mainloop()  # Esta linha deve estar ao final, chamando o loop principal da janela
janela.mainloop()

