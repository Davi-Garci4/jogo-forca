import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.jogo", "r") # Aqui eu estou chamando o arquivo criado, no modo de leitura "r"
    palavras = []
    for linha in arquivo:
        linha = linha.strip() #Essa função serve para tirar o "\n" das palavras do arquivo
        palavras.append(linha) # Aqui eu estou pegando cada linha do arquivo que contém uma palavra e jogando dentro da lista de palavras

    arquivo.close()

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta] # Aqui eu estou colocando a quantidade de infens coerente com a quantidade de letras da palavra secreta

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual é a letra:")
        chute = chute.strip().upper()
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (letra == chute):
                   letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

    print("Fim de jogo...")

if (__name__ == "__main__"):  #Aqui eu estou criando um arquivo próprio pro jogo e também ligando ele a interface inicial
        jogar()