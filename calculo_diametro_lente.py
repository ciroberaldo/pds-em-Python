
calibre = float(input("Digite a medida do calibre: "))
#vertical = float(input("Digite o valor da vertical: "))
diagonal = float(input("Digite o valor da Diagonal Maior: "))
ponte = float(input("Digite a medida da ponte: "))
dp = float(input("Gigite a medida do DP: "))

if diagonal > calibre + 4:
    diametro = float(diagonal + ponte - dp + diagonal + 4.0)
else:
    diametro = float(calibre + ponte - dp + calibre + 4.0)
 
print("Diametro ideal = ",diametro)
print("===========================")
print("Achando a Curva Base")

esferico = float(input("Digite o valor do grau Esferico: "))
cilindrico = float(input("Digite o valor do Cilindrico: "))

if cilindrico > 0  and esferico < 0: # esferico negativo / cilindrico positivo
    esferico = esferico + cilindrico
    cilindrico =  cilindrico * -1
    curva_base = float((esferico / 2) + 6)
    print(esferico, cilindrico)
    print("A Base é: ",curva_base)

elif esferico > 0 and cilindrico > 0: # esferico e cilindrico positivos
    esferico = esferico + cilindrico
    cilindrico = cilindrico * -1
    curva_base = float((esferico / 2) + 6)
    print("A Base é: ", curva_base)
    print(" + com +")

elif esferico < 0 and cilindrico < 0: # esferico e cilindrico negativo
    soma = esferico + cilindrico
    curva_base = float((soma / 2) + 6)
    print("A Base é: ", curva_base)
    print(" - com -")
else: # esferico positivo e cilindrico negativo
    curva_base = float((esferico / 2) + 5)
    print("A Base é: ", curva_base)
    print("senão")

print("===========================")
dicentracao = (calibre + ponte - dp) / 2
print("Dicentrar ", dicentracao, "mm")