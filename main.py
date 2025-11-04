import os #biblioteca de comandos do sistema operacional

from imigranteTela import MenuImigrante
from apoioTela import MenuApoio


def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear') 


#arquivo principal projeto integrador
def Menu(): #criar a função do menu
    executando = True
    while executando:
        # limpando a tela 
        LimpaTela()
        print("********************************************************************************************")
        print("                             SEJA BEM-VINDO(A) AO SISTEMA DE CADASTRO ")
        print("")
        print("                                  E GERENCIAMENTO DE IMIGRANTES")  
        print("")        
        print("********************************************************************************************")
        print("")

        print("                                   Dupla: HELEN e EVILY")

        # criando o menu principal 
        print("")
        print("     ===    Menu principal      === ")
        print("")
        print("")
        print("    1.      IMIGRANTE       ")
        print("")
        print("    2.      SERVIÇOS DE APOIO AO IMIGRANTE  ")
        print("")
        print("    9.      SAIR               ")
        print("")
        print("")

        opcao = input("Escolha uma opção: " ).strip()
        if opcao == "1":
            MenuImigrante()
        elif opcao == "2":
            MenuApoio()
        elif opcao == "9":
            print("Obrigado por utilizar esse app")
            executando=False
        else:
            print("Opção inválida")

#executar a função principal, construtor
if __name__ == "__main__":
    Menu()



