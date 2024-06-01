################## Sistema Bancário 2.0 - Alexandre Rodel de Almeida ###########################
##### Criação de um sistema de Bancário
# Parte 1: Módulo de Depósito
# Parte 2: Módulo de Consulta
# Parte 3: Módulo de Saque

######
#from IPython.display import clear_output

saldoAnterior = 0
limite = 500
extrato = ""
nSaques = 00
limiteSaques = 3

print("Seja bem vindo ao Banco DIO".center(10, '#'))
print("Escolha um de nossos serviços".center(10, '#'))
menu = """

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

=> """

while True:
    operacao = input(menu) 
        
    if operacao == "d":
        print("Bem vindo ao modulo de 'Deposito' do DIO Bankline.".center(10, '#'))
        print("Por favor, digite o valor do deposito.".center(10, '#'))
        deposito = float(input())
        if deposito > 0:
            print(f"Seu valor de deposito é de R$ {deposito}".center(10, '#'))
            print(f"Confirma a operacao de desposito no valor de R$ {deposito}?".center(10, '#'))
            print("Digite 0 para 'Sim' ou 1 para 'Nao'.".center(10, '#'))
            confirmaDeposito = int(input())
            
            if confirmaDeposito == 0:
                print("Deposito efetuado com Sucesso!".center(10, '#'))
            
            saldoAnterior += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
        else:
            print(f"A operação falhou! Digite um valor de depósito diferente de R$ {deposito} da próxima vez.")
    ######################################################################################################################
    elif operacao == "s":
        print("Bem vindo ao modulo de 'Saque' do DIO Bankline.".center(10, '#'))
        print("Por favor, digite o valor do saque.".center(10, '#'))
        saque = float(input())
        
        if saldoAnterior < saque <= saldoAnterior + limite:
            print(f"Atenção! Ao concluir essa operação, você estará utilizando o limite de R${limite} da sua conta.")
            print(f"Confirma a operacao de saque no valor de R$ {saque}?".center(10, '#'))
            print("Digite 0 para 'Sim' ou 1 para 'Nao'.".center(10, '#'))
            confirmaSaque = int(input())
            if confirmaSaque == 0:
                print("Saque efetuado com Sucesso!".center(10, '#'))
                saldoAnterior -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                nSaques += 1

        elif saque < saldoAnterior:
            print(f"Seu valor de saque é de R$ {saque}".center(10, '#'))
            print(f"Confirma a operacao de saque no valor de R$ {saque}?".center(10, '#'))
            print("Digite 0 para 'Sim' ou 1 para 'Nao'.".center(10, '#'))
            confirmaSaque = int(input())
            if confirmaSaque == 0:
                print("Saque efetuado com Sucesso!".center(10, '#'))
                saldoAnterior -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                nSaques += 1
        
        elif saque > saldoAnterior + limite:
            print("Não e possível realizar o saque.")

        elif nSaques > limiteSaques:
            print(f"Desculpe, você excedeu o seu limite diário de saques.")

        elif saque > 0:
            saldoAnterior -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            nSaques += 1
        
        else:
            print("O valor solicitado excedeu o limite disponível em sua conta para saque.")
###################################################################################################################
    elif operacao == "e":
        print("\n=================== Extrato ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo = R$ {saldoAnterior:.2f}")
        print("==================================================")
####################################################################################################################
    elif operacao == "q":
        break

    # if option == 1:    
    #     print("Deseja efetuar alguma outra operacao no DIO bankline?".center(10, '#'))
    #     print("Digite 0 voltar ao Menu Principal ou 1 Sair.".center(10, '#'))
    #     opcao = input("")
    #     if opcao == 1:
    #         pass
    #     print("Obrigado por escolher o DIO Bankline!".center(10, '#'))
    #     print("Até logo!")