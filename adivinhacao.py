import random

def jogar():    

    print("************************************")
    print("********Jogo da adivinhação!********")
    print("************************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontuacao = 1000

    ##Dificuldades!

    dificuldade = int(input("Selecione a dificuldade: 1-Fácil, 2-Médio, 3-Difícil \n" ))


    if(dificuldade == 1):
        tentativas = 10
        print ("##Você escolheu o modo Fácil##")
    elif(dificuldade == 2):
        tentativas = 5
        print ("##Você escolheu o modo Médio##")
    elif(dificuldade ==3):
        tentativas = 3
        print ("##Você escolheu o modo Difícil##")  
    else:
        tentativas = 1
        print ("##Você escolheu o modo Ultra Difícil!## \n " ) 
        print ("Só terá uma tentativa, e se errar, seus dados bancários serão vazados!\n")

    ##Sistema do jogo

    print("tente adivinhar o numero secreto. \n")
    print("você iniciará com ", pontuacao, " pontos. cada tentativa reduz seu placar final. \n")

    while ( tentativas > 0):
        chute = int(input("tente digitar um numero de 1 à 100 \n"))
        if(chute == numero_secreto):
            print("Acerto mizerave")
            break
        elif(chute < numero_secreto):
            print("tá menor que o número secreto")
            tentativas -= 1
            pontuacao -= chute       
        elif(chute < 1 or chute > 100):
            print("O número tem que estar entre 1 e 100")
            tentativas -= 1
            pontuacao -= chute           
        else:
            print("tá maior que o numero secreto")    
            tentativas -= 1
            pontuacao -= chute
            

    if(chute != numero_secreto):
        print("Fim do jogo, vc perdeu!")
        pontuacao = 0
        
    print("pontuacao ", pontuacao )

if(__name__ == "__main__"):
    jogar()

