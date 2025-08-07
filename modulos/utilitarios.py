import os

def caminho_arquivo(nome_arquivo, subpasta=None):
    base_dir = os.path.dirname(__file__)
    if subpasta:
        return os.path.join(base_dir, subpasta, nome_arquivo)
    return os.path.join(base_dir, nome_arquivo)