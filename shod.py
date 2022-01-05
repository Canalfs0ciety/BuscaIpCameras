# Script feito para achar ips de cameras de segurança utilizando a Api do shodan 
# Nomeie o projeto com qualquer nome, menos shodan.py, pois da erro
### Criado por @canalfsociety ###
### Com a ajuda do @Perverso ###

######## VISITE MEU SITE ########## canalfsociety.com ############

from shodan import Shodan
from shodan.exception import APIError
import time

print()
print('ACOMPANHE NOSSO SITE DE NOTICIAS')
print('https://www.canalfsociety.com/')
print()

#Pegue sua API Key no site do shodan na aba Acount e cole onde esta escrito MINHA API
api = Shodan('MINHA API')

try:
        # Aqui é o parametro de pesquisa
        # Ele esta configurado para retornar os ips de cameras de São Paulo, só mude o nome da cidade para ver de outras
        # Caso não retorne nenhum ip para a cidade que voce pesquisar, verifique se voce colocou os acentos nos nomes da cidade.
        results = api.search('port:37777 city:"são paulo" org:"CLARO S.A." product:"Dahua DVR"')

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
