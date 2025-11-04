from conn import Conectar
from opcao import ValidaAno
from opcao import CompletaTexto

def CadExperiencia(id):
    from imigrante import ListarTodosImigrantes
    print("*******************************************************************************************")
    print("                          Cadastrar Experiência Profissional ")
    print("*******************************************************************************************")
    print("")

    #SOLICITANDO INFORMAÇÕES COMPLEMENTARES
    while True:
        tipo = input("Informe o CARGO ou FUNÇÃO que ocupou: ")
        if tipo == "":
            print("Digite o cargo ou função que ocupou: ")
        else: 
            break
    while True:
        descricao = input("Informe o NOME da EMPRESA em que atuou: ")
        if descricao == "":
            print("Informe o nome da empresa em que atuou: ")
        else: 
            break
       
    while True:
        anoinicio = input("Informe o ANO INICIAL: ")
        try:
            ValidaAno(anoinicio)
            break  # Sai do loop se for válida
        except ValueError as e:
            print(e)
    #validando ano final
    while True:
        anotermino = input("Informe o ANO FINAL: ")
        try:
            ValidaAno(anotermino)
            break  # Sai do loop se for válida
        except ValueError as e:
            print(e)

    #CRIANDO A CONEXÃO 
    conn = Conectar()
    cursor=conn.cursor() 

    #enviar o comando para o banco de dados
    cursor.execute("INSERT INTO COMPLEMENTO(TIPO_COMPLEMENTO, DESCRICAO, ANO_INICIO, ANO_TERMINO, IDIMIGRANTE) VALUES(%s, %s, %s, %s, %s)", 
                   (tipo, descricao, anoinicio, anotermino, id)) #%s indica que vamos usar as variaveis
    conn.commit() #efetua a gravação do registro no banco

    print("")
    print("Experiência cadastrada com sucesso")

    
    input("Pressione enter para continuar!") #não direcionando a nada ele vai parar

    #fechando as conexoes
    cursor.close()
    conn.close()


def CadCurso(id):
    print("****************************")
    print("   Cadastrar Cursos   ")
    print("****************************")
    print("")

    while True:
        tipo = input("Informe o TIPO DE INFORMAÇÃO, se é um Curso, atividade ou Voluntariado: ")
        if tipo == "":
            print("Por favor, informe o tipo de Informação que deseja cadastrar: ")
        else: 
            break
    while True:
        descricao = input("Informe uma BREVE DESCRIÇÃO como o nome do curso ou das atividades realizadas: ")
        if descricao == "":
            print("Informe uma breve descrição como o nome do curso ou das atividades realizadas: ")
        else: 
            break
    while True:
        anoinicio = input("Informe o ANO INICIAL: ")
        try:
            ValidaAno(anoinicio)
            break  # Sai do loop se for válida
        except ValueError as e:
            print(e)
    #validando ano final
    while True:
        anotermino = input("Informe o ANO FINAL: ")
        try:
            ValidaAno(anotermino)
            break  # Sai do loop se for válida
        except ValueError as e:
            print(e)


    #CRIANDO A CONEXÃO 
    conn = Conectar()
    cursor=conn.cursor() #para executar comandos precisa usar o cursor

    #enviar o comando para o banco de dados
    cursor.execute("INSERT INTO COMPLEMENTO(TIPO_COMPLEMENTO, DESCRICAO, ANO_INICIO, ANO_TERMINO, IDIMIGRANTE) VALUES(%s, %s, %s, %s, %s)", 
                   (tipo, descricao, anoinicio, anotermino, id)) #%s indica que vamos usar as variaveis
    conn.commit() #efetua a gravação do registro no banco

    print("")
    print("Informação cadastrada com sucesso")

    #fechando as conexoes
    cursor.close()
    conn.close()



def ListarComplemento(id):
    print("*******************************************************************************************************")
    print("                         Lista de Informações Complementares         ")
    print("*******************************************************************************************************")
    print("")

     #CRIANDO A CONEXÃO 
    conn = Conectar()
    cursor=conn.cursor() 

    #ENVIANDO O COMANDO PARA O BANCO DE DADOS SELECIONAR
    cursor.execute("SELECT IDCOMPLEMENTO, TIPO_COMPLEMENTO, DESCRICAO, ANO_INICIO, ANO_TERMINO FROM COMPLEMENTO WHERE IDIMIGRANTE=%s ", (id,))

    #PERCORRENDO O RESULTAFO E MOSTRANDO EM TELA
    detalhescomplemento = cursor.fetchall()
    if not detalhescomplemento:
        print("")
        print("IMIGRANTE NÃO POSSUI INFORMAÇÕES COMPLEMENTARES NO CADASTRO.")
        print("")
    else:
        for idcomplemento, tipo, descricao, anoinicio, anotermino in detalhescomplemento: #a ordem precisa ser as mesmas dos campos da tabela. fetchall pega todos os dados e traz pra percorrer

            print("|" + f" {CompletaTexto(idcomplemento, 3, ' ')} | {CompletaTexto(tipo, 20, ' ')} | {CompletaTexto(descricao, 30, ' ')} | {CompletaTexto((anoinicio), 4, ' ')} | {CompletaTexto((anotermino), 4, ' ')}" + "|")
   
            print("|" + CompletaTexto(" ", 100, " ") +  "|")
            print("+" + CompletaTexto("-", 100, "-") + "+")


    #fechando as conexoes
    cursor.close()
    conn.close()

