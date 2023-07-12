import csv

#Função que calcula os pontos violentos e pontos não violentos por cidade e acumula eles     
def calc_crimes(csv_reader,pontos_violentos,pontos_nao_violentos):
    for linha in csv_reader: #Laço de repetição para calcular os pontos violentos e não violentos de cada linha do arquivo
        #CRIME VIOLENTOS
        pontos_violentos = pontos_violentos + (int(linha['Vitimas de Homicidio Doloso']) * 10)
        pontos_violentos = pontos_violentos + (int(linha["Vitimas de Latrocinio"]) * 10)
        pontos_violentos = pontos_violentos + (int(linha["Vitimas de Lesao Corp Seg Morte"]) * 10)
        pontos_violentos = pontos_violentos + (int(linha[" Roubo de Veiculo"]) * 3)
        pontos_violentos = pontos_violentos + (int(linha[" Roubos"]) * 2 )
        pontos_violentos = pontos_violentos + (int(linha[" Delitos Relacionados a Armas e Municoes"]) * 2)
        pontos_violentos = pontos_violentos + (int(linha[" Entorpecentes Trafico"]) * 5)

        #CRIMES NAO VIOLENTOS
        pontos_nao_violentos = pontos_nao_violentos + (int(linha[" Entorpecentes Posse"]) * 2)
        
        pontos_nao_violentos = pontos_nao_violentos + (int(linha["Furto de Veiculo "]) * 3)
        pontos_nao_violentos = pontos_nao_violentos + (int(linha[" Furtos"]) * 3)
        pontos_nao_violentos = pontos_nao_violentos + (int(linha[" Estelionato"]) * 1)

    return pontos_violentos,pontos_nao_violentos #retorna a soma dos pontos violentos e dos pontos não violentos do arquivo inteiro


#Função que calcula os pontos violentos e pontos não violentos por cidade em cada arquivo
def calc_pontos_cidades(csv_reader,cidade_pontos_violentos,cidade_pontos_nao_violentos):
    for linha in csv_reader:#Laço de repetição para calcular e adicionar em um variável os pontos violentos e não violentos de cada linha do arquivo
        pontos_violentos = (
            int(linha['Vitimas de Homicidio Doloso']) * 10 +
            int(linha['Vitimas de Latrocinio']) * 10 +
            int(linha['Vitimas de Lesao Corp Seg Morte']) * 10 +
            int(linha[' Roubo de Veiculo']) * 3 +
            int(linha[' Roubos']) * 2 +
            int(linha[' Delitos Relacionados a Armas e Municoes']) * 2 +
            int(linha[' Entorpecentes Trafico']) * 5
        )
        
        pontos_nao_violentos = (
            int(linha[' Entorpecentes Posse']) * 2 +
            int(linha['Furto de Veiculo ']) * 3 +
            int(linha[' Furtos']) * 3 +
            int(linha[' Estelionato']) * 1
        )
        
        cidade = linha['Municipios']
        
        #adicionar em um calendário a cidade e a pontuação dos pontos violentos e não violentos dessa cidade 
        cidade_pontos_violentos[cidade] = pontos_violentos 
        cidade_pontos_nao_violentos[cidade] = pontos_nao_violentos

    return cidade_pontos_violentos,cidade_pontos_nao_violentos #Retornar 2 calendários, contendo as cidades como chave e os pontos violentos e não violentos como valor


#Função que imprimi o rank das cidades
def imprimir(top_n,reverse,rank):
    x = 0
    top_n_cidades = sorted(rank, key=rank.get, reverse=reverse)[:top_n] # A lista top_n_cidades vai receber a lista de cidades contendo os seus pontos violentos ou pontos não violentos e podendo determinar pela variável reverse se quer que a lista seja crescente ou descrescente, e podendo determinar pela variável top_n qual a quantidade de cidades que deseja adicionar na lista.

    for cidade in top_n_cidades: #Laço de repetição para imprimir o ranking: 
        x = x + 1 #Variável que vai ser usado para imprimir a posição que a cidade está no ranking
        rank1 = rank[cidade]
        print(f'{x}- {cidade}: Pontos Violentos - {rank1}')
        rank[cidade] = rank1
             
    return rank


