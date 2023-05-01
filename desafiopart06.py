class Cev:
  def __init__(self):
    pass

  def desafio051(self):
    pt = int(input('Primeiro Termo: '))
    ra = int(input('Razão: '))
    for c in range(0,10):
      print(pt, end=' ')
      pt += ra
    print('ACABOU')

  def desafio052(self):
    cont = 0
    num = int(input('Digite um número: '))
    for c in range(1, num+1):
      if num % c == 0:
        print(f'({c})', end=' ')
        cont += 1
      else:
        print(c, end=' ')
    print(f'\nO número {num} foi divisivel {cont} vezes')
    if cont == 2:
      print('E por isso ele é PRIMO!')
    else:
      print('E por isso ele NÃO É PRIMO')

  def desafio053(self):
    inversa = []
    frase = input('Digite uma frase: ').strip().replace(' ', '').lower() #retirei os espaços do comeco e do meio da frase
    lista = frase.split() # coloquei em uma lista
    for c in range(len(frase)-1, -1, -1): # invertir a frase
      inversa.append(lista[0][c])
    junto = ''.join(inversa)
    print(f'O inverso de {frase} é {junto}')
    if junto == frase:# comparei se a frase normal e de tras para frente são iguais
      print('Temos um Palindromo')
    else:
      print('Não temos um palindromo')

  def desafio054(self):
    maior = menor = 0
    from datetime import date
    for cont in range(1,8):
      ano = int(input(f'Em que ano a {cont} pessoa nasceu? '))
      idade = date.today().year - ano
      if idade < 18:
        menor += 1
      else:
        maior += 1
    print(f'Ao todo tivemos {maior} pessoas maiores de idade')
    print(f'E também tivemos {menor} pessoas menores de idade')

  def desafio055(self):
    maior = menor = 0
    for cont in range(1,6):
      peso = float(input(f'Peso da {cont} pessoa: '))
      if maior == 0:
        maior = peso
        menor = peso
      if maior < peso:
        maior = peso
      if menor > peso:
        menor = peso  
    print(f'O maior peso lido foi de {maior}Kg\nO menor peso lido foi de {menor}Kg')

  def desafio056(self):
    while True:
      sexo = input('Digite seu sexo [M/F]: ').upper()[0].strip()
      if sexo == 'M' or sexo == 'F':
        print(f'Sexo {sexo} registrado com sucesso')
        break
      else:
        print('Dados Inválidos. Por favor tente novamente\n')

  def desafio057(self):
    soma = maior = cont = 0
    for c in range(1,5):
      print('='*20)
      nome = input('Nome: ').strip()
      idade = int(input('Idade: '))
      sexo = input('Sexo [M/F]: ').upper()[0].strip()
      soma += idade
      if maior < idade and sexo == 'M':
        maior = idade
        maisVelho = nome
      if idade < 20 and sexo == 'F':
        cont += 1
    media = soma / 4
    print(f'A media de idade do grupo é de {media:.1f} anos')
    print(f'O homem mais velho tem {maior} anos e se chama {maisVelho}')
    print(f'Ao todo são {cont} mulheres com menos de 20 anos')

  def desafio058(self):
    from random import randint
    acum = 0
    computador = randint(1,10)
    print('Skynet: Advinhe qual número estou pensando')
    while True:
      jogador = int(input('Jogador: '))
      if jogador > computador:
        print('Skeynet: Menos.. Tente novamente')
        acum += 1
      elif jogador < computador:
        print('Skynet: Mais.. Tente novamente')
        acum += 1
      else:
        break
    print(f'Skynet: Acertou com {acum} tentativas. Parabéns!')

  def desafio059(self):
    numUm = int(input('Primeiro valor: '))
    numDois = int(input('Segundo valor: '))
    while True:
      print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
      opc = int(input('>>>>> Qual a sua opção? '))
      if opc == 1:
        soma = numUm + numDois
        print(f'A soma entre {numUm} + {numDois} é {soma}')
      elif opc == 2:
        multi = numUm * numDois
        print(f'O resultado de {numUm} x {numDois} é {multi}')
      elif opc == 3:
        if numUm > numDois:
          maior = numUm
        else:
          maior = numDois
        print(f'Entre {numDois} e {numUm} o maior valor é {maior}')
      elif opc == 4:
        numUm = int(input('Primeiro valor: '))
        numDois = int(input('Segundo valor: '))
      elif opc > 5:
        print('Valor Inválido, Tente novamente')
      else:
        break

  def desafio060(self):
    num = int(input("Calcular seu fatorial: "))
    print(f'Calculando {num}! = {num} ', end='')
    for c in range(num-1, 0, -1):
      print(f'X {c} ', end='')
      num = num * c
    print(f'= {num}')