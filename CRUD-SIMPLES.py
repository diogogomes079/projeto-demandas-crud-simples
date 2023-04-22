import sqlite3
import datetime
from tabulate import tabulate

from Constantes import *

database = 'dados.sqlite3'

demanda = ''
resumo = ''


def Gera_data():
    data_lista = []
    data = datetime.date.today()
    if (data.day < 10):
        data_lista.append(f'0{data.day}')
    else:
        data_lista.append(data.day)
    if (data.month < 10):
        data_lista.append(f'0{data.month}')
    else:
        data_lista.append(data.month)

    data_formatada = "/".join(data_lista) + '/' + str(data.year)

    return data_formatada


# C: Create – Criar um novo registro.
def Create():
    loop = True
    while loop:
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Cadastrando Demanda")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        demanda = input("Digite o Numero da Demanda: ")
        print("\n================================")
        i = 0
        for linha in LISTA_STATUS:
            print(f"[{i+1}] - ", linha)
            i = i+1
        status = int(input("Informe o Status: "))
        print("\n================================")
        resumo = input("Informe o Resumo: ")
        print("\n================================\n")
        data = Gera_data()
        parada = int(input("Deseja cadastrar mais?\nDigite 0 para PARAR : "))
        if (parada == 0):
            loop = False
            
    conexao = sqlite3.connect(database)
    cursor = conexao.cursor()
    try:
        cursor.execute(f"INSERT INTO ticket (demanda, status, resumo, data) VALUES ('{demanda}', '{LISTA_STATUS[status-1]}', '{resumo}', '{data}')")
        conexao.commit()
    except sqlite3.IntegrityError:
        print(f"\n  ESSA DEMANDA JÁ ESTÁ CADASTRADA: {demanda}")
    conexao.close()


# R: Read – Ler um registro, ou uma lista de registros.
def Read(opcao="Padrão"):
    conexao = sqlite3.connect(database)
    cursor = conexao.cursor()
    if (opcao == "Padrão"):
        print("\n---------------------------------------------------------")
        print(f"--------------------Listagem [{opcao}]--------------------")
        print("---------------------------------------------------------\n")
        cursor.execute(
            f'SELECT demanda, status, resumo, data FROM ticket')
        dados_lidos = cursor.fetchall()
        conexao.close()
        return dados_lidos

    elif (opcao == "Demanda"):
        print("\n--------------------------------------------------------------")
        print(f"--------------------Listagem por [{opcao}]--------------------")
        print("--------------------------------------------------------------\n")
        cursor.execute(
            f'SELECT demanda, status, resumo, data FROM ticket ORDER by demanda;')
        dados_lidos = cursor.fetchall()
        conexao.close()
        return dados_lidos

    elif (opcao == "Status"):
        print("\n--------------------------------------------------------------")
        print(f"--------------------Listagem por [{opcao}]--------------------")
        print("--------------------------------------------------------------\n")
        cursor.execute(
            f'SELECT demanda, status, resumo, data FROM ticket ORDER by status;')
        dados_lidos = cursor.fetchall()
        conexao.close()
        return dados_lidos

    elif (opcao == "Data"):
        print("\n--------------------------------------------------------------")
        print(f"--------------------Listagem por [{opcao}]--------------------")
        print("--------------------------------------------------------------\n")
        cursor.execute(
            f'SELECT demanda, status, resumo, data FROM ticket ORDER by data;')
        dados_lidos = cursor.fetchall()
        conexao.close()
        return dados_lidos



# U: Update – Atualizar um registro.
def Update():
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Atualizando Demanda")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    demanda = input("Digite o Numero da Demanda: ")
    print("\n================================")
    i = 0
    for linha in LISTA_STATUS:
        print(f"[{i+1}] - ", linha)
        i = i+1
    status = int(input("Informe o Status: "))
    print("\n================================")
    resumo = input("Informe o Resumo: ")
    print("\n================================\n")
        
    conexao = sqlite3.connect(database)
    cursor = conexao.cursor()
    cursor.execute(f"UPDATE ticket SET status='{LISTA_STATUS[status-1]}', resumo='{resumo}' WHERE demanda= '{demanda}';")
    conexao.commit()
    print('Dados atualizados com sucesso.')
    conexao.close()


# D: Delete – Excluir um registro.
def Delete():
    conexao = sqlite3.connect(database)
    cursor = conexao.cursor()
    # cursor.execute()
    conexao.close()

def Search():
    pass


menu = ["Cadastrar", "Listar", "Listar por Demanda", "Listar por Status", "Listar por Data", "Pesquisar",
        "Atualizar", "Deletar", "Parar Programa?"]
loop = True
while loop:
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Menu Principal")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    i = 0
    for item in menu:
        if (i < len(menu)):
            print(f"[{i+1}] - ", item)
        i += 1
    escolha = int(input("Escolha uma opção: "))
    if (escolha == 1):
        Create()
        
    elif (escolha == 2):
        dados = Read()
        print(tabulate(dados, headers=["Demanda", "Status", "Resumo", "Data"]))
        
    elif (escolha == 3):
        dados = Read(opcao="Demanda")
        print(tabulate(dados, headers=["Demanda", "Status", "Resumo", "Data"]))
        
    elif (escolha == 4):
        dados = Read(opcao="Status")
        print(tabulate(dados, headers=["Demanda", "Status", "Resumo", "Data"]))
        
    elif (escolha == 5):
        dados = Read(opcao="Data")
        print(tabulate(dados, headers=["Demanda", "Status", "Resumo", "Data"]))
        
    elif (escolha == 6):
        Search()
        
    elif (escolha == 7):
        Update()
        
    elif (escolha == 8):
        Delete()
        
    elif (escolha == len(menu)):
        loop = False
    
    else:
        print("Opção Invalida!!!")
    print("\n================================")
#dados = [demanda, LISTA_STATUS[status-1], resumo, data]
#print(dados)

#Create(dados)



