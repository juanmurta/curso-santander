# Entrada do número de pacientes
n = int(input('quantidade').strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for i in range(n):
    nome, idade, status = input('Digite os dados com virgula.').strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def organizar_prioridades(pacientes):
    # função para mapear status para prioridade numérica
    def prioridade(paciente):
        status = paciente[2]
        if status == 'urgente':
            return 0
        elif status == 'idoso':
            return 1
        else:
            return 2

    # Ordena pela prioridade e depois pela idade decrescente
    return sorted(pacientes, key=lambda paciente: (prioridade(paciente), -paciente[1]))


# TODO: Exiba a ordem de atendimento com título e vírgulas:
def mostrar_lista(lista_organizada):
    nomes = [paciente[0] for paciente in lista_organizada]
    resultado = ', '.join(nomes)
    print(f'Ordem de Atendimento: {resultado}')


mostrar_lista(organizar_prioridades(pacientes))
