from random import choice, shuffle
import pyperclip

numeros = '0123456789'
letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_maisuculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
simbolos = '!@#$%&*+?'
escolhas = {
    0: numeros,
    1: letras_minusculas,
    2: letras_maisuculas,
    3: simbolos
}

qtd_digitos = int(raw_input('Quantidade de digitos: '))

# define as posicoes aleatorios que os caracteres serao inseridos
lista_pos = [i for i in range(qtd_digitos)]
shuffle(lista_pos)

# define a senha como uma lista cheia de Nones para conseguir substituir pelas
# posicoes mais tarde
senha = [None] * qtd_digitos

possiveis_caracteres = []
for pos in lista_pos:
    # se a lista estiver vazia redefine, isso acontece na primeira repeticao
    # e quando todas as posicoes ja foram escolhidas, devido ao pop no final
    # do loop
    if not possiveis_caracteres:
        possiveis_caracteres = [i for i in range(4)]
        shuffle(possiveis_caracteres)

    # escolhe um caracter aleatorio entre letras maiusculas e minusculas,
    # numeros ou simbolos
    char = choice(escolhas[possiveis_caracteres[0]])

    # se o caractere estiver na senha escolhe outro
    while char in senha:
        char = choice(escolhas[possiveis_caracteres[0]])

    senha[pos] = char

    possiveis_caracteres.pop(0)

senha = ''.join(senha)

print(senha)

pyperclip.copy(senha)

print('Copiado para a area de transferencia.')
