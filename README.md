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

<h2> Criando a ferramenta </h2>
<p> Fiz a importação das bibliotecas requests e BeautifulSoup para o scraping no meu site </p>

```python
import requests 
from bs4 import BeautifulSoup 

pagina = requests.get("https://oander.site")
soup = BeautifulSoup(pagina.text, features="html.parser")

```

<p> Definindo algumas funções, procurando por tags </p>

```python

def scraping():
  if pagina.status_code == 200:
    print(pagina.content)
  else:
      print("HTTP error",pagina.status_code)

def text():
   print(soup)

def title():
   print('')
   print(soup.title)
   print('')

def head():
   print('')
   head_ =soup.find('head')
   print(head_)

def meta():
   css_ = soup.find_all('meta')
   print(css_)

def script():
   print ('')
   s =soup.find_all('script')
   print(s)

def links():
   print ('')
   hf = soup.find_all('a')
   print(hf)

```
