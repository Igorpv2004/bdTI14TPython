from Model import Model

class Control:
    def __init__(self):
        self.opcao = -1
        self.modelo = Model()

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def Menu(self):
        print("Escolha uma das opções abaixo: \n"   +
              "\n0. Sair"                           +
              "\n1. Cadastrar"                      +
              "\n2. Consultar"                      +
              "\n3. Atualizar"                      +
              "\n4. Excluir")
        self.setOpcao(int(input()))

    def operacoes(self):
        while self.getOpcao() != 0:
            self.Menu()
            if self.getOpcao() == 0:
                print("Obrigado!")
            elif self.getOpcao() == 1:
                self.Cadastrar()
            elif self.getOpcao() == 2:
                print(self.modelo.selecionar())
            else:
                print("Opção escolhida inválida! Tente novamente!")

    def Cadastrar(self):
        print("Informe seu nome: ")
        nome = input()
        print("Informe seu telefone: ")
        telefone = input()
        print("Informe seu endereço: ")
        endereco = input()
        print("Informe sua data de nascimento: ")
        dataDeNascimento = input()
        print(self.modelo.inserir(nome, telefone, endereco, self.transformarData(dataDeNascimento)))

    def transformarData(self, texto):
        separado = texto.split('/')
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]
        return "{}-{}-{}".format(ano,mes,dia)

