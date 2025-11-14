import os

import cliente_service

import veiculo_service

from cliente import Cliente

from veiculo import Veiculo

import layout 

####### VARIÁVEIS GLOBAIS


   # execução do sistema
while True:

    layout.limpar_tela()
    layout.titulo()
    layout.menu()

    opcao=int(input("\nInforme uma opção: "))

    match opcao:
        case 1:
            layout.titulo()
            print("\n#### CADASTRO DE CLIENTES ####")
            cadastro_clientes()

            layout.pressione_continuar()

        case 2:
            layout.titulo()
            lista_clientes()
            layout.pressione_continuar()

        case 3:
            layout.titulo()
            print("\n#CADASTRO DE VEÍCULOS")
            cadastro_veiculos()   
            layout.pressione_continuar()
        
        case 4: 
            layout.titulo()
            lista_veiculos()
            layout.pressione_continuar()

        case 5:
            print("\n#ALUGAR CARRO")
            layout.pressione_continuar()

        case 6:
            print("\n#SAIR")
            
        case _:
            print("\n#OPÇÃO INVÁLIDA")
            layout.pressione_continuar()
