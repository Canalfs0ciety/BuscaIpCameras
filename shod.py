# Script feito para achar ips de cameras de segurança utilizando a Api do shodan 
# Nomeie o projeto com qualquer nome, menos shodan.py, pois da erro
### Criado por @canalfsociety ###
### Com a ajuda do @Perverso ###

######## VISITE MEU SITE ########## canalfsociety.com ############
###### BAIXE MEU APP NA PLAYSTORE ######## BOLETIM TEC ###########

from shodan import Shodan
from shodan.exception import APIError
import time

print()
print('ACOMPANHE NOSSO SITE DE NOTICIAS')
print('https://www.canalfsociety.com/')
print()

print('Va ao site shodan.io e crie uma conta caso nao tenha,\
aconselho criar usando um email .edu pois vc tera acesso premium.\
Depois va em Account e copie a Api Key')
time.sleep(3)

#Pegue sua API Key no site do shodan na aba Account e cole na hora que pedir
key = input('Digite sua API Key do Shodan: ')

api = Shodan(key)

cidade = (input('Digite o nome da cidade que voce quer pesquisar os Ips: '))

pesquisa = ('port:37777 org:"CLARO S.A." city:"%s" product:"Dahua DVR"' % (cidade))

try:
        # Aqui é o parametro de pesquisa
        # Caso não retorne nenhum ip para a cidade que voce pesquisar, verifique se voce colocou os acentos nos nomes da cidade.
        results = api.search(pesquisa)

        # Não precisa mexer nessa linha, aqui vai retornar quantos ips foram encontardos
        print('Resultados Encontrados: {}'.format(results['total']))
                       
        for result in results['matches']:          
                        
          nl = '\n'
          ip = (format(result['ip_str']),nl)
          
          # Vai Criar um txt no mesmo local do projeto, é onde vai salvar os ips
          with open("dispositivo.txt", "a") as l:
            l.writelines(ip)   
          
#Caso der algum erro vai retornar essa mensagem         
except Shodan.APIError:
        print('Error: {}'.format(APIError))
        
# Ele vai retornar quantos ips foram localizados e salvar todos eles no arquivo txt!!!

print()
print('A CONSULTA FOI SALVO EM >> dispositivo.txt')

time.sleep(5)
