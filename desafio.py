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

print("========= Bem-vindo ao Banco =========")

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        if not valor > 0:
            print("Valor inválido. O depósito deve ser positivo.")
            continue
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Informe o valor a ser sacado: "))
            if not valor > 0:
                print("Valor inválido. O saque deve ser positivo.")
                continue
            if valor <= saldo and valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")
            elif valor > saldo:
                print("Saque não realizado. Saldo insuficiente.")
            elif valor > limite:
                print("Saque não realizado. Valor acima do limite permitido.")
            else:
                print("Saque não realizado. Verifique o saldo e o limite.")
        else:
            print("Limite de saques atingido.")

    elif opcao == "e":
        print("============== Extrato ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=====================================")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
