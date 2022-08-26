import math


class Model:
    def __init__(self):
        self.notas = []
        self.Q = []
        self.A = []
        self.M = []
        self.soma = 0
        self.media = 0

    def getMedia(self):
        return self.media

    def setMedia(self, media):
        self.media = media

    def preencherNotas(self, nota):
        self.notas.append(nota)

    def calcularMedia(self):
        soma = 0
        for i in range(20):
            soma = soma + self.notas[i]
        self.setMedia(soma / 20)
        return self.getMedia()

    def contarVetor(self):
        contador = 0
        for i in range(20):
            if self.notas[i] > self.getMedia():
                contador = contador + 1
        return contador

    def preencherQ(self, num):
        self.Q.append(num)

    def maiorMenor(self):
        maior = self.Q[0]  # Posição 0 do vetor Q
        menor = self.Q[0]  # Posição 0 do vetor Q
        posicaoMaior = 0
        posicaoMenor = 0
        for i in range(20):
            if self.Q[i] > maior:
                maior = self.Q[i]  # Colentando o maior número do lista Q
                posicaoMaior = i  # Coletando a posição do maior elemento de Q
            elif self.Q[i] < menor:
                menor = self.Q[i]
                posicaoMenor = i
        return "O maior número do vetor Q é: {}, e ele está na posição: {} do vetor\nO menor número do vetor Q é: {}, e ele está na posição: {} do vetor".format(maior, int(posicaoMaior + 1), menor, int(posicaoMenor + 1))
    
    def preencherVetor(self, num):
        self.A.append(num)

    def preencherM(self, x):
        for i in range(10):
            self.M[i].appemd(int(self.A[i] * x))

    def mostraeM(self):
        msg = ""
        for i in range(10):
            msg = msg + "\n {}º posição: {}".format(int(i+1), self.M[i])
        return msg





