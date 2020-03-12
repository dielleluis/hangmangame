import random


def play():

    openning()
    secret_word = secretword()
    
    letras_acertadas = right_guesses(secret_word)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    error = 0

    while not enforcou and not acertou:
        guess = ask_guess()

        if guess in secret_word:
            disp_right_guesses(guess, letras_acertadas, secret_word)
        else:
            error += 1
            gallows(error)

        enforcou = error == 7
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        winner(secret_word)
    else:
        loser(secret_word)

    print('-*-*-*FIM DE JOGO-*-*-*-')



def openning():
    print('*-'*20)
    print('Bem vindo ao Jogo de Forca')
    print('*-'*20)


def secretword():
    arquivo = open('words.txt', 'r')
    words = []

    for linha in arquivo:
        linha = linha.strip()
        words.append(linha)

    arquivo.close()

    num = random.randrange(0, len(words))

    secret_word = words[num].upper()
    return secret_word


def right_guesses(word):
    return ['_' for letra in word]


def ask_guess():
    guess = input('Qual letra? ')
    guess = guess.strip().upper()
    return guess


def disp_right_guesses(guess, letras_acertadas, secret_word):
    index = 0
    for letra in secret_word:
        if guess == letra:
            letras_acertadas[index] = letra
        index += 1


def loser(secret_word):
    print('Você perdeu! A palavra era {}'.format(secret_word))


def winner(secret_word):
    print('Você ganhou! A palavra era {}'.format(secret_word))


def gallows(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == '__main__':
    play()