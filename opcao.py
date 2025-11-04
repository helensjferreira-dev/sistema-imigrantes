from datetime import datetime
import os

# def LimpaTela():
#     os.system('cls' if os.name == 'nt' else 'clear')
    
def CompletaTexto(pTexto, pTamanho, pCaracter):
    #convertendo valores em texto
    texto = str(pTexto)
    caracter = str(pCaracter)
    # calculando a quantidade de caracteres faltantes para completar o tamanho
    qtdeFaltande = pTamanho - len(texto)
    
    if (qtdeFaltande > 0 and len(caracter) == 1):
        resultado = texto + (caracter * qtdeFaltande)
    else:
        resultado = texto
        
    return resultado

def ValidaData(data_str):
    """
    Recebe uma data no formato dd/mm/yyyy, valida e retorna no formato yyyy-mm-dd.
    """
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return data.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida. Use o formato dd/mm/yyyy.")

def FormataData(data_str):
    """
    Recebe uma data no formato yyyy-mm-dd e retorna no formato dd/mm/yyyy.
    """
    try:
        if isinstance(data_str, str):
            data = datetime.strptime(data_str, "%Y-%m-%d")
        else:
            data = data_str
        return data.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida. Use o formato yyyy-mm-dd.")
    
def ValidaAno(entrada):
    try:
        ano = int(entrada)
        ano_atual = datetime.now().year
        if 1900 <= ano <= ano_atual + 5:
            return ano
        else:
            raise ValueError("Ano fora do intervalo permitido.")
    except ValueError:
        raise ValueError("Entrada inválida. Informe um ano inteiro, como 2025.")