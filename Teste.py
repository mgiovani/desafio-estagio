import unittest
import Desafio

class TesteMD5(unittest.TestCase):

	def testeInvalido1(self):
		result = Desafio.getMD5List('2022-02-19')
		esperado = []
		self.assertEqual(result, esperado)
		
	def testeInvalido2(self):
		result = Desafio.getMD5List('0')
		esperado = 'Formato de data incorreto'
		self.assertEqual(result, esperado)
	
	def testeInvalido3(self):
		result = Desafio.getMD5List('2019-02-32')
		esperado = 'Formato de data incorreto'
		self.assertEqual(result, esperado)
		
	def testeInvalido4(self):
		result = Desafio.getMD5List('asd')
		esperado = 'Formato de data incorreto'
		self.assertEqual(result, esperado)
	
	def testeValido1(self):
		result = Desafio.getMD5List('2019-02-19')
		esperado = ['48e299a1aa1b22052ca6d9182a76e9db']
		self.assertEqual(result, esperado)
	
	def testeValido2(self):
		result = Desafio.getMD5List('2019-02-17')
		esperado = []
		self.assertEqual(result, esperado)
		
	def testeValido3(self):
		result = Desafio.getMD5List('2018-02-01')
		esperado = ['4cc8bd111a5d9b3e3e157c10f4402d54', 'c0850c839f46c9eeda16cbe1a4123301']
		self.assertEqual(result, esperado)
		
	def testeValido4(self):
		result = Desafio.getMD5List('2018-05-10')
		esperado = ['b5e82339e91c4c6ba9c5168a1583744a']
		self.assertEqual(result, esperado)
		
		
if __name__ == "__main__":
	unittest.main()
