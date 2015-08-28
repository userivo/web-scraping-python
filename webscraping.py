# WEBSCRAPING COM PYTHON
# Um breve exercicio de raspagem de dados na web com Python. 
# O programa realiza uma requisicao ao endereco da pagina Hot 100 Billboard, 
# coleta os dados e imprime uma lista em terminal com: 
# nome do artista, titulo da faixa e sua posicao na lista.

# BIBLIOTECAS UTILIZADAS (necessaria a instalacao delas)
# REQUESTS: http://docs.python-requests.org/en/latest/
# BEAUTIFUL SOUP: www.crummy.com/software/BeautifulSoup/

# AUTOR: 
# YURI ALEXSANDER
# https://github.com/yurialeksndr

###

# IMPORTANDO BIBLIOTECAS
import requests
import bs4

#DECLARANDO VARIAVEIS (NAO SERAO UTILIZADAS CLASSES)
titulo = []
artista = []

# REQUISICAO : HOT 100 BILLBOARD
response = requests.get ("http://www.billboard.com/charts/hot-100")

#CASO A REQUISICAO TENHA SUCESSO
if response.status_code == 200:
	
	#UTILIZANDO A BIBLIOTECA BEAUTIFUL SOUP PARA ACESSAR O CONTEUDO DA REQUISICAO
	bsoup = bs4.BeautifulSoup(response.content, "html.parser")

	#SEPARANDO CADA LINHA INTEIRA EM UM ARRAY
	charts = bsoup.findAll("article", attrs={"class": "chart-row"})

	#PARA CADA ITEM DO ARRAY, SALVAR TITULO DA FAIXA E ARTISTA NOS RESPECTIVOS ARRAYS
	for row in charts:

		#AS CHAMADAS DO METODO "REPLACE" RETIRAM OS ESPACAMENTOS E QUEBRAS DE LINHA DO TEXTO ORIGINAL DO SITE
		titulo.append(row.find("div", attrs={"class" : "row-title"}).h2.text.replace("\t","").replace("\n", ""))
		artista.append(row.find("div", attrs={"class" : "row-title"}).h3.text.replace("\t","").replace("\n", ""))

	#IMPRIMINDO OS VALORES
	for x in range(0, 100):
		print "{}. {}- {}".format(x+1, artista[x], titulo[x])

else:
	print "A requisicao falhou!"


