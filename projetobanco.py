
menu = '''

--------------------------------------------------------

Bem vindo ao banco SP, escolha uma opção do menu abaixo:

====== MENU ======

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

==================

>> '''
valor = 0.00
saldo  = 0.00
limite = 500.00
vsaque = 0.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("")
        print("------ Depósito ------")
        print("")
        valor = float(input("Insira o valor desejado: R$  "))
        saldo += valor
        print("")
        print(f">> O seu saldo agora é R$ {saldo:.2f}")
        print("")
        extrato += (f"Depósito realizado no valor de R$ {valor:.2f}. \n")

    elif opcao == "2":
        print("")
        print("------ Saque ------")
        print("")
        if numero_saques >= 3:
            print("")
            print(">> Você excedeu o limite de saques diários!")
            print("")
        else:
            vsaque = float(input("Insira o valor para saque: R$  "))
            if vsaque > limite:
                print("")
                print("--------------- ERRO ---------------")
                print(">> Valor excede o limite autorizado.")
            elif vsaque > saldo:
                print("")
                print("-------- ERRO --------")
                print(">> Saldo insuficiente.")
            else:
                saldo -= vsaque
                print("")
                print(">> Operação realizada com sucesso!")
                print("")
                print(f"O seu saldo agora é R$ {saldo:.2f}")
                print("")
                extrato += (f"Saque realizado no valor de R$ {vsaque:.2f}. \n")
        numero_saques += 1
        
    elif opcao == "3":
        print("")
        print("------ Extrato ------")
        print("")
        if extrato == (""):
            print("")
            print(">> Não foram realizadas movimentações.")
            print ("")

        else:
            print(extrato)

    elif opcao == "4":
        break

    else:
        print("")
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print ("")
print("O banco SP agradece sua visita, volte sempre!")
print("")
print ("---------------------------------------")