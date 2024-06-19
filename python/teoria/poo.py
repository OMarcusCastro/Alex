

class Pessoa():
    '''
    funcoes em objetos sao chamados de metodos
    '''
    def __init__(self,nome,idade):
        self.nome = nome#self.x -> x é um atributo de pessoa
        self.idade = idade

    def verifica_maioridade(self):
        if self.idade<18:
            print('menor de idade')
        else:
            print("maior de idade")

class Escola():
    def __init__(self) :
        self.funcionarios = []

    def matricula_funcinario(self,funcuncionario):
        self.funcionarios.append(funcuncionario)

class Professor(Pessoa):
    def __init__(self, nome, idade,materia):
        super().__init__(nome, idade)
        self.materia = materia

    def ensina_algo(self,assunto):
        print(self.nome,'esta falando sobre',assunto)

#p1,p2 é uma instancia do onjeto pessoa
p1 = Pessoa('Alex',20)
p2 = Pessoa('Marcus',17)
pf=Professor("marcus",22,'programacao')
e = Escola()

e.matricula_funcinario(pf)

e.funcionarios[0].materia
 
pf.verifica_maioridade()


p1.verifica_maioridade()
p2.verifica_maioridade()


'''
'''