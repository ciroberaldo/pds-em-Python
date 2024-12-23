import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from alinhamentos import Alinhamento


tabelas = list()

nomeoticas = ('otica-visiolux','otica-central', 'otica-teffe', 'otica-prado', 'otica-perfil',
              'otica-zonatto', 'otica-ampla-visao', 'otica-visoluz', 'otica-anita','otica-malosti',
              'otica-marine', 'otica-marin', 'visao-araucaria','estilo-visao','klim-otica','preco-popular-duda-loja3',
              'otica-sao-braz', 'opticolor', 'outlet-dos-oculos','exame-visao', 'preco-popular-cic', 'sao-braz-ecoville',
              ,'preco-pop-fazenda', 'preco-pop-alm-tamandare', 'vista-alegre','otica-ipanema','otica-viena'
              ,'visao-hauer','scarpim','soho-vision','isa-batel','martini')


grid = Alinhamento(105,0)

img_file = 'logo.png'
mes = "Novembro"

    #montando a tabela

for z in range(len(nomeoticas)):
    with open("entrada de pedidos Novembro2024 (respostas) - Respostas ao formulário 1.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dataa = row["Data"].strip()
            otica = row["otica"].strip()
            servico = row["servicos"].strip()
            valor = row["valor"]
            if otica == nomeoticas[z]:
                tabelas.append(dataa)
                tabelas.append(servico)
                tabelas.append(valor)
          
    #iniciando a montagem do pdf      

    loja = "Fechamento {}".format(nomeoticas[z])
    nome_pdf = loja
    pdf = canvas.Canvas('{}.pdf'.format(nome_pdf), pagesize=A4)

    pdf.drawImage(img_file, grid.posicao(89.8), grid.posicao(241), width=grid.posicao(30), height=grid.posicao(30))

    pdf.setTitle(nome_pdf)


    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(grid.meioTitulo(105,float(len(loja))),grid.posicao(235), loja)

    pdf.setFillColorRGB(0.28, 0.28, 0.28)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(grid.meioMes(105,float(len(mes))),grid.posicao(228), mes)

    pdf.setFillColorRGB(0.95, 0.71, 0.19)
    pdf.rect(grid.posicao(30),grid.posicao(218.5), width = grid.posicao(147),height = grid.posicao(6), stroke = 1, fill = 1)
    pdf.setFillColor(colors.black)
    pdf.line(grid.posicao(60),grid.posicao(224.5),grid.posicao(60),grid.posicao(218))
    pdf.line(grid.posicao(152),grid.posicao(224.5),grid.posicao(152),grid.posicao(218))
    
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(grid.posicao(40),grid.posicao(220),"Data")
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(grid.posicao(97),grid.posicao(220),"Serviço")
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(grid.posicao(160),grid.posicao(220),"Valor")

    linhaY = 212
    linhaX = 40
    pula = 0
    somatotal = 0

    for palavra in tabelas:
        if pula == 0:
            linhaX = 35            
            pdf.rect(grid.posicao(30),grid.posicao(linhaY), width = grid.posicao(147),height = grid.posicao(6), stroke = 1, fill = 0)

            pdf.line(grid.posicao(60),grid.posicao(linhaY),grid.posicao(60),grid.posicao(linhaY+6))
            pdf.line(grid.posicao(152),grid.posicao(linhaY),grid.posicao(152),grid.posicao(linhaY+6))

            pdf.setFont("Helvetica", 10)
            pdf.drawString(grid.posicao(linhaX),grid.posicao(linhaY+1.5),palavra)

            pula = pula + 1
        elif pula == 1:
            linhaX = 98
            
            pdf.setFont("Helvetica", 10)
            if len(palavra) > 15:
                pdf.drawString(grid.posicao(linhaX-int(len(palavra)/2)),grid.posicao(linhaY+1.5),palavra)
            else:
                pdf.drawString(grid.posicao(linhaX),grid.posicao(linhaY+1.5),palavra)

            pula = pula + 1
        elif pula == 2:
            linhaX = 157
            pdf.setFont("Helvetica", 10)

            if len(palavra) == 1:
                pdf.drawString(grid.posicao(linhaX + 0.9),grid.posicao(linhaY+1.5),"R$ {},00".format(palavra))
            else:
                pdf.drawString(grid.posicao(linhaX),grid.posicao(linhaY+1.5),"R$ {},00".format(palavra))

            somatotal = somatotal + int(palavra)
            pula = 0
            linhaY = linhaY - 6
            

    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(grid.posicao(91),grid.posicao(linhaY - 5),"Valor R$ {},00".format(somatotal))

    pdf.showPage()
    pdf.save()
    somatotal = 0
    tabelas.clear()


