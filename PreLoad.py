import Desafio
import datetime
import time
from datetime import timedelta, date

def main():
	#PreLoad de 1 ano (Pode ser feito até o começo de 2009 de acordo com a necessidade)
	dataInicial = date(2018, 1, 1)
	dataFinal = date(2019, 2, 28)
	d = dataInicial
	delta = datetime.timedelta(days=1)
	while d <= dataFinal:
		print (d.strftime("%Y-%m-%d"), Desafio.getMD5List(d.strftime("%Y-%m-%d")))
		d += delta
		time.sleep(1)
		
if __name__ == "__main__":
	main()
