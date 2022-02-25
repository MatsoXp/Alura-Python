import forca
import adivinhacao

def escolhe_jogo():
    print('*******************************************')
    print('Bem Vindo, escolha um jogo para prosseguir!')
    print('*******************************************')

    print("1 - Forca ou 2 - Adivinhação")

    jogo = int(input("Qual o jogo? "))


    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()

    elif (jogo == 2):
        print("jogando Adivinhação")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()