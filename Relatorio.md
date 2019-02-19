# Relatório do Desenvolvimento - Desafio

## Dificuldades Encontradas

1. **Abordagem:** A maior das dificuldades surgiu ao tentar abordar o problema de uma maneira de alto nível, tentando simular exatamente o comportamento humano, utilizando o Selenium para fazer o download dos PDF's e sobreescrevendo a função chamarCaptcha para que não seja necessário respondê-lo. Após gastar algum tempo até que essa abordagem funcionasse me dei conta que isto deveria ser feito em baixo nível e que uma requisição POST com os valores corretos poderia facilmente burlar o Captcha e fornecer diretamente o PDF, somente sendo necessário salvá-lo e extrair o MD5.
2. **Rastreio de Requisições:** Outra dificuldade foi ao início do estudo do funcionamento do site do TSE onde achei um pouco confuso rastrear todas as requisições que estavam ocorrendo e como elas poderiam me ajudar, principalmente as feitas por meio de JSP's, isto foi provavelmente o estopim que causou a dificuldade citada anteriormente. 
3. **Outros:** Todos os outros problemas surgiram com o uso da abordagem inadequada utilizada à priori, houveram erros de configuração do Selenium, erro ao manter controle sobre os PDF's baixados e erros ao injetar o JavaScript modificado no site do TSE. Todos esses problemas foram resolvidos com buscas nas Documentações e StackOverflow porém muito tempo foi tomado.


## Justificativas de Métodos



## Fontes de Pesquisa

- [TSE](http://www.tse.jus.br/servicos-judiciais/publicacoes-oficiais/diario-da-justica-eletronico/diario-da-justica-eletronico-1) 
- [Docs - Date](https://docs.python.org/3/library/datetime.html#datetime.date.year)
- [StackOverflow - Date Format](https://stackoverflow.com/questions/15509345/extracting-double-digit-months-and-days-from-a-python-date)
- [Docs - BeatifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Docs - StdTypes](https://docs.python.org/3/library/stdtypes.html#dict)
- [Selenium](https://selenium-python.readthedocs.io/api.html)
- [StackOverflow - Download com Selenium](https://stackoverflow.com/questions/45573483/how-to-check-downloaded-files-selenium-webdriver)
- [Docs - Shutil](https://docs.python.org/3/library/shutil.html#shutil.move)
- [Docs - OS](https://docs.python.org/3/library/os.html)
- [Docs - Hashlib](https://docs.python.org/3.3/library/hashlib.html)
- [StackOverflow - Delete Folder Contents](https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder-in-python)
- [Docs - Re](https://docs.python.org/3/library/re.html)