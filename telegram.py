import telepot
import time
import socket
import requests
from bs4 import BeautifulSoup as bs
import base64
bot = telepot.Bot('1472212275:AAH7iQFurDg5zMfBpftmXE03XTk-9t0Ixvo')

def portal():
	url = 'https://portal.ifrn.edu.br/'

	response = requests.get(url)

	page = bs(response.text, 'html.parser')

	noticias = page.find_all('span', {'class':"news_title"})
	try:
		for noticia in noticias:
			bot.sendMessage(802671978,noticia.text+'\n')
	except:
		pass
def suap():
	cabecalho = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
	'Cookie': 'csrftoken=ITvvG3kAwA5okQspUtUUe9Aj0El3MqbdoO0x1sPvbXfxI27evJYzRv0MRDiAPY6t; sessionid=pz8ck3wynos5vitcx774av45y2subtqa'
}
	base64_message = 'YWJjMTIzQA=='
	base64_bytes = base64_message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	message = message_bytes.decode('ascii')
	dados = {
	'csrfmiddlewaretoken': 'NvNOTW6Nvq3A8meiDqK7ldvSpwjptyChtqiQelBIaNdJwyT7eGOMYzVlgvgWw6xx',
	'username': '20201014040036',
	'password': message,
	'this_is_the_login_form': '1',
	'next':'/',
	'g-recaptcha-response': ''	
	}


	url = 'https://suap.ifrn.edu.br/accounts/login/?next=/'

	
	with requests.Session() as s:
		resp = s.post(url, headers=cabecalho, data=dados)
		resp1 = s.get('https://suap.ifrn.edu.br/edu/aluno/20201014040036/?tab=boletim')
		html = bs(resp1.text,'html.parser')
		tabela = html.find('table', {'class':"borda"})
		parametro = tabela.find_all('td', {'class':"align-center"})
		nota_matematica = parametro[6].text
		nota_web = parametro[28].text
		bot.sendMessage(802671978,'\n'+f'''

matematica = {nota_matematica}

web_design = {nota_web}

''')


def g1():

	resp = requests.get('https://g1.globo.com/')

	page = bs(resp.text, 'html.parser')

	noticias_lista = []

	noticias = page.find_all('div', {'class':"feed-post-body-resumo"})
	for noticia in noticias:
		bot.sendMessage(802671978,noticia.text)
		time.sleep(1)



bot.sendMessage(802671978,'\n'+'''


1 = scan digite: /scan ipDoSite
2 = noticias portal digite: portal /portal
3 = ve notas digite: suap ou /suap
4 = ve ip do site digite: /ip site
''')


def recebendoMsg(msg):
	mensagem = msg['text']

	if 'scan' in mensagem:
	
	
		
		site = mensagem.split()
		site = site[1]
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ports = [20,21,22,23,25,53,67,68,80,110,123,156,143,161,179,443,1723,1863,3128,3389,8000,8080]
		resut = []
		try:
			for port in ports:
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				resp = client.connect_ex((site,port))
				if resp == 0:
					bot.sendMessage(802671978,f'[+++] porta {port} aberta. {socket.getservbyport(port)}[+++]')
		except:
			pass
		client.close
	elif '/portal' in mensagem:
		portal()
		print('noticias portal com sucesso')
	elif '/suap' in mensagem:
		suap()
		print('notas com sucesso')
	elif '/ip' in mensagem:
		m = mensagem.split()

		ip = socket.gethostbyname(m[1])
		bot.sendMessage(802671978,ip)
		print('ip com sucesso')
	elif '/g1' in mensagem:
		g1()
		print('noticias g1 com sucesso')
bot.message_loop(recebendoMsg)

while True:
	pass