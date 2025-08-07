from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry  # Certifique-se de ter o pacote instalado: pip install tkcalendar
import os
from db_models import Tutor
from database import database
from modulos.aba_som import som_e_expressao_acao
from utilitarios import caminho_arquivo

logo_splash = caminho_arquivo("splash.png", subpasta=os.path.join("..", "..", "imagensipojucao"))
som_relatorio = caminho_arquivo("relatorio_finalizado.mp3", subpasta="sons")

def montar_aba_consulta(aba_consulta, inner_frame):
    frame = ttk.LabelFrame(aba_consulta, text="Consulta Avançada com Período")
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    var_nome = tk.StringVar()
    var_cpf = tk.StringVar()

    ttk.Label(frame, text="Nome contém:").grid(row=0, column=0, sticky="w")
    entry_nome = ttk.Entry(frame, textvariable=var_nome, width=30)
    entry_nome.grid(row=0, column=1, sticky="w")

    ttk.Label(frame, text="CPF contém:").grid(row=1, column=0, sticky="w")
    entry_cpf = ttk.Entry(frame, textvariable=var_cpf, width=30)
    entry_cpf.grid(row=1, column=1, sticky="w")

    ttk.Label(frame, text="De:").grid(row=2, column=0, sticky="w")
    entry_data_inicio = DateEntry(frame, date_pattern="dd/mm/yyyy", width=12)
    entry_data_inicio.grid(row=2, column=1, sticky="w")

    ttk.Label(frame, text="Até:").grid(row=3, column=0, sticky="w")
    entry_data_fim = DateEntry(frame, date_pattern="dd/mm/yyyy", width=12)
    entry_data_fim.grid(row=3, column=1, sticky="w")

    tree = ttk.Treeview(frame, columns=("id", "nome", "cpf", "cadastro"), show="headings", height=12)
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("cpf", text="CPF")
    tree.heading("cadastro", text="Cadastro")
    tree.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

    def consultar():
        tree.delete(*tree.get_children())
        nome_filtro = var_nome.get().strip()
        cpf_filtro = var_cpf.get().strip()
        data_inicio = datetime.strptime(entry_data_inicio.get(), "%d/%m/%Y")
        data_fim = datetime.strptime(entry_data_fim.get(), "%d/%m/%Y")

        query = database.session.query(Tutor)
        if nome_filtro:
            query = query.filter(Tutor.nome.ilike(f"%{nome_filtro}%"))
        if cpf_filtro:
            query = query.filter(Tutor.cpf.ilike(f"%{cpf_filtro}%"))
        query = query.filter(Tutor.data_cadastro >= data_inicio)
        query = query.filter(Tutor.data_cadastro <= data_fim)

        resultados = query.all()
        for r in resultados:
            data_formatada = r.data_cadastro.strftime("%d/%m/%Y")
            tree.insert("", "end", values=(r.id, r.nome, r.cpf, data_formatada))

        som_e_expressao_acao("buscar")

    def limpar():
        var_nome.set("")
        var_cpf.set("")
        tree.delete(*tree.get_children())

    ttk.Button(frame, text="🔎 Consultar", command=consultar).grid(row=4, column=1, sticky="e", pady=5)
    ttk.Button(frame, text="🧹 Limpar", command=limpar).grid(row=4, column=0, sticky="w", pady=5)





















