import csv

tabelas = list()

nomeoticas = ('otica-visiolux','otica-central', 'otica-teffe', 'otica-prado', 'otica-perfil',
              'otica-zonatto', 'otica-ampla-visao', 'otica-visoluz', 'otica-anita','otica-malosti',
              'otica-marine', 'otica-marin', 'visao-araucaria','estilo-visao','klim-otica','preco-popular-duda-loja3',
              'otica-sao-braz', 'opticolor', 'outlet-dos-oculos','exame-visao', 'preco-popular-cic', 'sao-braz-ecoville',
              ,'preco-pop-fazenda', 'preco-pop-alm-tamandare', 'vista-alegre','otica-ipanema','otica-viena'
              ,'visao-hauer','scarpim','soho-vision','isa-batel','martini')


    #montando a tabela
fechamento_anterior = 0
somatotal = 0

for z in range(len(nomeoticas)):
    with open("entrada de pedidos Novembro2024 (respostas) - Respostas ao formulário 1.csv", "r") as file:
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


