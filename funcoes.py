import os
import time


def limpatela():
    os.system('cls')

def esperar(segundos):
    time.sleep(segundos)

    
def lerstring(mensagem):
    while True:
        variavel = input(mensagem)
        if len(variavel)>1:
            return variavel
        else:
            print('Valor Informado Incorretamente! ')


