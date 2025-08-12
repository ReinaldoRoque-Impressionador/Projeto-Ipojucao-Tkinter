from datetime import datetime, timedelta


from modulos import dados_compartilhados as dc
from modulos.utilitarios import caminho_arquivo


def gerar_msg_servico(cliente, texto_relatorio):
    return f"Olá, {cliente['nome']}! 🐾 Aqui está o resumo dos serviços prestados:\n{texto_relatorio}"

def gerar_msg_pix(pix_link):
    return f"Para pagamento via PIX, utilize o seguinte link ou QRCode:\n{pix_link}"

def gerar_msg_explicativa(validade=None):
    if not validade:
        validade = (datetime.now() + timedelta(days=3)).strftime('%d/%m/%Y')
    return (
        f"O pagamento é válido até {validade}. 💰\n"
        "Para confirmar o serviço, recomendamos realizar o pagamento até esta data.\n"
        "Qualquer dúvida, estamos à disposição!"
    )

def gerar_msg_admin(nome, relatorio_texto):
    return f"📋 Relatório do sistema para {nome}:\n{relatorio_texto}"









