# cliente_utils.py

from db_models import Tutor
from database import database
from modulos.dados_compartilhados import usuarios
from modulos.utilitarios import caminho_arquivo

def salvar_ou_atualizar_cliente(id_cliente, nome, cpf):
    if not nome or not cpf:
        return "Campos obrigatórios"

    if id_cliente:
        cliente = database.session.query(Tutor).filter_by(id=int(id_cliente)).first()
        if cliente:
            cliente.nome = nome
            cliente.cpf = cpf
            try:
                database.session.commit()
                return "Cliente atualizado"
            except:
                database.session.rollback()
                return "Erro ao atualizar"
    else:
        novo = Tutor(nome=nome, cpf=cpf)
        try:
            database.session.add(novo)
            database.session.commit()
            return "Cliente salvo"
        except:
            database.session.rollback()
            return "Erro ao salvar"

def excluir_cliente_por_id(id_cliente):
    cliente = database.session.query(Tutor).filter_by(id=id_cliente).first()
    if cliente:
        try:
            database.session.delete(cliente)
            database.session.commit()
            return "Cliente excluído"
        except:
            database.session.rollback()
            return "Erro ao excluir"
    return "Cliente não encontrado"

def buscar_clientes_por_nome(nome):
    return database.session.query(Tutor).filter(Tutor.nome.ilike(f"%{nome}%")).all()

# ✨ Etapa 1: Criar  para lógica de cliente
# Aqui ficam as funções que lidam com banco de dados e regras de negócio:




























# from models import Cliente
# from db import SessionLocal
#
# def salvar_cliente(dados):
#     """Salva um novo cliente no banco"""
#     session = SessionLocal()
#     cliente = Cliente(**dados)
#     session.add(cliente)
#     session.commit()
#     session.close()
#
# def buscar_cliente(id_cliente):
#     """Busca um cliente pelo ID"""
#     session = SessionLocal()
#     cliente = session.query(Cliente).filter_by(id=id_cliente).first()
#     session.close()
#     return cliente
#
# def deletar_cliente(id_cliente):
#     """Deleta um cliente pelo ID"""
#     session = SessionLocal()
#     cliente = session.query(Cliente).filter_by(id=id_cliente).first()
#     if cliente:
#         session.delete(cliente)
#         session.commit()
#     session.close()
#
# def editar_cliente(id_cliente, novos_dados):
#     """Edita dados de um cliente existente"""
#     session = SessionLocal()
#     cliente = session.query(Cliente).filter_by(id=id_cliente).first()
#     if cliente:
#         for campo, valor in novos_dados.items():
#             setattr(cliente, campo, valor)
#         session.commit()
#     session.close()
#
#
#
#     # funções relacionadas ao cliente
#     # 🛠️ Este arquivo traz a lógica do CRUD. E pode crescer com filtros, validações e relatórios.