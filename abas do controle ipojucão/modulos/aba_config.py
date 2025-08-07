#from dados_compartilhados import var_raca, caracteristicas_racas
import tkinter as tk
import os
from modulos.aba_som import tocar_som

#import dados_compartilhados as dc # var_porte, var_raca, dados_pet, imagens_racas, imagens_portes
#from main import inner_frame
from utilitarios import caminho_arquivo

logo_splash = caminho_arquivo("splash.png", subpasta=os.path.join("..", "..", "imagensipojucao"))
som_relatorio = caminho_arquivo("relatorio_finalizado.mp3", subpasta="sons")


var_raca = tk.StringVar
from dados_compartilhados import variaveis
def usar_dados_banho_preco():
    # porte = dc.var_porte.get()
    porte = variaveis["var_porte"].get()
    preco_banho = dc.dados_pet.get(porte, {}).get("preços", {}).get("Banho", 0)
    print(f"Banho para porte {porte} custa R$ {preco_banho}")


import tkinter as tk
from tkinter import ttk


# def montar_aba_config(aba):
#     # Permitir expansão
#     aba.grid_rowconfigure(0, weight=1)
#     aba.grid_columnconfigure(0, weight=1)

def montar_aba_config(aba_config, inner_frame):
    aba_config.grid_rowconfigure(0, weight=1)
    aba_config.grid_columnconfigure(0, weight=1)

    canvas = tk.Canvas(aba)
    canvas.grid(row=0, column=0, sticky="nsew")

    scrollbar_y = ttk.Scrollbar(aba, orient="vertical", command=canvas.yview)
    scrollbar_y.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar_y.set)

    inner_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    dc.var_porte.trace_add("write", lambda *args: atualizar_exemplo())

    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    inner_frame.bind("<Configure>", ajustar_scroll)

    # 🧩 Exemplo de conteúdo
    frame_exemplo = ttk.LabelFrame(inner_frame, text="Seção de Exemplo")
    frame_exemplo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    ttk.Label(frame_exemplo, text="Alguma informação importante").grid(row=0, column=0, sticky="w")


    # Canvas + Scrollbar
# def montar_aba_config(aba):
#     canvas = tk.Canvas(aba)
#     canvas.grid(row=0, column=0, sticky="nsew")
#
#     aba.grid_rowconfigure(0, weight=1)
#     aba.grid_columnconfigure(0, weight=1)
# # canvas = tk.Canvas(aba)
# # scrollbar_y = ttk.Scrollbar(aba, orient="vertical", command=canvas.yview)
# # canvas.configure(yscrollcommand=scrollbar_y.set)
#
#
#     # Frame rolável
# inner_frame = ttk.Frame(canvas)
# canvas.create_window((0, 0), window=inner_frame, anchor="nw")
#
# def ajustar_scroll(event):
#     canvas.configure(scrollregion=canvas.bbox("all"))
#     inner_frame.bind("<Configure>", ajustar_scroll)
#
#     # === A partir daqui, crie widgets dentro do inner_frame ===
#
#     # Exemplo básico
# frame_exemplo = ttk.LabelFrame(inner_frame, text="Seção de Exemplo")
# frame_exemplo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#
# ttk.Label(frame_exemplo, text="Alguma informação importante").grid(row=0, column=0, sticky="w")

    # Repita quantos blocos quiser (outros frames, grids, entradas, etc.)

    # Se quiser ativar algo quando o porte mudar


def atualizar_exemplo():
    porte = dc.var_porte.get()
    print(f"Porte selecionado na aba é: {porte}")

base_path = "/imagensipojucao"

