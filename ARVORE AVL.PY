class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, matricula, nome):
        if not self.raiz:
            self.raiz = Aluno(matricula, nome)
        else:
            self.raiz = self._inserir_recursivo(self.raiz, matricula, nome)

    def _inserir_recursivo(self, no_atual, matricula, nome):
        if not no_atual:
            return Aluno(matricula, nome)

        if matricula < no_atual.matricula:
            no_atual.esquerda = self._inserir_recursivo(no_atual.esquerda, matricula, nome)
        else:
            no_atual.direita = self._inserir_recursivo(no_atual.direita, matricula, nome)

        no_atual.altura = 1 + max(self._get_altura(no_atual.esquerda), self._get_altura(no_atual.direita))

        fator_balanceamento = self._get_fator_balanceamento(no_atual)

        if fator_balanceamento > 1 and matricula < no_atual.esquerda.matricula:
            return self._rotacao_direita(no_atual)

        if fator_balanceamento < -1 and matricula > no_atual.direita.matricula:
            return self._rotacao_esquerda(no_atual)

        if fator_balanceamento > 1 and matricula > no_atual.esquerda.matricula:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        if fator_balanceamento < -1 and matricula < no_atual.direita.matricula:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual

    def _get_altura(self, no):
        if not no:
            return 0
        return no.altura

    def _get_fator_balanceamento(self, no):
        if not no:
            return 0
        return self._get_altura(no.esquerda) - self._get_altura(no.direita)

    def _rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

    def _rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

    def pesquisa(self, matricula):
        if not self.raiz:
            return None
        else:
            return self._pesquisa_recursiva(self.raiz, matricula)

    def _pesquisa_recursiva(self, no_atual, matricula):
        if not no_atual:
            return None

        if matricula == no_atual.matricula:
            return no_atual

        if matricula < no_atual.matricula:
            return self._pesquisa_recursiva(no_atual.esquerda, matricula)
        else:
            return self._pesquisa_recursiva(no_atual.direita, matricula)

    def em_ordem(self):
        if not self.raiz:
            print("A árvore está vazia.")
        else:
            self._em_ordem_recursivo(self.raiz)

    def _em_ordem_recursivo(self, no_atual):
        if no_atual:
            self._em_ordem_recursivo(no_atual.esquerda)
            print("Matrícula:", no_atual.matricula, "- Nome:", no_atual.nome)
            self._em_ordem_recursivo(no_atual.direita)


# Criação da base de dados
arvore = ArvoreAVL()
arvore.inserir(1001, "João")
arvore.inserir(1005, "Maria")
arvore.inserir(1002, "Pedro")
arvore.inserir(1004, "Ana")
arvore.inserir(1003, "Lucas")
# Adicione mais alunos aqui, se desejar.

# Pesquisa por matrícula
matricula_pesquisa = 1002
aluno_encontrado = arvore.pesquisa(matricula_pesquisa)

if aluno_encontrado:
    print("Aluno encontrado:")
    print("Matrícula:", aluno_encontrado.matricula)
    print("Nome:", aluno_encontrado.nome)
else:
    print("Aluno não encontrado.")

# Apresentação da base de dados em ordem
print("\nBase de dados em ordem:")
arvore.em_ordem()
