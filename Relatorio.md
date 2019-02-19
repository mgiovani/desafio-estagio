# Relatório do Desenvolvimento - Desafio

## Dificuldades Encontradas
1. **Abordagem:** A maior das dificuldades surgiu ao tentar abordar o problema de uma maneira de alto nível, tentando simular exatamente o comportamento humano, utilizando o Selenium para fazer o download dos PDF's e sobreescrevendo a função chamarCaptcha para que não seja necessário respondê-lo. Após gastar algum tempo até que essa abordagem funcionasse me dei conta que isto deveria ser feito em baixo nível e que uma requisição POST com os valores corretos poderia facilmente burlar o Captcha e fornecer diretamente o PDF, somente sendo necessário salvá-lo e extrair o MD5.
2. **Rastreio de Requisições:** Outra dificuldade foi ao início do estudo do funcionamento do site do TSE onde achei um pouco confuso rastrear todas as requisições que estavam ocorrendo e como elas poderiam me ajudar, principalmente as feitas por meio de JSP's, isto foi provavelmente o estopim que causou a dificuldade citada anteriormente. 
3. **Outros:** Todos os outros problemas surgiram com o uso da abordagem inadequada utilizada à priori, houveram erros de configuração do Selenium, erro ao manter controle sobre os PDF's baixados e erros ao injetar o JavaScript modificado no site do TSE. Todos esses problemas foram resolvidos com buscas nas Documentações e StackOverflow porém muito tempo foi tomado.

## Justificativas de Métodos
1. **Path.join:** Tendo em vista estar programando em Windows e a alta chance do código ser executado em outros sistemas, foi utilizado o path.join para que ele usasse a definição de caminho de cada sistema.
2. **Requests.post:** Substituindo a versão com o uso do Selenium, o uso do POST deixou todo o código mais rápido e simples pois apenas é feita uma requisição e esta é gravada em um arquivo .pdf, nada perto do fluxo anterior que era muito mais complexo.
3. **Formato de Entrada:** Foi escolhido o formato de data na entrada como sendo do tipo [ISO 8601]((https://www.w3.org/TR/NOTE-datetime-970915.html)) simplesmente por se tratar de um padrão internacional bem estabelecido e facilitar o uso do date do Python.
4. **Persistência de Dados:** As seguintes opções foram consideradas: CSV, Plain Text e SQLite. Os dois primeiros ofereciam grande facilidade por qualquer programa conseguir mostrar os dados inseridos (o que também pode ser um problema) e talvez fossem opções melhores para poucos dados mas o SQLite além de portável teve um grande peso ao seu favor no que diz respeito à escalabilidade e facilidade de filtragem de dados. Como a base de dados cresce a cada dia o seu tamanho é crescente e teoricamente infindo.
5. **DeletaArquivos():** Por ser uma função de conferência para o processamento todos os PDF's baixados através do conjunto de funções aqui presente necessariamente já existe armazenado em algum outro lugar e sua existência seria desnecessariamente redundante. Em um longo prazo os PDF's poderiam tomar muito espaço para nada pois seu MD5 já está persistido.
6. **Leitura da Entrada:** A leitura do arquivo .py é feita de maneira sequêncial e até a entrada de uma data vazia com a intenção de facilitar/posibilitar testes e execuções em massa.

## Ambiente Utilizado
1. [Jupyter Notebook - PiP Version](https://jupyter.org/install)
2. [Notepad++](https://notepad-plus-plus.org/download/v7.6.3.html)
3. [Python 3.7.1](https://www.python.org/downloads/windows/)
4. [GitHub Desktop](https://desktop.github.com/)
5. [Chrome - Versão 72.0.3626.109](https://www.google.com/chrome/)
6. [Windows 10 Pro 64 bits](https://www.microsoft.com/pt-br/windows/get-windows-10)

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
- [Date - ISO](https://www.w3.org/TR/NOTE-datetime-970915.html)
- [Docs - Unittest](https://docs.python.org/3/library/unittest.html)