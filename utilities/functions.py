from classes_main  import classes
from termcolor import colored
from time import sleep
import json
import os

def exibir():
    
    print(colored("-=-" * 15, "white"))
    sleep(1)

def cadastro_menu():
   
    print(colored("Aguarde, estamos iniciando!", "magenta"))
    users = {} 
    new_number = [1, 2, 3, 4]
    flag = 0  

    while flag not in new_number:
        exibir()
        print(colored("Menu de opções:\n", "red", attrs=["reverse", "bold"]))
        print(colored("1 - CADASTRO(DESPESA/USUÁRIO)", "yellow"))
        print(colored("2 - LISTAGEM(DESPESA/CADASTRO)", "green"))
        print(colored("3 - EXCLUIR(DESPESA)", "blue"))
        print(colored("4 - SAIR\n", "cyan"))
        exibir()

        try:
            option = int(input("Digite uma Opção (1-4):➣ "))
        except ValueError:
            print(colored("Opção inválida! Digite um número entre 1 e 4.", "red"))
            flag = False

        if option == 1:
            cadastrar_despesa(users)
        elif option == 2:
            listar_despesas(users)
        elif option == 3:
            excluir_despesa(users)
        elif option == 4:
            print(colored("Saindo...", "red"))
            flag = True
        else:
            print(colored("Opção Inválida! Tente novamente.", "red"))


def cadastrar_despesa(users):
    nome = input("Digite o nome do cliente: ➣ ").strip().upper()
    custo_tipo = input("Digite o Tipo de Despesa: ").strip().upper()
    try:
        value = float(input("Digite o Valor da Despesa:R$ "))
    except ValueError:
        print(colored("Valor inválido! Digite um número.", "red"))
        return

    data_input = input("Digite a data (DD/MM): ").strip()

    if nome not in users:
        users[nome] = []


    users[nome].append({
        "nome_usuario": nome,
        "Tipo de Despesa": custo_tipo,
        "Valor da Despesa": value,
        "Data da Despesa": data_input
    })

    print(colored("Despesa cadastrada com sucesso!", "green"))


def listar_despesas(users):
   
    if not users:
        print(colored("Nenhum usuário ou despesa cadastrada.", "magenta"))
        return

    for nome, despesas in users.items():
        print(colored(f"Nome: {nome}", "blue"))
        for despesa in despesas:
            print(colored(f"  Tipo de Despesa: {despesa['Tipo de Despesa']}", "blue"))
            print(colored(f"  Valor da Despesa: R${despesa['Valor da Despesa']:.2f}", "green"))
            print(colored(f"  Data da Despesa: {despesa['Data da Despesa']}", "yellow"))
            print(colored("-=-=-=-=-=-=-=-=-=-=-", "light_grey"))
        sleep(1)


def excluir_despesa(users):
  
    if not users:
        print(colored("Nenhum usuário ou despesa cadastrada.", "magenta"))
        return

    name_user = input("Digite o nome do cliente: ➣ ").strip().upper()
    tipo_user = input("Digite o tipo de despesa: ➣ ").strip().upper()

    if name_user not in users:
        print(colored("Usuário não encontrado.", "red"))
        return

    despesas_removidas = []
    users[name_user] = [
        despesa for despesa in users[name_user]
        if not (despesa["Tipo de Despesa"].strip().upper() == tipo_user.upper() and despesas_removidas.append(despesa))
       
    ]
    if despesas_removidas:
        print(colored("Despesa(s) excluída(s) com sucesso!", "cyan"))
        salvar_despesas_removidas(despesas_removidas)
    else:
        print(colored("Nenhuma despesa encontrada para excluir.", "light_magenta"))


def salvar_despesas_removidas(despesas_removidas, arquivo='json/despesas_removidas.json'):
   
    if os.path.exists(arquivo) and os.path.getsize(arquivo) > 0:
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados_existentes = json.load(f)
        except json.JSONDecodeError:
         
            print("Aviso: O arquivo JSON estava corrompido. Será sobrescrito.")
            dados_existentes = []
    else:
   
        dados_existentes = []

    dados_existentes.extend(despesas_removidas)

    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados_existentes, f, ensure_ascii=False, indent=4)

    print(f"Despesas removidas salvas em {arquivo} com sucesso!")

if __name__ == "__main__":
    cadastro_menu()