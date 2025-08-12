import subprocess
import sys
import os


def instalar_requisitos():
    caminho_requisitos = os.path.join(os.getcwd(), "requirements.txt")

    if not os.path.exists(caminho_requisitos):
        print("❌ Arquivo requirements.txt não encontrado.")
        return

    print("📦 Instalando pacotes do requirements.txt...\n")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", caminho_requisitos])
        print("\n✅ Todos os pacotes foram instalados com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar pacotes: {e}")


if __name__ == "__main__":
    instalar_requisitos()