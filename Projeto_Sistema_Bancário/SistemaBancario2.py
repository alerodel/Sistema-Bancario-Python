################## Sistema Bancário 2.0 - Alexandre Rodel de Almeida ###########################
##### Melhoria do Sistema de Bancário criado anteriormente

import textwrap

def menu():
    menu = """\n
    ====================== MENU ======================
    [d]\tDeposito
    [s]\tSaque
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

#menu()

###################################################################################################################

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        print(f"Seu valor de deposito é de R$ {valor}")
        print(f"Confirma a operacao de desposito no valor de R$ {valor}?")
        print("Digite 0 para 'Sim' ou 1 para 'Nao'.")
        confirmaDeposito = int(input())
        
        if confirmaDeposito == 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! o valor informado é inválido. @@@")
    return saldo, extrato

######################################################################################################################

def sacar(*, saldo, valor, extrato, limite, nSaques, limiteSaques):        
    if saldo < valor <= saldo + limite:
        print(f"\n=== Atenção! Ao concluir essa operação, você estará utilizando o limite de R${limite} da sua conta. ===")
        print(f"\n=== Confirma a operacao de saque no valor de R$ {valor}? ===")
        print("\n=== Digite 0 para 'Sim' ou 1 para 'Nao'. ===")
        confirmaSaque = int(input())
        if confirmaSaque == 0:
            print("\n === Saque realizado com Sucesso! ===")
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            nSaques += 1
    elif valor < saldo:
        print(f"\n=== Seu valor de saque é de R$ {valor} ===")
        print(f"\n=== Confirma a operacao de saque no valor de R$ {valor}? ===")
        print("\n=== Digite 0 para 'Sim' ou 1 para 'Nao'. ===")
        confirmaSaque = int(input())
        if confirmaSaque == 0:
            print("\n=== Saque realizado com Sucesso! ===")
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            nSaques += 1
    elif valor > saldo + limite:
        print("\n@@@ Não e possível realizar o saque. @@@")
    elif nSaques > limiteSaques:
        print(f"\n@@@ Desculpe, você excedeu o seu limite diário de saques. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        nSaques += 1
    else:
        print("\n@@@ O valor solicitado excedeu o limite disponível em sua conta para saque. @@@")
    return saldo, extrato

###################################################################################################################

def exibirExtrato(saldo, /, *, extrato):
    print("\n=================== Extrato ====================")
    print("\n=== Não foram realizadas movimentações. ===" if not extrato else extrato)
    print(f"\nSaldo = R$ {saldo:.2f}")
    print("==================================================")

####################################################################################################################

def criarUsuario(usuarios):
    print("Informe o seu número de CPF:")
    CPF = input("")
    usuario = filtrarUsuario(CPF, usuarios)
    
    #Verificação do número do CPF (serve para saber se já existe algum usuário com o mesmo CPF)
    if usuario:
        print("\n@@@ Esse CPF já consta no sistema. procure o gerente da sua conta! @@@")
        return

    print("Insira o nome completo:")
    Nome = input("")
    print("Insira a data de nascimento no formato 'dd-mm-aaaa':")
    DataNasc = input("")
    print("Informe agora seu endereço no formato 'CEP', 'Número da Residência', 'Complemento':")
    Endereco = input("")

    usuarios.append({"Nome": Nome, "Data Nascimento": DataNasc, "CPF": CPF, "Endereco": Endereco})
    print("\n=== Usuário Cadastrado com sucesso! ===")

####################################################################################################################

def filtrarUsuario(cpf, usuarios):
    usuariosFiltrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None

####################################################################################################################

def criarConta():
    pass

####################################################################################################################

def listarContas():
    pass

####################################################################################################################

def main():
    agencia = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    usuarios = []
    contas = []
    nSaques = 0
    limiteSaques = 3

    while True:   
        operacao = menu()

        if operacao == "d":
            print("Bem vindo ao modulo de 'Deposito' do DIO Bankline.")
            print("Por favor, digite o valor do deposito.")
            valor = float(input())
            
            saldo, extrato = depositar(
                saldo,
                valor,
                extrato
            )
        
        elif operacao == "s":
            print("Bem vindo ao modulo de 'Saque' do DIO Bankline.")
            print("Por favor, digite o valor do saque.")
            valor = float(input())

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                nSaques = nSaques,
                limiteSaques = limiteSaques
            )            

        elif operacao == "e":
            exibirExtrato(saldo, extrato = extrato)

        elif operacao == "nu":
            criarUsuario(usuarios)

        elif operacao == "q":
            break

main()