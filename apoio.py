from conn import Conectar #IMPORTANDO CONECTAR AO BD
from opcao import CompletaTexto


def NovoApoio(): #CRIANDO FUNÇÃO CADASTRAR INSTITUIÇÃO DE APOIO
    print("")
    print("**********************************")
    print(" Cadastrar Serviço de Apoio ")
    print("************************************")
    print("")

    #SOLICITANDO DADOS DA INSTITUIÇÃO COM VERIFICAÇÃO POR LAÇO DE REPETIÇÃO
    while True:
        tipo = input("Informe o tipo de apoio que é oferecido: ")
        if tipo == "":
            print("Por favor, informe o tipo de apoio que a instituição oferece: ")
        else:
            break
    while True:
        descricao = input("Descreva com detalhes os serviços oferecidos: ")
        if descricao == "":
            print("Por favor, descreva com detalhes os serviços oferecidos: ")
        else:
            break
    while True:
        nome = input("Informe o nome da Instituição de Apoio: ")
        if nome == "":
            print("Por favor, digite o nome da instituição que oferece o serviço: ")
        else:
            break        
    rua= input("Informe (se souber) o nome da rua onde fica localizada a instituição: ")
    numero= input("Informe (se souber) o número do endereço da instituição: ")
    complemento=input("Informe (se houver) o complemento ou ponto de referência do endereço: ")
    while True:
        cidade=input("Informe a cidade onde a instituição está localizada: ")
        if cidade == "":
            print("Por favor, informe a cidade onde a instituição está localizada: ")
        else:
            break
    while True: 
        estado= input("Informe a sigla do Estado onde a instituição está localizada: ")
        if estado == "":
            print("Por favor, informe o Estado onde a instituição está localizada")
        else:
            break    
    telefone=input("Informe o telefone ou e-mail para contato: ")
    print("")

    #CRIANDO A CONEXÃO 
    conn = Conectar()
    cursor=conn.cursor() 

    #enviar o comando para o banco de dados
    cursor.execute("INSERT INTO APOIO(TIPO_SERVICO, DESCRICAO, NOME_INSTITUICAO, ENDERECO_RUA, ENDERECO_NUMERO, ENDERECO_COMPLEMENTO, ENDERECO_CIDADE, ENDERECO_ESTADO, TELEFONE) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                   (tipo, descricao, nome, rua, numero, complemento, cidade, estado, telefone,)) #%s indica que vamos usar as variaveis
    conn.commit() #efetua a gravação do registro no banco

    print("")
    print("Instituição cadastrada com sucesso")
    print("")

    #esse comando é para parar a execução do programa até pressionar enter 
    input("Pressione enter para continuar!") 

    #fechando as conexoes
    cursor.close()
    conn.close()


def ListarTodasInstituicoes(): #CRIANDO A FUNÇÃO PARA LISTAR TUDO
    print("******************************************************************************************************************")
    print("                                      Lista de Instituições de Apoio")
    print("******************************************************************************************************************")
    print("")

     #CRIANDO A CONEXÃO 
    conn = Conectar()
    cursor=conn.cursor() 

    #ENVIANDO O COMANDO PARA O BANCO DE DADOS SELECIONAR
    
    cursor.execute("SELECT IDAPOIO, TIPO_SERVICO, DESCRICAO, NOME_INSTITUICAO FROM APOIO")

    #PERCORRENDO O RESULTADO E MOSTRANDO EM TELA

    for idapoio, tipo, descricao, nome in cursor.fetchall(): #a ordem precisa ser as mesmas dos campos da tabela. 
        
        print("")

        print("| ID: " + f" {CompletaTexto(idapoio, 3, ' ')} | {CompletaTexto(tipo, 14, ' ')} | {CompletaTexto(descricao, 20, ' ')} | {CompletaTexto((nome), 30, ' ')}" + "|")
   
        print("|" + CompletaTexto(" ", 150, " ") +  "|")
        print("+" + CompletaTexto("-", 150, "-") + "+")
    
     

    #fechando as conexoes
    cursor.close()
    conn.close()

def DetalheServico(): #CRIANDO A FUNÇÃO PARA DETALHAR ALGUM SERVIÇO
    print("*******************************************************************************************")
    print("                                 Detalhe de Serviços de Apoio ")
    print("*******************************************************************************************")
    print("")

    while True: 
        iddigitado = input("Informe o ID do serviço: ").strip()
        if not iddigitado or not iddigitado.isdigit(): 
           print("ID inválido. Digite um número.")
           continue
 
        
        idapoio = int(iddigitado) 
        break

    # criando conexão com o banco de dados
    conn = Conectar()
    cursor = conn.cursor()

    #ENVIANDO A BD E EXIBINDO A LISTA
    cursor.execute("SELECT IDAPOIO, TIPO_SERVICO, DESCRICAO, NOME_INSTITUICAO, ENDERECO_RUA, ENDERECO_NUMERO, ENDERECO_COMPLEMENTO, ENDERECO_CIDADE, ENDERECO_ESTADO, TELEFONE FROM APOIO WHERE IDAPOIO = %s", (idapoio,))

    resultados = cursor.fetchall()

    if not resultados:
        print("\n Nenhum serviço encontrado com esse ID.\n")
    else:
        for idapoio, tipo, descricao, nome, rua, numero, complemento, cidade, estado, telefone in resultados:
            print(f"ID: {idapoio}")
            print(f"Tipo: {tipo}")
            print(f"Descrição: {descricao}")
            print(f"Instituição: {nome}")
            print(f"Endereço: {rua},{numero} {complemento} {cidade} {estado}")
            print(f"Telefone: {telefone}")
            print("")
        #FECHANDO A CONEXÃO
    cursor.close()
    conn.close()

    input("pressione enter para voltar ao menu")


def AlterarServico2(idapoio): #CRIANDO A FUNÇÃO ALTERAR
    print("******************************")
    print(" Alterando o Serviço ")
    print("******************************")
    print("")

    print("Informe os novos valores do serviço:") #INCLUIR NOVOS DADOS COM VALIDAÇÃO DE PREENCHIMENTO OBRIGATÓRIO
    while True: 
        tipo = input("Informe o tipo de apoio: ")
        if tipo == "":
            print("Por favor, informe o tipo de apoio que a instituição oferece: ")
        else:
            break
    while True:
        descricao = input("Descreva com detalhes os serviços oferecidos: ")
        if descricao == "":
            print("Por favor, descreva com detalhes os serviços oferecidos: ")
        else:
            break
    while True:
        nome = input("Informe o nome da Instituição de Apoio: ")
        if nome == "":
            print("Por favor, digite o nome da instituição que oferece o serviço: ")
        else:
            break        
    rua= input("Informe (se souber) o nome da rua onde fica localizada a instituição: ")
    numero= input("Informe (se souber) o número do endereço da instituição: ")
    complemento=input("Informe (se houver) o complemento ou ponto de referência do endereço: ")
    while True:
        cidade=input("Informe a cidade onde a instituição está localizada: ")
        if cidade == "":
            print("Por favor, informe a cidade onde a instituição está localizada: ")
        else:
            break
    while True: 
        estado= input("Informe a sigla do Estado onde a instituição está localizada: ")
        if estado == "":
            print("Por favor, informe o Estado onde a instituição está localizada")
        else:
            break    
    telefone=input("Informe o telefone ou e-mail para contato: ")
# criando conexão com o banco de dados
    conn = Conectar()
    cursor = conn.cursor()

    # enviando comando sql para alterar o servico
    cursor.execute("UPDATE APOIO SET TIPO_SERVICO = %s,  DESCRICAO=%s, NOME_INSTITUICAO = %s, ENDERECO_RUA = %s,ENDERECO_NUMERO = %s,ENDERECO_COMPLEMENTO = %s,ENDERECO_CIDADE = %s,ENDERECO_ESTADO = %s, TELEFONE = %s WHERE IDAPOIO = %s", (tipo, descricao, nome, rua, numero, complemento, cidade, estado, telefone, idapoio))
    conn.commit()
    #FECHANDO CONEXAO
    cursor.close()
    conn.close()

    print("Servico atualizado com sucesso!")
    input("pressione enter para voltar ao menu")


def ExcluirServico2(idapoio): #CRIANDO FUNÇAO EXCLUIR
    print("")
    print("******************************")
    print(" Excluir o Serviço ")
    print("******************************")
    print("")

    confirmar = input("Deseja realmente excluir o servico (informe 1 para confirmar):").strip()
    if(confirmar == '1'):
        #criando conexao com o banco de dados
        conn = Conectar()
        cursor = conn.cursor()
    
        # enviando comando sql para excluir o servico
        cursor.execute("DELETE FROM APOIO WHERE IDAPOIO = %s",(idapoio,))

        conn.commit()
            #FECHANDO CONEXAO
        cursor.close()
        conn.close()

        print("Serviço removido com sucesso!")
        print("")
    else:
        print("Operação cancelada!")

    input("pressione enter para voltar ao menu")


def ListarServicosTipo(): #CRIANDO FUNÇÃO DE PESQUISA POR TIPO
    from buscas import opcaoServicoTipo, ContinuarTipo
    print("***************************************************************************************************************************************************")
    print("                                                  Pesquisa de serviço por tipo ")
    print("***************************************************************************************************************************************************")
    print("")

    tipo = input("Informe o tipo de serviço (uma parte do texto): ")
    print("")

    #criando a conexao
    conn = Conectar()
    cursor = conn.cursor()

    #enviando o camando para o banco de dados

    cursor.execute("""SELECT IDAPOIO, TIPO_SERVICO, DESCRICAO, NOME_INSTITUICAO, ENDERECO_CIDADE, ENDERECO_ESTADO FROM APOIO
    WHERE UPPER(TIPO_SERVICO) LIKE UPPER(%s)
       OR UPPER(DESCRICAO) LIKE UPPER(%s)""", (f"%{tipo}%", f"%{tipo}%"))
    
    buscaservicotipo = cursor.fetchall()
    if not buscaservicotipo:
        print("Nenhum serviço encontrado.")
        opcaoServicoTipo()

    else:

    #percorrendo o resultado e mostrando em tela
        for idapoio, tipo, descricao, nome, cidade, estado in buscaservicotipo:
            print("")

            print("| ID: " + f" {CompletaTexto(idapoio, 3, ' ')} | {CompletaTexto(tipo, 14, ' ')} | {CompletaTexto(descricao, 30, ' ')} | {CompletaTexto((nome), 20, ' ')} | {CompletaTexto((cidade), 15, ' ')} | {CompletaTexto((estado), 5, ' ')}" + "|")
   
            print("|" + CompletaTexto(" ", 150, " ") +  "|")
            print("+" + CompletaTexto("-", 150, "-") + "+")

        ContinuarTipo()
            

    #fechando a conexao
    cursor.close()
    conn.close()

def ListarServicosCidade(): #CRIANDO PESQUISA POR CIDADE
    from buscas import opcaoServicoCidade, ContinuarCidade
    print("***************************************************************************************************************************************************")
    print("                                                Pesquisa de serviços por cidade ")
    print("***************************************************************************************************************************************************")
    print("")

    cidade = input("Informe o nome da cidade: ")
    print("")

    #criando a conexao
    conn = Conectar()
    cursor = conn.cursor()

    #enviando o comando para o banco de dados
    cursor.execute("""
    SELECT IDAPOIO, TIPO_SERVICO, DESCRICAO, NOME_INSTITUICAO, ENDERECO_CIDADE, ENDERECO_ESTADO
    FROM APOIO
    WHERE UPPER(ENDERECO_CIDADE) LIKE UPPER(%s)
""", (f"%{cidade}%",))

    buscaservico = cursor.fetchall()

    if not buscaservico:
        print("Nenhum serviço encontrado.")
        opcaoServicoCidade()

    else:
    #percorrendo o resultado e mostrando em tela
        for idapoio, tipo, descricao, nome, cidade, estado in buscaservico:
        # print(f"{idapoio} - {tipo} - {descricao} - {nome} - {cidade} - {estado}")
        # print("")


            print("| ID: " + f" {CompletaTexto(idapoio, 3, ' ')} | {CompletaTexto(tipo, 20, ' ')} | {CompletaTexto(descricao, 30, ' ')} | {CompletaTexto(nome, 30, ' ')} | {CompletaTexto((cidade), 10, ' ')} | {CompletaTexto((estado), 5, ' ')}" + "|")
   
            print("|" + CompletaTexto(" ", 150, " ") +  "|")
            print("+" + CompletaTexto("-", 150, "-") + "+")
            print("")
        ContinuarCidade()


    #fechando a conexao
    cursor.close()
    conn.close()