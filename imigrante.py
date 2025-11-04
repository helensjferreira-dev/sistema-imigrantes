from conn import Conectar
from complementoTela import MenuComplemento, ListarComplemento
from opcao import ValidaData, CompletaTexto


def NovoImigrante():
    
    print("********************************************************************************************")
    print("                                CADASTRAR IMIGRANTE ")
    print("********************************************************************************************")
    print("")

    #SOLICITANDO DADOS DO IMIGRANTE com verificação de preenchimento obrigatório
    while True:
        nome = input("Informe o PRIMEIRO NOME: ")
        if nome == "":
            print("Digite o primeiro nome do imigrante: ")
        else: 
            break
    while True:
        sobrenome = input("Informe o SOBRENOME COMPLETO: ")
        if sobrenome == "":
            print("Digite o sobrenome do imigrante: ")
        else: 
            break
    while True:
        nacionalidade = input("Informe a NACIONALIDADE e a SIGLA do país de origem: ")
        if nacionalidade == "":
            print("Digite a nacionalidade do imigrante e a sigla do seu país de origem: ")
        else:
            break
    while True:
        idioma = input("Informe os IDIOMAS falados: ")
        if idioma =="":
            print("Digite os idiomas falados pelo imigrante: ")
        else:
            break

    #validando a data de nascimento
    while True:
        datanascimento = input("Informe a DATA DE NASCIMENTO no formato (dd/mm/yyyy): ")
        if datanascimento == "":
            print("Por favor: digite a data.")
            continue  # Volta para o início do loop
    
        try:
            datanascimento = ValidaData(datanascimento)
            break  # Sai do loop se a data for válida
        except ValueError as e:
            print(e)

    documento= input("Informe o DOCUMENTO PESSOAL: ")

    contato=input("Informe os DADOS PARA CONTATO como telefone e/ou e-mail, se houver: ")
        

    #CRIANDO A CONEXÃO 
    conn = Conectar()
    cursor=conn.cursor() #para executar comandos precisa usar o cursor

    #enviar o comando para o banco de dados
    cursor.execute("INSERT INTO IMIGRANTE(PRIMEIRO_NOME, SOBRENOME, NACIONALIDADE, IDIOMA, DATA_NASCIMENTO, DOCUMENTO_IDENTIFICACAO, CONTATO) VALUES(%s, %s, %s, %s, %s, %s, %s)", 
                   (nome, sobrenome, nacionalidade, idioma, datanascimento, documento, contato,)) #%s indica que vamos usar as variaveis
    conn.commit() #efetua a gravação do registro no banco

    print("")
    print("Imigrante cadastrado com sucesso")
        #fechando as conexoes
    cursor.close()
    conn.close()
    id = cursor.lastrowid #COMANDOS PARA GARANTIR QUE O ID CONTINUARA SENDO USADO 
    return id

def Continuar(id): #CONTINUAR BUSCA POR NOME SIM OU NÃO
    from imigranteTela import MenuImigrante
    opcao = input("*** Deseja adicionar Informações Complementares do imigrante?\n Digite (s) para Sim OU (n) para Não: " )
    if opcao.lower() == "s":
        MenuComplemento(id)
        
    elif opcao.lower() == "n":
        MenuImigrante()
    else:
            print("Opção inválida")

            print("Pressione enter para continuar")

def Continuar3(): #CONTINUAR BUSCA POR PAIS
    from imigranteTela import MenuImigrante
    while True:
        print("")
        opcao = input("*** Deseja exibir detalhes de algum desses imigrantes? Digite: \n\n(1) EXIBIR DETALHES \n (2) CONTINUAR BUSCA \n (3) RETORNAR AO MENU Imigrante: " ).strip()
        if opcao == "1":
                
            print("")
            id=input("DIGITE o id do imigrante que deseja consultar: ")
            DetalheImigrante(id)
            ListarComplemento(id)
                

        elif opcao == "2":
            BuscarImigranteNacionalidade()
                
            
        elif opcao == "3":
            return                
        else:
            print("Opção inválida")



def opcaoBusca():
    from imigranteTela import MenuImigrante
    while True:
        print("")
        op2 = input("*** Digite: \n\n (1) CONTINUAR BUSCA \n (2) RETORNAR AO MENU Imigrante: \n ").strip()
        if op2 == "1":
            BuscarImigranteNome()
            
        elif op2 == "2":
            return
                
        else:
            print("Opção inválida.")


def opcao2Busca():
    while True:
        from imigranteTela import MenuImigrante
        print("")
        op2 = input("*** Digite: \n\n (1) CONTINUAR BUSCA \n (2) Retornar ao Menu Imigrante: \n ").strip()
        if op2 == "1":
            BuscarImigranteNacionalidade()
                
            
        elif op2 == "2":
            return
                
        else:
            print("Opção inválida")


