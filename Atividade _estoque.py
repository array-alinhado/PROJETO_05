import os
os.system("cls || clear")

# Grupo = joão, Itauã Gualberto, leonardo
# Sala = G-93313


def limpar_tela():
    os.system("cls || clear")

# Classe Produto
class Produto:
    def __init__(self, nome, preco, quantidade, codigo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo
    
    def __str__(self):
        return f"{self.codigo} - {self.nome}, Preço:$ {self.preco}, Quantidade em estoque: {self.quantidade}"

# Classe Estoque
class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"O produto '{produto.nome}' foi adicionado ao estoque.")

    def buscar_produto_por_codigo(self, codigo):
        resultados = [produto for produto in self.produtos if codigo.lower() in produto.codigo.lower()]
        return resultados

    def remover_produto(self, codigo):
        produto_a_remover = None
        for produto in self.produtos:
            if produto.codigo == codigo:
                produto_a_remover = produto
                break
        if produto_a_remover:
            self.produtos.remove(produto_a_remover)
            print(f"O produto '{produto_a_remover.nome}' foi removido do estoque.")
        else:
            print(f"Produto com código {codigo} não encontrado.")

    def listar_produtos(self):
        if not self.produtos:
            print("O estoque está vazio.")
        else:
            for produto in self.produtos:
                print(produto)

    def registrar_entrada_saida(self, codigo, quantidade, tipo='entrada'):
        for produto in self.produtos:
            if produto.codigo == codigo:
                if tipo == 'entrada':
                    produto.quantidade += quantidade
                    print(f"Entrada registrada: +{quantidade} do produto '{produto.nome}'.")
                elif tipo == 'saida':
                    if produto.quantidade >= quantidade:
                        produto.quantidade -= quantidade
                        print(f"Saída registrada: -{quantidade} do produto '{produto.nome}'.")
                    else:
                        print(f"Não tem estoque para este produto '{produto.nome}'.")
                return
        print(f"Produto com código {codigo} não encontrado")

# Função para exibir o menu
def exibir_menu():
    print("\n====== Menu ======")
    print("1. Adicionar produto")
    print("2. Procurar produto por nome")
    print("3. Remover produto")
    print("4. Listar todos os produtos")
    print("5. Registrar entrada/saída de produto")
    print("6. Sair")
    print("======================")

# Função principal
def main():
    estoque = Estoque()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade inicial: "))
            codigo = input("Digite o código do produto: ")
            produto = Produto(nome, preco, quantidade, codigo)
            estoque.adicionar_produto(produto)
            limpar_tela()

        elif opcao == '2':
            nome = input("Digite o codigo do produto para buscar: ")
            resultados = estoque.buscar_produto_por_codigo(codigo)
            if resultados:
                print("Produtos encontrados:")
                for produto in resultados:
                    print(produto)
            else:
                print("Nenhum produto encontrado com esse nome.")
                
        elif opcao == '3':
            codigo = input("Digite o código do produto para remover: ")
            estoque.remover_produto(codigo)
            

        elif opcao == '4':
            print("Lista de produtos em estoque:")
            estoque.listar_produtos()
            

        elif opcao == '5':
            codigo = input("Digite o código do produto para movimentação: ")
            tipo = input("Digite 'entrada' para entrada ou 'saida' para saída: ").lower()
            quantidade = int(input("Digite a quantidade: "))
            estoque.registrar_entrada_saida(codigo, quantidade, tipo)
            

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Não tem essa opção! Tente novamente.")

if __name__ == "__main__":
    main()