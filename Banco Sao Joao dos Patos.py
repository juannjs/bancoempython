entrada = 1
contas = [500, 500, 500]

def senhas (senha):
    if senha == 111:
        conta = 0
    elif senha == 222:
        conta = 1
    elif senha == 333:
        conta = 2
    return conta

def depositar (conta, p, valor):
    conta[p] = conta[p] + valor

def sacar (conta, p, valor):
    conta[p]= conta[p] - valor

def transferir (conta, p, pt, valor):
    conta[p] = conta[p] - valor
    conta[pt] = conta[pt] + valor

def consultar (conta, p):
    print (f"Seu saldo atual é: {conta[p]}")
    print ()
    

def menu ():
    print ("1 - Consultar\n2 - Sacar\n3 - Transferir\n4 - Depositar\n5 - Sair da conta atual")
    print ()
    
while entrada == 1:
    entrada = int (input ("Banco São João dos Patos\n1- Acessar conta\n2- Sair do programa: "))
    print ()

    if entrada == 1:
        senha = int (input ("Digite sua senha: "))
        pos = senhas(senha)
        print ()
        opcao = 1
        while opcao != 5:
            menu ()
            opcao = int (input ("Digite sua opção: "))
            print ()
            if opcao == 1:
                consultar (contas, pos)
                
            elif opcao == 2:
                valor = int (input ("Digite o valor do saque: "))
                print ("\n Saque realizado com sucesso \n")
                sacar (contas, pos, valor)
                
            elif opcao == 3:
                valor = int (input ("Digite o valor da transferencia: "))
                posT = int (input ("Digite o numero da conta: "))
                print ("\n Transferencia realizada com sucesso \n")
                transferir (contas, pos, posT, valor)
                
            elif opcao == 4:
                valor = int (input ("Digite o valor do deposito: "))
                print ("\n Deposito realizado com sucesso \n")
                depositar (contas, pos, valor)
