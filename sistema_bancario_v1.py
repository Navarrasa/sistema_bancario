import os, time

menu = """
Qual operação deseja efetuar?
________________________
|                      |
|    [D] Depositar     | 
|    [S] Sacar         |
|    [E] Extrato       |
|    [Q] Sair          |
|______________________|
\n"""
saldo = 0
limite_saque = 500
LIMITE_DIARIO = 3
extrato = ""
numero_saques = 0

def continuar_programa():
    opcao2 = input("\nDeseja efetuar outra operação?\n[s] Sim\n[n] Não\n")
    if opcao2 == "s":
        time.sleep(1)
        os.system("cls")
    else:
        print("Operação finalizada, encerrando programa...")
        time.sleep(2)
        exit()

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Qual valor deseja depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            continuar_programa()
        else:
            print("Valor inválido!")
            time.sleep(3)
            os.system("cls")
            break
    
    if opcao == "s":
        verificar_saldo = float(input("Qual valor deseja sacar? "))
        if verificar_saldo > saldo:
            print("Operação Bloqueada, saldo insuficiente!")
            time.sleep(3)
            os.system("cls")
            break
        if numero_saques == LIMITE_DIARIO:
            print("Operação Bloqueada! Limite de Saques Diário já atingido!")
            time.sleep(3)
            os.system("cls")
            break
        else:        
            numero_saques += 1
            saldo - verificar_saldo
            extrato += f"Saque: R${verificar_saldo:.2f}\n"
            continuar_programa()
    
    if opcao == "e":
        print("\n============ EXTRATO ============")
        print("Não foram realizada movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=================================")
        continuar_programa()
        time.sleep(3)
        os.system("cls")

    if opcao == "q":
        print("Encerrando programa...")
        time.sleep(3)
        os.system("cls")
        break
        




