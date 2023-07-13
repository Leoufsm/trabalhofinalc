class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

base_de_dados = [
    Aluno(1001, "João"),
    Aluno(1002, "Maria"),
    Aluno(1003, "Pedro"),
    Aluno(1004, "Ana"),
    Aluno(1005, "Carlos"),
    # Adicione mais alunos aqui, se desejar.
]
def pesquisa_interpolacao(chave, base_de_dados):
    inicio = 0
    fim = len(base_de_dados) - 1

    while inicio <= fim and chave >= base_de_dados[inicio].matricula and chave <= base_de_dados[fim].matricula:
        posicao = inicio + ((chave - base_de_dados[inicio].matricula) * (fim - inicio)) // (base_de_dados[fim].matricula - base_de_dados[inicio].matricula)

        if base_de_dados[posicao].matricula == chave:
            return base_de_dados[posicao]

        if base_de_dados[posicao].matricula < chave:
            inicio = posicao + 1
        else:
            fim = posicao - 1

    return None
chave_pesquisa = 1003
aluno_encontrado = pesquisa_interpolacao(chave_pesquisa, base_de_dados)
if aluno_encontrado:
    print("Aluno encontrado:")
    print("Matrícula:", aluno_encontrado.matricula)
    print("Nome:", aluno_encontrado.nome)
else:
    print("Aluno não encontrado.")
