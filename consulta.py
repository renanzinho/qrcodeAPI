from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup as bs
import requests
import urllib2, urllib


'''
	Essa funcao recebe o codigo do qrcode, a localizacao do celular e retorna uma lista com os itens comprados
	in:
		code: String
			  Codigo do QRCode
		location: String
			 	  Latitude e longitude do usuario no momento da requisicao
	out:
		items: List
			   Lista de itens que estao no XML da nota
'''
def parsing(code, location):

	geolocator = Nominatim()
	loc = geolocator.reverse(location)
	state = loc.address.split(',')[-4][1:]
	
	if state == 'PE':
		page = requests.get(code)
		soup = bs(page.text, 'xml')
		purchases = soup.find_all('det')
		items = []

		for item in purchases:
			items.append({
				'nome': item.xProd.text,
				'ean': item.cEAN.text,
				'quantidade': item.qCom.text,
				'valor unitario': item.vUnCom.text,
				'valor total': item.vProd.text
			})

		return items
	# elif state == 'CE':
	# 	page = requests.get(code)
	# 	soup = bs()
	else:
		print('Estado nao suportado ainda')

	pass


code = 'http://nfce.sefaz.pe.gov.br/nfce-web/consultarNFCe?chNFe=26180561365284014407650250000171701000171708&nVersao=100&tpAmb=1&cDest=09598592413&dhEmi=323031382d30352d31325432303a35393a35372d30333a3030&vNF=100.20&vICMS=0.00&digVal=6d746b52634a417554615539524a496c5043574e45536b696364633d&cIdToken=000001&cHashQRCode=2ED8C866536E124DFDC507EF1CFAB21285A7AEC6'




location = '-8.0555060005587 -34.9509729136151'
location = ', '.join(location.split(' '))

parsing(code, location)
