import os #biblioteca de comandos do sistema operacional
from apoio import NovoApoio, ListarTodasInstituicoes, DetalheServico, AlterarServico2, ExcluirServico2, ListarServicosTipo, ListarServicosCidade

def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear') #forma simplificada de fazer o if



def MenuApoio(): #criar a função do menu
    from confereID import ConfereIdapoio, ConfereIdapoioAlt
    while True:
        # limpando a tela 
        LimpaTela()
        
        # criando o menu  
        print("---------------------------      Menu Serviços de Apoio     -------------------------------- ")
        print("")
        print("(1) CADASTRAR SERVIÇO DE APOIO    (2) LISTAR SERVIÇOS    (3) VER DETALHES DOS SERVIÇOS")
        print("")
        print("(4) ALTERAR CADASTRO DE SERVIÇOS         (5) EXCLUIR CADASTRO DE SERVIÇOS")
        print("")
        print("(6) BUSCAR SERVIÇOS por tipo        (7) BUSCAR SERVIÇOS por cidade")
        print("")
        print("                    (9) Voltar ao Menu Principal ")
        print("")
        print("-----------------------------------------------------------------------------------")
        print("")

        opcao = input("Escolha uma opção: " )
        if opcao == "1":
            NovoApoio()
        elif opcao == "2":
            ListarTodasInstituicoes()
            input("Pressione enter para continuar! ")
        elif opcao == '3':
            # chamando o metodo que lista todos os servico para que o usuario escolha um
            LimpaTela()
            ListarTodasInstituicoes()
            print("")
            # chamando o metodo para ver detalhes do SERVIÇO
            DetalheServico()
        elif opcao == '4':
            #chamando o metodo para listar todos os servicos para escolher um
            LimpaTela()
            ListarTodasInstituicoes()
            print("")
            #chamando o metodo para alterar o SERVIÇO
            ConfereIdapoioAlt()

        elif opcao == '5':
            #chamando o metodo para listar todos os servicos para escolher um
            LimpaTela()
            ListarTodasInstituicoes()
            print("")
            #chamando o metodo para excluir o servico
            ConfereIdapoio()
        elif opcao == '6':
            ListarServicosTipo()
            input("Pressione enter para continuar!")
        elif opcao == '7':
            ListarServicosCidade()
            input("Pressione enter para continuar!")
        elif opcao == "9":
            return
        else:
            print("Opção inválida")