def montar_aba_config(aba_config, inner_frame):
    # ==== Frame base de layout ====
    frame_config = ttk.Frame(aba_config)
    frame_config.grid(pady=10)


    # Label de seleção do porte
    ttk.Label(frame_config, text="Selecione o Porte:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    dc.combobox_porte = ttk.Combobox(aba_config, textvariable=dc.var_porte,
                                     values=list(dc.dados_pet.keys()), state="readonly", width=25)
    dc.combobox_porte.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    dc.combobox_porte.bind("<<ComboboxSelected>>", atualizar_lista_racas)

    # Label de seleção da raça
    ttk.Label(frame_config, text="Selecione a Raça:").grid(row=0, column=1, padx=10, pady=5, sticky="w")
    dc.combobox_raca = ttk.Combobox(aba_config, textvariable=dc.var_raca,
                                    values=[], state="readonly", width=30)
    dc.combobox_raca.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    dc.combobox_raca.bind("<<ComboboxSelected>>", atualizar_caracteristicas)

    # Label para imagem
    dc.label_imagem = tk.Label(aba_config, text="Nenhuma imagem disponível", width=200, height=200)
    dc.label_imagem.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Texto com as características da raça
    dc.texto_caracteristicas = tk.Text(aba_config, height=8, width=60)
    dc.texto_caracteristicas.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Inicializar com valores padrão
    atualizar_lista_racas()


# ========== Funções internas ==========

def atualizar_lista_racas(event=None):
    porte = dc.var_porte.get()
    racas = dc.dados_pet.get(porte, {}).get("raças", [])
    dc.combobox_raca["values"] = racas

    if racas:
        dc.var_raca.set(racas[0])
        atualizar_caracteristicas()
    else:
        dc.var_raca.set("")
        dc.combobox_raca.set("Nenhuma raça")
        dc.texto_caracteristicas.delete(1.0, tk.END)

    atualizar_imagem_porte(porte)


def atualizar_imagem_porte(porte):
    nome_arquivo = dc.imagens_portes.get(porte, "")
    caminho = os.path.join(base_path, nome_arquivo)

    if os.path.exists(caminho):
        img = Image.open(caminho).resize((200, 200))
        from utils_imagem import fade_in_imagem  # ou importe de onde salvou

        fade_in_imagem(dc.label_imagem, imagem)
        #img_tk = ImageTk.PhotoImage(img)
        # 🔄 Atribuir como imagem padrão antes de raça ser exibida
        #dc.label_imagem.img_ref = img_tk  # mantém referência genérica
        #dc.label_imagem.config(image=img_tk, text="")

        # dc.label_imagem.img_ref_porte = img_tk  # 🔒 mantém referência
        # dc.label_imagem.img_ref_raca = img_tk
        dc.label_imagem.config(image=img_tk, text="")

        # img_tk = ImageTk.PhotoImage(img)
        # dc.label_imagem.config(image=img_tk, text="")
        # dc.label_imagem.image = img_tk
    else:
        dc.label_imagem.config(text="Imagem do porte não encontrada", image="")
        dc.label_imagem.image = None


import os
from PIL import Image
import dados_compartilhados as dc

def tocar_som_transicao():
    caminho = os.path.join("../Planilha Controle Ipojucão/sons", "woof.wav")  # substitua pelo nome do seu som
    #threading.Thread(target=playsound, args=(caminho,), daemon=True).start() # Somente se for usar pacote playsound
    tocar_som(caminho)

def atualizar_caracteristicas(event=None):
    #raca = dc.var_raca.get()
    #porte = dc.var_porte.get()
    raca = variaveis["var_raca"].get
    porte = variaveis["var_porte"].get

    # 📝 Atualiza descrição
    descricao = dc.caracteristicas_racas.get(raca, "Sem descrição cadastrada.")
    dc.texto_caracteristicas.delete("1.0", "end")
    dc.texto_caracteristicas.insert("1.0", descricao)

    # 🖼️ Caminho da imagem principal
    caminho_imagem = os.path.join("../Planilha Controle Ipojucão/imagensipojucao", porte, f"{raca}.jpg")

    # 🧯 Fallback se a imagem específica da raça não existir
    if not os.path.exists(caminho_imagem):
        caminho_imagem = os.path.join("../Planilha Controle Ipojucão/imagensipojucao", "sem_imagem.jpg")

    if os.path.exists(caminho_imagem):
        imagem = Image.open(caminho_imagem).resize((200, 200))
        # img_tk = ImageTk.PhotoImage(imagem)
        # dc.label_imagem.img_ref = img_tk
        # dc.label_imagem.config(image=img_tk, text="")
        from utils_imagem import fade_in_imagem  # ou importe de onde salvou

        fade_in_imagem(dc.label_imagem, imagem)
        tocar_som_transicao()
    else:
        dc.label_imagem.config(image="", text="Imagem não encontrada")

