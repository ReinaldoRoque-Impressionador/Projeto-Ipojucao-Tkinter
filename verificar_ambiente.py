import sys
import os
import tkinter
import pandas as pd

def verificar_ambiente():
    print("✅ Verificação do Ambiente Virtual")
    print("-" * 40)

    # Caminho do Python
    print(f"📍 Python executável: {sys.executable}")

    # Versão do Python
    print(f"🐍 Versão do Python: {sys.version}")

    # Diretório atual
    print(f"📁 Diretório atual: {os.getcwd()}")

    # Verificar pacotes
    print("\n📦 Verificando pacotes essenciais:")
    try:
        print(f"Tkinter: {tkinter.TkVersion}")
    except Exception as e:
        print(f"❌ Erro com Tkinter: {e}")

    try:
        print(f"Pandas: {pd.__version__}")
    except Exception as e:
        print(f"❌ Erro com Pandas: {e}")

    print("\n✅ Ambiente verificado com sucesso!")

if __name__ == "__main__":
    verificar_ambiente()