class Cev:

  def __init__(self):
    pass

  def desafio071(self):
    dinheiro = float(input('Que valor você quer sacar? R$'))
    cedulas50 = dinheiro // 50
    if cedulas50 > 0:
      print(f'Total de {cedulas50:.0f} cédulas de R$50')
    sobra50 = dinheiro - (cedulas50 * 50)
    cedulas20 = sobra50 // 20
    if cedulas20 > 0:
      print(f'Total de {cedulas20:.0f} cédulas de R$20')
    sobra20 = sobra50 - (cedulas20 * 20)
    cedulas10 = sobra20 // 10
    if cedulas10 > 0:
      print(f'Total de {cedulas10:.0f} cédulas de R$10')
    sobra10 = sobra20 - (cedulas10 * 10)
    if sobra10 > 0:
      print(f'Total de {sobra10:.0f} cédulas de R$1')

  def desafio072a(self):
    from num2words import num2words
    num = int(input('Digite um número entre 0 e 20: '))
    while num > 20 or num < 0:
      num = int(input('Digite um número entre 0 e 20: '))
    texto = num2words(num, lang='pt_BR')
    print(f'Você digitou o número {texto}')

  def desafio072b(self):
    numExt = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinto', 'seis', 'sete',
              'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze',
              'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
              'vinte')
    while True:
      num = int(input('Número: '))
      while num > 20 or num < 0:
        num = int(input('Número: '))
      print(numExt[num])
      break

  def desafio073(self):
    nba = ('Boston Celtics', 'Golden State Warriors', 'Los Angeles Lakers',
           'Chicago Bulls', 'Miami Heat', 'Washington Wizards',
           'Memphis Grizzlies', 'New York Knicks', 'Philadelphia 76ers',
           'Cleveland Cavaliers')
    print('-' * 30)
    print(f'Lista de times da NBA: {nba}')
    print('-' * 30)
    print(f'Os 5 primeiros são {nba[:5]}')
    print('-' * 30)
    print(f'Os 4 ultimos são {nba[len(nba)-4:]}')
    print('-' * 30)
    times = []
    cont = 0
    for time in nba:
      times.append(time)
      cont += 1
      if time == 'Miami Heat':
        equipe = time
        posicao = cont
    times.sort()
    print(f'Times em ordem alfabetica: {times}')
    print('-' * 30)
    print(f'{equipe} está na {posicao} posição')

  def desafio074(self):
    from random import randint
    num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    maior = menor = 0
    print('Os valores sorteados foram: ', end=' ')
    for n in range(1, 6):
      sort = num[randint(0, 9)]
      print(sort, end=' ')
      if maior == 0:
        maior = sort
        menor = sort
      elif menor > sort:
        menor = sort
      elif maior < sort:
        maior = sort
    print(f'\nO maior valor sorteado foi {maior}')
    print(f'O menor valor sorteado foi {menor}')

  def desafio075(self):
    cont = 0
    numUm = int(input('Número 0: '))
    numDois = int(input('Número 1: '))
    numTres = int(input('Número 2: '))
    numQuatro = int(input('Número 3: '))
    tupla = (numUm, numDois, numTres, numQuatro)
    print(f'O 9 aparece {tupla.count(9)}x')
    if tupla.count(3) > 0:
      print(f'O 3 aparece na posição {tupla.index(3)}')
    else:
      print('Não há número 3')
    print('Os números pares são:', end=' ')
    for num in tupla:
      if num % 2 == 0:
        print(num, end=' ')
      else:
        cont += 1
        if cont > 3:
          print('Não há números pares')

  def desafio076(self):
    print('=' * 35)
    print('LISTAGEM DE PREÇOS')
    print('=' * 35)
    tupla = ('lapis', 1.75, 'borracha', 2, 'caderno', 15.90, 'estojo', 25,
             'transferidor', 4.20, 'compasso', 9.99, 'mochila', 120.32,
             'canetas', 22.30, 'livro', 34.90)
    for c in range(0, len(tupla)):
      if c % 2 == 0:
        print(f'{tupla[c]:.<30}R$', end=' ')
      else:
        print(f'{tupla[c]:>6.2f}')

  def desafio077(self):
    tupla = ('hacker', 'tecnologia', 'codigo', 'python', 'chatgpt',
             'algoritmo', 'software', 'malware', 'ransonware', 'javascript',
             'linux', 'redes')
    for i in range(0, len(tupla)):
      print(f'\nNa palavra {tupla[i].upper()} temos', end=' ')
      for letra in tupla[i]:
        if letra in 'aeiou':
          print(letra, end=' ')

  def desafio078(self):
    num = []
    cont = cont2 = 0
    for c in range(0, 5):
      num.append(int(input(f'Digite um valor na posição {c}: ')))
    print(f'Você digitou os valores {num}')
    print(f'O maior valor digitado foi {max(num)} nas posições ', end='')
    for c in num:
      if c == max(num):
        print(f'{cont}..', end='')
      cont += 1
    print(f'\nO menor valor digitado foi {min(num)} nas posições ', end='')
    for c in num:
      if c == min(num):
        print(f'{cont2}..', end='')
      cont2 += 1

  def desafio079(self):
    num = []
    while True:
      numero = int(input('Digite um valor: '))
      if numero not in num:
        num.append(numero)
        print('Valor adicionado com sucesso...')
      else:
        print('Valor duplicado! Não vou adicionar...')
      opc = ' '
      while opc != 'S' and opc != 'N':
        opc = str(input('Quer continuar [S/N]: ')).upper().strip()
      if opc == 'N':
        break
    num.sort()
    print(f'Você digitou os valores {num}')

  def desafio080(self):
    num = []
    for i in range(0, 5):
      numero = int(input('Digite um valor: '))
      if i == 0 or numero > num[-1]:
        num.append(numero)
      else:
        pos = 0
        while pos < len(num):
          if numero <= num[pos]:
            num.insert(pos, numero)
            break
          pos += 1
    print(num)