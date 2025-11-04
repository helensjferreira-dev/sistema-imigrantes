import mysql.connector


def Conectar(): #CONEXAO DE CASA
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="helen",
        password="minhaSenha123",
        database="DBPROJETOINTEG"
        )


# # conn = Conectar()
# # curso=conn.cursor() #teste se bd ta interligado
# # curso.execute("SELECT NOME_COMPLETO FROM IMIGRANTE")
# # for NOME_COMPLETO in curso.fetchall():
# #     print(NOME_COMPLETO)
# # conn.close()

