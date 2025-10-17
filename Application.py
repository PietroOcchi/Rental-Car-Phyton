import os

from cliente import Cliente
####### FUNÇÕES GLOBAIS
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pressione_continuar():
    input("Pressione Enter para continuar...")


####### TITULO DO SISTEMA
def titulo():
    limpar_tela()
    print("#"*50)
    print("#"+ " "*15 +"LOCADORA DE CARROS" + " "*15+"#")
    print("#"*50)

####### MENU PRINCIPAL
def menu():
    print("\n#Menu de Opções")
    print("1 - Cadastro de Clientes")
    print("2 - Cadastro de Veículos")
    print("3 - Alugar Carro")
    print("4 - Sair do Sistema")

####### FUNÇÕES DO SISTEMA
def cadastro_clientes():

    nome = input("Nome: ")
    codigo_cliente = int(input("Código dokm cliente: "))
    ano_nascimento = int(input("Ano de nascimento: "))
    email = input("E-mail: ")

    cliente1 = Cliente(codigo_cliente,nome,ano_nascimento,email)


    print("Cliente cadastrado com sucesso!")
    print(cliente1)


def cadastro_veiculos():
    modelo = input("Nome: ")
    codigo_veiculo = int(input("Código do veículo: "))
    ano = int(input("Ano: ")) 
    cor = input("Cor: ")


while True:
    limpar_tela()
    titulo()
    menu()

    opcao=int(input("\nInforme uma opção: "))

    match opcao:
        case 1:
            titulo()
            print("\n#### CADASTRO DE CLIENTES ####")
            cadastro_clientes()
            pressione_continuar()

        case 2:
            titulo()
            print("\n#CADASTRO DE VEÍCULOS")
            cadastro_veiculos()
            pressione_continuar()

        case 3:
            print("\n#ALUGAR CARRO")
            pressione_continuar()

        case 4:
            print("\n#SAIR")
            
        case 5:
            print("\n#OPÇÃO INVÁLIDA")
            pressione_continuar()




