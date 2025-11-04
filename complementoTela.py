import os
from complemento import CadCurso, CadExperiencia, ListarComplemento, AlterarComplemento2, ExcluirComplemento2

def LimpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def MenuComplemento(id):
    while True:
        from imigrante import DetalheImigrante

        # limpando a tela 
        LimpaTela()
        #mostrando os dados do imigrante
        DetalheImigrante(id)
        ListarComplemento(id)

        # criando o menu Complemento
        print("---------------------------      Menu Informações Complementares     -------------------------------- ")
        print("")
        print("(1) CADASTRAR EXPERIÊNCIAS PROFISSIONAIS           (2) CADASTRAR CURSOS E FORMAÇÕES ")
        print("")
        print("(3) ALTERAR INFORMAÇÕES COMPLEMENTARES            (4) EXCLUIR INFORMAÇÕES COMPLEMENTARES            ")
        print("")
        print("                    (9) Voltar ao Menu Imigrante")
        print("")
        print("-----------------------------------------------------------------------------------")
        print("")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            # chamando o metodo para cadastrar experiência profissional
            CadExperiencia(id)
            input("Pressione enter para continuar!")

        elif opcao == '2':
            # chamando o metodo para cadastrar todos os cursos
            CadCurso(id)
            input("Pressione enter para continuar!")


        elif opcao == '3':
            # chamar o metodo de alterar informação complementar
            AlterarComplemento2(id)
            input("Pressione enter para continuar!")

        elif opcao == '4':
            # chamar o metodo de excluir informação complementar
            ExcluirComplemento2(id)
            input("Pressione enter para continuar!")


        elif opcao == '9':
            return
        else:
            print("Opção inválida")
