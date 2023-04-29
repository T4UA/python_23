class Cev:
  def __init__(self):
    pass

  def desafio021(self):
    import pygame
    pygame.init()
    pygame.mixer.music.load('cbj.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()

  def desafio022(self):
    nome = input('Digite seu nome completo: ').strip()
    print('Analisando seu nome...')
    print(f'Seu nome em maiúsculo é {nome.upper()}')
    print(f'Seu nome em minúsculo é {nome.lower()}')
    cont = soma = 0
    for letra in nome.replace(" ",""):
      cont += 1
    print(f'Seu nome tem ao todo {cont} letras')
    for letra in nome.split()[0]:
      soma += 1
    print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {soma} letras')
    '''
    print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')})'
    print(f'Seu primeiro nome tem {nome.find(" ")} letras)'
    separa = nome.split()
    print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])})'
    '''

  def desafio023(self):
    num = int(input('Informe um número: '))
    print(f'Analisando o número {num}')
    cont = cont_2 = cont_3 = 0
    while num > 10:
      if num > 1000:
        num -= 1000
        cont += 1
      elif num < 1000 and num > 100:
        cont_2 += 1
        num -= 100
      elif num < 100:
        num -= 10
        cont_3 += 1
        
    print(f'Unidade: {num}')
    print(f'Dezena: {cont_3}')
    print(f'Centena: {cont_2}')
    print(f'Milhar: {cont}')

  def desafio024(self):
    cid = input('Em que cidade vocẽ nasceu: ').upper().strip()
    separar = cid.split()
    if separar[0] == 'SANTO':
      print('TRUE')
    else:
      print('FALSE')

  def desafio025(self):
    nome = input('Qual o seu nome completo: ').lower().strip()
    silva = 'silva' in nome
    print(f'Seu nome tem Silva? {silva}')

  def desafio026(self):
    frase = input('Digite uma frase: ').lower().strip()
    print(f'A letra A aparece {frase.count("a")} vezes na frase.')  
    print(f'A primeira letra A aparece na posição {frase.find("a")+1}')
    print(f'A última letra A apareceu na posição {frase.rfind("a")+1}')

  def desafio027(self):
    nome = input('Digite seu primeiro nome: ').strip()
    print('Muito prazer em te conhecer!')
    lista = nome.split()
    print(f'Seu primeiro nome é {lista[0]}')
    print(f'Seu último nome é {lista[-1]}')

  def desafio028(self):
    from time import sleep
    from random import randint
    print('Vou pensar em um número de 0 a 5. Tente advinhar...')
    num = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(3)
    pc = randint(0, 5)
    if num == pc:
      print('PARABÉNS! Você conseguiu me vencer!')
    else:
      print(f'GANHEI! Eu pensei no número {pc} e não no {num}!')

  def desafio029(self):
    veloc = float(input('Qual é a velocidade atual do carro? '))
    if veloc > 80:
      excesso = veloc - 80
      multa = excesso * 7
      print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
      print(f'Vocẽ deve pagar uma multa de R${multa:.2f}!')
    print('Tenha um bom dia! Dirija com segurança!')

  def desafio030(self):
    num = int(input('Me diga um número: '))
    if num % 2 == 0:
      print(f'O número {num} é PAR')
    else:
      print(f'O número {num} é ÍMPAR')        
