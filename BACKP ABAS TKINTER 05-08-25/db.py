from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Criação do engine com SQLite
engine = create_engine('sqlite:///ipojucadb.db', echo=True)

# Classe base para os modelos
Base = declarative_base()

# Criador de sessões
SessionLocal = sessionmaker(bind=engine)

#1.  — configura o banco de dados
# Esse arquivo centraliza a conexão com o banco de dados