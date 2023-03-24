import random

def jogar():

    mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0



    while (not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_tentativas(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        print("Você Acertou!")
    else:
        print("Você errou!")


    print("Fim do jogo")



def marca_tentativas(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def pede_chute():
    chute = input("Qual letra? \n")
    chute = chute.strip().upper()
    return chute

def mensagem_abertura():
    print("************************************")
    print("********Jogo da Forca!**************")
    print("************************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

if(__name__ == "__main__"):
    jogar()
