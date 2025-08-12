import requests
import re
from tkinter import ttk
from pprint import  pprint
from modulos.utilitarios import caminho_arquivo

from modulos import dados_compartilhados as dc
from modulos.utilitarios import caminho_arquivo

from aba_itau import api_key, link_api, parametros, descricao

from audio import tocar_musica, tocar_som_curto, parar_musica
from aba_som import som_login, som_relatorio, tocar_trilha, alternar_som_estado

itau_api_key = "https://oauthd.itau/identity/connect/token"

itau_link_api = "https://secure.api.itau/pix_recebimentos_conciliacoes/v2"


# client id
#ed184230-cae3-3517-839e-a15e07ca9327



# client secret: f151063b-693e-43e0-b0d6-6ffa5c124225
#
#
#
# token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlZDE4NDIzMC1jYWUzLTM1MTctODM5ZS1hMTVlMDdjYTkzMjciLCJleHAiOjE3NTE2ODI0MTEsImlhdCI6MTc1MTY4MjExMSwic291cmNlIjoic3RzLXNhbmRib3giLCJlbnYiOiJQIiwiZmxvdyI6IkNDIiwic2NvcGUiOiJjYXNobWFuYWdlbWVudC1jb25zdWx0YWJvbGV0b3MtdjEtYXdzLXNjb3BlIiwidXNlcm5hbWUiOiJyb3F1ZXJlaW5hbGRvQGdtYWlsLmNvbSIsIm9yZ2FuaXphdGlvbk5hbWUiOiJBdXRvIENhZGFzdHJvIn0.Xsk2qW7L7IVjxajW-0lhrw7tENRnFSjMQBTWAUP0nCo


# Cobrança imediata (indireto)
#
# post   //{id_cobranca_imediata_pix}
#
# patch   /cobrancas_imediata_pix
#
# get   / cobrancas_imediata_pix/{id_cobanca_imediata_pix}/qrcode
#
#
#
# COBRANÇA COM VENCIMENTO (indireto)
#
# post /cobrancas_vencimento_pix
#
# patch  /cobrancas_vencimento_pix/{id_cobranca_vencimento_pix}
#
# get  /cobrancas_vencimento_pix/{id_cobranca_vencimento_pix}/qrcode
#
#
#
#
#
#
#


