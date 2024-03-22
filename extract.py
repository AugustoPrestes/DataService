######################################################################################################
#### Utilizaremos essa area para fazer a raspagem de dados do site "https://statusinvest.com.br"   ###
#### Para conseguirmos os dados que alimentaram a API                                              ###
######################################################################################################

# Seção de importações
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options




# Recebendo a Variavel para carregar a pagina
URL = 'https://statusinvest.com.br/acoes/busca-avancada'

# Abrindo o Site
print('Iniciando a requisição')
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get(URL)

# Parar para não ter problema com o site
print('Dormindo por 5 sec')
sleep(5)

# Buscando o Botão de Busca
print("Buscando Elementos")
btnBuscar = driver.find_element_by_xpath(
    '//div/button[contains(@class, "find")]')

# Clicando
btnBuscar.click()
print("Cliquei, vou dormir por 5 sec novamente!")
sleep(5)

# Fechando o Anuncio caso tenha
print("Fechando o Anuncio")

# baixando os dados
print("Baixando os dados")
btnDownload = driver.find_element_by_xpath(
    '//div/button[contains(@class, "btn-download")]')

# Clicando
btnDownload.click()
