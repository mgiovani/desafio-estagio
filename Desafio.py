#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from datetime import date

from selenium import webdriver
import time


def getMD5(url):
	return 'asd-asd'

def toISO(data):
	data = data.split('/')
	if(len(data) < 3): return None
	
	return data[2] +'-'+ data[1] +'-'+ data[0]

def getMD5List(data):
	data = date.fromisoformat(data)
	#if data < datetime.now()
		#result = buscaDB(data)
		#if result:
		#    return result
	
	url = 'http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/diario.do'
	parametros = {'action' : 'buscarDiarios', 'page' : 'diarioPageLastList.jsp', 'voDiarioSearch.listState.itensPerPage' : '100', 
				  'voDiarioSearch.tribunal' : 'TSE', 'voDiarioSearch.calendario' : 'false', 'voDiarioSearch.mesAnoPub' : data.strftime('%m')+'/'+str(data.year)} 
	
	req = requests.get(url, params=parametros)
	if req.status_code != 200:
		return req.status_code
	
	driver = webdriver.Chrome()
	driver.get(req.url)
	
	jsModificado = open('jsModificado.js', 'r')
	driver.execute_script(jsModificado.read())
	jsModificado.close()

	soup = bs(req.text, 'html.parser')
	tabela = soup.find_all('tr')
	diarios = dict()
	
	#For que remove o header e footer da tabela
	for i in range(1, len(tabela)-1):
		td = tabela[i].find_all('td')
		
		if len(td) < 3: continue
		key = td[0].get_text()
		
		dataDiario = date.fromisoformat(toISO(td[1].get_text()))
		if dataDiario.day != data.day: continue
		
		md5Diario = getMD5(td[2])
		diarios.setdefault(key, [str(dataDiario), md5Diario])
	
	print(diarios)
	
	#Download pdf
	#insertDB(lista)




getMD5List('2018-12-18')
time.sleep(20)




