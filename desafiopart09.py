class Cev:
  def __init__(self):
    pass

  def desafio081(self):
    numeros = []
    while True:
      numeros.append(int(input('Digite um valor: ')))
      opc = ' '
      while opc != 'N' and opc != 'S':
        opc = input('Quer continuar [S/N]: ').upper().strip()
      if opc == 'N':
        break
    print(f'Você digitou {len(numeros)} elementos')
    numeros.sort(reverse=True)
    print(f'Os valores em ordem decrescente são {numeros}')
    if 5 in numeros:
      print(f'O valor 5 faz parte da lista!')
    else:
      print('O valor 5 não foi encontrado na lista!')

  def desafio082(self):
    numeros = []
    pares = []
    impares = []
    while True:
      numeros.append(int(input('Digite um valor: ')))
      opc = ' '
      while opc != 'S' and opc != 'N':
        opc = input('Quer continuar [S/N]: ').strip().upper()
      if opc == 'N':
        break
    print(f'A lista completa é {numeros}')
    for num in numeros:
      if num % 2 == 0:
        pares.append(num)
      else:
        impares.append(num)
    print(f'A lista de pares é {pares}')
    print(f'A lista de impares é {impares}')

  def desafio083(self):
    cont = 0
    exp = input('Digite a expressão: ')
    for i in exp:
      if i == '(' or i == ')':
        cont += 1
    if cont % 2 == 0:
      print('Sua expressão está valida')
    else:
      print('Sua expressão está errada')

  def desafio084(self):
    nomes = []
    pesos = []
    while True:
      nomes.append(input('Nome: '))
      pesos.append(float(input('Peso: ')))
      opc = ' '
      while opc != 'S' and opc != 'N':
        opc = input('Quer continuar [S/N]: ').upper().strip()
      if opc == 'N':
        break
    print(f'Ao todo você cadastrou {len(nomes)} pessoas')
    print(f'O maior peso foi de {max(pesos):.1f}Kg. Peso de ', end='')
    for i, v in enumerate(pesos):
      if v == max(pesos):
        print(f'[{nomes[i].title()}]', end=' ')
    print(f'\nO menor peso foi de {min(pesos):.1f}Kg. Peso de ', end='')
    for i, e in enumerate(pesos):
      if e == min(pesos):
        print(f'[{nomes[i].title()}]', end=' ')

  def desafio085(self):
    numeros = [[],[]]
    for c in range(1,8):
      num = int(input(f'Digite o valor {c}:'))
      if num % 2 == 0:
        numeros[0].append(num)
      else:
        numeros[1].append(num)
    numeros[0].sort()
    numeros[1].sort()
    print(f'Os valores pares digitados foram: {numeros[0]}')
    print(f'Os valores impares digitados foram: {numeros[1]}')

  def desafio086(self):
    l = v = 0
    matriz = [[],[],[]]
    for num in range(0, 9):
      matriz[l].append(int(input(f'Digite um valor para {l, v}: ')))
      v += 1
      if v == 3:
        l += 1
        v = 0
    v = l = 0
    print('=-'*30)
    for valor in range(0,9):
      print(f'[{matriz[l][v]:^5}]', end='')
      v += 1
      if v == 3:
        print()
        l += 1
        v = 0

  def desafio087(self):
    linha = coluna = 0
    matriz = [[],[],[]]
    for numero in range(0, 9):
      matriz[linha].append(int(input(f'Digite um valor para {linha, coluna}: ')))
      coluna += 1
      if coluna == 3:
        linha += 1
        coluna = 0
    coluna = linha = 0
    print('=-'*30)
    for valor in range(0,9):
      print(f'[{matriz[linha][coluna]:^5}]', end='')
      coluna += 1
      if coluna == 3:
        print()
        linha += 1
        coluna = 0
    print('=-'*30)
    pares = maior = soma = 0
    for linha in range(0,3):
      for coluna in range(0,3):
        if maior == 0 and linha == 1:
          maior = matriz[linha][coluna]
        else: 
          if matriz[linha][coluna] > maior and linha == 1:
              maior = matriz[linha][coluna]
        if coluna == 2:
          soma += matriz[linha][coluna]
        if matriz[linha][coluna] % 2 == 0:
          pares += matriz[linha][coluna] 
    print(f'A soma dos valores pares é: {pares}')
    print(f'A soma dos valores da terceira coluna é {soma}')
    print(f'O maior valor da segunda linha é {maior}')

  def desafio088(self):
    from random import randint
    from time import sleep
    c = 1
    jogo = []
    print('JOGO DA MEGA SENA')
    opc = int(input('Quantos jogos você quer sortear? '))
    print(f'SORTEANDO {opc} JOGOS')
    while c <= opc:
      sleep(1)
      for i in range(0,6):
        num = randint(1,60)
        if num not in jogo:
          jogo.append(num)
      jogo.sort()
      print(f'Jogo {c}: {jogo}')
      jogo.clear()
      c += 1

  def desafio089(self):
    cont = 0
    alunos = []
    notas1 = []
    notas2 = []
    medias = []
    while True:
      nome = input('Nome: ').strip()
      alunos.append(nome)
      nota1 = float(input('Nota 1: '))
      notas1.append(nota1)
      nota2 = float(input('Nota 2: '))
      notas2.append(nota2)
      media = (nota1 + nota2) / 2
      medias.append(media)
      media = 0
      opc = ' '
      while opc != 'N' and opc != 'S':
        opc = input('Quer continuar? [S/N]: ').upper().strip()
      cont += 1
      if opc == 'N':
        print('-='*30)
        print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
        for c in range(0,len(alunos)):
          print(f'{c:<4}{alunos[c]:<10}{medias[c]:>8.1f}')
        while True:  
          print('-='*30)
          resp = int(input('Mostrar notas de qual aluno? (999 p/ interromper): '))
          if resp <= len(alunos):
            print(f'Notas de {alunos[resp]} são {notas1[resp], notas2[resp]}')
          else:  
            break
        break

  def desafio090(self):
    aluno = {}
    nome = input('Nome: ')
    aluno['nome'] = nome
    nota = float(input(f'Média de {nome}: '))
    aluno['media'] = nota
    if nota >= 7 and nota <= 10:
      aluno['situação'] = 'Aprovado'
    elif nota < 7 and nota >= 4:
      aluno['situação'] = 'Recuperação'
    elif nota < 4 and nota >= 0:
      aluno['situação'] = 'Reprovado'
    else:
      print('Média inválida')
    print('-='*30)
    for k,v in aluno.items():
      print(f'- {k} é igual a {v}')
    print(aluno)