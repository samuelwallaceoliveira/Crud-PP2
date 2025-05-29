def exibir_produto(produto, id=None):
    if id:
        print(f"ID: {id}")
    for chave, valor in produto.items():
        print(f"{chave}: {valor}")

def exibir_menu():
    print('''
    Mercadinho
    Escolha uma opção:
    1. Cadastrar um produto
    2. Listar produtos cadastrados
    3. Procurar dados de um produto
    4. Alterar dados de um produto
    5. Excluir dados de um produto
    0. Salvar e Fechar
    ''')


def cadastrar(produtos):
    identificador = input("Insira um ID para o produto: ")

    produto = {
        "categoria" : input("Qual produto você deseja cadastrar? "),
        "valor": float(input("Qual o valor do produtor? ").replace(",",".")),
        "Unidade" : input("Qual a unidade de medida deste produto? ").lower()
    }

    subst = {
        "kilo" : "kg",
        "litro" : "L",
        "unidade": "und"
    }
    produto["Unidade"] = subst.get(produto["Unidade"],produto["Unidade"])
    produtos[identificador] = produto


def listar(produtos):
    if len(produtos) == 0:
        print("Não a produtos cadastrados")
    
    else:
        for id, prod  in produtos.items():
            exibir_produto(prod, id)

def buscar(produtos):
    Id_Buscar = input("Insira o id para a busca: ")

    if Id_Buscar in produtos:
        exibir_produto(produtos[Id_Buscar], Id_Buscar)
    else:
        print(f"{Id_Buscar} não foi encotrado")


def excluir(produtos):
     Id_Buscar = input("Insira o id para a busca: ")
     
     if Id_Buscar in produtos:
        exibir_produto(produtos[Id_Buscar], Id_Buscar)
     excluir = input("Você deseja exluir esse produto? (Digite 1 para sim e 0 para não): ")
     
     if excluir == "1":
            del produtos[Id_Buscar]
            print(f"Produto com o ID {Id_Buscar} foi deletado com sucesso")
     else:
        print(f"ID: {Id_Buscar} não foi excluido")


def valor_compra(produtos):
      Id_Buscar = input("Insira o id para a busca: ")

      if Id_Buscar in produtos:
          qtd = int(input("Insira a quantidade do produto: "))


def alterar(produtos):
    Id_Buscar = input("Insira o id para a busca: ")

    if Id_Buscar in produtos:
        exibir_produto(produtos[Id_Buscar], Id_Buscar)
        
        confirm = input("Você deseja alterar esse produto? (1 para sim e 0 para não) ")

        if confirm == "1":
            Nprod = {
                "categoria" : input("Novo produto"),
                "valor" : input("Novo valor"),
                "unidade": input("Nova unidade")
            }

            produtos[Id_Buscar] = Nprod
            exibir_produto(produtos[Id_Buscar], Id_Buscar)
        
        else:
            print("Produto não alterado")


import json

def salvar_dados(produtos, filename="dados.json"):
    with open(filename, "w") as f:
        json.dump(produtos, f)

def load_dados(filename="dados.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return[]
    

def main():
    produtos= load_dados()
    opcoes = ""


    while opcoes != "0":

        exibir_menu()
        opcoes = input("Qual opcão você seleciona? ")
 
        if opcoes == "1":
            cadastrar(produtos)
        elif opcoes == "2":
            listar(produtos)
        elif opcoes == "3":
            buscar(produtos)
        elif opcoes == "4":
            alterar(produtos)
        elif opcoes == "5":
            excluir(produtos)
        elif opcoes == "0":
            salvar_dados(produtos)
            break
        else:
            print("Opção inválida!!!")

if __name__ == "__main__":
    main()