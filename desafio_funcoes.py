import textwrap


def menu():
    menu = '''\n
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar Usuário
    [c] Criar Conta Corrente
    [lc] Listar Contas
    [lu] Listar Usuários  
    [q] Sair
    => '''
    return input(textwrap.dedent(menu))


def verificar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None


def criar_usuario(usuarios):
    cpf = input('Informe o CPF: ').replace('-', '').replace('.', '').replace(' ', '')
    if len(cpf) == 11 and cpf.isnumeric():
        usuario = verificar_usuario(cpf, usuarios)

        if usuario:
            print('Usuário já Cadastrado.')
            return

        nome = input('Informe o nome completo: ')
        data_nascimento = input('Informe o data de nascimento (dd/mm/yyyy): ')
        endereco = input('Informe o endereço (logradouro - nro - bairro - cidade - sigla estado): ')

        usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
        print('#' * 5 + ' Usuário criado com sucesso. ' + '#' * 5)

    else:
        print('Cpf Inválido')
    

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF: ').replace('-', '').replace('.', '').replace(' ', '')
    if len(cpf) == 11 and cpf.isnumeric():
        usuario = verificar_usuario(cpf, usuarios)
        if usuario:
            print('#' * 5 + ' Conta criada com sucesso. ' + '#' * 5)
            return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

        print('#' * 20 + ' Usuário não encontrado, informar um cpf existente. ' + '#' * 20)
        return None

    else:
        print('Cpf Inválido')
        return None


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
    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print(f'Saldo atual: R$ {saldo:.2f}')
    else:
        print('Informe um valor válido.')

    return saldo, extrato


def extrato_conta(saldo, numero_saques, /, *, extrato, limite_saques):
    print(30 * '#' + 'Extrato' + 30 * '#')
    print('Não existe movimentações.' if not extrato else extrato)
    print(f'O seu saldo atual é de R$ {saldo:.2f} e você tem {limite_saques - numero_saques} saque(s) restante hoje')
    print(67 * '#')


def lista_contas(contas):
    for conta in contas:
        linha = f'''
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
    '''
        print('#' * 100)
        print(textwrap.dedent(linha))


def lista_usuarios(usuarios):
    for usuario in usuarios:
        linha = f'''
            Nome: {usuario['nome']}
            Data de Nascimento: {usuario['data_nascimento']}
            CPF: {usuario['cpf']}
            Endereço: {usuario['endereco']}
        '''
        print('#' * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 0

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Digite o valor do deposito: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            if numero_saques < LIMITE_SAQUES:
                valor = float(input('Digite o valor do saque: '))
                saldo, extrato, numero_saques = sacar(
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
            extrato_conta(saldo, numero_saques, extrato=extrato, limite_saques=LIMITE_SAQUES)

        elif opcao == 'u':
            criar_usuario(usuarios)

        elif opcao == 'c':
            conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == 'lu':
            lista_usuarios(usuarios)

        elif opcao == 'lc':
            lista_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Operação inválida, por favor selecione novamente a opção desejada.')


main()
