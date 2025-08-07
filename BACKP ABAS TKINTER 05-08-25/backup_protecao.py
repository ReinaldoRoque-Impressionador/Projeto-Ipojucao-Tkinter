from backup_protecao import fazer_backup_arquivos

arquivos_criticos = ["aba_login_fusion.py", "dados_compartilhados.py", "audio.py"]
fazer_backup_arquivos(arquivos_criticos)

import os
import shutil
from datetime import datetime

def fazer_backup_arquivos(arquivos, pasta_origem="modulos", pasta_backup="backup_arquivos"):
    if not os.path.exists(pasta_backup):
        os.makedirs(pasta_backup)

    data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")

    for nome_arquivo in arquivos:
        caminho_origem = os.path.join(pasta_origem, nome_arquivo)
        if os.path.exists(caminho_origem):
            nome_backup = f"{nome_arquivo.replace('.py', '')}_backup_{data_hora}.py"
            caminho_destino = os.path.join(pasta_backup, nome_backup)
            shutil.copy2(caminho_origem, caminho_destino)
            print(f"🛡️ Backup criado: {nome_backup}")
        else:
            print(f"⚠️ Arquivo não encontrado: {nome_arquivo}")