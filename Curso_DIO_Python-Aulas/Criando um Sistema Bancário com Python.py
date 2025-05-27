menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = input("Informe o valor do depósito: ")
        if valor.replace('.', '', 1).isdigit():  # Verifica se o valor é um número
            valor = float(valor)
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print("Operação falhou! Insira um número válido.")

    elif opcao == "s":
        valor = input("Informe o valor do saque: ")
        if valor.replace('.', '', 1).isdigit():
            valor = float(valor)
            if valor > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor > limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print("Operação falhou! Insira um número válido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")