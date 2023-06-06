from funcoes import *


limpatela()
print('Bem-Vindo ao Jogo da Forca!!')
esperar(segundos=2)
acertou = False
while acertou==False:
       limpatela()
       tentativas = 5
       print('Para começar um novo jogo vamos definir o desafiante e o competidor!')
       desafiante = input('Insira o nome do Desafiante: ')
       competidor = input('Insira o nome do Competidor: ')
       limpatela()

       print('Essa parte é para o Desafiante!')
       esperar(1)
       print('Vamos definir uma palavra chave e mais 3 dicas para o competidor!')
       esperar(3)
       palavrachave = lerstring('Digite a palavra chave: ')
       letrasdescobertas = ['*' for letra in palavrachave]
       dica1 = lerstring('Dica 1: ')
       dica2 = lerstring('Dica 2: ')
       dica3 = lerstring('Dica 3: ')
       limpatela()

       print('Vamos começar o Jogo!')
       print ('Você tem 5 tentativas para adivinhar a palavra! ')
       esperar(3)
       print('*'*len(palavrachave))
       
       while True:
              print('(1) Jogar')
              print('(2) Dica')
              opcao = input()
                     
              if opcao == '1':
                     letra = input('Arrisque uma letra: ')
                     if letra in palavrachave:
                            for i in range(len(palavrachave)):
                                   if letra == palavrachave[i]:
                                          letrasdescobertas[i] = letra
                                          print('Você acertou uma letra!!')
                                          palavraexibida = ''. join(letrasdescobertas)
                                          esperar(1)
                                          limpatela()
                                          print(palavraexibida)
                     else:
                            tentativas -= 1
                            print ('Essa letra não está na palavra!')
                            print('Você ainda tem:', tentativas, 'tentativa(s)')

                            
                     if '*' not in letrasdescobertas:
                            ganhador = competidor
                            perdedor = desafiante
                            print('Parabéns!!! Você adivinhou a palavra!!')
                            arquivo = open('lg.txt', 'a')
                            arquivo.write('Rodada da Palavra - '+palavrachave+'\n'+'Ganhador da Rodada:'+ganhador+'\n'+'Perdedor da Rodada: '+perdedor+'\n')
                            arquivo.close()
                            outrogame = print('Para começar um novo jogo pressione (1) Ou se quiser parar de jogar aperte (2)')
                            escolha = input()
                            if escolha == '1':
                                   break
                            elif escolha == '2':
                                   acertou = True
                                   try:
                                          arquivo = open('lg.txt', 'r')
                                          resumo = arquivo.read() 
                                          print(resumo)
                                          arquivo.close()
                                          esperar(2)
                                          acertou = True
                                          break
                                          
                                   except:
                                          arquivo = open('lg.forca', 'w')
                                          arquivo.close()
                                          esperar(3)
                                          
                                                               
                            else:
                                   print('Número Inválido')
                                   
                     elif tentativas== 0:
                            ganhador = desafiante
                            perdedor = competidor
                            print('Você não conseguiu adivinhar a palavra')
                            print('A palavra era:', palavrachave)
                            arquivo = open('lg.txt', 'a')
                            arquivo.write('Rodada da Palavra - '+palavrachave+'\n'+'  Ganhador da Rodada: '+ganhador+'\n'+'Perdedor da Rodada:  '+perdedor+'\n')
                            arquivo.close()
                            outrogame = print('Para começar um novo jogo pressione (1) Ou se quiser parar de jogar aperte (2)')
                            escolha = input()
                            if escolha == '1':
                                   break

                            elif escolha == '2':
                                   try:
                                          arquivo = open('lg.txt', 'r')
                                          resumo = arquivo.read() 
                                          print(resumo)
                                          arquivo.close()
                                          esperar(2)
                                          acertou = True
                                          break
                                   except:
                                          arquivo = open('lg.forca', 'w')
                                          arquivo.close()
                                          esperar(3)
              

              elif opcao == '2':
                     escolha = input("Escolha uma dica entre 1-3: ")
                     if escolha == '1':
                            limpatela()
                            print('A dica é:',dica1)
                     elif escolha == '2':
                            limpatela()
                            print('A dica é:',dica2)
                     elif escolha == '3':
                            limpatela()
                            print('A dica é:',dica3)
                     else:
                            print('Número Inválido!')                      
                            
              else:
                     print('Valor Informado Inválido!! ')
                     esperar(2)
                     limpatela()