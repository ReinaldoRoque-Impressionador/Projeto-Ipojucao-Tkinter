import tkinter as tk
from tkinter import ttk, messagebox

from cliente_utils import (
    salvar_ou_atualizar_cliente,
    buscar_clientes_por_nome,
    excluir_cliente_por_id
)
from db_models import Tutor
from database import database
from modulos.aba_som import som_e_expressao_acao
from modulos import dados_compartilhados as dc
from modulos.utilitarios import caminho_arquivo

logo_splash = caminho_arquivo("splash.png", subpasta=os.path.join("..", "..", "imagensipojucao"))
som_relatorio = caminho_arquivo("relatorio_finalizado.mp3", subpasta="sons")

def montar_aba_clientes(aba_clientes, inner_frame):
    frame = ttk.LabelFrame(aba_clientes, text="Cadastro de Clientes")
    frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    var_id = tk.StringVar()
    var_nome = tk.StringVar()
    var_cpf = tk.StringVar()

    # Campos
    ttk.Label(frame, text="ID:").grid(row=0, column=0, sticky="w")
    entry_id = ttk.Entry(frame, textvariable=var_id, state="readonly", width=10)
    entry_id.grid(row=0, column=1, sticky="w")

    ttk.Label(frame, text="Nome:").grid(row=1, column=0, sticky="w")
    entry_nome = ttk.Entry(frame, textvariable=var_nome, width=40)
    entry_nome.grid(row=1, column=1, sticky="w")

    ttk.Label(frame, text="CPF:").grid(row=2, column=0, sticky="w")
    entry_cpf = ttk.Entry(frame, textvariable=var_cpf, width=30)
    entry_cpf.grid(row=2, column=1, sticky="w")

    # Tabela
    tree = ttk.Treeview(frame, columns=("id", "nome", "cpf"), show="headings", height=10)
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("cpf", text="CPF")
    tree.grid(row=6, column=0, columnspan=3, padx=5, pady=10)

    def carregar_clientes():
        tree.delete(*tree.get_children())
        clientes = database.session.query(Tutor).all()
        for c in clientes:
            tree.insert("", "end", values=(c.id, c.nome, c.cpf))

    def salvar_cliente():
        nome = var_nome.get().strip()
        cpf = var_cpf.get().strip()
        resultado = salvar_ou_atualizar_cliente(var_id.get(), nome, cpf)
        messagebox.showinfo("Resultado", resultado)
        som_e_expressao_acao("salvar")
        carregar_clientes()
        limpar_campos()

    def excluir_cliente():
        item = tree.selection()
        if not item:
            messagebox.showwarning("Selecione", "Escolha um cliente na lista.")
            return
        id_sel = int(tree.item(item[0], "values")[0])
        resultado = excluir_cliente_por_id(id_sel)
        messagebox.showinfo("Resultado", resultado)
        som_e_expressao_acao("excluir")
        carregar_clientes()
        limpar_campos()

    def editar_cliente():
        item = tree.selection()
        if not item:
            messagebox.showwarning("Selecione", "Escolha um cliente na lista.")
            return
        id_sel, nome_sel, cpf_sel = tree.item(item[0], "values")
        var_id.set(id_sel)
        var_nome.set(nome_sel)
        var_cpf.set(cpf_sel)
        som_e_expressao_acao("editar")

    def buscar_clientes():
        termo = var_nome.get().strip()
        tree.delete(*tree.get_children())
        resultados = buscar_clientes_por_nome(termo)
        for r in resultados:
            tree.insert("", "end", values=(r.id, r.nome, r.cpf))
        som_e_expressao_acao("buscar")

    def limpar_campos():
        var_id.set("")
        var_nome.set("")
        var_cpf.set("")

    # Botões
    ttk.Button(frame, text="Salvar", command=salvar_cliente).grid(row=3, column=1, sticky="e", pady=5)
    ttk.Button(frame, text="Buscar por Nome", command=buscar_clientes).grid(row=3, column=0, sticky="w", pady=5)
    ttk.Button(frame, text="Editar Selecionado", command=editar_cliente).grid(row=4, column=0, sticky="w", pady=5)
    ttk.Button(frame, text="🗑 Excluir Selecionado", command=excluir_cliente).grid(row=4, column=1, sticky="e", pady=5)
    ttk.Button(frame, text="🧹 Limpar Campos", command=limpar_campos).grid(row=5, column=1, sticky="e", pady=5)

    carregar_clientes()


