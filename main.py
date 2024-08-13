from bs4 import BeautifulSoup, Comment

# Carregando o contéudo HTML
html_doc = """
<html><head><title>Título da página</title></head>
<body><p class="titulo">Este é um parágrafo.</p></body></html>
"""

# Inicializando o BeautifulSoup com lxml
soup = BeautifulSoup(html_doc, "lxml")

# Acessando o título da página
title = soup.title
#print(title.text) # Saída: Título da Página

# Acessando parágrafos e classes
p = soup.find("p", class_="titulo")
#print(p.text)

soup = BeautifulSoup("""<html>

<body>
    <p class='titulo'>Este é um parágrafo.</p>
    <p>texto</p>
    <a href="https://www.google.com"></a>
    <img src="https://www.w3schools.com/images/lamp.jpg" alt="Lamp" width="32" height="32">
    <!-- This is a comment -->
</body>

</html>""","html.parser")
#print(soup.p)

text = soup.body.string # Retorna o texto dentro de uma tag
comment = soup.find(string=lambda text: isinstance(text, Comment))
#print(comment)

# Encontrando todas as tags <a> (links)
links = soup.find_all("a")
print([link.get("href") for link in links])

# Acessando atributos
img = soup.find("img")
print(img["src"]) # Acessando o atributo 'src'