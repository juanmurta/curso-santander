import textwrap


def menu():
    menu = '''\n
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar Usuário
    [c] Criar Conta Corrente
    [l] Listar Contas 
    [q] Sair
    => '''
    return input(textwrap.dedent(menu))


def criar_usuario(nome, data_nascimento, cpf, endereco_completo):
    pass


def criar_conta_corrente(agencia, numero_conta, usuario):
    pass


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > 0:
        if saldo >= valor:
            if valor <= limite:
                saldo -= valor
                numero_saques += 1
                extrato += f'Sacado: R$ {valor:.2f}\n'
                print(f'Saldo atual: R$ {saldo:.2f}')
            else:
                print('O valor do saque ultrapassou o limite por saque.')
        else:
            print('Saldo insuficiente.')
    else:
        print('Informe um valor válido.')
    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print(f'Saldo atual: R$ {saldo:.2f}')
    else:
        print('Informe um valor válido.')

    return saldo, extrato


def extrato_conta(saldo, LIMITE_SAQUES, numero_saques, /, *, extrato):
    print(30 * '#' + 'Extrato' + 30 * '#')
    print('Não existe movimentações.' if not extrato else extrato)
    print(f'O seu saldo atual é de R$ {saldo:.2f} e você tem {LIMITE_SAQUES - numero_saques} saque(s) restante hoje')
    print(67 * '#')


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Digite o valor do deposito: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            if numero_saques < LIMITE_SAQUES:
                valor = float(input('Digite o valor do saque: '))
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )
            else:
                print('Você ultrapassou a quantidade de 3 saques diários.')

        elif opcao == 'e':
            extrato_conta(saldo, LIMITE_SAQUES, numero_saques, extrato=extrato)

        elif opcao == 'u':
            print('criar usuario')

        elif opcao == 'c':
            print('criar conta corrente')

        elif opcao == 'q':
            break

        else:
            print('Operação inválida, por favor selecione novamente a opção desejada.')


main()