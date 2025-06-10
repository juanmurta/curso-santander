menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor_depositado = int(input('Digite o valor do deposito: '))
        saldo += valor_depositado
        print(f'Saldo atual: R$ {saldo:.2f}')

    elif opcao == 's':
        valor_sacado = int(input('Digite o valor do saque: '))
        if saldo >= valor_sacado:
            if valor_sacado <= limite:
                if numero_saques < LIMITE_SAQUES:
                    saldo -= valor_sacado
                    numero_saques += 1
                    print(f'Saldo atual: R$ {saldo:.2f}')
                else:
                    print('Você ultrapassou a quantidade de 3 saques diários.')
            else:
                print('O valor do saque ultrapassou o limite por saque.')
        else:
            print('Saldo insuficiente.')

    elif opcao == 'e':
        print(f'''
        Extrato
        O seu saldo atual é de R$ {saldo:.2f} e você tem {LIMITE_SAQUES - numero_saques} saques disponíveis hoje..
        ''')

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a opção desejada.')
