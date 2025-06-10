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
        valor_depositado = float(input('Digite o valor do deposito: '))
        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f'Depósito: R$ {valor_depositado:.2f}\n'
            print(f'Saldo atual: R$ {saldo:.2f}')
        else:
            print('Informe um valor válido.')

    elif opcao == 's':
        valor_sacado = float(input('Digite o valor do saque: '))
        if valor_sacado > 0:
            if saldo >= valor_sacado:
                if valor_sacado <= limite:
                    if numero_saques < LIMITE_SAQUES:
                        saldo -= valor_sacado
                        numero_saques += 1
                        extrato += f'Sacado: R$ {valor_sacado:.2f}\n'
                        print(f'Saldo atual: R$ {saldo:.2f}')
                    else:
                        print('Você ultrapassou a quantidade de 3 saques diários.')
                else:
                    print('O valor do saque ultrapassou o limite por saque.')
            else:
                print('Saldo insuficiente.')
        else:
            print('Informe um valor válido.')

    elif opcao == 'e':
        print(30 * '#' + 'Extrato' + 30 * '#')
        print('Não existe movimentações.' if not extrato else extrato)
        print(f'O seu saldo atual é de R$ {saldo:.2f} e você tem {LIMITE_SAQUES - numero_saques} saque(s) restante hoje'
              f'hoje.')
        print(67 * '#')

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a opção desejada.')
