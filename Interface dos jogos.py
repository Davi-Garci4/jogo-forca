import cod_forca
import adivinhação

def inicial():
    print("*********************************")
    print("********Escolha seu jogo!********")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogando Forca....")
        cod_forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação...")
        adivinhação.jogar()

if (__name__ == "__main__"):
    inicial()