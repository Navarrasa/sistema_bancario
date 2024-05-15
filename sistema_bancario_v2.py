# Keyword only ==> *
# Positional Only ==> /
# TODO Criar uma lista de usuários e contas bancárias
# TODO Criar duas novas funções: Cadastrar usuário e Cadastrar conta bancária

def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato,):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(cliente):
    usuarios = []


#def conta_bancaria()

#def listar_contas(contas)

def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [ncu] Novo Cadastro de Usuário
    [ccb] Cadastrar Conta Bancária
    [e] Extrato
    [lc] Listar Contas
    [q] Sair

    => """
    return input(menu)

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo ,extrato = deposito(saldo,valor,extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "ncu":
            print("Novo Usuario")
        elif opcao == "ccb":
            print("Nova CCB")
        elif opcao == "lc":
            print("Listando Contas:")
        elif opcao == "q":
            print("Encerrando o Programa...")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()