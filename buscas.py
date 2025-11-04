from apoio import ListarServicosCidade, ListarServicosTipo, DetalheServico
from apoioTela import MenuApoio

#ESCOLHA busca serviço por cidade

def opcaoServicoCidade():
    while True:        
        print("")
        op2 = input("*** Digite: \n\n (1) CONTINUAR BUSCA \n (2) RETORNAR AO MENU Serviços de Apoio: " ).strip() #REMOVE ESPAÇOS
        if op2 == "1":
            ListarServicosCidade()
             
        elif op2 == "2":
            return
                
        else:
            print("Opção inválida. *** Digite: \n\n (1) CONTINUAR BUSCA \n (2) RETORNAR AO MENU Serviços de Apoio: ")
            input("Pressione Enter para tentar novamente. ")

#ESCOLHA busca serviço por tipo

def opcaoServicoTipo():
    while True:   
        print("")
        op2 = input("*** Digite: \n\n (1) CONTINUAR BUSCA \n (2) RETORNAR AO MENU Serviços de Apoio: " ).strip()
        if op2 == "1":
            ListarServicosTipo()
            
        elif op2 == "2":
            return
                
        else:
            print("Opção inválida. *** Digite: \n\n (1) CONTINUAR BUSCA \n (2) RETORNAR AO MENU Serviços de Apoio: ")
            input("Pressione enter para tentar novamente. ")


#CONTINUAR BUSCAS 

def ContinuarCidade():
    while True:
        print("")
        opcao = input("*** Deseja exibir detalhes de algum desses serviços? Digite: \n\n (1) EXIBIR DETALHES \n (2) CONTINUAR BUSCA \n (3) RETORNAR AO MENU Serviços: " ).strip()
        if opcao == "1":
                
            print("")
            DetalheServico()
                
        elif opcao == "2":
            ListarServicosCidade()
            return
                        
        elif opcao == "3":
            return
                
        else:
            print("Opção inválida. *** Deseja exibir detalhes de algum desses serviços? Digite: \n\n (1) EXIBIR DETALHES \n (2) CONTINUAR BUSCA \n (3) RETORNAR AO MENU Serviços: ")
            input("Pressione enter para tentar novamente. ")

def ContinuarTipo(): #continuar pesquisando serviços por tipo
    while True:
        print("")
        opcao = input("*** Deseja exibir detalhes de algum desses serviços? Digite: \n\n (1) EXIBIR DETALHES \n (2) CONTINUAR BUSCA \n (3) RETORNAR AO MENU Serviços: " )
        if opcao == "1":
                
            print("")
            DetalheServico()
                

        elif opcao == "2":
            return
                
            
        elif opcao == "3":
            return
                
        else:
            print("Opção inválida")
            input("Pressione enter para continuar. ")
