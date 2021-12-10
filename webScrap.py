import requests
import pandas as pd
from bs4 import BeautifulSoup
import mysql.connector as sql



def Main():
	url = "https://mott.pe/noticias/datos-curiosos-que-te-despertaran-las-ganas-por-aprender-mas/"
	page = requests.get(url)

	soup = BeautifulSoup(page.content, 'html.parser')

	# Datos

	data = soup.find_all('b')

	datosScrapeds = list()

	for x in data:
		datosScrapeds.append(x.text)



	print(datosScrapeds)

	# Si quieres usar este script para cargar directo a una base de datos usa el siguiente bloque

#	connect = sql.connect(
#		host='',
#		user='',
#		passwd='',
#		db=''
#		)
#
#	cursor = connect.cursor()

	

#	for a in datosScrapeds:
#		title = "Dato Curioso"
#		sqlInsert = 'INSERT INTO WebScraping (Title, Data) VALUES (%s, %s)'
#		val = (title, a)
#		cursor.execute(sqlInsert,val)
#		connect.commit()
#		print("Valor insertado...")


Main()


