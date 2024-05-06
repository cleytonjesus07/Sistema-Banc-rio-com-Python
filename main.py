valor_conta: float = 0.0
extrato: str = ""
quantidade_de_saques : int = 1
LIMITE_DE_SAQUE : float = 500.00

def deposito() -> None:
    global valor_conta, extrato
    deposito = float(input("Forneça o valor a ser depositado: "))
    valor_conta += deposito
    extrato += f"Depósito de R${"{:,.2f}".format(deposito)}\n"

def saque() -> None:
    global extrato, valor_conta, quantidade_de_saques
    valor = float(input("Forneça o valor a ser sacado: "))
    if quantidade_de_saques > 3:
        print("Limite de saque diário atingido")
        return
    if valor > LIMITE_DE_SAQUE : 
        print("Valor maior que o limite\n")
        return
    if valor <= valor_conta:
        valor_conta -= valor
        extrato += f"Saque de R${"{:,.2f}".format(valor)}\n"
        print("Saque efetuado com sucesso!\n")
        quantidade_de_saques += 1
    else:
        print("Saldo insuficiente.")

def mostrar_extrato() -> None:
    global extrato
    if not extrato:
        print("Não há nada no extrato")
    else:
        print("\n=====EXTRATO=====")
        print(f"\n{extrato}")
        print("================")

print("\n")
print("Sistema Bancário".center(40, "="))

tentar_novamente: bool = True

while tentar_novamente:
    print(f"\nSaldo atual R${"{:,.2f}".format(valor_conta)}")
    print("""
1 - Depositar
2 - Sacar
3 - Visualizar extrato
4 - Sair
    """)
    escolha = input("Escolha: ")
    match escolha:
        case "1":
            deposito()
        case "2":
            saque()
        case "3":
            mostrar_extrato()
        case "4":
            tentar_novamente = False
            print("Obrigado por ter utilizado os nossos serviços bancários! :)\n")
        case _:
            print("Escolha inválida\nTente novamente")
