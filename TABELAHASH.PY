base_de_dados = {
    1001: {"nome": "João", "idade": 30, "salario": 5000},
    1002: {"nome": "Maria", "idade": 35, "salario": 6000},
    1003: {"nome": "Pedro", "idade": 28, "salario": 4500},
    1004: {"nome": "Ana", "idade": 32, "salario": 5500},
    1005: {"nome": "Carlos", "idade": 40, "salario": 7000},
    # Adicionar mais .
}
class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def calcular_indice(self, chave):
        return chave % self.tamanho

    def adicionar_elemento(self, chave, valor):
        indice = self.calcular_indice(chave)
        self.tabela[indice].append((chave, valor))

    def buscar_elemento(self, chave):
        indice = self.calcular_indice(chave)
        elementos = self.tabela[indice]
        for elemento in elementos:
            if elemento[0] == chave:
                return elemento[1]
        return None

tabela_hash = TabelaHash(10)

# Preenchendo a tabela hash com os dados da base_de_dados
for chave, valor in base_de_dados.items():
    tabela_hash.adicionar_elemento(chave, valor)

# Pesquisando um funcionário pelo número de identificação (chave)
chave_pesquisa = 1003
funcionario = tabela_hash.buscar_elemento(chave_pesquisa)
if funcionario:
    print("Funcionário encontrado:")
    print("Nome:", funcionario["nome"])
    print("Idade:", funcionario["idade"])
    print("Salário:", funcionario["salario"])
else:
    print("Funcionário não encontrado.")
