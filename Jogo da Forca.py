# -*- coding: utf-8 -*-

#Jogo da Forca
#Programação Orientada a Objetos

from random import  randint
import os

quadro = ['''

>>>>>>>>>>Jogo da Forca<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']



class Forca():
    #Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_corretas = []
        self.erros = 0

    #Método para adivinhar a letra
    def adivinhar(self, letra):
        if letra in self.palavra:
            if letra not in self.letras_corretas:
                self.letras_corretas.append(letra)
        else:
            if letra not in self.letras_erradas:
                self.letras_erradas.append(letra)
                self.erros += 1

    #Método para verificar se o jogo terminou
    def acabou(self):
        return self.erros == 6

    #Método para verificar se o jogador venceu
    def venceu(self):
        for i in self.palavra:
            if i not in self.letras_corretas:
                return False
        return True

    #Método para não mostrar a letra no quadro
    def esconder_letra(self):
        print(f"Palavra: ", end=" ")
        for i in self.palavra:
            if i not in self.letras_corretas:
                print("_", end="")
            else:
                print(i, end="")
        print("\n")

    #Método para checar o status do jogo e imprimir o quadro na tela
    def imprime_estado(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(quadro[self.erros])
        self.esconder_letra()
        print("Letras Corretas: ", end="")
        for i in self.letras_corretas:
            if i != self.letras_corretas[:-1] :
                print(f"{i},", end="")
            else:
                print(f"{i}")
        print("\n")
        print("Letras Erradas: ", end="")
        for i in self.letras_erradas:
            if i != self.letras_erradas[:-1]:
                print(f"{i},", end="")
            else:
                print(f"{i}")
        print("\n")


def palavra_aleatoria():
    arquivo = open("palavras.txt", "rt", encoding="UTF-8")
    palavras = arquivo.readlines()
    return palavras[randint(0, len(palavras) - 1)].strip()

def main():
    jogo = Forca(palavra_aleatoria().lower())

    #Enquanto o jogo não tiver terminado print do status, solicita uma letra e faz a leitura do caractere
    while not (jogo.venceu() or jogo.acabou()):
        jogo.imprime_estado()
        letra = str(input("Digite uma letra: "))
        jogo.adivinhar(letra)


    #Verifica o status do jogo
    jogo.imprime_estado()

    if jogo.venceu():
        print("\n\033[1;32mParabéns! Você venceu!!\033[m")
    else:
        print("\n\033[1;31mGame Over! Você perdeu\033[m")
        print(f"A palavra era: {jogo.palavra}")


if __name__ == "__main__":
    main()

