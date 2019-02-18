# Entrevista de Estágio Justiça Fácil - Desafio

## Problema

Os [diários oficiais](https://pt.wikipedia.org/wiki/Di%C3%A1rio_Oficial) são jornais criados, mantidos e administrados por governos para publicar as literaturas dos atos oficiais da administração pública executiva, legislativa e judiciária.

Todos os dias, a equipe de Processamento tem que verificar se os diários do [Tribunal Superior Eleitoral](http://www.tse.jus.br/servicos-judiciais/publicacoes-oficiais/diario-da-justica-eletronico/diario-da-justica-eletronico-1) foram baixados corretamente. A equipe já tem a data, edição e [hash MD5](https://pt.wikipedia.org/wiki/MD5) do arquivo PDF do caderno, e precisam de um sistema auxiliar para realizar a conferência dos cadernos baixados pelo Processamento, ou seja, um sistema que receba uma data e retorne os MD5 dos cadernos daquele dia.

## Interface esperada

O candidato deve criar uma função que receba uma data de publicação e retorne uma lista de hash MD5 dos PDFs dos cadernos publicados na data buscada.

O código deve ser escrito preferencialmente em Python.

## Critérios avaliados

Abaixo estão os critérios utilizados (por ordem de importância) para avaliar os candidatos:

1. **Relatório do desenvolvimento**, constando, pelo menos: dificuldades encontradas, justificativas dos métodos utilizados, fontes de pesquisa acessadas;
2. **Versionamento de todo o código desenvolvido**: o código deve estar em um repositório público e observando as boas práticas de versionamento;
3. **Documentação** contendo no mínimo uma explicação básica do projeto e como executá-lo;
4. **O sistema desenvolvido deve estar funcionando conforme o esperado**, com uma boa estrutura e observando as boas práticas de desenvolvimento.

## Extras

Os itens abaixo serão considerados como bônus:

- Testes automatizados;
- Salvar os resultados de forma persistente e reaproveitável;
- Melhorias propostas pelo candidato.

Toda a documentação e relatório deve ser feita em [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) e estar no mesmo repositório do projeto.
