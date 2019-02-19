# Documentação - Desafio

## Problema Recebido

Os [diários oficiais](https://pt.wikipedia.org/wiki/Di%C3%A1rio_Oficial) são jornais criados, mantidos e administrados por governos para publicar as literaturas dos atos oficiais da administração pública executiva, legislativa e judiciária.
Todos os dias, a equipe de Processamento tem que verificar se os diários do [Tribunal Superior Eleitoral](http://www.tse.jus.br/servicos-judiciais/publicacoes-oficiais/diario-da-justica-eletronico/diario-da-justica-eletronico-1) foram baixados corretamente. A equipe já tem a data, edição e [hash MD5](https://pt.wikipedia.org/wiki/MD5) do arquivo PDF do caderno, e precisam de um sistema auxiliar para realizar a conferência dos cadernos baixados pelo Processamento, ou seja, um sistema que receba uma data e retorne os MD5 dos cadernos daquele dia.

## Solução Proposta

A solução é um conjunto de funções que recebe uma data no formato ISO e retorna uma lista dos MD5 dos PDF's daquele dia, assim como proposto. Para isso são utilizadas um GET direto ao site do TSE que retorna os diários daquele dia e é feito um POST para cada um deles a fim de se obter o PDF referente. Com este PDF em mãos o hash é facilmente extraído e adicionando em um banco de dados SQLite para acelerar consultas com mesmo resultado e não realizar processamento desnecessário. Isso compõe o fluxo principal das funções que contam com lançamentos de algumas exceções descritas posteriormente.

## Requisitos
1. Python 3.X.X
2. Módulos Python:
	1. requests
	2. sqlite3
	3. os
	4. time
	5. hashlib
	6. shutil
	7. datetime
	8. bs4


## Executando Projeto

1. Para clonar o repositório basta usar o seguinte comando no diretório escolhido:
```sh
$ git clone https://github.com/mgiovani/desafio-estagio.git
```

2. Dentro da pasta raiz do repositório a seguinte chamada inicia a execução:
```sh
$ python Desafio.py
```

3. Enquanto o código está sendo executado a entrada é composta por uma data no formato [ISO 8601](https://www.w3.org/TR/NOTE-datetime-970915.html) (AAAA-MM-DD) e o fim da sua execução é determinado quando recebe uma data vazia (apenas Enter).
```sh
Data no formato ISO (AAAA-MM-DD): 2019-02-19
```

4. O retorno da função é uma lista de MD5 dos PDF's publicados naquela data.
```sh
['48e299a1aa1b22052ca6d9182a76e9db']
```

## Executando Testes

1. Para clonar o repositório basta usar o seguinte comando no diretório escolhido:
```sh
$ git clone https://github.com/mgiovani/desafio-estagio.git
```

2. Dentro da pasta raiz do repositório a seguinte chamada inicia a  chamadas dos testes:
```sh
$ python Testes.py
```

3. Enquanto o código está sendo executado é exibido um feedback dos testes realizados e caso esteja tudo certo será mostrado algo como:
```sh
........
----------------------------------------------------------------------
Ran 8 tests in 0.259s
OK
```
	
## Executando Preload

1. Para clonar o repositório basta usar o seguinte comando no diretório escolhido:
```sh
$ git clone https://github.com/mgiovani/desafio-estagio.git
```

2. Para alterar o período do preload (padrão de 1 ano) basta alterar as seguintes variáveis do arquivo PreLoad.py:
```python
dataInicial = date(2018, 1, 1)
dataFinal = date(2019, 2, 28)
```

3. Dentro da pasta raiz do repositório a seguinte chamada inicia o preload:
```sh
$ python PreLoad.py
```

4. Enquanto o código está sendo executado será mostrado algo como:
```sh
2018-01-01 []
2018-01-02 ['36ea65471a94bbcff2242c70e0c00b65']
2018-01-03 ['f11c228ca9ece4ede7a65c6386e68d4f']
2018-01-04 ['1d137000a73818371682c7fecad5b583']
2018-01-05 ['32181366f209bda57cbf4f042c89eb89']
```

## Exceções e Retornos

| Retorno | Erro |
| ------ | ------ |
| [] | Nenhum diário publicado nesta data (inclui datas futuras) |
| Request nao realizado | Não foi possível fazer o request (principal causa: sem conexão com a internet) |
| Formato de data incorreto | A entrada não foi informada no formato ISO |
| 100 <= Retorno >= 505 | [HTTP Response Codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) |
