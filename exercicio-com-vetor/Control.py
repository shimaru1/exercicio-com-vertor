from Model import Model


class Control:
    def __init__(self):
        self.model = Model()
        self.opcao = - 1

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("\n\n\nEscolha uma das opções abaixo: \n" +
              "\n0. Sair" +
              "\n1. Exercício 01" +
              "\n2. Exercício 02 e Exercício 03" +
              "\n3. Exercício 04" +
              "\n4. Exercício 05" +
              "\n5. Exercício 06" +
              "\n6. Exercício 07" +
              "\n7. Exercicio 08" +
              "\n8. Exercício 09" +
              "\n9. Exercicio 10 " +
              "\n10. Exercício 11" +
              "\n11. Exercício 12" +
              "\n12. Exercício 13")
        self.setOpcao(int(input()))

    def operacao(self):
        while (self.getOpcao() != 0):
            self.menu()
            if self.getOpcao() == 0:
                print("obrigado!")
            elif self.getOpcao() == 1:
                self.exercicio1()
            elif self.getOpcao() == 2:
                self.exercicio2()
            elif self.getOpcao() == 3:
                self.exercicio4()
            else:
                print("Opção invalida!")

    def exercicio1(self):
        for i in range(20):
            print("informe a {}º nota: ".format(int(i + 1)))
            nota = float(input())

            while (nota < 0) or (nota > 10):
                print("Nota Invalida, digite novamente!")
                nota = float(input())
            self.model.preencherNotas(nota)
        print("A media das notas é: {}".format(self.model.calcularMedia()))
        print("Há {} notas maiores que a média".format(self.model.contarVetor()))

    def exercicio2(self):
        for i in range(20):
            print("informe o {}º número: ".format(int(i + 1)))
            num = float(input())
            while num < 0:
                print("Nota Invalida, digite novamente!")
                num = float(input())
                self.model.preencherQ(num)
        print(self.model.maiorMenor())

    def exercicio4(self):
        for i in range(10):
            print("informe a {}º nota: ".format(int(i + 1)))
            num = float(input())
            self.model.preencherVetor(num)
        print("informe um número que será o multiplicador")
        x = int(input())
        self.model.preencherM(x)
        print(self.model.mostraeM())

