import tkinter as tk
from PIL import Image, ImageTk
import os
import pygame

# 🎵 Inicialização de som
pygame.init()
pygame.mixer.init()

# 🧩 Importações do projeto
from backup_revisar.aba_login_fusion_a import criar_login
from modulos.audio import som_evento
from utilitarios import caminho_arquivo

# 🖼️ Splash com logo
def mostrar_splash(janela):
    splash = tk.Toplevel(janela)
    splash.overrideredirect(True)
    largura, altura = 500, 300
    x = (splash.winfo_screenwidth() - largura) // 2
    y = (splash.winfo_screenheight() - altura) // 2
    splash.geometry(f"{largura}x{altura}+{x}+{y}")

    logo_path = caminho_arquivo("logo_ipojucao.png", subpasta="imagens")
    if os.path.exists(logo_path):
        img = Image.open(logo_path).resize((largura, altura))
        img_tk = ImageTk.PhotoImage(img)
        label = tk.Label(splash, image=img_tk)
        label.image = img_tk
        label.grid(row=0, column=0, sticky="nsew")
        splash.grid_rowconfigure(0, weight=1)
        splash.grid_columnconfigure(0, weight=1)
    else:
        tk.Label(splash, text="Ipojucão", font=("Segoe UI", 24)).grid(row=0, column=0)

    splash.after(2500, lambda: [splash.destroy(), iniciar_login(janela)])

# 🔐 Callback após login
def abrir_janela_principal(nome, perfil):
    janela_principal = tk.Tk()
    janela_principal.title(f"Ipojucão • Bem-vindo {nome}")
    janela_principal.geometry("900x600")

    tk.Label(janela_principal, text=f"🐾 Bem-vindo(a), {nome}!", font=("Segoe UI", 18)).grid(row=0, column=0, padx=20, pady=20)
    tk.Label(janela_principal, text=f"Perfil: {perfil}", font=("Segoe UI", 12)).grid(row=1, column=0, padx=20)

    # Aqui você pode adicionar suas abas e funcionalidades
    # Exemplo: notebook = ttk.Notebook(janela_principal)

    janela_principal.mainloop()

# 🚀 Início do sistema
def iniciar_login(janela):
    criar_login(janela, ao_logar_callback=abrir_janela_principal)

def iniciar_sistema():
    janela_inicial = tk.Tk()
    janela_inicial.withdraw()
    som_evento("abertura")
    mostrar_splash(janela_inicial)
    janela_inicial.mainloop()

# 🧭 Ponto de entrada
if __name__ == "__main__":
    print("✅ Executando main.py com aba_login_fusion")
    iniciar_sistema()












