# parametros = {
#     Authorizations: # "TOKEN ATUALIZADO"  "oauth2"  "Bearer seu_token_aqui",  # Use o token correto
#     x-itau-apikey: "https://oauthd.itau/identity/connect/token"  # "sua_api_key"
#     x-itau-correlationID: "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", # "sua_correlation_id"
#
#     ispb_decodificador: "60701190"   # "string (ISPB)",
#     numero_documento_decodificador: "41034181840"  # "string (Número do Documento)",
#     url: "spi-h.itau.com.br/pix/qr/v1/c3d189b4-c859-4218-b9de-b44594755a2e",
#     #string (URL)",
#     qrcode_emv: "00020101021126860014BR.GOV.BCB.PIX2564spi-h.itau.com.br/pix/qr/v1/323d1438-0ed3-4525-ae9f-7e856c7f15c25204000053039865802BR5907Eduardo6009SAO PAULO62070503***6304966E"
#     pix_link: "https://pix.bcb.gov.br/qr/MDAwMjAxMDEwMjExMjY5NTAwMTRCUi5HT1YuQkNCLlBJWDI1NzNzcGkuaG9tLmNsb3VkLml0YXUuY29tLmJyL2RvY3VtZW50b3MvZjJiYzU5NmMtNWFkNi00YjhiLTlhMDEtNmQxMWNmY2YzZDAxNTIwNDAwMDA1MzAzOTg2NTQwOTk5OTkwMC4wMDU4MDJCUjU5MTBOZXltYXIgQ1BGNjAwOVNBTyBQQVVMTzYyNjAwNTIyOHJ4WmJGcldTNHVhQVcwUno4ODlBUTUwMzAwMDE3QlIuR09WLkJDQi5CUkNPREUwMTA1MS4wLjA2MzA0Q0YxMg==" # "string (PIX Link)",
#     codigo_municipio: "2304458"  #"string (Código Município)",
#     data_prevista_pagamento: "2023-08-28T12:00:00.0Z"   #"string (Data)",
#     agencia: "string (Agência)",
#     conta: "string (Conta)",
#
#
#     #id_cobranca_vencimento_pix: ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$ # "seu_id_cobranca"
#     calendario: # # Adicione detalhes do calendário aqui
#     },
#     devedor: ("CPF - CNPJ")
#     nome: "Nome do Devedor"
#     recebedor: ("Estrutura do participante indireto")
#     valor: ("Valor da Cobrança com Vencimento")
#     ioc: ("Descrição: Estrutura com informações do identificador da localização do payload. Observação: A localização é a URL onde os dados cobrança são exibidos.")
#     status: <=31 characters - Enum:"ATIVA""CONCLUIDA""REMOVIDA_PELO_USUARIO_RECEBEDOR""REMOVIDA_PELO_PSP"
#             #Descrição: Status da cobrança. Na criação da cobrança será enviada sempre com o status "ATIVA". Caso tenha alterações no status desse QrCode, as opções de valor do campo são: ATIVA, CONCLUIDA, REMOVIDA_PELO_PSP, REMOVIDA_PELO_USUARIO_RECEBEDOR.
#             #Observação: Estado do registro da cobrança. Não se confunde com o estado da cobrança em si, ou seja, não guarda relação com o fato de a cobrança encontrar-se vencida ou expirada, por exemplo.
#             #Os status são assim definidos:
#             #ATIVA: indica que o registro se refere a uma cobrança que foi gerada mas ainda não foi paga nem removida.
#             #CONCLUIDA: indica que o registro se refere a uma cobrança que já foi paga e, por conseguinte, não pode acolher outro pagamento.
#             #REMOVIDO_PELO_USUARIO_RECEBEDOR: indica que o usuário recebedor solicitou a remoção do registro da cobrança.
#             #REMOVIDO_PELO_PSP: indica que o PSP Recebedor solicitou a remoção do registro da cobrança.
#     txid: string (Identificador da Cobrança) [a-zA-Z0-9]{26,35}
#             #Descrição: O campo txid determina o identificador da transação. O objetivo desse campo é ser um elemento que possibilite ao PSP do recebedor apresentar ao usuário recebedor a funcionalidade de conciliação de pagamentos.
#             #Observação: Na pacs.008, é referenciado como TransactionIdentification <txId> ou idConciliacaoRecebedor.
#             #Em termos de fluxo de funcionamento, o txid é lido pelo aplicativo do PSP do pagador e, depois de confirmado o pagamento, é enviado para o SPI via pacs.008. Uma pacs.008 também é enviada ao PSP do recebedor, contendo, além de todas as informações usuais do pagamento, o txid. Ao perceber um recebimento dotado de txid, o PSP do recebedor está apto a se comunicar com o usuário recebedor, informando que um pagamento específico foi liquidado.
#             #O txid é criado exclusivamente pelo usuário recebedor e está sob sua responsabilidade. O txid, no contexto de representação de uma cobrança, é único por CPF/CNPJ do usuário recebedor. Cabe ao PSP recebedor validar essa regra na API Pix.
#             #Este código deve possuir entre 26 e 35 posições, podendo conter letras minúsculas (a-z), letras maiúsculas (A-Z) e números (0-9).
#     chave: string (Chave DICT do Recebedor) <= 77 characters
# #           Descrição: Campo que contém a chave Pix registrada na DICT que será utilizada para recebimento da cobrança.
#     solicitacaoPagador: <= 140 characters
# #Descrição: O campo solicitacaoPagador, determina um texto a ser apresentado ao pagador para que ele possa digitar uma informação correlata, em formato livre, a ser enviada ao recebedor.
# #Observação: Esse texto será preenchido, na pacs.008, pelo PSP do pagador, no campo RemittanceInformation. O tamanho do campo na pacs.008 está limitado a 140 caracteres.
# #Campo retornado somente se o parâmetro de entrada foi colocado na requisição.
#     infoAdicionais: [
#         { "nome": "Campo 1"
#           "valor": "Informação Adicional 1"
#         }
#     ]
#         Array of objects (Informações Adicionais) <= 50
#                     #Descrição: Cada respectiva informação adicional contida na lista (nome e valor) deve ser apresentada ao pagador.
#                     #Observação: Pode-se adicionar quantas informações adicionais desejar.
#                     #Campo retornado somente se o parâmetro de entrada foi colocado na requisição.
#
#
#
#
#
#
#
# resposta = requests.get(link_api, params=parametros)
#
# if resposta.status_code == 200:
#     dados_requisicao = resposta.json()
#     pprint.pprint(dados_requisicao)
#     temp = dados_requisicao[""][""]
#     descricao = dados_requisicao["current"]["condition"]["text"]
#     print(temp)
#     print(descricao)
#
#
#
#
# RESPONSES
#
# 201  QR Code com vencimento criado
#
# 400   Requisição com formato inválido
#
# 404 Recurso solicitado não foi encontrado
#
#
# 503   Serviço não está disponível no momento. Serviço solicitado
#         pode estar em manutenção ou fora da janela de funcionamento



def rodape_imagem(frame_pai):
    caminho_img = os.path.join("imagensipojucao", "rodape", "footer.png")
    if os.path.exists(caminho_img):
        img = Image.open(caminho_img).resize((1000, 80))
        img_tk = ImageTk.PhotoImage(img)
        rodape = tk.Label(frame_pai, image=img_tk)
        rodape.image = img_tk  # mantém referência da imagem

        # Posiciona no final da grid
        rodape.grid(row=999, column=0, columnspan=999, sticky="ew")  # usa row "alta" para evitar conflito
    else:
        print("Imagem do rodapé não encontrada.")

def rodape_imagem(frame_pai):
    caminho_img = os.path.join("imagensipojucao", "rodape", "footer.png")
    if os.path.exists(caminho_img):
        img = Image.open(caminho_img).resize((1000, 80))
        img_tk = ImageTk.PhotoImage(img)
        rodape = tk.Label(frame_pai, image=img_tk)
        rodape.image = img_tk  # mantém referência da imagem

        # Posiciona no final da grid
        rodape.grid(row=999, column=0, columnspan=999, sticky="ew")  # usa row "alta" para evitar conflito
    else:
        print("Imagem do rodapé não encontrada.")

#barra_audio(frame_aba_itau)  # ou frame_aba_menu, frame_aba_config, etc.