def ListarTodosImigrantes():
    print("*******************************************************************************************************")
    print("                                      Lista de Imigrantes ")
    print("*******************************************************************************************************")
    print("")

     #CRIANDO A CONEXÃO 
    conn = Conectar()
    cursor=conn.cursor() 

    #ENVIANDO O COMANDO PARA O BANCO DE DADOS SELECIONAR
    cursor.execute("SELECT IDIMIGRANTE, PRIMEIRO_NOME, SOBRENOME, NACIONALIDADE FROM IMIGRANTE")


    for id, nome, sobrenome, nacionalidade in cursor.fetchall():
                
        print("|" + f" {CompletaTexto(id, 3, ' ')} | {CompletaTexto(nome.title(), 1, ' ')} {CompletaTexto(sobrenome.title(),40, ' ')} | {CompletaTexto(nacionalidade, 20, ' ')}")
   
        print("|" + CompletaTexto(" ", 100, " ") +  "|")
        print("+" + CompletaTexto("-", 100, "-") + "+")


        
    #fechando as conexoes
    cursor.close()
    conn.close()

def DetalheImigrante(id):
    from imigranteTela import LimpaTela
    LimpaTela()

    print("")
    print("*******************************************************************************************************")
    print("                                Detalhes do Imigrante ")
    print("*******************************************************************************************************")
    print("")

     #CRIANDO A CONEXÃO COM O BANCO DE DADOS
    conn = Conectar()
    cursor=conn.cursor() 

    cursor.execute("SELECT IDIMIGRANTE, PRIMEIRO_NOME, SOBRENOME, NACIONALIDADE, IDIOMA, DATA_NASCIMENTO, DOCUMENTO_IDENTIFICACAO, CONTATO FROM IMIGRANTE WHERE IDIMIGRANTE=%s", (id,)) 

    resultados = cursor.fetchall()
    if not resultados:
        print("Nenhum imigrante encontrado.")
    else:
        for id, nome, sobrenome, nacionalidade, idioma, datanascimento, documento, contato in resultados: 
            print(
            f"Id: {id}\n\n"
            f"Nome completo: {nome.title()} {sobrenome.title()}\n\n"
            f"Nacionalidade: {nacionalidade}\n\n"
            f"Idiomas falados: {idioma}\n\n"
            f"Data de nascimento: {datanascimento}\n\n"
            f"Documento: {documento}\n\n"
            f"Contato: {contato}\n\n"
            
        )

            
           
    cursor.close()
    conn.close()


def AlterarImigrante2(id):
    print("********************************************************************************************")
    print("                               Alterando o Imigrante ")
    print("********************************************************************************************")
    print("")
    
    #criando a conexao
    conn = Conectar()
    cursor = conn.cursor()

 
    print("Informe os novos valores do imigrante")
    while True:
        nome = input("Informe o PRIMEIRO NOME: ")
        if nome == "":
            print("Digite o primeiro nome do imigrante: ")
        else: 
            break
    while True:
        sobrenome = input("Informe o SOBRENOME COMPLETO: ")
        if sobrenome == "":
            print("Digite o sobrenome do imigrante: ")
        else: 
            break
    while True:
        nacionalidade = input("Informe a NACIONALIDADE e a SIGLA do país de origem: ")
        if nacionalidade == "":
            print("Digite a nacionalidade do imigrante e a sigla do seu país de origem: ")
        else:
            break
    while True:
        idioma = input("Informe os IDIOMAS falados: ")
        if idioma =="":
            print("Digite os idiomas falados pelo imigrante: ")
        else:
            break
        #validando a data de nascimento
    while True:
        datanascimento = input("Informe a DATA DE NASCIMENTO no formato (dd/mm/yyyy): ")
        if datanascimento == "":
            print("Por favor: digite a data.")
            continue  # Volta para o início do loop
        
        try:
                datanascimento = ValidaData(datanascimento)
                break  # Sai do loop se a data for válida
        except ValueError as e:
            print(e)

    while True:
        documento= input("Informe o DOCUMENTO PESSOAL: ")
        if documento == "":
            print("Digite o documento do imigrante: ")
        else:
            break
    contato=input("Informe os DADOS PARA CONTATO como telefone e/ou e-mail, se houver: ")
            

    #enviando comando sql para alterar o imigrante
    cursor.execute("UPDATE IMIGRANTE SET PRIMEIRO_NOME=%s, SOBRENOME=%s,NACIONALIDADE=%s, IDIOMA=%s, DATA_NASCIMENTO=%s, DOCUMENTO_IDENTIFICACAO=%s, CONTATO=%s WHERE IDIMIGRANTE=%s", (nome, sobrenome, nacionalidade, idioma,  datanascimento, documento, contato, id)) 

    conn.commit()

    cursor.close()
    conn.close()

    print("Imigrante atualizado com sucesso")
    input("Pressione enter para voltar ao menu")


def ExcluirImigrante(id):
    print("********************************************************************************************")
    print("                                  Excluir o Imigrante ")
    print("********************************************************************************************")
    print("")

    confirmar=input("*** Deseja realmente excluir o imigrante (DIGITE 1 para confirmar): ").strip()
    if(confirmar =='1'):

    #CRIANDO A CONEXÃO COM O BANCO DE DADOS
        conn=Conectar()
        cursor=conn.cursor() 
        # Primeiro exclui complementos relacionados
        cursor.execute("DELETE FROM COMPLEMENTO WHERE IDIMIGRANTE = %s", (id,))
        # Depois exclui o imigrante
        cursor.execute("DELETE FROM IMIGRANTE WHERE IDIMIGRANTE = %s", (id,))
        conn.commit()

        cursor.close()
        conn.close()

        print("Imigrante excluído com sucesso")
        print("")
        input("Pressione enter para voltar ao menu")
    else:
        print("Operação cancelada!")


