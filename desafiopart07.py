class Cev:
  def __init__(self):
    pass

  def desafio061(self):
    c = 1
    pt = int(input('Primeiro termo: '))
    ra = int(input('Razão: '))
    while c < 11:
      print(pt, end=' -> ')
      pt += ra
      c += 1
    print('FIM')

  def desafio062(self):
    c = 0
    cont = 0
    pt = int(input('Primeiro termo: '))
    ra = int(input('Razão: '))
    while c < 10:
      print(pt, end=' -> ')
      pt += ra
      c += 1
    print('PAUSA')
    while True:
      opc = int(input('\nQuantos termos você quer mostrar a mais? '))
      if opc == 0:
        break
      else:
        for i in range(1,opc+1):
          print(pt, end=' -> ')
          pt += ra
        print('PAUSA')
      cont += opc
    tot = c + cont
    print(f'Progressão finalizada com {tot} termos mostrados')

  def desafio063(self):
    num = int(input('Quantos termos você quer mostrar? '))
    a = 0
    b = 1
    print(f'{a} -> {b}', end=' -> ')
    for cont in range(0,num - 2):
      c = a + b
      a = b
      b = c
      print(c, end=' -> ')
    print('FIM')

  def desafio064(self):
    soma = cont = 0
    while True:
      num = int(input('Digite um número [999 para parar]: '))
      if num == 999: 
        break
      else:
        soma += num
        cont += 1
    print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')

  def desafio065(self):
    cont = soma = maior = memor = 0
    while True:
      num = int(input('Digite um número: '))
      soma += num
      cont += 1
      if maior == 0:
        maior = num
        menor = num
      if num > maior:
        maior = num
      if num < menor:
        menor = num
      opc = input('Quer continuar [S/N]? ').strip().upper()[0]
      if opc != 'S':
        break
    media = soma / cont
    print(f'Você digitou {cont} números e a média foi {media:.2f}\nO maior valor foi {maior} e o menor foi {menor}')

  def desafio066(self):
    soma = cont = 0
    while True:
      num = int(input('Digite um valor (999 para parar): '))
      if num == 999:
        break
      soma += num
      cont += 1
    print(f'Você digitou {cont} números, que totaliza {soma}')

  def desafio067(self):
    while True:
      print('='*33)
      num = int(input('Quer ver a tabuada de qual valor? '))
      print('='*33)
      if num < 0:
        print('PROGRAMA TABUADA ENCERRADO.Volte sempre!')
        break
      for c in range(1,11):
        print(f'{num} x {c:2} = {num*c}')

  def desafio068(self):
    from random import randint
    print('-' * 30)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-' * 30)
    cont = 0
    while True:
      num = int(input('Diga um valor: '))
      opc = input('PAR ou ÍMPAR? ').strip().lower()[0]
      while opc not in 'pi':
        opc = input('PAR ou ÍMPAR? ').strip().lower()[0]
      print('-' * 30)
      pc = randint(0,10)
      soma = num + pc
      print(f'Você jogou {num} e o computador {pc}. Total de {soma} ', end='')
      if soma % 2 == 0:
        print('DEU PAR')
        if opc == 'p':
          cont += 1
        else:
          print('Você Perdeu!')
          break
      else:
        print('DEU ÍMPAR')
        if opc == 'i':
          cont += 1
        else:
          print('Você Perdeu!')
          break
      print('Você Venceu!\nVamos jogar novamente...')
      print('-' * 30)    
    print(f'Você venceu {cont} vezes')

  def desafio069(self):
    totMasc = totMaior = totFemin = 0
    while True:
      print('-' * 30)
      print('CADASTRE UMA PESSOA')
      print('-' * 30)
      idade = int(input('Idade: '))
      sexo = ' '
      while sexo not in 'MF':
        sexo = input('Sexo: [F/M] ').strip().upper()[0]
      print('-' * 30)
      opc = ' '
      while opc not in 'SN':
        opc = input('Quer continuar: [S/N] ').strip().upper()[0]
      print('-' * 30)
      if idade >= 18:
        totMaior += 1
      if sexo == 'M':
        totMasc += 1
      if sexo == 'F' and idade < 20:
        totFemin += 1
      if opc == 'N':
        break
    print(f'Total de pessoas com mais de 18 anos: {totMaior}')
    print(f'Ao todo temos {totMasc} homens cadastrados')
    print(f'E temos {totFemin} mulheres com menos de 20 anos')

  def desafio070(self):
    print('-' * 30)
    print('LOJA SUPER BARATÃO')
    print('-' * 30)
    soma = mil = menor = 0
    while True:
      nomeP = input('Nome do Produto: ').strip()
      preco = float(input('Preço: R$'))
      soma += preco
      opc = ' '
      while opc not in 'SN':
        opc = input('Quer continuar [S/N]: ').strip().upper()[0]
      if preco > 1000:
        mil += 1
      if menor == 0 or preco < menor:
        menor = preco
        produtoBarato = nomeP
      if opc == 'N':
        break
    print('-------------FIM DO PROGRAMA------------')
    print(f'O total da compra foi de R${soma:.2f}')
    print(f'Temos {mil} produtos custando mais de R$1000,00')
    print(f'O produto mais barato foi a {produtoBarato} que custa R${menor:.2f}')
        