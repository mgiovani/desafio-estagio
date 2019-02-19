# Documentação - Desafio

### Executando Projeto

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

### Executando Testes

1. Para clonar o repositório basta usar o seguinte comando no diretório escolhido:
```sh
$ git clone https://github.com/mgiovani/desafio-estagio.git
```

2. Dentro da pasta raiz do repositório a seguinte chamada inicia a  chamadas dos testes:
```sh
$ python Testes.py
```

3. Enquanto o código está sendo executado é exibido um feedback de cada teste que está sendo executado:
```sh

```

### Exceções e Retornos

| Retorno | Erro |
| ------ | ------ |
| [] | Nenhum diário publicado nesta data (inclui datas futuras) |
| Request nao realizado | Não foi possível fazer o request (principal causa: sem conexão com a internet) |
| Formato de data incorreto | A entrada não foi informada no formato ISO |
| 100 <= Retorno >= 505 | [HTTP Response Codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) |
