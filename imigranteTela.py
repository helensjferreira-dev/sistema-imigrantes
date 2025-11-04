import os #biblioteca de comandos do sistema operacional 
from imigrante import NovoImigrante, ListarTodosImigrantes, AlterarImigrante2, ExcluirImigrante2, Continuar, BuscarImigranteNome, BuscarImigranteNacionalidade 
def LimpaTela(): 
    os.system('cls' if os.name == 'nt' else 'clear') 

def MenuImigrante(): #criar a função do menu 
    from complementoTela import MenuComplemento 
    from confereID import confereID, ConfereIdalt, ConfereIdex
    while True: 
         
        #limpando a tela 
        LimpaTela() 
        # criando o menu 
        print("-------------------------------- Menu Imigrante ----------------------------------- ") 
        print("") 
        print("(1) CADASTRAR IMIGRANTE     (2) LISTAR IMIGRANTES    (3) VER DETALHES DO IMIGRANTE")
        print("") 
        print("       (4) ALTERAR CADASTRO              (5) EXCLUIR IMIGRANTE") 
        print("") 
        print("   (6) BUSCAR IMIGRANTE por nome       (7) BUSCAR por país de origem") 
        print("") 
        print("                    (9) Voltar ao Menu Principal ") 
        print("") 
        print("-----------------------------------------------------------------------------------") 
        print("") 
        opcao = input("Escolha uma opção: " ) 
        if opcao == "1": 
        # chamando o metodo para cadastrar novo imigrante 
            id = NovoImigrante() 
            Continuar(id) 
        #opção se quer cadastrar informações complementares 
        elif opcao == "2": 
        #chamando o metodo para listar todos os imigrantes 
            ListarTodosImigrantes() 
            input("Pressione enter para continuar! ") 
        elif opcao == "3": #chamando o metodo que lista todos para que o usuário escolha 1 
            ListarTodosImigrantes() 
            confereID() 
        #chamando o método para validar e exibir detalhes do imigrante, caso haja cadastro 
        elif opcao == "4": 
        #chamando o metodo para listar todos os imigrantes para escolher 1
            ListarTodosImigrantes() 
            print("") 
            ConfereIdalt() #chamando o método para alterar os dados do imigrante 
        elif opcao == "5": 
            ListarTodosImigrantes() 
            print("") 
            ConfereIdex() #chamando o metodo para listar todos os imigrantes 
        elif opcao == "6": 
            BuscarImigranteNome() 
            input("Pressione enter para continuar!") 
        elif opcao == "7": 
            BuscarImigranteNacionalidade() 
            input("Pressione enter para continuar!") 
        #chamando o metodo para buscar todos os imigrantes por pais 
        elif opcao == "9": 
            return 
        else: 
            print("Opção inválida")