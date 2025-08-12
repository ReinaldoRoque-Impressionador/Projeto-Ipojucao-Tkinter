import os

pasta_sons = os.path.join(os.getcwd(), "sons")
print("🎵 Arquivos na pasta 'sons':")
for arquivo in os.listdir(pasta_sons):
    print(" -", arquivo)