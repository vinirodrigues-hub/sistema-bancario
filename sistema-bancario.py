limite = 0
saldo = 0
print("-" * 30)
print("$ Conta Bancaria $")
print("-" * 30)
senha_correta = input("Crie uma senha: ")
while limite < 3:

    senha = input("Digite sua senha: ")

    if senha == senha_correta:
        print("Acesso concedido!")
        limite = 0

        opcao = 0


        while opcao != 4:

            print("1 - Consultar saldo")
            print("2 - Depositar dinheiro")
            print("3 - Sacar dinheiro")
            print("4 - Sair")

            opcao = int(input("O que deseja fazer? "))

            if opcao == 1:
                print(f"Seu saldo é de R$ {saldo:.2f}")

            elif opcao == 2:
                deposito = float(input("Quanto deseja depositar? "))

                if deposito <= 0:
                    print("Não é possível fazer o depósito.")
                else:
                    saldo = deposito + saldo
                    print("Ok, depositado.")

            elif opcao == 3:
                saque = float(input("Quanto deseja sacar? "))

                if saque > saldo:
                    print("Você não tem dinheiro o suficiente para efetuar o saque.")

                elif saque <= 0:
                    print("Não é possível fazer o saque.")

                else:
                    saldo = saldo - saque
                    print("Ok, sacando.")

            elif opcao == 4:
                print("Saindo...")

            else:
                print("Opção inválida!")

        voltar = input("Deseja voltar ao menu de login? (s/n): ")

        if voltar == "s":
            continue
        else:
            print("Saindo...")
            break

    else:
        print("Conta incorreta! Caso erre 3 vezes sua conta será bloqueada.")

    limite += 1

if limite == 3:
    print("Conta bloqueada!")