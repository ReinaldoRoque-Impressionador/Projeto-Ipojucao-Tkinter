import tkinter as tk

import os

def caminho_arquivo(nome_arquivo, subpasta=None):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # sobe da pasta modulos para raiz

    if subpasta:
        return os.path.join(base_dir, "imagensipojucao", subpasta, nome_arquivo)
    return os.path.join(base_dir, "imagensipojucao", "imagens", nome_arquivo)


if __name__ == "__main__":
    print(caminho_arquivo("teste.txt"))
    print(caminho_arquivo("teste.txt", "subpasta"))

    caminho = caminho_arquivo("dados.txt", "arquivos")
    print("Caminho:", caminho)
    print("Existe?", os.path.exists(caminho))