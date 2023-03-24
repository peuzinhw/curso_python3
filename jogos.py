def escolhe_jogo():

    import forca
    import adivinhacao

    print("************************************")
    print("********Escolha seu Jogo!***********")
    print("************************************")

    escolhaJogo = int(input("Digite (1) para Jogo da Forca ou (2) para Jogo da Adivinhação. \n"))

    if(escolhaJogo == 1):
        forca.jogar()
    elif(escolhaJogo == 2):
        adivinhacao.jogar()
    

if(__name__ == "__main__"):
    escolhe_jogo()