def rodape_imagem(frame_pai):
    caminho_img = os.path.join("imagensipojucao", "rodape", "footer.png")
    if os.path.exists(caminho_img):
        img = Image.open(caminho_img).resize((1000, 80))
        img_tk = ImageTk.PhotoImage(img)
        rodape = tk.Label(frame_pai, image=img_tk)
        rodape.image = img_tk  # mantém referência da imagem

        # Posiciona no final da grid
        rodape.grid(row=999, column=0, columnspan=999, sticky="ew")  # usa row "alta" para evitar conflito
    else:
        print("Imagem do rodapé não encontrada.")

#barra_audio(frame_aba_clientes)  # ou frame_aba_menu, frame_aba_config, etc.







# from tkinter import ttk, messagebox
# import tkinter as tk
# #from models import salvar_cliente  # Certifique-se de importar a função correta
# from db_models import salvar_cliente
# # import pygame
# # pygame.mixer.init()
#
# from aba_clientes import montar_aba_clientes
# from aba_som import tocar_som, alternar_som_estado
#
# from cliente_utils import salvar_ou_atualizar_cliente
# from aba_som import som_e_expressao_acao
#
#
# from aba_som import clair_de_lune
# clair_de_lune()
#
#
#
# # aba_clientes.py
#
# from tkinter import Frame, Label, Entry, Button, messagebox
# from db_models import Tutor  # importa os modelos que precisa
# from database import database  # para realizar commits
# from flask import Flask
#
# # ABA CLIENTES NOVA EM 24/07/2025
# #================================
# #================================
# import tkinter as tk
# from tkinter import ttk, messagebox
# from db_models import Tutor  # Modelo Tutor do SQLAlchemy
# from database import database
#
#
# def montar_aba_clientes(aba):
#     frame = ttk.LabelFrame(aba, text="Cadastro de Clientes")
#     frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#
#     # Variáveis
#     var_id = tk.StringVar()
#     var_nome = tk.StringVar()
#     var_cpf = tk.StringVar()
#
#     # Campos
#     ttk.Label(frame, text="ID:").grid(row=0, column=0, sticky="w")
#     entry_id = ttk.Entry(frame, textvariable=var_id, state="readonly", width=10)
#     entry_id.grid(row=0, column=1, sticky="w")
#
#     ttk.Label(frame, text="Nome:").grid(row=1, column=0, sticky="w")
#     entry_nome = ttk.Entry(frame, textvariable=var_nome, width=40)
#     entry_nome.grid(row=1, column=1, sticky="w")
#
#     ttk.Label(frame, text="CPF:").grid(row=2, column=0, sticky="w")
#     entry_cpf = ttk.Entry(frame, textvariable=var_cpf, width=30)
#     entry_cpf.grid(row=2, column=1, sticky="w")
#
#     # Tabela
#     tree = ttk.Treeview(frame, columns=("id", "nome", "cpf"), show="headings", height=10)
#     tree.heading("id", text="ID")
#     tree.heading("nome", text="Nome")
#     tree.heading("cpf", text="CPF")
#     tree.grid(row=6, column=0, columnspan=3, padx=5, pady=10)
#
#     def carregar_clientes():
#         tree.delete(*tree.get_children())
#         clientes = database.session.query(Tutor).all()
#         for c in clientes:
#             tree.insert("", "end", values=(c.id, c.nome, c.cpf))
#
#     carregar_clientes()
#
#     from cliente_utils import salvar_ou_atualizar_cliente
#     from aba_som import som_e_expressao_acao
#
#     def salvar_cliente():
#         nome = var_nome.get().strip()
#         cpf = var_cpf.get().strip()
#         resultado = salvar_ou_atualizar_cliente(var_id.get(), nome, cpf)
#         messagebox.showinfo("Resultado", resultado)
#         som_e_expressao_acao("salvar")
#         carregar_clientes()
#         limpar_campos()

    # def salvar_cliente():
    #     nome = var_nome.get().strip()
    #     cpf = var_cpf.get().strip()
    #
    #     if not nome or not cpf:
    #         messagebox.showwarning("Campos obrigatórios", "Informe nome e CPF.")
    #         return
    #
    #     if var_id.get():  # Atualizar
    #         cliente = database.session.query(Tutor).filter_by(id=int(var_id.get())).first()
    #         if cliente:
    #             cliente.nome = nome
    #             cliente.cpf = cpf
    #             try:
    #                 database.session.commit()
    #                 messagebox.showinfo("Atualizado", "Cliente atualizado com sucesso!")
    #                 limpar_campos()
    #                 carregar_clientes()
    #             except Exception as e:
    #                 database.session.rollback()
    #                 messagebox.showerror("Erro", f"Erro ao atualizar: {e}")
    #         else:
    #             messagebox.showerror("Erro", "Cliente não encontrado.")
    #     else:  # Novo
    #         cliente = Tutor(nome=nome, cpf=cpf)
    #         try:
    #             database.session.add(cliente)
    #             database.session.commit()
    #             messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")
    #             limpar_campos()
    #             carregar_clientes()
    #         except Exception as e:
    #             database.session.rollback()
    #             messagebox.showerror("Erro", f"Erro ao salvar: {e}")
    #
    # def excluir_cliente():
    #     item = tree.selection()
    #     if not item:
    #         messagebox.showwarning("Selecione", "Escolha um cliente na lista.")
    #         return
    #     id_sel = int(tree.item(item[0], "values")[0])
    #     cliente = database.session.query(Tutor).filter_by(id=id_sel).first()
    #     if not cliente:
    #         messagebox.showerror("Erro", "Cliente não encontrado.")
    #         return
    #     if messagebox.askyesno("Confirmação", f"Deseja excluir '{cliente.nome}'?"):
    #         try:
    #             database.session.delete(cliente)
    #             database.session.commit()
    #             messagebox.showinfo("Removido", "Cliente excluído.")
    #             limpar_campos()
    #             carregar_clientes()
    #         except Exception as e:
    #             database.session.rollback()
    #             messagebox.showerror("Erro", f"Erro ao excluir: {e}")
    #
    # def editar_cliente():
    #     item = tree.selection()
    #     if not item:
    #         messagebox.showwarning("Selecione", "Escolha um cliente na lista.")
    #         return
    #     id_sel, nome_sel, cpf_sel = tree.item(item[0], "values")
    #     var_id.set(id_sel)
    #     var_nome.set(nome_sel)
    #     var_cpf.set(cpf_sel)
    #
    # def buscar_clientes():
    #     termo = var_nome.get().strip()
    #     tree.delete(*tree.get_children())
    #     resultados = database.session.query(Tutor).filter(Tutor.nome.ilike(f"%{termo}%")).all()
    #     for r in resultados:
    #         tree.insert("", "end", values=(r.id, r.nome, r.cpf))
    #
    # def limpar_campos():
    #     var_id.set("")
    #     var_nome.set("")
    #     var_cpf.set("")
    #
    # # Botões
    # ttk.Button(frame, text="Salvar", command=salvar_cliente).grid(row=3, column=1, sticky="e", pady=5)
    # ttk.Button(frame, text="Buscar por Nome", command=buscar_clientes).grid(row=3, column=0, sticky="w", pady=5)
    # ttk.Button(frame, text="Editar Selecionado", command=editar_cliente).grid(row=4, column=0, sticky="w", pady=5)
    # ttk.Button(frame, text="🗑 Excluir Selecionado", command=excluir_cliente).grid(row=4, column=1, sticky="e", pady=5)
    # ttk.Button(frame, text="🧹 Limpar Campos", command=limpar_campos).grid(row=5, column=1, sticky="e", pady=5)
