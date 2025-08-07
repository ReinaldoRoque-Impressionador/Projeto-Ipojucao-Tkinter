from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, date
from database import database
#from main import login_manager  # ou de onde você instanciou
from login_config import login_manager

# === TABELA: USUÁRIO (LOGIN) ===
class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    email = database.Column(database.String, unique=True, nullable=False)
    senha = database.Column(database.String, nullable=False)

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

# === TABELA: TUTOR ===
class Tutor(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    cpf = database.Column(database.String, unique=True, nullable=False)
    telefone = database.Column(database.String)
    email = database.Column(database.String, unique=True)
    endereco = database.Column(database.String)
    numero = database.Column(database.String)
    complemento = database.Column(database.String)
    data_cadastro = database.Column(database.DateTime, default=datetime.now)

    pets = database.relationship('Pet', backref='tutor', lazy=True)

# === TABELA: PET ===
class Pet(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    idade_anos = database.Column(database.String)
    idade_meses = database.Column(database.String)
    porte = database.Column(database.String)
    raca = database.Column(database.String)
    descricao_pelagem = database.Column(database.String)
    foto = database.Column(database.String, default='default.jpg')

    tutor_id = database.Column(database.Integer, database.ForeignKey('tutor.id'), nullable=False)
    atendimentos = database.relationship('Atendimento', backref='pet', lazy=True)

# === TABELA: ATENDIMENTO ===
class Atendimento(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    data_servico = database.Column(database.Date, nullable=False, default=date.today)
    servicos_realizados = database.Column(database.String)
    observacoes = database.Column(database.String)

    pet_id = database.Column(database.Integer, database.ForeignKey('pet.id'), nullable=False)
    pagamento = database.relationship('Pagamento', backref='atendimento', uselist=False)

# === TABELA: PAGAMENTO ===
class Pagamento(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    status = database.Column(database.String, nullable=False)
    forma_pagamento = database.Column(database.String)
    valor_total = database.Column(database.Float, nullable=False)
    desconto_fixo = database.Column(database.Float, default=0)
    desconto_percentual = database.Column(database.Float, default=0)
    data_pagamento = database.Column(database.Date)

    atendimento_id = database.Column(database.Integer, database.ForeignKey('atendimento.id'), nullable=False)

# === TABELA: CLIENTE ===
class Cliente(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    cpf = database.Column(database.String, unique=True)
    email = database.Column(database.String, unique=True)

# === FUNÇÕES CRUD: CLIENTE ===
def salvar_cliente(nome):
    novo_cliente = Cliente(nome=nome)
    database.session.add(novo_cliente)
    try:
        database.session.commit()
        return True
    except Exception as e:
        database.session.rollback()
        print("Erro ao salvar cliente:", e)
        return False

def listar_clientes():
    return database.session.query(Cliente).all()

def atualizar_cliente(id_cliente, novo_nome):
    cliente = database.session.query(Cliente).filter_by(id=id_cliente).first()
    if cliente:
        cliente.nome = novo_nome
        try:
            database.session.commit()
            return True
        except Exception as e:
            database.session.rollback()
            print("Erro ao atualizar cliente:", e)
    return False

def buscar_clientes(campo, valor):
    query = database.session.query(Cliente)
    if campo == "ID":
        return query.filter(Cliente.id == int(valor)).all()
    elif campo == "CPF":
        return query.filter(Cliente.cpf.like(f"%{valor}%")).all()
    elif campo == "E-mail":
        return query.filter(Cliente.email.like(f"%{valor}%")).all()
    return []

def excluir_cliente(id_cliente):
    cliente = database.session.query(Cliente).filter_by(id=id_cliente).first()
    if cliente:
        try:
            database.session.delete(cliente)
            database.session.commit()
            return True
        except Exception as e:
            database.session.rollback()
            print("Erro ao excluir cliente:", e)
    return False






# from email.policy import default
# from enum import unique
#
# from sqlalchemy.orm import backref
# from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy.sql import func
#
# from database import database
#
#
# #from ipojucao import database, login_manager
# from flask_login import UserMixin
#
#
#
# from datetime import date
# from .Cliente import salvar_cliente  # substitua "salvar" pelo nome real do arquivo
#
#
# from datetime import datetime
#
# # === TABELA: TUTOR ===
# class Tutor(database.Model):
#     id = database.Column(database.Integer, primary_key=True)
#     nome = database.Column(database.String, nullable=False)
#     cpf = database.Column(database.String, unique=True, nullable=False)
#     telefone = database.Column(database.String)
#     email = database.Column(database.String, unique=True)
#     endereco = database.Column(database.String)
#     numero = database.Column(database.String)
#     complemento = database.Column(database.String)
#
#     data_cadastro = database.Column(database.DateTime, default=datetime.now)  # 🆕 Novo campo!
#
#     pets = database.relationship('Pet', backref='tutor', lazy=True)
#
# # === TABELA: PET ===
# class Pet(database.Model):
#     id = database.Column(database.Integer, primary_key=True)
#     nome = database.Column(database.String, nullable=False)
#     idade_anos = database.Column(database.String)
#     idade_meses = database.Column(database.String)
#     porte = database.Column(database.String)
#     raca = database.Column(database.String)
#     descricao_pelagem = database.Column(database.String)
#     foto = database.Column(database.String, default='default.jpg')
#
#     tutor_id = database.Column(database.Integer, database.ForeignKey('tutor.id'), nullable=False)
#     atendimentos = database.relationship('Atendimento', backref='pet', lazy=True)
#
#
# # === TABELA: ATENDIMENTO ===
# class Atendimento(database.Model):
#     id = database.Column(database.Integer, primary_key=True)
#     data_servico = database.Column(database.Date, nullable=False, default=date.today)
#     servicos_realizados = database.Column(database.String)  # Ex: "Banho, Tosa, Hidratação"
#     observacoes = database.Column(database.String)
#
#     pet_id = database.Column(database.Integer, database.ForeignKey('pet.id'), nullable=False)
#     pagamento = database.relationship('Pagamento', backref='atendimento', uselist=False)
#
#
# # === TABELA: PAGAMENTO ===
# class Pagamento(database.Model):
#     id = database.Column(database.Integer, primary_key=True)
#     status = database.Column(database.String, nullable=False)  # "Pago", "Em Aberto"
#     forma_pagamento = database.Column(database.String)         # "PIX", "Débito", "Crédito", "Dinheiro"
#     valor_total = database.Column(database.Float, nullable=False)
#     desconto_fixo = database.Column(database.Float, default=0)
#     desconto_percentual = database.Column(database.Float, default=0)
#     data_pagamento = database.Column(database.Date)
#
#     atendimento_id = database.Column(database.Integer, database.ForeignKey('atendimento.id'), nullable=False)
#
#
#
# class Cliente(database.Model):
#     id = database.Column(database.Integer, primary_key=True)
#     nome = database.Column(database.String, nullable=False)
#     cpf = database.Column(database.String, unique=True)
#     email = database.Column(database.String, unique=True)
#
# # class Cliente(Base):
# #     __tablename__ = "clientes"
# #     id = Column(Integer, primary_key=True)
# #     nome = Column(String, nullable=False)
# #     cpf = Column(String, unique=True)
# #     email = Column(String, unique=True)
#
# #
# @login_manager.user_loader
# def load_usuario(id_usuario):
#     return Usuario.query.get(int(id_usuario))
#
#
# def salvar_cliente(nome):
#     novo_cliente = Cliente(nome=nome)
#
#     database.session.add(novo_cliente)
#
#     try:
#         database.session.commit()
#
#         return True
#     except Exception as e:
#         database.session.rollback()
#         print("Erro ao salvar cliente:", e)
#         return False
#
# def listar_clientes():
#     return database.session.query(Cliente).all()
#
# def atualizar_cliente(id_cliente, novo_nome):
#     cliente = database.session.query(Cliente).filter_by(id=id_cliente).first()
#     if cliente:
#         cliente.nome = novo_nome
#         try:
#             database.session.commit()
#             return True
#         except Exception as e:
#             database.session.rollback()
#             print("Erro ao atualizar:", e)
#     return False
#
#
#
# def buscar_clientes(campo, valor):
#     if campo == "ID":
#         return database.session.query(Cliente).filter(Cliente.id == int(valor)).all()
#     elif campo == "CPF":
#         return database.session.query(Cliente).filter(Cliente.cpf.like(f"%{valor}%")).all()
#     elif campo == "E-mail":
#         return database.session.query(Cliente).filter(Cliente.email.like(f"%{valor}%")).all()
#     return []
#
# def excluir_cliente(id_cliente):
#     cliente = session.query(Cliente).filter_by(id=id_cliente).first()
#     if cliente:
#         try:
#             database.session.delete(cliente)
#             database.session.commit()
#             return True
#         except Exception as e:
#             database.session.rollback()
#             print("Erro ao excluir cliente:", e)
#     return False
#
# class Usuario(database.Model, UserMixin):
#     id = database.Column(database.Integer, primary_key=True)
#     nome_pet = database.Column(database.String, nullable=False)
#     idade_anos = database.Column(database.String)
#     idade_meses = database.Column(database.String)
#     tutor_1 = database.Column(database.String, nullable=False)
#     telef_tutor1 = database.Column(database.String, nullable=Fa
#     email_tutor1 = database.Column(database.String, unique=True)
#     tutor_2 = database.Column(database.String)
#     telef_tutor2 = database.Column(database.String)
#     email_tutor2 = database.Column(database.String, unique=True)
#     endereco = database.Column(database.String, nullable=False)
#     numero = database.Column(database.String, nullable=False)
#     complemento = database.Column(database.String)
#     foto_pet = database.Column(database.String, default='default.jpg')
#     foto_tutor1 = database.Column(database.String, 'default1.jpg')
#     foto_tutor2 = database.Column(database.String, 'default2.jpg')
#     #posts = database.relationship('Post', backref='autor', lazy=True)
#     #cursos = database.Column(database.String, nullable=False, default='Não Informado')
#
#
# class Servicos(database.Model, UserMixin):
#     banho = database.Column(database.Integer)
#     hidratracao = database.Column(database.Integer)
#     desembolo = database.Column(database.Integer)
#     remocao_pelos = database.Column(database.Integer)
#     corte_unhas = database.Column(database.Integer)
#     escovacao_dentes = database.Column(database.Integer)
#     tosa_higienica = database.Column(database.Integer)
#     tosa_maquina = database.Column(database.Integer)
#     tosa_tesoura = database.Column(database.Integer)
#     leva_tras = database.Column(database.Integer)
#
# class Porte(database.Model, UserMixin):
#     pequeno = database.Column(database.Integer)
#     medio = database.Column(database.Integer)
#     grande = database.Column(database.Integer)
#     maior = database.Column(database.Integer)
#
# class Condicoes(database.Model, UserMixin)
#     individual = database.Column(database.Integer)
#     quinzenal = database.Column(database.Integer)
#     mensal = database.Column(database.Integer)
#
# class Abatimento(database.Model, UserMixin):
#     fixo = database.Column(database.Integer)
#     percentual = database.Column(database.Integer)
#
# class status(database.Model, UserMixin):
#     aberto = database.Column(database.Integer)
#     pago = database.Column(database.Integer)
#
# class Forma(database.Model, UserMixin):
#     pix = database.Column(database.Integer)
#     debito = database.Column(database.Integer)
#     credito = database.Column(database.Integer)
#     especie = database.Column(database.Integer)
#
# class Calendario(database.Model, UserMixin):
#     servico = database.Column
#     cadastro = database.Column
#     pagamento = database.Column
#     inicial = database.Column
#     final = database.Column
#
# class Recomendacoes(database.Model, UserMixin):
#     cuidados = database.Column
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
#     def contar_posts(self):
#         return len(self.posts)
#
# class Post(database.Model):
#     id = database.Column(database.Integer, primary_key=True)
#     titulo = database.Column(database.String, nullable=False)
#     corpo = database.Column(database.Text, nullable=False)
#     data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
#     id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)

