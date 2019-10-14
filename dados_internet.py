#importa a funcao de acessar e ler o html da pagina
from urllib.request import urlopen

url = "http://blog.conradosaud.com.br/exemplos/scrapingSimples.html"
pagina = urlopen(url)
texto = pagina.read().decode('utf8')

#remove os espacamentos da tecla TAB
texto = texto.replace("\t", "")

#remove a quebra de linha
lista = texto.split("\n")

#cria variaveis globais para criar csv
nomeProduto = ""
nomeMarca = ""
precoVista = ""
precoParcelado = ""
csv = []

#padrao para encontrar o nome do produto
htmlNomeProduto1 = '<div class="row">'
htmlNomeProduto2 = '<p class="lead">'

#padrao para encontrar o nome da marca
htmlInicioMarca = '<p><strong>'
htmlFimMarca = '</strong></p>'

#padrao para encontrar os precos
htmlVista = 'precoVista">'
htmlParcelado = 'precoParcelado">'

contador = 0

while contador < len(lista):
    
    #encontra nome do produto
    if lista[contador] == htmlNomeProduto1:
        if lista[contador+1].startswith(htmlNomeProduto2):
            nEncontrado1 = 1 + (lista[contador+1].index(">"))
            nEncontrado2 = lista[contador+1].index("</p>")
            
            nomeProduto = lista[contador+1][nEncontrado1:nEncontrado2]
            
    #encontra nome da marca
    if lista[contador].startswith(htmlInicioMarca):
        nEncontrado1 = len(htmlInicioMarca) + (lista[contador].index(htmlInicioMarca))
        nEncontrado2 = lista[contador].index(htmlFimMarca)
        
        nomeMarca = lista[contador][nEncontrado1:nEncontrado2]
        
    #encontra precos
    if lista[contador].find(htmlVista) != -1:

        #preco a vista
        nEncontrado1 = len(htmlVista) + (lista[contador].find(htmlVista))
        nEncontrado2 = 0
        
        contadorAux = nEncontrado1
        while(contadorAux < len(lista[contador])):
            if(lista[contador][contadorAux:contadorAux+1] == "<"):
                nEncontrado2 = contadorAux
                break
            contadorAux += 1

        precoVista = lista[contador][nEncontrado1:nEncontrado2]
        
	#preco parcelado
        nEncontrado1 = len(htmlParcelado) + (lista[contador].find(htmlParcelado))
        nEncontrado2 = 0

        contadorAux = nEncontrado1
        while(contadorAux < len(lista[contador])):
            if(lista[contador][contadorAux:contadorAux+1] == "<"):
                nEncontrado2 = contadorAux
                break
            contadorAux += 1

        precoParcelado = lista[contador][nEncontrado1:nEncontrado2]

    #verifica se todas variaveis foram preenchidas para adicionar ao csv
    if len(nomeProduto) > 1 and len(nomeMarca) > 1 and len(precoVista) > 1 and len(precoParcelado) > 1:
        csvAux = nomeProduto+";"+nomeMarca+";"+precoVista+";"+precoParcelado+";"
        csv.append(csvAux)

        #zera variaveis para que a proxima verificacao seja valida
        nomeProduto = ""
        nomeMarca = ""
        precoVista = ""
        precoParcelado = ""
    
    contador+=1
    

#csv criado com sucesso!
for item in csv:
    print(item)