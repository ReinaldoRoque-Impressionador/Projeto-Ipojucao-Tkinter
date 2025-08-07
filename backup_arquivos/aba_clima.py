# import pygame
# pygame.mixer.init()

from pprint import pprint
import requests
from utilitarios import caminho_arquivo

logo_splash = caminho_arquivo("splash.png", subpasta=os.path.join("..", "..", "imagensipojucao"))
som_relatorio = caminho_arquivo("relatorio_finalizado.mp3", subpasta="sons")

def montar_aba_clima(aba_clima, inner_frame):
    api_key = "f1e5d72cde264a6c89615014250507"
    link_api = "http://api.weatherapi.com/v1/current.json"

    parametros = {
        "key": api_key,
        "q": "São Paulo",
        "lang": "pt"
    }

    resposta = requests.get(link_api, params=parametros)

    if resposta.status_code == 200:
        dados_requisicao = resposta.json()
        pprint(dados_requisicao)
        temp = dados_requisicao["current"]["temp_c"]
        descricao = dados_requisicao["current"]["condition"]["text"]
        print(temp)
        print(descricao)


api_key = "f1e5d72cde264a6c89615014250507"


link_api = "http://api.weatherapi.com/v1/current.json"

parametros = {
    "key": api_key,
    "q": "São Paulo",
    "lang": "pt"
}

resposta = requests.get(link_api, params=parametros)

if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    pprint(dados_requisicao)
    temp = dados_requisicao["current"]["temp_c"]
    descricao = dados_requisicao["current"]["condition"]["text"]
    print(temp)
    print(descricao)



# status code
# 200 ->  deu certo a requisição
# 300 ->  redirecionada
# 400 ->  não conseguiu fazer a requisição
# 500 ->  deu um erro no sistemaa





