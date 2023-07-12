import random



def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = chute_usuario()

        if (chute in palavra_secreta):
            letras_corretas(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim de jogo...")


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.jogo", "r")  # Aqui eu estou chamando o arquivo criado, no modo de leitura "r"
    palavras = []
    for linha in arquivo:
        linha = linha.strip()  # Essa função serve para tirar o "\n" das palavras do arquivo
        palavras.append(linha)  # Aqui eu estou pegando cada linha do arquivo que contém uma palavra e jogando a palavra dentro da lista de palavras

    arquivo.close()

    numero = random.randrange(0, len(palavras))  # Esse metodo vai escolher um numero aleatório dentro dos parâmetros estabelecidos
    palavra_secreta = palavras[numero].upper()  # Aqui vai ser escolhida uma palavra_secreta, dentro da lista de palavras, pelo index aleatório gerado pela função acima e sera deixada todas as letras em maiúsculo
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]  # Aqui eu estou colocando a quantidade de infens coerente com a quantidade de letras da palavra secreta

def chute_usuario():
    chute = input("Qual é a letra:")
    chute = chute.strip().upper()
    return chute

def letras_corretas(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (letra == chute):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

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

if (__name__ == "__main__"):  #Aqui eu estou criando um arquivo próprio pro jogo e também ligando ele a interface inicial
        jogar()