def main():

    #ARQUIVO JAN 2021
    with open("jan-21.csv", "r", encoding="utf-8") as arquivo:
        csv_reader = csv.DictReader(arquivo, delimiter=";")
        pontos_violentos = 0
        pontos_nao_violentos= 0
        pontos_violentos,pontos_nao_violentos = calc_crimes(csv_reader,pontos_violentos,pontos_nao_violentos)
        crimes_violentos_2021 = pontos_violentos
        crimes_nao_violentos_2021 = pontos_nao_violentos 
    

    #ARQUIVO JAN 2022
    with open("jan-22.csv", "r", encoding="utf-8") as arquivo:
        pontos_violentos = 0
        pontos_nao_violentos= 0
        csv_reader = csv.DictReader(arquivo, delimiter=";")
        pontos_violentos,pontos_nao_violentos = calc_crimes(csv_reader,pontos_violentos,pontos_nao_violentos)
        crimes_violentos_2022 = pontos_violentos
        crimes_nao_violentos_2022 = pontos_nao_violentos 
    

    #ARQUIVO JAN 2023
    with open("jan-23.csv", "r", encoding="utf-8") as arquivo:
        pontos_violentos = 0
        pontos_nao_violentos= 0
        csv_reader = csv.DictReader(arquivo, delimiter=";")
        pontos_violentos,pontos_nao_violentos = calc_crimes(csv_reader,pontos_violentos,pontos_nao_violentos)
        crimes_violentos_2023 = pontos_violentos
        crimes_nao_violentos_2023 = pontos_nao_violentos 


    crimes_violentos = {"2021":crimes_violentos_2021, "2022": crimes_violentos_2022, "2023": crimes_violentos_2023}
    crimes_nao_violentos = {"2021":crimes_nao_violentos_2021, "2022": crimes_nao_violentos_2022, "2023": crimes_nao_violentos_2023}
    print("---------------------------------------------------")
    print("Indicadores globais por ano")
    print("---------------------------------------------------")
    print("Crimes Violentos")
    print("- 2021:",crimes_violentos["2021"])
    print("- 2022:",crimes_violentos["2022"])
    print("- 2023:",crimes_violentos["2023"])
    print()
    print("Crimes Não Violentos")
    print("- 2021:",crimes_nao_violentos["2021"])
    print("- 2022:",crimes_nao_violentos["2022"])
    print("- 2023:",crimes_nao_violentos["2023"])


    #Abre os 3 arquivos no modo de leitura
    with open('jan-21.csv', 'r', encoding='utf-8') as arquivo21,open('jan-22.csv', 'r', encoding='utf-8') as arquivo22,open('jan-23.csv', 'r', encoding='utf-8') as arquivo23:
        lista_arq = [arquivo21,arquivo22,arquivo23] #Adiciona os 3 arquivos em uma lista
        cidade_pontos_violentos = {}
        cidade_pontos_nao_violentos = {}
        pontos_violentos = {}
        pontos_nao_violentos = {}
        for arquivo in lista_arq:#Laço de repetição para que leia cada arquivo que esteja na lista de arquivos
            csv_reader = csv.DictReader(arquivo, delimiter=";")
            cidade_pontos_violentos,cidade_pontos_nao_violentos = calc_pontos_cidades(csv_reader,cidade_pontos_violentos,cidade_pontos_nao_violentos) #Retornar os dicionarios cidade_pontos_violentos e cidade_pontos_nao_violentos calculados na função calc_pontos_cidades
            
            
            for cidade in cidade_pontos_violentos: #Laço de repetição para cada cidade que esteja dentro do dicionário de cidade_pontos_violentos
            
            
                if cidade in pontos_violentos: #Verificar se a cidade está no dicionário que vamos armazenar a cidade e os pontos violentos dos (3 ARQUIVOS)
                    pontos_violentos[cidade] += cidade_pontos_violentos[cidade] #Caso a cidade esteja no dicionário, adicionamos os pontos acumulando eles, para que tenha os pontos dos 3 arquivos daquela cidade

                else: #Caso a cidade não esteja no dicionário, adicionamos a cidade e pontos daquele cidade
                    pontos_violentos[cidade] = cidade_pontos_violentos[cidade]

            for cidade in cidade_pontos_nao_violentos: #Laço de repetição para cada cidade que esteja dentro do dicionário de cidade_pontos_nao_violentos

                if cidade in pontos_nao_violentos: #Verificar se a cidade está no dicionário que vamos armazenar a cidade e os pontos violentos dos (3 ARQUIVOS)
                    pontos_nao_violentos[cidade] += cidade_pontos_nao_violentos[cidade]#Caso a cidade esteja no dicionário, adicionamos os pontos acumulando eles, para que tenha os pontos dos 3 arquivos daquela cidade

                else:#Caso a cidade não esteja no dicionário, adicionamos a cidade e pontos daquele cidade
                    pontos_nao_violentos[cidade] = cidade_pontos_nao_violentos[cidade]
                

    print()
    print()
    print()
    

    #Imprimir top 20 cidades com maiores indices de crimes violentos
    print("#####################################################################")
    print("Listar as top 20 cidades com maiores indices de crimes violentos")
    print("#####################################################################")
    rank = imprimir(20,True,pontos_violentos)
    print()
    print()

    #Imprimir top 15 cidades com menores indices de crimes violentos
    print("#####################################################################")
    print("Listar as top 15 cidades com menores indices de crimes violentos")
    print("#####################################################################")
    rank = imprimir(15,False,pontos_violentos)
    print()
    print()

    #Imprimir top 50 cidades com maiores indices de crimes não violentos
    print("#####################################################################")
    print("Listar as top 50 cidades com maiores indices de crimes não violentos ")
    print("#####################################################################")
    rank = imprimir(50,True,pontos_nao_violentos)
    print()
    print()

    #Imprimir top 7 cidades com menores indices de crimes não violentos
    print("#####################################################################")
    print("Listar as top 7 cidades com menores indices de crimes não violentos ")
    print("#####################################################################")
    rank = imprimir(7,False,pontos_nao_violentos)
    print()
    print()

    import json
    #Salvando JSON crimes violentos
    try:
        with open("crimes_violentos.json", "w") as arquivo:
            json.dump(pontos_violentos, arquivo,indent=4)

    except OSError:
        print("Erro ao salvar")

    #Salvando JSON crimes não violentos
    try:
        with open("crimes_nao_violentos.json", "w") as arquivo:
            json.dump(pontos_nao_violentos, arquivo,indent=4)

    except OSError:
        print("Erro ao salvar")


main()      
            