def multiplicar(a, b):  # função para multiplicar 2 numeros
    return a * b


resultado = multiplicar(5, 3) + multiplicar(2, 4)

print(resultado)
print('*' * 50)


def calcular_media(*numeros):  # realizar a média de n numeros.
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media


print(calcular_media(5, 3, 9, 10, 20))
print('*' * 50)

# como declarar lambda
somar = lambda x: x + 3

print(somar(5))
print('*' * 50)

try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção

print('*' * 50)

# usando with para abertura e fechamento do arquivo automaticamente
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
# leitura de arquivo
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

print('*' * 50)
# escrita de arquivo
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()

