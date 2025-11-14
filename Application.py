import os

import service.cliente_service as cliente_service

import service.veiculo_service as veiculo_service

from model.cliente import Cliente

from model.veiculo import Veiculo

import service.layout_service as layout_service 

####### VARIÁVEIS GLOBAIS


   # execução do sistema
while True:

    layout_service.limpar_tela()
    layout_service.titulo()
    layout_service.menu()

    opcao=int(input("\nInforme uma opção: "))

    match opcao:
        case 1:
            layout_service.titulo()
            print("\n#### CADASTRO DE CLIENTES ####")
            cadastro_clientes()

            layout_service.pressione_continuar()

        case 2:
            layout_service.titulo()
            lista_clientes()
            layout_service.pressione_continuar()

        case 3:
            layout_service.titulo()
            print("\n#CADASTRO DE VEÍCULOS")
            cadastro_veiculos()   
            layout_service.pressione_continuar()
        
        case 4: 
            layout_service.titulo()
            lista_veiculos()
            layout_service.pressione_continuar()

        case 5:
            print("\n#ALUGAR CARRO")
            layout_service.pressione_continuar()

        case 6:
            print("\n#SAIR")
            
        case _:
            print("\n#OPÇÃO INVÁLIDA")
            layout_service.pressione_continuar()