# from dados_compartilhados import var_raca, caracteristicas_racas
# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# import os
# import time
# import matplotlib
# import pandas as pd
# import matplotlib.pyplot as plt
# from aba_som import tocar_som, alternar_som_estado
# # import pygame
# # pygame.mixer.init()
#
# # Abaixo: ABA CONSULTA ALTERADA EM 22/07/2025 22:26 HS. VERIFICAR O QUE FICA DA ANTIGA
#
# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# import os
# from aba_som import tocar_som  # você pode incluir alternar_som_estado se quiser
#
# # 🐾 Lista simulada de pets cadastrados (substitua por acesso real)
# from dados_compartilhados import pets_cadastrados  # deve ser uma lista de dicionários com ID e dados
#
# def montar_aba_consulta(aba):
#     aba.grid_columnconfigure(0, weight=1)
#     aba.grid_rowconfigure(1, weight=1)
#
#     tocar_som("som/som_consulta.mp3")  # Som ao abrir a aba
#
#     # 🔍 Filtro
#     tk.Label(aba, text="Buscar por:", font=("Segoe UI", 11)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
#     filtro_tipo = ttk.Combobox(aba, values=["Nome do Pet", "CPF Tutor", "Celular Tutor"], state="readonly", width=20)
#     filtro_tipo.grid(row=0, column=1, padx=10, pady=5)
#     filtro_tipo.set("Nome do Pet")
#
#     entrada_busca = tk.Entry(aba, width=30)
#     entrada_busca.grid(row=0, column=2, padx=10, pady=5)
#
#     btn_buscar = ttk.Button(aba, text="🔎 Buscar", command=lambda: buscar_pet(filtro_tipo.get(), entrada_busca.get(), frame_resultados))
#     btn_buscar.grid(row=0, column=3, padx=10, pady=5)
#
#     # 🔁 Frame rolável
#     canvas = tk.Canvas(aba)
#     scrollbar = ttk.Scrollbar(aba, orient="vertical", command=canvas.yview)
#     canvas.configure(yscrollcommand=scrollbar.set)
#     canvas.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
#     scrollbar.grid(row=1, column=4, sticky="ns")
#
#     frame_resultados = ttk.Frame(canvas)
#     canvas.create_window((0, 0), window=frame_resultados, anchor="nw")
#
#     def ajustar_scroll(event):
#         canvas.configure(scrollregion=canvas.bbox("all"))
#     frame_resultados.bind("<Configure>", ajustar_scroll)
#
# def buscar_pet(filtro, valor, frame_resultados):
#     from dados_compartilhados import pets_cadastrados  # caso você atualize em tempo real
#     tocar_som("som/som_busca.mp3")  # Som ao buscar
#
#     from mascote import mostrar_mascote_expressivo
#
#     mostrar_mascote_expressivo(janela, expressao="anotando")
#     mostrar_mascote_expressivo(janela, expressao="triste")  # ou "negativo" se preferir
#
#
#
#     for widget in frame_resultados.winfo_children():
#         widget.destroy()
#
#     valor = valor.strip().lower()
#     resultados = []
#
#     # 🔎 Filtragem
#     for pet in pets_cadastrados:
#         if filtro == "Nome do Pet" and pet["nome"].lower() == valor:
#             resultados.append(pet)
#         elif filtro == "CPF Tutor" and pet["cpf_tutor"].lower() == valor:
#             resultados.append(pet)
#         elif filtro == "Celular Tutor" and pet["celular_tutor"].lower() == valor:
#             resultados.append(pet)
#
#     if not resultados:
#         tk.Label(frame_resultados, text="❌ Nenhum resultado encontrado.", font=("Segoe UI", 11)).pack(pady=10)
#         return
#
#     # 🎯 Exibição múltipla se houver nomes repetidos
#     for i, pet in enumerate(resultados):
#         frame_pet = ttk.LabelFrame(frame_resultados, text=f"PET {pet['id']} - {pet['nome']}", padding=10)
#         frame_pet.grid(row=i, column=0, padx=10, pady=10, sticky="ew")
#
#         # 📋 Dados principais
#         dados = f"""
# 🐶 Nome: {pet['nome']}
# 📏 Porte: {pet['porte']}
# 🧬 Raça: {pet['raca']}
# 👤 Tutor: {pet['tutor']}
# 📞 Celular: {pet['celular_tutor']}
# 🧾 CPF: {pet['cpf_tutor']}
# """
#         tk.Label(frame_pet, text=dados.strip(), justify="left", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w")
#
#         # 📸 Imagem PET
#         caminho_pet = f"imagensipojucao/pets/pet_{pet['id']}.jpg"
#         if os.path.exists(caminho_pet):
#             img_pet = Image.open(caminho_pet).resize((130, 130))
#             img_pet_tk = ImageTk.PhotoImage(img_pet)
#             lbl_pet = tk.Label(frame_pet, image=img_pet_tk)
#             lbl_pet.image = img_pet_tk
#             lbl_pet.grid(row=0, column=1, padx=10)
#         else:
#             tk.Label(frame_pet, text="(Sem imagem do PET)").grid(row=0, column=1)
#
#         # 👤 Imagem Tutor
#         caminho_tutor = f"imagensipojucao/tutores/tutor_{pet['id']}.jpg"
#         if os.path.exists(caminho_tutor):
#             img_tutor = Image.open(caminho_tutor).resize((110, 110))
#             img_tutor_tk = ImageTk.PhotoImage(img_tutor)
#             lbl_tutor = tk.Label(frame_pet, image=img_tutor_tk)
#             lbl_tutor.image = img_tutor_tk
#             lbl_tutor.grid(row=0, column=2, padx=10)
#         else:
#             tk.Label(frame_pet, text="(Sem imagem do Tutor)").grid(row=0, column=2)
#
#
#
#
# # # Acima: ABA CONSULTA ALTERADA EM 22/07/2025 22:26 HS. VERIFICAR O QUE FICA DA ANTIGA
#
#
#
#
#
#
#
#
#
#
#
# from aba_som import musica_consulta_pet
# musica_consulta_pet()
# mostrar_mascote_expressivo(janela, "beijo")
#
# import dados_compartilhados as dc # var_porte, var_raca, dados_pet, imagens_racas, imagens_portes
# def consulta_dados_banho_preco():
#     porte = dc.var_porte.get()
#     preco_banho = dc.dados_pet.get(porte, {}).get("preços", {}).get("Banho", 0)
#     print(f"Banho para porte {porte} custa R$ {preco_banho}")
#
# #info = caracteristicas_racas.get(dc.var_raca.get(), {})
#
# import tkinter as tk
# from tkinter import ttk
# import dados_compartilhados as dc  # Importe o que precisar de forma compartilhada
#
# def montar_aba_consulta(aba):
#     # Permitir expansão
#     aba.grid_rowconfigure(0, weight=1)
#     aba.grid_columnconfigure(0, weight=1)
#
#     # Canvas + Scrollbar
#     canvas = tk.Canvas(aba)
#     scrollbar_y = ttk.Scrollbar(aba, orient="vertical", command=canvas.yview)
#     canvas.configure(yscrollcommand=scrollbar_y.set)
#
#     canvas.grid(row=0, column=0, sticky="nsew")
#     scrollbar_y.grid(row=0, column=1, sticky="ns")
#
#     # Frame rolável
#     inner_frame = ttk.Frame(canvas)
#     canvas.create_window((0, 0), window=inner_frame, anchor="nw")
#
#     def ajustar_scroll(event):
#         canvas.configure(scrollregion=canvas.bbox("all"))
#     inner_frame.bind("<Configure>", ajustar_scroll)
#
#     # === A partir daqui, crie widgets dentro do inner_frame ===
#
#     # Exemplo básico
#     frame_exemplo = ttk.LabelFrame(inner_frame, text="Seção de Exemplo")
#     frame_exemplo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#
#     ttk.Label(frame_exemplo, text="Alguma informação importante").grid(row=0, column=0, sticky="w")
#
#     # Repita quantos blocos quiser (outros frames, grids, entradas, etc.)
#
#     # Se quiser ativar algo quando o porte mudar
#     dc.var_porte.trace_add("write", lambda *args: atualizar_exemplo())
#
# def atualizar_exemplo():
#     porte = dc.var_porte.get()
#     print(f"Porte selecionado na aba é: {porte}")
#
# # ABAIXO MODELO DE FILTRO POR CPF OU CELULAR.
# tk.Label(aba, text="🔎 Buscar por:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
# filtro_tipo = ttk.Combobox(aba, values=["Nome do Pet", "CPF Tutor", "Celular Tutor"], state="readonly")
# filtro_tipo.grid(row=0, column=1, padx=10, pady=5)
# filtro_tipo.set("Nome do Pet")
#
# entrada_busca = tk.Entry(aba)
# entrada_busca.grid(row=0, column=2, padx=10, pady=5)
#
# btn_buscar = ttk.Button(aba, text="Buscar", command=lambda: buscar_pet(filtro_tipo.get(), entrada_busca.get()))
# btn_buscar.grid(row=0, column=3, padx=10)
#
# # ACIMA MODELO DE FILTRO POR CPF OU CELULAR
#
# # def montar_aba_consulta(frame_base):
# #     # Cria widgets dentro do frame_base
# #     # === Scrollable frame ===
# #     # Criação do canvas e da scrollbar
# #     canvas = tk.Canvas(inner_frame)
# #     scrollbar_y = ttk.Scrollbar(inner_frame, orient="vertical", command=canvas.yview)
# #     canvas.configure(yscrollcommand=scrollbar_y.set)
# #
# #     # Posicionamento usando
# #     canvas.grid(row=0, column=0, sticky="nsew")  # Ocupa toda a célula
# #     scrollbar_y.grid(row=0, column=1, sticky="ns")  # Fica ao lado do canvas, altura total
# #
# #     # Frame interno rolável
# #     scrollable_frame = ttk.Frame(canvas)
# #     canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# #
# #     # Atualiza o scrollregion automaticamente
# #     scrollable_frame.bind(
# #         "<Configure>",
# #         lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
# #     )
#
#
# # CONSULTA CONSULTA CONSULTA
#
# def criar_frame_consulta(parent):
#     frame_consulta = ttk.LabelFrame(parent, text="Informações Sobre o PET")
#     frame_consulta.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
#
#     frame_consulta = ttk.LabelFrame(inner_frame, text="Consultando PET")
#     frame_consulta.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
#
#     import dados_compartilhados as dc
#
#     def tocar_musica_consulta_pet():
#         caminho = os.path.join("som", "musica_consulta_pet.mp3")
#         #threading.Thread(target=playsound, args=(caminho,), daemon=True).start() #Somente se for usas pacote playsound
#         tocar_som(caminho)
#         # preenche campos como nome, idade, etc...
#         tocar_musica_consulta_pet()
#
#     def mostrar_imagem_pet(frame):
#         caminho_imagem_pet = os.path.join("imagens/pets", "pet_exemplo.jpg")  # Substitua por PET dinâmico
#         if os.path.exists(caminho_imagem_pet):
#             img = Image.open(caminho_imagem_pet).resize((150, 150))
#             img_tk = ImageTk.PhotoImage(img)
#             label_img_pet = tk.Label(frame, image=img_tk)
#             label_img_pet.image = img_tk
#             label_img_pet.grid(row=0, column=5, padx=10, pady=10, sticky='ne')
#
#     def mostrar_imagem_tutor(frame, tutor_id, linha, coluna):
#         caminho_imagem_tutor = os.path.join("imagens/tutores", f"tutor_{tutor_id}.jpg")
#         if os.path.exists(caminho_imagem_tutor):
#             img = Image.open(caminho_imagem_tutor).resize((60, 60))
#             img_tk = ImageTk.PhotoImage(img)
#             label_img_tutor = tk.Label(frame, image=img_tk)
#             label_img_tutor.image = img_tk
#             label_img_tutor.grid(row=linha, column=coluna, padx=5, pady=5, sticky='w')
#
#             mostrar_imagem_tutor(frame_consulta, tutor_id=1, linha=4, coluna=2)
#             mostrar_imagem_tutor(frame_consulta, tutor_id=2, linha=7, coluna=2)
#
# # 📌 Etapa 4: Exibição dinâmica na aba_consulta
#     # Na , use o ID ou nome do PET/tutor consultado para buscar e carregar a imagem com:
#
#     def exibir_imagem_consulta(tipo, id_ref, frame_destino):
#         pasta = "pets" if tipo == "pet" else "tutores"  📌📌📌📌📌📌 # alterar para nome correto das pastas 📌📌📌📌
#         caminho = os.path.join("imagens", pasta, f"{tipo}_{id_ref}.jpg")
#         if os.path.exists(caminho):
#             img = Image.open(caminho).resize((150, 150))
#             img_tk = ImageTk.PhotoImage(img)
#             label = tk.Label(frame_destino, image=img_tk)
#             label.image = img_tk
#             label.grid(row=0, column=5)
#
#     def atualizar_porte_precos():
#         porte = dc.var_porte.get()
#         preco_banho = dc.dados_pet.get(porte, {}).get("preços", {}).get("Banho", 0)
#         print(f"Banho para porte {porte} custa R$ {preco_banho}")
#
# # (ABAIXO)  VERIFICAR SE ESTÁ NA ORDEM DE CHAMADA CORRETA ESTE CÓDIGO:
#
# from PIL import ImageTk, Image
# import os
#
# def exibir_imagem(tipo, id_unico, frame_destino):
#     caminho = f"imagensipojucao/{'pets' if tipo == 'pet' else 'tutores'}/{tipo}_{id_unico}.jpg"
#     if os.path.exists(caminho):
#         img = Image.open(caminho).resize((160, 160))
#         img_tk = ImageTk.PhotoImage(img)
#         label_img = tk.Label(frame_destino, image=img_tk)
#         label_img.image = img_tk  # manter referência
#         label_img.pack(pady=5)
#     else:
#         tk.Label(frame_destino, text="Sem imagem")
#
# # (ABAIXO)  VERIFICAR SE ESTÁ NA ORDEM DE CHAMADA CORRETA ESTE CÓDIGO:
#
#     # nome Pet
#     frame_nome_pet = ttk.LabelFrame(frame_consulta, text="Nome do Pet", anchor='w')
#     frame_nome_pet.grid(row=1, column=0, padx=10, pady=10, sticky='w')
#     entry_nome = tk.Entry(frame_consulta)
#     entry_nome.grid(row=1, column=1, columnspan=4, pady=1, sticky='nsew')
#
#     # idade
#     frame_idadedopetanos = ttk.LabelFrame(frame_consulta, text="Idade Anos")
#     frame_idadedopetanos.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
#     entry_idadedopetanos = tk.Entry(frame_consulta)
#     entry_idadedopetanos.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
#
#     frame_idadedopetmeses = ttk.LabelFrame(frame_consulta, text="Meses")
#     frame_idadedopetmeses.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')
#     entry_idadedopetmeses = tk.Entry(frame_consulta)
#     entry_idadedopetmeses.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')
#
#     # Tutor 1
#     frame_tutor1 = ttk.LabelFrame(frame_consulta, text="Tutor 1", anchor='e')
#     frame_tutor1.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')
#     entry_tutor_1 = tk.Entry(frame_consulta)
#     entry_tutor_1.grid(row=4, column=1, padx=10, pady=10, sticky='nsew')
#
#     # telefone1
#     frame_telefone_1 = ttk.LabelFrame(frame_consulta, text="Telefone Tutor 1", anchor='e')
#     frame_telefone_1.grid(row=5, column=0, padx=10, pady=10, sticky='e')
#     entry_telefone_1 = tk.Entry(frame_consulta)
#     entry_telefone_1.grid(row=5, column=1, padx=10, pady=10, sticky='nsew')
#     # email Tutor1
#     frame_email_tutor_1 = ttk.LabelFrame(frame_consulta, text="email Tutor 1", anchor='e')
#     frame_email_tutor_1.grid(row=6, column=0, padx=10, pady=10, sticky='e')
#     entry_email_tutor_1 = tk.Entry(frame_consulta)
#     entry_email_tutor_1.grid(row=6, column=1, padx=10, pady=10, sticky='nsew')
#
#     # tutor 2
#     frame_tutor2 = ttk.LabelFrame(frame_consulta, text="Tutor 2", anchor='e')
#     frame_tutor2.grid(row=7, column=0, padx=10, pady=10, sticky='nsew')
#     # Campo de entrada (Entry)
#     entry_tutor_2 = tk.Entry(frame_consulta)
#     entry_tutor_2.grid(row=7, column=1, padx=10, pady=10, sticky='nsew')
#
#     # telefone 2
#     frame_telefone_2 = ttk.LabelFrame(frame_consulta, text="Telefone Tutor 2", anchor='e')
#     frame_telefone_2.grid(row=8, column=0, padx=10, pady=10, sticky='nsew')
#     # Campo de entrada (Entry)
#     entry_telefone_2 = tk.Entry(frame_consulta)
#     entry_telefone_2.grid(row=8, column=1, padx=10, pady=10, sticky='nsew')
#     frame_telefone_2a = ttk.LabelFrame(frame_consulta, text="Telefone_a", borderwidth=1, relief='solid')
#     entry_telefone_2a = tk.Entry(inner_frame)
#     entry_telefone_2a.grid(row=9, column=0, padx=10, pady=10, sticky='nsew')
#
#     # email Tutor2
#     frame_email_tutor_2 = ttk.LabelFrame(frame_consulta, text="email Tutor 2", anchor='e')
#     frame_email_tutor_2.grid(row=9, column=1, padx=10, pady=10, sticky='e')
#     entry_email_tutor_2 = tk.Entry(frame_consulta)
#     entry_email_tutor_2.grid(row=10, column=0, padx=10, pady=10, sticky='nsew')
#
#     # Criando um Frame para Endereço e Observações
#     logradouro = ttk.LabelFrame(frame_consulta, text="Endereço e Observações")
#     # logradouro.config(height=170)  # Define a altura manualmente
#     logradouro.grid(row=13, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")
#     # frame_logradouro.grid_propagate(False)  # Impede que os widgets internos alterem o tamanho do frame
#
#     # Endereço Logradouro
#     frame_enderecopet = ttk.LabelFrame(frame_consulta, text="Endereço", anchor='e')
#     frame_enderecopet.grid(row=14, column=0, padx=10, pady=10, sticky='nsew')
#     # Campo de entrada (Entry)
#     entry_enderecopet = tk.Entry(frame_consulta)
#     entry_enderecopet.grid(row=14, column=1, padx=10, pady=10, sticky='nsew', columnspan=6)
#     # entry_nome.grid(row=1, column=0, columnspan=4, pady=1, sticky='nsew')
#
#     # endereço Número
#     frame_endereconumero = ttk.LabelFrame(frame_consulta, text="Número", anchor='e')
#     frame_endereconumero.grid(row=15, column=0, padx=10, pady=10, sticky='nsew')
#     # Campo de entrada (Entry)
#     entry_endereconumero = tk.Entry(frame_consulta)
#     entry_endereconumero.grid(row=15, column=1, padx=10, pady=10, sticky='nsew')
# qua
#     # Endereço Complemento
#     ttk.Label(frame_endereco, text="Complemento").grid(row=15, column=2, padx=10, pady=10, sticky='nsew')
#     # Campo de entrada (Entry)
#     entry_enderecocomplemento = ttk.Entry(frame_endereco)
#     entry_enderecocomplemento.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
#
#     frame_recomendacoes = ttk.LabelFrameFrame(frame_consulta, text="Recomendações", borderwidth=1, relief='solid')
#     frame_recomendacoes.grid(row=20, column=0, columnspan=4, padx=10, pady=5, sticky="w")
#
#     # Observações sobre o PET
#     frame_recomendacoes = ttk.LabelFrame(frame_consulta, text="Recomendações Sobre o pet", borderwidth=1,
#                                          relief='solid')
#     frame_recomendacoes.grid(row=21, column=0, columnspan=5, padx=10, pady=10, sticky='nsew')
#     # Campo de entrada (Entry)
#     campo_observacoes = tk.Text(frame_consulta, width=80, height=12, borderwidth=2, relief='solid')
#     campo_observacoes.grid(row=30, column=0, columnspan=6, padx=10, pady=10)
# 
#