#================================
#================================
# ABA CLIENTES NOVA EM 24/07/2025






# ABA CLIENTES EDITADA EM 24/JULHO/2025
# def montar_aba_clientes(app):
#     # Exemplo de aba simples em Tkinter
#     frame = Frame()
#     frame.pack()
#
#     Label(frame, text="Nome do Tutor:").grid(row=0, column=0)
#     entry_nome = Entry(frame)
#     entry_nome.grid(row=0, column=1)
#
#     Label(frame, text="CPF:").grid(row=1, column=0)
#     entry_cpf = Entry(frame)
#     entry_cpf.grid(row=1, column=1)
#
#     def salvar_cliente():
#         nome = entry_nome.get()
#         cpf = entry_cpf.get()
#
#         if not nome or not cpf:
#             messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
#             return
#
#         novo_tutor = Tutor(nome=nome, cpf=cpf)
#         try:
#             with app.app_context():
#                 database.session.add(novo_tutor)
#                 database.session.commit()
#             messagebox.showinfo("Sucesso", "Tutor salvo com sucesso!")
#             entry_nome.delete(0, 'end')
#             entry_cpf.delete(0, 'end')
#         except Exception as e:
#             messagebox.showerror("Erro", f"Não foi possível salvar.\n{e}")
#
#     Button(frame, text="Salvar", command=salvar_cliente).grid(row=2, columnspan=2)
#
#     return frame
#
# aba_clientes = ttk.Frame(notebook)
# notebook.add(aba_clientes, text="Clientes")
# montar_aba_clientes(aba_clientes)
#
# def montar_aba_clientes(aba):
#     frame = ttk.LabelFrame(aba, text="Cadastro de Clientes")
#     frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#
#     ttk.Label(frame, text="Nome do Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
#
#     var_nome = tk.StringVar()
#     entry_nome = ttk.Entry(frame, textvariable=var_nome, width=40)
#     entry_nome.grid(row=0, column=1, padx=5, pady=5, sticky="w")
#
#
#     def tocar_musica_cliente():
#         caminho = os.path.join("som", "clair_de_lune_prelude.mp3")
#         #threading.Thread(target=playsound, args=(caminho,), daemon=True).start()  #Sómente se for usar pacote playsound
#         tocar_som(caminho)
#         # preenche campos como nome, idade, etc...
#         tocar_musica_cliente()
#
#
#     def salvar():
#         nome = var_nome.get().strip()
#         if not nome:
#             messagebox.showwarning("Campo obrigatório", "Por favor, insira o nome do cliente.")
#             return
#
#         sucesso = salvar_cliente(nome)
#         if sucesso:
#             messagebox.showinfo("Salvo com sucesso", f"Cliente '{nome}' foi salvo no banco!")
#             var_nome.set("")  # limpa o campo
#         else:
#             messagebox.showerror("Erro", "Erro ao salvar o cliente.")
#
#     btn_salvar = ttk.Button(frame, text="Salvar Cliente", command=salvar)
#     btn_salvar.grid(row=1, column=1, padx=5, pady=10, sticky="e")
#
#
# tree = ttk.Treeview(frame, columns=("id", "nome", "cpf", "email"), show="headings", height=10)
# tree.heading("id", text="ID")
# tree.heading("nome", text="Nome")
# tree.heading("cpf", text="CPF")
# tree.heading("email", text="E-mail")
#
#
#
#
# def listar_clientes():
#     return session.query(Cliente).all()
#
# def atualizar_cliente(id_cliente, novo_nome):
#     cliente = session.query(Cliente).filter_by(id=id_cliente).first()
#     if cliente:
#         cliente.nome = novo_nome
#         try:
#             session.commit()
#             return True
#         except Exception as e:
#             session.rollback()
#             print("Erro ao atualizar:", e)
#     return False
#
#     # 🔎 Campos de busca
#     ttk.Label(frame, text="Buscar por:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
#     campo_busca = ttk.Combobox(frame, values=["ID", "CPF", "E-mail"], state="readonly")
#     campo_busca.set("CPF")
#     campo_busca.grid(row=2, column=1, sticky="w")
#
#     var_busca = tk.StringVar()
#     entry_busca = ttk.Entry(frame, textvariable=var_busca, width=30)
#     entry_busca.grid(row=2, column=2, padx=5, sticky="w")
#
#     def buscar():
#         resultados = buscar_clientes(campo_busca.get(), var_busca.get())
#         tree.delete(*tree.get_children())
#         for c in resultados:
#             tree.insert("", "end", values=(c.id, c.nome, c.cpf, c.email))
#
#     ttk.Button(frame, text="🔍 Buscar", command=buscar).grid(row=2, column=3, padx=5, pady=5)
#
#     # 🗑 Botão excluir
#     def excluir():
#         item = tree.selection()
#         if not item:
#             messagebox.showwarning("Excluir", "Selecione um cliente.")
#             return
#         id_cliente = int(tree.item(item[0], "values")[0])
#         if messagebox.askyesno("Confirmar exclusão", "Deseja mesmo excluir este cliente?"):
#             if excluir_cliente(id_cliente):
#                 messagebox.showinfo("Excluído", "Cliente removido.")
#                 carregar_clientes()
#             else:
#                 messagebox.showerror("Erro", "Não foi possível excluir.")
#
#     ttk.Button(frame, text="🗑 Excluir Selecionado", command=excluir).grid(row=3, column=2, sticky="e", padx=5, pady=5)
#
#
# app = criar_app()
# with app.app_context():
#     database.create_all()

# ABA CLIENTES EDITADA EM 24/07/2025