def ExcluirImigrante2(id):
    print("********************************************************************************************")
    print("                                  Excluir o Imigrante ")
    print("********************************************************************************************")
    print("")

#criando a conexao
    conn = Conectar()
    cursor = conn.cursor()

    confirmar=input("*** Deseja realmente excluir o imigrante (DIGITE 1 para confirmar): ")
    if(confirmar =='1'):

            # Primeiro exclui complementos relacionados
        cursor.execute("DELETE FROM COMPLEMENTO WHERE IDIMIGRANTE = %s", (id,))
            # Depois exclui o imigrante
        cursor.execute("DELETE FROM IMIGRANTE WHERE IDIMIGRANTE = %s", (id,))
        conn.commit()

        cursor.close()
        conn.close()

        print("Imigrante excluído com sucesso")
        print("")
    else:
        print("Operação cancelada!")
    input("Pressione enter para voltar ao menu")


    
def BuscarImigranteNome():
    print("********************************************************************************************")
    print("                            Pesquisa de Imigrante por nome ")
    print("********************************************************************************************")
    print("")


    buscanome = input("Informe o NOME do imigrante (ou uma parte do nome): ")
    print("")

    #criando a conexao
    conn = Conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT IDIMIGRANTE, PRIMEIRO_NOME, SOBRENOME, NACIONALIDADE FROM IMIGRANTE
    WHERE UPPER(TRIM(PRIMEIRO_NOME)) LIKE UPPER(%s)
       OR UPPER(TRIM(SOBRENOME)) LIKE UPPER(%s)
       OR UPPER(CONCAT(TRIM(PRIMEIRO_NOME), ' ', TRIM(SOBRENOME))) LIKE UPPER(%s)
""", (f"%{buscanome}%", f"%{buscanome}%", f"%{buscanome}%"))


    buscapornome = cursor.fetchall()
    if not buscapornome:
        print("")
        input("Nenhum imigrante encontrado. ")
        opcaoBusca()

    else:
    #percorrendo o resultado e mostrando em tela
        print("")

        for id, nome, sobrenome, nacionalidade in buscapornome:
                                
            print("|" + f" {CompletaTexto(id, 3, ' ')} | {CompletaTexto(nome.title(), 1, ' ')} {CompletaTexto(sobrenome.title(),25, ' ')} | {CompletaTexto(nacionalidade, 20, ' ')}")
   
            print("|" + CompletaTexto(" ", 100, " ") +  "|")
            print("+" + CompletaTexto("-", 100, "-") + "+")

        Continuar2()

    #fechando a conexao
    cursor.close()
    conn.close()

def Continuar2():
    from imigranteTela import MenuImigrante

    while True:

        print("")
        opcao = input("*** Deseja exibir detalhes de algum desses imigrantes? DIGITE: \n\n (1) EXIBIR DETALHES \n (2) CONTINUAR BUSCA \n (3) RETORNAR AO MENU IMIGRANTE " ).strip()
        if opcao == "1":
                
            print("")
            id=input("Digite o id do imigrante que deseja consultar: ")
            DetalheImigrante(id)
            ListarComplemento(id)
                

        elif opcao == "2":
            BuscarImigranteNome()
                
            
        elif opcao == "3":
            return
                
        else:
            print("Opção inválida")



def BuscarImigranteNacionalidade():
    print("********************************************************************************************")
    print("                         Pesquisa de Imigrante por Nacionalidade ")
    print("********************************************************************************************")
    print("")

    buscapais = input("Informe a nacionalidade (sigla ou nome do país): ")
    print("")

    #criando a conexao
    conn = Conectar()
    cursor = conn.cursor()

    #enviando o camando para o banco de dados
    cursor.execute(f"""SELECT IDIMIGRANTE, PRIMEIRO_NOME, SOBRENOME, NACIONALIDADE FROM IMIGRANTE WHERE UPPER(NACIONALIDADE) LIKE UPPER(%s)""", (f"%{buscapais}%",))

    buscanacionalidade = cursor.fetchall()
    if not buscanacionalidade:
        print("Nenhum imigrante encontrado.")
        opcao2Busca()

    else:
            #percorrendo o resultado e mostrando em tela
        print("")

        for id, nome, sobrenome, nacionalidade in buscanacionalidade:
                                
            print("|" + f" {CompletaTexto(id, 3, ' ')} | {CompletaTexto(nome.title(), 1, ' ')} {CompletaTexto(sobrenome.title(),25, ' ')} | {CompletaTexto(nacionalidade, 20, ' ')}")
   
            print("|" + CompletaTexto(" ", 100, " ") +  "|")
            print("+" + CompletaTexto("-", 100, "-") + "+")

        Continuar3()
        return 

 

    #fechando a conexao
    cursor.close()
    conn.close()

