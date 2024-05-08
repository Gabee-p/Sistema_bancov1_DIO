
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

while True:
    opcao = input(menu)

    if opcao == "1":
        print("\n--------------------------------------------------------")
        print("Depósito:\n")

        valor = float(input("Insira o valor desejado: R$  "))
        
        if valor > 0:
            saldo += valor
            print ("\n>> Operação realizado com sucesso.")
            extrato += f"Depósito realizado: R$ {valor:.2f}. \n"
        
        else:
            print("\n>> ERRO: Valor inválido.\n")

    elif opcao == "2":
        print("\n--------------------------------------------------------")
        print("Saque:\n")

        if numero_saques >= 3:
            print("\n>> Você excedeu o limite de saques diários!")
            
        else:
            vsaque = float(input("Insira o valor para saque: R$  "))
            if vsaque > limite:
                print("\n>> ERRO: Valor excede o limite autorizado.")
            elif vsaque > saldo:
                print("\n>> ERRO: Saldo insuficiente.")
            elif vsaque <= 0:
                print("\n>> ERRO: Valor inválido.")
            else:
                saldo -= vsaque
                print("\n>> Operação realizada com sucesso.")
                numero_saques += 1
                extrato += (f"Saque realizado:    R$ {vsaque:.2f}. \n")      
        
    elif opcao == "3":
        print("\n--------------------------------------------------------")
        print("Extrato:\n")

        if extrato == (""):
            print("\n>> Não foram realizadas movimentações.")
            print(f">> Saldo: R$ {saldo:.2f}.")

        else:
            print(extrato)
            print("\n                ***                          \n")
            print (f">> Saldo: R$ {saldo:.2f}.")

    elif opcao == "4":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")

print("\nO banco SP agradece sua visita, volte sempre!\n")
print ("---------------------------------------")