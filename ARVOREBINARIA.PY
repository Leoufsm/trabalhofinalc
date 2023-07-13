class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

base_de_dados = [
    Produto(1001, "Camiseta", 29.99),
    Produto(1002, "Calça Jeans", 79.99),
    Produto(1003, "Tênis", 99.99),
    Produto(1004, "Bolsa", 49.99),
    Produto(1005, "Óculos de Sol", 59.99),
    # Adicione mais produtos aqui, se desejar.
]
class No:
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, produto):
        if self.raiz is None:
            self.raiz = No(produto)
        else:
            self._inserir_recursivo(produto, self.raiz)

    def _inserir_recursivo(self, produto, no_atual):
        if produto.codigo < no_atual.produto.codigo:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(produto)
            else:
                self._inserir_recursivo(produto, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(produto)
            else:
                self._inserir_recursivo(produto, no_atual.direita)

    def pesquisar(self, codigo):
        return self._pesquisar_recursivo(codigo, self.raiz)

    def _pesquisar_recursivo(self, codigo, no_atual):
        if no_atual is None or no_atual.produto.codigo == codigo:
            return no_atual.produto

        if codigo < no_atual.produto.codigo:
            return self._pesquisar_recursivo(codigo, no_atual.esquerda)
        else:
            return self._pesquisar_recursivo(codigo, no_atual.direita)
arvore = ArvoreBinaria()

# Preenchendo a árvore binária com os dados da base_de_dados
for produto in base_de_dados:
    arvore.inserir(produto)

# Pesquisando um produto pelo código
codigo_pesquisa = 1003
produto_encontrado = arvore.pesquisar(codigo_pesquisa)
if produto_encontrado:
    print("Produto encontrado:")
    print("Código:", produto_encontrado.codigo)
    print("Nome:", produto_encontrado.nome)
    print("Preço:", produto_encontrado.preco)
else:
    print("Produto não encontrado.")
