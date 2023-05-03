valor_em_conta = 0
def saque(valordesc):
    global valor_em_conta
    if valor_em_conta > valordesc:
        valor_em_conta -= valordesc
        print(f"valor em conta:R${valor_em_conta}")
    else:
        print("Saldo insuficiente")


def deposito(valordep):
    global valor_em_conta
    valor_em_conta += valordep
    print(f"valor em conta:R${valor_em_conta}")


def valor_vizualizar():
    global valor_em_conta
    print(f"R${valor_em_conta}")

print("Bem vindo ao Banco!")

while True:
    print("Como podemos lhe ajudar: \n 1- Depositar \n 2- Sacar \n 3- Saldo \n 4- Sair")
    esc = int(input("Podemos lhe ajudar? "))

    if esc == 1:
        print("Quanto deseja depositar?")
        deposito(int(input()))
    elif esc == 2:
        print("Quanto deseja sacar?")
        saque(int(input()))
    elif esc == 3:
        valor_vizualizar()
    elif esc == 4:
        print("Saindo...")
        break
    else:
        print("Opção invalida, tente novamente!")

    input()
