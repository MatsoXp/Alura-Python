import random

def jogar():

    mensagem_inicio()
    palavra_secreta = carrega_palavra_secreta()
    letras_corretas = inicializa_letras_palavras(palavra_secreta)

    print(letras_corretas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_corretas, palavra_secreta)

        else:
            erros += 1
            desenha_forca(erros)
            print("Você tem mais {} tentativas".format(7-erros))

        enforcou = erros == 7
        acertou = "_" not in letras_corretas

        print(letras_corretas)


    if(acertou):
        imprime_mensagem_venceu(palavra_secreta)

    else:
        imprime_mensagem_perdeu(palavra_secreta)

#funções
def mensagem_inicio():
    print('***************************')
    print('Bem Vindo ao jogo de Forca!')
    print('***************************')


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_palavras(palavra):
    lista = ["_" for letra in palavra]
    return lista

def pede_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_corretas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_corretas[posicao] = letra
        posicao += 1


def desenha_forca(erros):
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


def imprime_mensagem_venceu(palavra_secreta):
    print("Você Ganhou!!!\n")
    print("A palavra secreta era {}! \n".format(palavra_secreta))

def imprime_mensagem_perdeu(palavra_secreta):
    print("Você Perdeu!!!\n")
    print("A palavra secreta era {}! \n".format(palavra_secreta))

if (__name__ == "__main__"):
    jogar()