# import pygame
# pygame.init()
# pygame.mixer.init()
# import tkinter as tk
# from tkinter import ttk
# import os
# import sys
# from PIL import Image, ImageTk
#
# #from modulos.aba_login import criar_login
# from modulos.aba_login_fusion import criar_login
# from modulos.aba_relatorios import montar_aba_relatorios
# from modulos.barra_som import criar_barra_som
# from modulos.mascote import mascote_piscante, mostrar_mascote_expressivo
# from modulos.som import som_evento
# from modulos.dados_compartilhados import inicializar_variaveis
# from modulos.dados_compartilhados import variaveis
#
# from utilitarios import caminho_arquivo
# from modulos.dados_compartilhados import usuarios
#
# from modulos.ipojucao_login import iniciar_login
#
# def abrir_janela_principal(janela):
#     dc.inicializar_variaveis(janela)
#     estrutura.aba_ativa = tk.StringVar(master=janela, value="")
#
#     def ao_logar(nome, perfil):
#         janela.deiconify()
#         tk.Label(janela, text=f"🐾 Bem-vindo(a), {nome}!", font=("Segoe UI", 18), bg="#ffffff").place(x=30, y=10)
#         tk.Label(janela, text=f"Perfil: {perfil}", font=("Segoe UI", 12), bg="#ffffff").place(x=30, y=40)
#
#         estrutura.frame_navegacao = ttk.Frame(janela)
#         estrutura.frame_navegacao.place(x=0, y=0, width=1200, height=60)
#
#         estrutura.titulo_aba = tk.Label(janela, text="Bem-vindo ao Sistema Ipojucão", font=("Segoe UI", 18))
#         estrutura.titulo_aba.place(x=20, y=10)
#
#         estrutura.notebook = ttk.Notebook(janela)
#         estrutura.notebook.place(x=30, y=80, width=1140, height=580)
#
#         mascote_piscante(janela)
#         mostrar_mascote_expressivo(janela, "feliz")
#         criar_barra_som(janela)
#
#         # Adiciona abas conforme perfil
#         def adicionar_aba(nome, frame_fn, acesso="Todos"):
#             if acesso == "Administrador" and perfil != "Administrador":
#                 return
#             aba = ttk.Frame(estrutura.notebook)
#             estrutura.notebook.add(aba, text=nome)
#             frame_fn(aba, estrutura.inner_frame)
#
#
#         abas_menu = [
#             ("Cadastro", montar_aba_cadastro),
#             ("Clientes", montar_aba_clientes),
#             ("Clima", montar_aba_clima),
#             ("Configuração", montar_aba_config),
#             ("Consulta", montar_aba_consulta),
#             ("Diagnóstico", lambda aba: criar_menu_diagnostico(janela, estrutura.notebook)),
#             ("Financeiro", montar_aba_financeiro),
#             ("Itaú API", montar_aba_itau, "Administrador"),
#             ("Relatórios", montar_aba_relatorios, "Administrador")
#         ]
#         #adicionar_aba_financeiro(estrutura.notebook, estrutura.inner_frame)
#         for item in abas_menu:
#             nome, funcao = item[0], item[1]
#             acesso = item[2] if len(item) > 2 else "Todos"
#             adicionar_aba(nome, funcao, acesso)
#
#     janela.after(100, lambda: criar_login(janela, ao_logar))
#     janela.mainloop()
#
# # 🚀 INICIALIZAÇÃO DO SISTEMA
# def iniciar_sistema():
#     janela_inicial = tk.Tk()
#     janela_inicial.withdraw()
#     mostrar_splash(janela_inicial)
#     som_evento("abertura")
#     janela_inicial.after(2600, lambda: criar_login(janela_inicial, ao_logar_callback=abrir_janela_principal))
#     janela_inicial.mainloop()
#
#
#
# # pygame.init()
# # pygame.mixer.init()
# caminho_intro = caminho_arquivo("bouncy _pet_intro.mp3", subpasta="sons")
#
# pygame.mixer.music.load(caminho_intro)
# if os.path.exists(caminho_intro):
#     pygame.mixer.music.load(caminho_intro)
# else:
#     print(f"🔍 Arquivo de som não encontrado: {caminho_intro}")
# #from modulos.ipojucao_login import criar_login, abrir_janela_principal
#
# print("Executando main.py correto")
#
#
#
# from modulos.ipojucao_login import criar_login, abrir_janela_principal
#
#
# # def iniciar_app():
# #     janela_inicial = tk.Tk()
# #     criar_login(janela_inicial, ao_logar_callback=abrir_janela_principal)
# #     janela_inicial.mainloop()
#
#
# logo_splash = caminho_arquivo("splash.png", subpasta=os.path.join("..", "..", "imagensipojucao"))
# som_relatorio = caminho_arquivo("bouncy _pet_intro.mp3", subpasta="sons")
# # 🔧 Módulos locais
# import estrutura
#
# splash_path = caminho_arquivo("splash.png", subpasta=os.path.join("..", "..", "imagensipojucao"))
#
#
# # 🎬 Splash com logo
# def mostrar_splash():
#     splash = tk.Toplevel(root)
#     splash.overrideredirect(True)
#     largura, altura = 500, 300
#     x = (splash.winfo_screenwidth() - largura) // 2
#     y = (splash.winfo_screenheight() - altura) // 2
#     splash.geometry(f"{largura}x{altura}+{x}+{y}")
#
#     logo_path = "imagens/logo_ipojucao.png"
#     if os.path.exists(logo_path):
#         img = Image.open(logo_path).resize((largura, altura))
#         img_tk = ImageTk.PhotoImage(img)
#         label = tk.Label(splash, image=img_tk)
#         label.image = img_tk
#         label.grid(row=0, column=0, sticky="nsew")
#         splash.grid_rowconfigure(0, weight=1)
#         splash.grid_columnconfigure(0, weight=1)
#     else:
#         tk.Label(splash, text="Ipojucão", font=("Segoe UI", 24)).pack(expand=True)
#
#     splash.after(2500, lambda: [splash.destroy(), iniciar_app()])
#
#
# #🧭 PONTO DE PARTIDA
# if __name__ == "__main__":
#     print("✅ Executando main.py corretamente")
#     iniciar_sistema()
#
# # # porte = variaveis["var_porte"].get()
# # from modulos.dados_compartilhados import variaveis, inicializar_variaveis
# # import modulos.dados_compartilhados as dc
# # import pygame
# # pygame.init()
#
#
#         # Widget no layout principal
# # Simulação de dados compartilhados
# class Dados:
#     def __init__(self, janela):
#         self.variaveis = {
#             "var_tipo_pacote": tk.StringVar(master=janela, value="Quinzenal")
#         }
#
#         self.variaveis_servicos = {
#             "Banho": tk.BooleanVar(),
#             "Hidratação": tk.BooleanVar(),
#             "Desembolo": tk.BooleanVar(),
#             "Remoção de Pelos": tk.BooleanVar(),
#             "Corte de Unhas": tk.BooleanVar(),
#             "Tosa Higiênica": tk.BooleanVar(),
#             "Tosa na Máquina": tk.BooleanVar(),
#             "Tosa na Tesoura": tk.BooleanVar(),
#             "Leva e Trás": tk.BooleanVar(),
#         }
#
#         self.pacotes_servicos = {
#             "Quinzenal": {
#                 "incluidos": ["Banho", "Banho"],
#                 "bonus_opcoes": ["Tosa Higiênica", "Hidratação"]
#             },
#             "Mensal": {
#                 "incluidos": ["Banho"] * 4,
#                 "bonus_opcoes": ["Tosa Higiênica", "Hidratação"]
#             }
#         }
#
# root = tk.Tk()
# dc = Dados(root)        # Criação da instância Dados com root
# janela = root           # Usa root como janela principal
# inicializar_variaveis(janela)
#
# # dc.pacotes_servicos = {
# #     "Pacote 1": ["Banho", "Corte de Unhas"],
# #     "Pacote 2": ["Tosa na Máquina", "Remoção de Pelos"]
# # }
#
# # Agora é seguro criar variáveis vinculadas à interface
#
# var_porte = variaveis["var_porte"]
# var_raca = variaveis["var_raca"]
# var_tipopelo = variaveis["var_tipopelo"]
# var_pagamento = variaveis["var_pagamento"]
# var_descricao = variaveis["var_descricao"]
#
# dc.pacotes_servicos = {
#     "Quinzenal": {
#         "incluidos": ["Banho", "Banho"],
#         "bonus_opcoes": ["Tosa Higiênica", "Hidratação"]
#     },
#     "Mensal": {
#         "incluidos": ["Banho", "Banho", "Banho", "Banho"],
#         "bonus_opcoes": ["Tosa Higiênica", "Hidratação"]
#     }
# }
#
# # Serviços que o cliente solicita
# servicos_solicitados = ["Banho", "Hidratação", "Desembolo", "Remoção de Pelos","Corte de Unhas", "Tosa Higiênica", "Tosa na Máquina",
#         "Tosa na Tesoura", "Leva e Trás" ]
#
# # Função para verificar serviços extras
#
# def verificar_servicos(pacote, solicitados):
#     pacote_info = dc.pacotes_servicos.get(pacote)
#     permitidos = pacote_info["incluidos"] + pacote_info["bonus_opcoes"]
#
#     extras = [s for s in solicitados if s not in permitidos]
#
#     if extras:
#         print(f"⚠️ Serviços não previstos no pacote {pacote}:")
#         for servico in extras:
#             print(f"  - {servico}")
#     else:
#         print(f"✅ Todos os serviços solicitados estão dentro do pacote {pacote}.")
#
# # Criação do alerta visual
# frame_alerta = ttk.LabelFrame(janela, text="Alerta de Serviços")
# frame_alerta.grid(row=0, column=0, padx=10, pady=10)
# label_alerta = tk.Label(frame_alerta, text="", fg="red", font=("Arial", 10, "bold"))
# label_alerta.grid()
#
#
# def verificar_servicos_extras_visual():
#     pacote = dc.variaveis.get("var_tipo_pacote", tk.StringVar()).get()
#     pacote_info = dc.pacotes_servicos.get(pacote, {})
#     permitidos = pacote_info.get("incluidos", []) + pacote_info.get("bonus_opcoes", [])
#     extras = []
#
#     for servico, var in dc.variaveis_servicos.items():
#         if var.get() and servico not in permitidos:
#             extras.append(servico)
#
#     if extras:
#         texto_alerta = "⚠️ Serviços não previstos no pacote: " + ", ".join(extras)
#         label_alerta.config(text=texto_alerta)
#     else:
#         label_alerta.config(text="✅ Todos os serviços estão dentro do pacote.")
#
# ttk.Button(janela, text="Verificar serviços", command=verificar_servicos_extras_visual).grid(row=1, column=0, pady=10)
#
# # Exemplo de uso
# verificar_servicos("Quinzenal", servicos_solicitados)
# verificar_servicos("Mensal", servicos_solicitados)
#
#
# # 🔽 FORMULÁRIO COM .grid()
# ttk.Label(janela, text="Porte:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
# ttk.Entry(janela, textvariable=var_porte).grid(row=0, column=1, padx=5, pady=5)
#
# ttk.Label(janela, text="Raça:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
# ttk.Entry(janela, textvariable=var_raca).grid(row=1, column=1, padx=5, pady=5)
#
# ttk.Label(janela, text="Tipo de Pelo:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
# ttk.Entry(janela, textvariable=var_tipopelo).grid(row=2, column=1, padx=5, pady=5)
#
# ttk.Label(janela, text="Pagamento:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
# ttk.Entry(janela, textvariable=var_pagamento).grid(row=3, column=1, padx=5, pady=5)
#
# ttk.Label(janela, text="Descrição:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
# ttk.Entry(janela, textvariable=var_descricao).grid(row=4, column=1, padx=5, pady=5)
#
# # 👀 Exibe os valores atuais no console (opcional)
#
# # Teste simples para verificar se está tudo certo:
# print(variaveis["var_porte"].get())
#
# for chave, var in variaveis.items():
#     print(f"{chave} = '{var.get()}'")
#
# # 🎯 Abas
# from modulos.aba_login import criar_login
# from modulos.aba_clima import montar_aba_clima
# from modulos.aba_cadastro import montar_aba_cadastro
# from modulos.aba_clientes import montar_aba_clientes
# from modulos.aba_consulta import montar_aba_consulta
# from modulos.aba_config import montar_aba_config
# from modulos.aba_diagnostico import criar_menu_diagnostico
# from modulos.aba_financeiro import montar_aba_financeiro
# #from modulos.aba_itau import montar_aba_itau
# #
#
# # 🐶 Perfis
# abas_exclusivas = {
#     "Administrador": ["Itaú API", "Relatórios"]
# }

# Para imagem do splash
# 🚀 Iniciar aplicação
# def iniciar_app():
#     janela = tk.Toplevel()
#     #janela.withdraw()
#     janela.title("Sistema Ipojucão")
#     janela.geometry("1200x700")
#     janela.configure(bg="#ffffff")


# # ⏩ Ponto de partida
# if __name__ == "__main__":
#     print("Python executando em:", sys.executable)
#     mostrar_splash()
#     som_evento("abertura")
#
#     root.mainloop()
#