# def atualizar_caracteristicas(event=None):
#     raca = dc.var_raca.get()
#     info = dc.caracteristicas_racas.get(raca, {})
#     imagem_nome = dc.imagens_racas.get(raca, "")
#     caminho = os.path.join(base_path, imagem_nome)
#
#     dc.texto_caracteristicas.delete(1.0, tk.END)
#     if info:
#         dc.texto_caracteristicas.insert(tk.END, f"Raça: {raca}\n")
#         dc.texto_caracteristicas.insert(tk.END, f"Peso: {info.get('peso')}\n")
#         dc.texto_caracteristicas.insert(tk.END, f"Tamanho: {info.get('tamanho')}\n")
#         dc.texto_caracteristicas.insert(tk.END, f"Pelos: {info.get('pelos')}\n")
#         dc.texto_caracteristicas.insert(tk.END, f"Temperamento: {info.get('temperamento')}\n")
#     else:
#         dc.texto_caracteristicas.insert(tk.END, "Sem dados disponíveis.")
#
#     if os.path.exists(caminho):
#         img = Image.open(caminho).resize((200, 200))
#         img_tk = ImageTk.PhotoImage(img)
#         dc.label_imagem.config(image=img_tk, text="")
#         dc.label_imagem.image = img_tk
#     else:
#         dc.label_imagem.config(text="Imagem da raça não encontrada", image="")
#         dc.label_imagem.image = None













