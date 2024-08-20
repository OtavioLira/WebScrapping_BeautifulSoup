# Acessando Filhos e Descendentes
from bs4 import BeautifulSoup

html_doc = "<html><body><p>Texto</p></body></html>"
soup = BeautifulSoup(html_doc, 'html.parser')

# Acessando filhos da tag <body>
body_tag = soup.body
print(body_tag.contents) # Saida: [<p>Texto</p>]

# Iterando sobre os filhos
for child in body_tag.children:
    print(child)  

# Acessando todos os descendentes

### Manipulando conteudo do texto
html_doc = """
<html><body>
<p>Texto 1</p>
<p>Texto 2</p>
<p>Texto 3</p>
</body></html>
"""

soup = BeautifulSoup(html_doc, "html.parser")

# Proximo irmão da primeira tag <p>
first_p = soup.p
next_p = first_p.find_next_sibling("p")

print(next_p.text) # Saída: Texto 2
previous_p = next_p.find_previous_sibling("p")
print(previous_p.text) # Saída: Texto 1

### Navegando Entre Elementos Adjacentes
html_doc = """
<html><body>
<p>Texto 1</p>
<a href='#'>Link</a>
<p>Texto 2</p>
</body></html>
"""

soup = BeautifulSoup(html_doc, "html.parser")