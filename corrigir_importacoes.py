import os

def corrigir_importacoes(caminho_raiz):
    for pasta, _, arquivos in os.walk(caminho_raiz):
        for arquivo in arquivos:
            if arquivo.endswith(".py"):
                caminho_completo = os.path.join(pasta, arquivo)
                with open(caminho_completo, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                novo_conteudo = conteudo.replace(
                    "from utilitarios import caminho_arquivo",
                    "from modulos.utilitarios import caminho_arquivo"
                )
                if conteudo != novo_conteudo:
                    with open(caminho_completo, "w", encoding="utf-8") as f:
                        f.write(novo_conteudo)
                    print(f"Corrigido: {caminho_completo}")

# Use o caminho da raiz do seu projeto
corrigir_importacoes("C:/Users/VEIRANO/PycharmProjects/ModuloTkinter/Planilha Controle Ipojucão/modulos")
