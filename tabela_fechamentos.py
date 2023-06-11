import csv

tabelas = list()

nomeoticas = ('otica-visiolux','otica-central', 'otica-teffe', 'otica-prado', 'otica-clauss', 'parque-otica', 'otica-perfil',
              'otica-zonatto', 'otica-ampla-visao', 'otica-miraluz', 'otica-visoluz', 'otica-anita','otica-malosti',
              'otica-marine', 'otica-marin', 'visao-araucaria','mercadao-fazenda', 'estilo-visao', 'preco-popular-posto',
              'preco-popular-portao','klim-otica','preco-popular-duda-loja3', 'otica-sao-braz', 'opticolor', 'outlet-dos-oculos',
              'exame-visao','laboratorio-universo', 'preco-popular-cic', 'sao-braz-orleans', 'sao-braz-ponto-final',
              'preco-pop-fazenda','top-vision', 'preco-pop-alm-tamandare', 'vista-alegre','otica-ipanema','otica-viena')


    #montando a tabela
fechamento_anterior = 0
somatotal = 0

for z in range(len(nomeoticas)):
    with open("pedidos_maio_2023 - Respostas ao formulário 1.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            otica = row["otica"].strip()
            servico = row["servicos"].strip()
            valor = row["valor"]
            if otica == nomeoticas[z] and servico == "fechamento anterior":
                fechamento_anterior = int(valor)
            if otica == nomeoticas[z]:
                nome = otica
                somatotal = somatotal + int(valor)
        
        if somatotal == 0:
            nome = nomeoticas[z]        
        tabelas.append(nome)
        tabelas.append(somatotal)
        somatotal = 0
        if fechamento_anterior > 0:
            tabelas.append(fechamento_anterior)
            fechamento_anterior = 0
        else:
            tabelas.append("ok")

pula = 0
# escrevendo o arquivo .csv
arq = open("tabela_fechamentos.csv", "a")
arq.write("Otica,Valor,Fechamento-Anterior" + '\n')
arq.close()

for c in tabelas:
    arq = open("tabela_fechamentos.csv", "a")
    if pula == 2:
        arq.write(str(c) + '\n')
        pula = 0
    elif pula == 1:
        arq.write(str(c) + ',')
        pula = 2
    elif pula == 0:
        arq.write(str(c) + ',')
        pula = 1
    arq.close()


print(tabelas)


