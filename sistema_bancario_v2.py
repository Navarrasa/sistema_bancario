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

def cadastrar_usuario(usuarios):
    cpf = input("Digite o seu CPF (somente números): ")

    usuario = verificar_cadastro_cliente(cpf,usuarios)
    if usuario:
        print("Já existe um cadastro com este CPF!")
        return
    
    nome = input("Digite o seu nome: ")
    data_nasc = input("Digite a sua data de nascimento neste modelo: dd-mm-aaaa: ")
    endereco = input("Digite o seu endereço neste modelo: Logradouro-Número-Bairro-Cidade/Sigla(UE): ")
    usuarios.append({"nome": nome ,"data_nascimento": data_nasc ,"endereço": endereco , "cpf": cpf})
    print("Cliente cadastrado com sucesso!")

def verificar_cadastro_cliente(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def conta_bancaria(agencia, numero_conta, usuarios):
    cpf = input("Digite o seu CPF (somente números): ")
    usuario = verificar_cadastro_cliente(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia ,"numero_conta": numero_conta ,"usuario": usuario}
    print("Usuário não cadastrado com este CPF, cadastro de nova conta bancária, encerrado.")

def listar_contas(contas):
    for conta in contas:
        print(f"""
        Agência:{conta['agencia']}
        Conta:{conta['numero_conta']}
        Titular:{conta['usuario']['nome']}
        """)

def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [nu] Novo Usuário
    [ccb] Cadastrar Conta Bancária
    [e] Extrato
    [lc] Listar Contas
    [q] Sair

    => """
    return input(menu).lower()

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
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

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "ccb":
            numero_conta = len(contas) + 1
            conta = conta_bancaria(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("Encerrando o Programa...")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()