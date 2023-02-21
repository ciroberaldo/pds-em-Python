class Alinhamento():
    def __init__(self,valor , frase) -> None:

        self.valor = valor
        self.frase = frase

    def posicao(self,valor):
        return valor/0.352777

    def meioTitulo(self,valor1,valor2):
        return (valor1 - (valor2+6))/0.352777

    def meioMes(self,valor3,valor4):
        return (valor3 - (valor4+2))/0.352777


