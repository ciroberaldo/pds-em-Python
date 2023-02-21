import csv

soma = 0
titulos = {}
valores = {}
tabelas = list()
nomeoticas = ('otica-visiolux','otica-central', 'otica-teffe', 'otica-prado', 'otica-clauss', 'parque-otica', 'otica-perfil',
              'otica-zonatto', 'otica-ampla-visao', 'otica-miraluz', 'otica-visoluz', 'otica-anita','otica-malosti',
              'otica-marine', 'otica-marin', 'visao-araucaria','mercadao-fazenda', 'estilo-visao', 'preco-popular-posto',
              'preco-popular-portao','klim-otica','preco-popular-duda-loja3', 'otica-sao-braz', 'opticolor', 'outlet-dos-oculos',
              'exame-visao','laboratorio-universo', 'preco-popular-cic', 'sao-braz-orleans', 'sao-braz-ponto-final',
              'preco-pop-fazenda','top-vision', 'preco-pop-alm-tamandare', 'vista-alegre')
for z in range(len(nomeoticas)):
    with open("entrada de pedidos janeiro 2023 - Respostas ao formulário 1.csv", "r") as file:
        reader = csv.DictReader(file)  # usando a função csv
        # next(reader)  # ignorando a primeira coluna
        for row in reader:
            dataa = row["Data"].strip()
            otica = row["otica"].strip()
            servico = row["servicos"].strip()
            valor = row["valor"]
            if otica == nomeoticas[z]:
                tabelas.append(dataa)
                tabelas.append(servico)
                tabelas.append(valor)

    pula = 0
    somaotica = 0

    # escrevendo o arquivo .csv
    arq = open(nomeoticas[z] + ".csv", "a")
    arq.write("Data,Servico,Valor" + '\n')
    arq.close()

    for c in tabelas:
        arq = open(nomeoticas[z] + ".csv", "a")
        if pula == 2:
            arq.write(c + '\n')
            somaotica = somaotica + float(c)
            pula = 0
        else:
            arq.write(c + ',')
            pula = pula + 1
        arq.close()

    arq = open(nomeoticas[z] + ".csv", "a")
    arq.write(str(somaotica))
    arq.close()
    tabelas.clear()

with open("entrada de pedidos janeiro 2023 - Respostas ao formulário 1.csv", "r") as file:
    reader = csv.DictReader(file)  # usando a função csv
    # next(reader)  # ignorando a primeira coluna
    for row in reader:
        otica = row["otica"].strip()
        valor = row["valor"]
        soma = soma + float(valor)
        if otica in valores:  # dicionario
            valores[otica] = valores[otica] + float(row["valor"])
        if otica not in titulos:  # dicionario
            titulos[otica] = 0
            valores[otica] = float(row["valor"])
        titulos[otica] += 1

# lista do fechamentos no console
print('-' * 30)
print('FEFECHAMENTO DAS ÓTICAS')
print('-' * 30)
for i in valores:
    print(f'{i} = {valores[i]:.2f}')
print(soma)
print(titulos)
