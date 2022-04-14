from colorama import Fore, Back, Style
from unidecode import unidecode
import random
import json

class Termo():
    def __init__(self, validas, respostas, max_tentativas):
        self.validas = {unidecode(p).lower(): p.lower() for p in validas}
        self.respostas = {unidecode(p).lower(): p.lower() for p in respostas}
        self.max_tentativas = max_tentativas
        self.tentativas = []
        self.gabaritos = []
        print("JOGO DE PALAVRAS - 5 LETRAS")
        print("<tente adivinhar a palavra ou digite SAIR para encerrar o jogo>\n")

    @staticmethod
    def ganhar(gabarito):
        if gabarito=='aaaaa':
            return True
        else:
            return False

    def print_palavra(self, palavra, gabarito):
        palavra_print = self.validas[palavra].upper()
        mapa_cores = {
            'x': Fore.RED,
            'p': Fore.YELLOW,
            'a': Fore.CYAN
        }
        print(Style.BRIGHT, end='')
        if gabarito=='aaaaa':
            print(Back.GREEN, end='')
        for p,g in zip(palavra_print, gabarito):
            print(mapa_cores[g] + p, end=' ')
        print(Style.RESET_ALL)

    def print_game(self):
        i=0
        for t,g in zip(self.tentativas,self.gabaritos):
            self.print_palavra(t,g)
            i+=1
        while i<self.max_tentativas:
            print("_ _ _ _ _")
            i+=1
        print("")

    def avaliar_tentativa(self, tentativa, resposta):
        gab_1_pass=''
        gabarito=''
        letras_resposta = list(resposta)
        for t,r in zip(tentativa, resposta):
            if t == r:
                letras_resposta.remove(t)
                gab_1_pass += 'a'
            else:
                gab_1_pass += 'x'

        for t,r,g in zip(tentativa, resposta, gab_1_pass):
            if g == 'a':
                gabarito += 'a'
            elif t in letras_resposta:
                letras_resposta.remove(t)
                gabarito += 'p'
            else:
                gabarito += 'x'
        self.gabaritos.append(gabarito)

        return gabarito

    def obter_palavra(self, num_tentativa):
        obter=True
        while obter:
            print(f"Tentativa #{num_tentativa}: ", end='')
            palavra = unidecode(str(input())).lower()
            if palavra == 'sair':
                return None
            elif palavra=="luiza":
                print("Sempre certa! <3 Pode continuar")
            elif palavra in self.tentativas:
                print("Você já tentou essa palavra.")
            elif palavra in self.validas.keys():
                obter=False 
            else: 
                print("Palavra inválida.")
        self.tentativas.append(palavra)

        return palavra

    def jogar(self):
        resposta = random.choice(list(self.respostas.keys()))
        for t in range(1,self.max_tentativas+1):
            p=self.obter_palavra(t)
            if p is None:
                print("Jogo Encerrado.")
                break
            g=self.avaliar_tentativa(p, resposta)
            self.print_game()
            ganhar=self.ganhar(g)
            if ganhar:
                print(f"Você acertou em {t} tentativas!")
                break
            if t==self.max_tentativas:
                print(f"Não foi dessa vez, a palavra era: {self.respostas[resposta].upper()}")

if __name__ == '__main__':
    with open('palavras.json', encoding='utf-8', mode='r') as f:
        palavras = json.load(f)
    termo = Termo(validas=palavras["validas"]+palavras["respostas"],
                    respostas=palavras["respostas"],
                    max_tentativas=6)
    
    termo.jogar()