#aba_config = ttk.Frame(janela)
# aba_config = ttk.Frame(aba_principal)
# aba_principal.add(aba_config, text="Configuração")
#
#
# aba_config.grid(padx=10, pady=10)  # Adicionando padding para melhor visualização
# janela.geometry("1400x600")  # Ajuste o tamanho da janela conforme necessário
# janela.state('zoomed')  # Abre em tela cheia
#
# # Criando um Frame para a barra de rolagem
# scrollable_frame = ttk.Frame(janela)
# scrollable_frame.grid(row=0, column=0, sticky="nsew")
#
# # Configuração da janela
# janela.grid_rowconfigure(0, weight=1)
# janela.grid_columnconfigure(0, weight=1)
#
# scrollable_frame.grid_rowconfigure(0, weight=1)
# scrollable_frame.grid_columnconfigure(0, weight=1)
#
# # Criando o Canvas e as Scrollbars
# canvas = tk.Canvas(scrollable_frame)
# vertical_scrollbar = ttk.Scrollbar(scrollable_frame, orient="vertical", command=canvas.yview)
# horizontal_scrollbar = ttk.Scrollbar(scrollable_frame, orient="horizontal", command=canvas.xview)
#
# # Criando o Frame dentro do Canvas
# inner_frame = ttk.Frame(canvas)
#
# # Ajustando a rolagem
# inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
#
# # Criando a janela dentro do Canvas
# canvas.create_window((0, 0), window=inner_frame, anchor="nw")
#
# # Posicionando o Canvas e as Scrollbars
# canvas.grid(row=0, column=0, sticky="nsew")
# vertical_scrollbar.grid(row=0, column=1, sticky="ns")
# horizontal_scrollbar.grid(row=1, column=0, sticky="ew")
#
# # Configurando as barras de rolagem
# canvas.configure(yscrollcommand=vertical_scrollbar.set)
# canvas.configure(xscrollcommand=horizontal_scrollbar.set)
#
# # Garantindo que a rolagem funcione corretamente
# def ajustar_tamanho_canvas(event):
#     canvas.configure(scrollregion=canvas.bbox("all"))
#
# inner_frame.bind("<Configure>", ajustar_tamanho_canvas)
#
# # Adicione alguns widgets ao inner_frame como exemplo
# for i in range(50):
#     ttk.Label(inner_frame, text=f"Item {i}").grid(row=i, column=0, sticky="w")
# # Configurar a largura da coluna do inner_frame para permitir a rolagem horizontal
# inner_frame.grid_columnconfigure(0, minsize=300)  # Ajuste o tamanho conforme necessário
#
# # Definindo o tamanho do Canvas
# canvas.config(height=700)  # Aumente a altura do Canvas se necessário
# canvas.config(width=800) # Aumente a largura do Canvas se necessário
#
# # Criando as abas (Notebook)
# aba_config = ttk.Frame(notebook)
# notebook.add(aba_config, text="Configuração")
# notebook.grid(row=0, column=0, sticky='nsew')  # Use grid corretamente
#
# # Criando aba de configuração
# aba_config = ttk.Frame(notebook)
# notebook.add(aba_config, text="Configuração")
#
# frame_config = ttk.Frame(aba_config)
# frame_config.grid(pady=10)
#
#
#
# # Dicionário para armazenar imagens dos portes
# imagens_portes = {
#     "pequeno": "pequeno.jpg",
#     "médio": "medio.jpg",
#     "grande": "grande.jpg",
#     "maior": "maior.jpg"
# }
#
#
#
# # ADICIONANDO CARACTERÍSTICAS DO PET
# # Dicionário de características das raças
# caracteristicas_racas = {
#     "Chihuahua": {
#         "peso": "1 a 3 kg",
#         "tamanho": "15 a 23 cm",
#         "pelos": "Curto",
#         "temperamento": "Dócil",
#         "imagem": "chihuahua.png"  # Adicione o caminho para a imagem
#     },
#     "Labrador": {
#         "peso": "25 a 36 kg",
#         "tamanho": "55 a 62 cm",
#         "pelos": "Curto e grosso",
#         "temperamento": "Dócil",
#         "imagem": "labrador.png"
#     },
#     "Bulldog": {
#         "peso": "18 a 25 kg",
#         "tamanho": "30 a 40 cm",
#         "pelos": "Curto",
#         "temperamento": "Agressivo",
#         "imagem": "bulldog.png"
#     }
#     # Adicione mais raças conforme necessário
# }
#
# class App:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Cadastro PET SHOP")
#
#         # Criação do Notebook para as abas
#         self.notebook = ttk.Notebook(self.root)
#         self.notebook.grid(row=0, column=0, sticky='nsew')  # Usando grid para o Notebook
#
#         # Criação da aba_config
#         self.aba_config = ttk.Frame(self.notebook)
#         self.notebook.add(self.aba_config, text='Configuração')
#
#         # Combobox de Raça
#         self.combobox_raca = ttk.Combobox(self.aba_config, values=list(caracteristicas_racas.keys()))
#         self.combobox_raca.grid(row=0, column=0, padx=10, pady=10)
#         self.combobox_raca.bind("<<ComboboxSelected>>", self.atualizar_caracteristicas)
#
#         # Campo de texto para características
#         self.texto_caracteristicas = tk.Text(self.aba_config, height=10, width=50)
#         self.texto_caracteristicas.grid(row=1, column=0, padx=10, pady=10)  # Mudado para row=1, column=0
#
#         # Configuração de expansão
#         self.root.grid_rowconfigure(0, weight=1)
#         self.root.grid_columnconfigure(0, weight=1)
#
#     def atualizar_caracteristicas(self, event):
#         raca_selecionada = self.combobox_raca.get()
#         if raca_selecionada in caracteristicas_racas:
#             info = caracteristicas_racas[raca_selecionada]
#             self.texto_caracteristicas.delete(1.0, tk.END)  # Limpa o campo de texto
#             self.texto_caracteristicas.insert(tk.END, f"Peso: {info['peso']}\n")
#             self.texto_caracteristicas.insert(tk.END, f"Tamanho: {info['tamanho']}\n")
#             self.texto_caracteristicas.insert(tk.END, f"Pelos: {info['pelos']}\n")
#             self.texto_caracteristicas.insert(tk.END, f"Temperamento: {info['temperamento']}")
#
#
#
# # ADICIONANDO CARACTERÍSTICAS DO PET
#
#
#
#
#
#'
#
# # Funções para atualizar imagens
# def update_porte_image(event=None):
#     porte = var_porte.get().strip()
#     image_path = os.path.join(base_path, imagens_portes.get(porte, ''))
#     if os.path.exists(image_path):
#         img = Image.open(image_path).resize((200, 200))
#         img_tk = ImageTk.PhotoImage(img)
#         label_imagem.config(image=img_tk)
#         label_imagem.image = img_tk
#     else:
#         label_imagem.config(text="Imagem do porte não encontrada", image="")
#         label_imagem.image = None
#

