from conn import Conectar

def confereID():
    from complementoTela import MenuComplemento  
    while True: 
        iddigitado = input("Informe o ID do imigrante: ").strip()
        if not iddigitado or not iddigitado.isdigit(): 
           print("ID inválido. Digite um número.")
           continue
 
        
        id = int(iddigitado) 

        conn = Conectar()
        cursor=conn.cursor() 

        cursor.execute("SELECT IDIMIGRANTE, PRIMEIRO_NOME, SOBRENOME, NACIONALIDADE, IDIOMA, DATA_NASCIMENTO, DOCUMENTO_IDENTIFICACAO, CONTATO FROM IMIGRANTE WHERE IDIMIGRANTE=%s", (id,)) 

        resultados = cursor.fetchall()
        if not resultados:
            print("Nenhum imigrante encontrado.")
        else:
            MenuComplemento(id)
            break


def ConfereIdalt():
    from imigrante import AlterarImigrante2
    while True: 
        iddigitado = input("Informe o ID do imigrante: ").strip()
        if not iddigitado or not iddigitado.isdigit(): 
           print("ID inválido. Digite um número.")
           continue
 
        
        id = int(iddigitado) 

        conn = Conectar()
        cursor=conn.cursor() 

        cursor.execute("SELECT IDIMIGRANTE, PRIMEIRO_NOME, SOBRENOME, NACIONALIDADE, IDIOMA, DATA_NASCIMENTO, DOCUMENTO_IDENTIFICACAO, CONTATO FROM IMIGRANTE WHERE IDIMIGRANTE=%s", (id,)) 

        resultados = cursor.fetchall()
        if not resultados:
            print("Nenhum imigrante encontrado.")
        else:
            AlterarImigrante2(id)
            break




def ConfereIdex():
    from imigrante import ExcluirImigrante2
    while True: 
        iddigitado = input("Informe o ID do imigrante: ").strip()
        if not iddigitado or not iddigitado.isdigit(): 
           print("ID inválido. Digite um número.")
           continue
 
        
        id = int(iddigitado) 

        conn = Conectar()
        cursor=conn.cursor() 

        cursor.execute("SELECT IDIMIGRANTE, PRIMEIRO_NOME, SOBRENOME, NACIONALIDADE, IDIOMA, DATA_NASCIMENTO, DOCUMENTO_IDENTIFICACAO, CONTATO FROM IMIGRANTE WHERE IDIMIGRANTE=%s", (id,)) 

        resultados = cursor.fetchall()
        if not resultados:
            print("Nenhum imigrante encontrado.")
        else:
            ExcluirImigrante2(id)
            break


def ConfereIdapoio():
    from apoio import ExcluirServico2
    while True: 
        iddigitado = input("Informe o ID do serviço: ").strip()
        if not iddigitado or not iddigitado.isdigit(): 
           print("ID inválido. Digite um número.")
           continue
 
        
        idapoio = int(iddigitado) 

        conn = Conectar()
        cursor=conn.cursor() 

        cursor.execute("SELECT IDAPOIO, TIPO_SERVICO, DESCRICAO, NOME_INSTITUICAO, ENDERECO_RUA, ENDERECO_NUMERO, ENDERECO_COMPLEMENTO, ENDERECO_CIDADE, ENDERECO_ESTADO, TELEFONE FROM APOIO WHERE IDAPOIO = %s", (idapoio,)) 

        resultados = cursor.fetchall()
        if not resultados:
            print("Nenhum serviço encontrado.")
        else:
            ExcluirServico2(idapoio)
            break


def ConfereIdapoioAlt():
    from apoio import AlterarServico2
    while True: 
        iddigitado = input("Informe o ID do serviço: ").strip()
        if not iddigitado or not iddigitado.isdigit(): 
           print("ID inválido. Digite um número.")
           continue
 
        
        idapoio = int(iddigitado) 

        conn = Conectar()
        cursor=conn.cursor() 

        cursor.execute("SELECT IDAPOIO, TIPO_SERVICO, DESCRICAO, NOME_INSTITUICAO, ENDERECO_RUA, ENDERECO_NUMERO, ENDERECO_COMPLEMENTO, ENDERECO_CIDADE, ENDERECO_ESTADO, TELEFONE FROM APOIO WHERE IDAPOIO = %s", (idapoio,)) 

        resultados = cursor.fetchall()
        if not resultados:
            print("Nenhum serviço encontrado.")
        else:
            AlterarServico2(idapoio)
            break


