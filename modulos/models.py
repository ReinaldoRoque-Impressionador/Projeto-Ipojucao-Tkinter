from sqlalchemy import Column, Integer, String
from db import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String)
    email = Column(String)
    endereco = Column(String)
    cidade = Column(String)


# define a estrutura da tabela de clientes
# 📌 Aqui você define como o cliente é armazenado no banco.