# # Função para atualizar a lista de raças
# def atualizar_lista_racas(event=None):
#     porte = var_porte.get().strip()
#     print(f"Selecionado Porte: {porte}")  # Debug
#     time.sleep(0.5)  # Pausa para garantir atualização
#
#     #racas = dados_pet.get(porte, {}).get("raças", [])
#     racas = list(dados_pet.get(porte, {}).get("raças", [])) # Capitalize para correspondência
#     combobox_raca["values"] = racas
#     combobox_raca.set("Selecione uma raça")
#     update_porte_image(event)
#
#     if racas:
#         combobox_raca.set(racas[0])  # Define a primeira raça como padrão
#         update_raca_image()  # Atualiza a imagem da raça assim que uma raça é definida
#     else:
#         combobox_raca.set("Nenhuma raça disponível")

# Função para atualizar a imagem da raça
# def update_raca_image(event=None):
#     #raca = combobox_raca.get().strip()
#     raca = var_raca.get().strip()
#     image_path = os.path.join(base_path, imagens_racas.get(raca, ''))
#     print(f"Selecionado Raça: {raca}")  # Debug
#     print(f"Imagem do porte em: {image_path}")  # Debug
#     time.sleep(0.9)  # Pausa para garantir que a variável foi atualizada
#
#     # Verifique se o nome do arquivo não está vazio
#     if not imagens_racas.get(raca):
#         print(f"Nome do arquivo não encontrado para a raça: {raca}")  # Debug
#         time.sleep(0.9)  # Pausa para garantir que a variável foi atualizada
#         label_imagem.config(text="Imagem da raça não encontrada", image="")
#         time.sleep(0.5)  # Pausa para garantir que a variável foi atualizada
#         label_imagem.image = None
#         return
#
#     print(f"Imagem do porte em: {image_path}")  # Debug
#
#     if os.path.exists(image_path):
#         img = Image.open(image_path).resize((200, 200))
#         img_tk = ImageTk.PhotoImage(img)
#         label_imagem.config(image=img_tk)
#         label_imagem.image = img_tk
#     else:
#         label_imagem.config(text="Imagem da raça não encontrada", image="")
#         label_imagem.image = None
#         #     except Exception as e:
#         #     print(f"Erro ao carregar imagem da raça: {e}")
#         # else:
#         label_imagem.config(text="Imagem não encontrada", image="")
#         label_imagem.image = None
#
#
# # Criando Combobox para seleção de porte
# ttk.Label(aba_config, text="Selecione o Porte:").grid(row=0, column=0, padx=10, pady=5)
# combobox_porte = ttk.Combobox(aba_config, textvariable=var_porte, values=list(dados_pet.keys()), state="readonly")
# combobox_porte.grid(row=1, column=0, padx=10, pady=5)
# combobox_porte.bind("<<ComboboxSelected>>", lambda event: [atualizar_lista_racas(event), update_porte_image(event)])
#
#
#
# # Criando Combobox para seleção de raça
# ttk.Label(aba_config, text="Selecione a Raça:").grid(row=0, column=1, padx=10, pady=5, sticky="w")
# combobox_raca = ttk.Combobox(aba_config, textvariable=var_raca, state="readonly")
# combobox_raca.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
# combobox_raca.bind("<<ComboboxSelected>>", update_raca_image)
#
#
# # Configurando a coluna para expandir
# aba_config.grid_columnconfigure(0, weight=1)
#
# combobox_raca.bind("<<ComboboxSelected>>", update_raca_image)
#
#
#
# # Criando Label para exibir imagens
# label_imagem = tk.Label(aba_config, text="Nenhuma imagem disponível", width=180, height=180)
# label_imagem.grid(row=2, column=0, columnspan=4, padx=10, pady=10)


# Adicionando `trace_add` para ativar automaticamente a atualização da imagem e das raças
# var_porte.trace_add("write":, lambda *args: atualizar_lista_racas(event=None))
# var_porte.trace_add("write", lambda *args: update_porte_image(event=None))


# # Criando o frame principal para dados cadastrais
# frame_cadastro = ttk.LabelFrame(inner_frame, text="Dados Cadastrais")
# frame_cadastro.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")
