<h1> Web Scraping </h1>

Utilizando a biblioteca beautifulsoup4

<strong> Descrição: </strong>
<p>O BeautifulSoup é uma biblioteca Python popular para extrair dados de documentos HTML e XML. Ele oferece uma interface simples e poderosa para analisar e navegar na estrutura da árvore do documento.</p>

<strong> Instalação: </strong>
```
pip install beautifulsoup4
```

<strong> Importando a biblioteca: </strong>

```python
from bs4 import BeautifulSoup
```

<strong> Carregando o conteúdo: </strong>
<p> Você pode carregar o conteúdo de um arquivo HTML ou de uma string HTML:</p>

``` python 
with open('arquivo.html', 'r') as f:
    html_content = f.read()
```

<strong> Carregando de uma string: </strong>

``` python
html_content = """
<html>
<head>
    <title>Exemplo</title>
</head>
<body>
    <p>Este é um parágrafo.</p>
</body>
</html>
"""
```
<strong> Criando o analisador: </strong>
<p> Crie um objeto BeautifulSoup para analisar o conteúdo:</p>

``` python
soup = BeautifulSoup(html_content, 'html.parser')
```

<strong> Navegando na estrutura: </strong>
<p> O objeto soup representa a árvore do documento. Você pode navegar pela estrutura usando diversos métodos:</p>

<ol>
<li>find(): Encontra a primeira tag correspondente a um seletor CSS.</li>
<li>findAll(): Encontra todas as tags correspondentes a um seletor CSS.</li>
<li>find_parent(): Encontra a tag pai de uma tag específica.</li>
<li>find_next_sibling(): Encontra a próxima tag irmã de uma tag específica.</li>
<li>find_previous_sibling(): Encontra a tag irmã anterior de uma tag específica.</li>
</ol>