#opção para alterar se tiver complemento para alterar

def AlterarComplemento2(id):
    print("")
    print(" === Alterando Informações do Imigrante === ")
    print("")
    
    while True:
        iddigitado = input("Informe o código da informação: ").strip()
        if not iddigitado or not iddigitado.isdigit(): 
           print("ID inválido. Digite um número.")
           continue
         
        idcomplemento = int(iddigitado) 
        break
    conn = Conectar()
    cursor = conn.cursor()
    

#VERIFICANDO SE EXISTEM INFORMAÇÕES CADASTRADAS
    cursor.execute("""
    SELECT IDCOMPLEMENTO, TIPO_COMPLEMENTO, DESCRICAO, ANO_INICIO, ANO_TERMINO, IDIMIGRANTE FROM COMPLEMENTO
   WHERE IDCOMPLEMENTO =%s and IDIMIGRANTE=%s""", (idcomplemento,id))
    
            
    buscaporidcomplemento= cursor.fetchall()
    if not buscaporidcomplemento:
        print("")
        input("Não há informações complementares cadastradas para alterar OU o código da Informação está incorreto. ")
        return
        
    else:

        while True:
            tipo = input("Informe o tipo de Informação Complementar (Curso ou Experiência Profissional): ")
            if tipo == "":
                print("Por favor, informe o tipo de Informação que deseja cadastrar: ")
            else: 
                break
        while True:
            descricao = input("Informe uma breve descrição como o nome ou as atividades realizadas: ")
            if descricao == "":
                print("Informe uma breve descrição como o nome ou as atividades realizadas: ")
            else: 
                break
        
        while True:
            anoinicio = input("Informe o ano inicial: ")
            try:
                ValidaAno(anoinicio)
                break  # Sai do loop se for válida
            except ValueError as e:
                print(e)
        #validando ano final
        while True:
            anotermino = input("Informe o ano final: ")
            try:
                ValidaAno(anotermino)
                break  # Sai do loop se for válida
            except ValueError as e:
                print(e)
            
            

        cursor.execute("UPDATE COMPLEMENTO SET TIPO_COMPLEMENTO = %s, DESCRICAO = %s, ANO_INICIO = %s, ANO_TERMINO = %s WHERE IDCOMPLEMENTO = %s",
                   (tipo, descricao, anoinicio, anotermino, idcomplemento))
        conn.commit()

        cursor.close()
        conn.close()

        print("Informação atualizada com sucesso")
        input("Pressione enter para continuar")


#opção: por idimigrante

def ExcluirComplemento2(id):
    print("")
    print("                   === Excluindo Informações Complementares do Imigrante ===                  ")
    print("")


    conn = Conectar()
    cursor = conn.cursor()


    cursor.execute("""
    SELECT IDCOMPLEMENTO, TIPO_COMPLEMENTO, DESCRICAO, ANO_INICIO, ANO_TERMINO FROM COMPLEMENTO
   WHERE IDIMIGRANTE =%s""", (id,))
            
    buscaporidimigrante= cursor.fetchall()
    if not buscaporidimigrante:
        print("")
        print("Não há informações complementares cadastradas. ")
        input("Pressione enter para continuar. ")
        return
        
    else:
        #listar todos os complementos do imigrante e depois pedir o numero da informação para excluir
        ListarComplemento(id)
        print("")

        while True: 
            iddigitado = input("Informe o ID da Informação que deseja excluir: ").strip()
            if not iddigitado or not iddigitado.isdigit(): 
                print("ID inválido. Digite um número.")
                continue
    
            idcomplemento = int(iddigitado) 
            

            ids_disponiveis = [linha[0] for linha in buscaporidimigrante]
            if idcomplemento not in ids_disponiveis:
                print("Esse código não pertence às informações desse imigrante.")
                print("")
                input("Pressione enter para continuar. ")
                continue
            break

        while True:
            confirma=input("Deseja realmente excluir a informação? Digite s para Sim ou n para Não: ").lower()
            if confirma == "n":
                print("Operação cancelada. ")
                input("Pressione enter para continuar. ")
                break
            elif confirma == "s":
                cursor.execute("DELETE FROM COMPLEMENTO WHERE IDIMIGRANTE = %s AND IDCOMPLEMENTO=%s",(id,idcomplemento))
                conn.commit()

                cursor.close()
                conn.close()

                
                print("Informação excluída com sucesso")
                print("")
                break

            else:
                print("Opção inválida. Digite s para confirmar ou n para cancelar.")

        input("Pressione enter para continuar")

      


