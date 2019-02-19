import requests
import sqlite3
import os
import time
import hashlib
import json
import shutil
from datetime import date
from os import path
from bs4 import BeautifulSoup as bs

jsonPath = path.join(os.getcwd(), "md5List.json")
bdPath = path.join(os.getcwd(), "sqlite.db")
downPath = path.join(os.getcwd(), "Downloads", "")


def getId(dados):
    idD = dados.find('a')['href'].replace('javascript:chamarCaptcha(', '').replace(',\'TSE\');', '')
    return idD

def getMD5(key, idD):       
    #Todos os diarios serao baixados para a pasta downloads e 'renomeados'
    diarioPath = path.join(os.getcwd(), "Downloads", key.replace('/', '_')+".pdf")

    #Post realizado para download só precisa desses parametros pra funcionar
    urlDownload = 'http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/diario.do'
    parametros = {'action' : 'downloadDiario', 'captchaValidacao' : 'ok', 'id' : idD, 'tribunal' : 'TSE'} 

    req2 = requests.post(urlDownload, data=parametros)

    if req2.status_code != 200:
        return req2.status_code       
    
    if not os.path.exists(downPath): os.makedirs(downPath)
    with open(diarioPath, 'wb') as file:
        file.write(req2.content)
    
    #Timeout para caso nunca baixe o pdf procurado / a cada segundo verifica se ele existe (ja foi baixado)
    timeout = 20
    while not os.path.exists(diarioPath):
        timeout = timeout - 1
        if timeout == 0: break
        time.sleep(1)

    if os.path.isfile(diarioPath):
        md5 = hashlib.md5(open(diarioPath,'rb').read()).hexdigest()
    return md5

def toISO(data):
    data = data.split('/')
    if(len(data) < 3): return None
    
    return data[2] +'-'+ data[1] +'-'+ data[0]

def buscaBDId(idD):
    bd = sqlite3.connect(bdPath) 
    cursor = bd.cursor()
    cursor.execute('SELECT diario.md5 FROM diario WHERE id='+idD)
    md5 = -1
    for linha in cursor.fetchall():
        md5 = linha[0]
    bd.close()
    return md5

def buscaBD(data):
    bd = sqlite3.connect(bdPath) 
    cursor = bd.cursor()
    cursor.execute("SELECT diario.md5 FROM diario WHERE data='"+data+"'")
    md5 = []
    for linha in cursor.fetchall():
        md5.append(linha[0])
    bd.close()
    if len (md5) < 1: md5 = -1
    return md5

def insereBD(key, dataDiario, md5Diario, idDiario):
    bd = sqlite3.connect(bdPath) 
    cursor = bd.cursor()
    cursor.execute('INSERT INTO diario(numero, data, md5, id) VALUES (?,?,?,?)', (key, dataDiario, md5Diario, idDiario))
    bd.commit()
    bd.close()
    
def deletaArquivos():
    shutil.rmtree(downPath)
    if not os.path.exists(downPath): os.makedirs(downPath)

def getMD5List(data):
    result = buscaBD(data)
    if result != -1: return result
    
    data = date.fromisoformat(data)    
    
    #Url que retorna todos os diarios daquele dia pedido
    urlBusca = 'http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/diarioTxt.do'   
    parametros = {'action' : 'buscarDiarios', 'voDiarioSearch.tribunal' : 'TSE', 'page' : 'diarioPageTextualList.jsp', 
                  'voDiarioSearch.dataPubIni' : data.strftime("%d/%m/%Y"), 'voDiarioSearch.dataPubFim' : data.strftime("%d/%m/%Y")} 
    
    req = requests.get(urlBusca, params=parametros)
    if req.status_code != 200:
        return req.status_code
    
    soup = bs(req.content, 'html.parser')
    tabela = soup.find_all('tr')
    
    listaMd5 = []
    #For que remove o header e footer da tabela
    for i in range(2, len(tabela)):
        td = tabela[i].find_all('td')
        
        #Sao necessarios os 3 campos para ser adicionado
        if len(td) < 3: continue
        key = td[0].get_text()
        
        dataDiario = date.fromisoformat(toISO(td[1].get_text()))
        if dataDiario.day != data.day: continue
        
        idDiario = getId(td[2])
        md5Diario = buscaBDId(str(idDiario))
        if md5Diario == -1: 
            md5Diario = getMD5(key, idDiario)
            insereBD(str(key), str(dataDiario), str(md5Diario), idDiario)
        listaMd5.append(md5Diario)
    
    #Evita acumulo de pdfs redundantes 
    deletaArquivos()
    return listaMd5

def main():
	while True:
		data = input("Data no formato ISO (AAAA-MM-DD): ")
		if data == '': break
		print (getMD5List(data))

if __name__ == "__main__":
	main()
