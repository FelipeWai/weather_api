import requests
from pprint import pprint
from api_key import api_key
from datetime import datetime

class CidadeInvalidaError(Exception):
    pass

base_url = "http://api.weatherapi.com/v1/current.json?"


cidade = input("Digite a cidade: ")

param = {
    "key": api_key,
    "q": cidade,
    "lang": "pt"
}

try:

    response = requests.get(base_url, params=param)
    informacoes_da_cidade = response.json()


    informacoes_na_tela_do_usuario = {
        'Temp': informacoes_da_cidade['current']['temp_c'],
        'vel_vento': informacoes_da_cidade['current']['wind_kph'],
        'nome': informacoes_da_cidade['location']['name'],
        'estado': informacoes_da_cidade['location']['region'],
        'country': informacoes_da_cidade['location']['country'],
        'horario': datetime.fromtimestamp(informacoes_da_cidade['location']['localtime_epoch']).strftime('%H:%M:%S'),
    }
        
    if response.status_code == 400:
        raise CidadeInvalidaError ("Type a valid city!")



    print(f"""
            Nome: {informacoes_na_tela_do_usuario['nome']}
            Estado: {informacoes_na_tela_do_usuario['estado']}
            country: {informacoes_na_tela_do_usuario['country']}
            Velocidade do Vento: {informacoes_na_tela_do_usuario['vel_vento']}
            Sensação Térmica: {informacoes_na_tela_do_usuario['Temp']}
            horario: {informacoes_na_tela_do_usuario['horario']}""")


except KeyError as e:
    print(f"Erro: {e}")