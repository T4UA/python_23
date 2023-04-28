class Cev:
  def __init__(self):
    pass

  def desafio001(self):
    print('Hello World!')

  def desafio002(self):
    nome = input('Digite seu nome: ')
    print(f'É um prazer te conhecer, {nome}')

  def desafio003(self):
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))
    print(f'A soma entre {num1} e {num2} é igual a {num1 + num2}!')

  def desafio004(self):
    word = input('Digite algo: ')
    print(f'O tipo primitivo desse valor é {type(word)}')
    print(f'Só tem espaços? {word.isspace()}')
    print(f'É um número? {word.isnumeric()}')
    print(f'É alfavetico? {word.isalpha()}')
    print(f'É alfanumerico? {word.isalnum()}')
    print(f'Está maiúscula? {word.isupper()}')
    print(f'Está minúscula? {word.islower()}')
    print(f'Está capitalizado: {word.istitle()}')

  def desafio005(self):
    num = int(input('Digite um número: '))
    print(f'Analisando o valor {num}, seu antecessor é {num-1} e seu sucessor é {num+1}')

  def desafio006(self):
    num = int(input('Digite um número: '))
    print(f'O dobro de {num} vale {num*2}.')
    print(f'O triplo de {num} vale {num*3}.')
    print(f'A raiz quadrada de {num} é igual a {num**(1/2):.2f}')

  def desafio007(self):
    quant = soma = 0
    for cont in range(1,3):
      num = float(input(f'Digite a nota {cont} do aluno: '))
      quant += 1
      soma += num
    print(f'A média entre as notas do aluno é {soma/quant:.1f}')

  def desafio008(self):
    m = float(input('Distancia em metros: '))
    print(f'A medida de {m:.1f}m corresponde a:')
    print(f'{m/1000} km')
    print(f'{m/100} hm')
    print(f'{m/10} dam')
    print(f'{m*10:.0f} dm')
    print(f'{m*100:.0f} cm')
    print(f'{m*1000:.0f} mm')

  def desafio009(self):
    num = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 12)
    for cont in range(1,11):
      print(f'{num} x {cont:2} = {num * cont}')
    print('-' * 12)
  
  def desafio010(self):
    real = float(input('Quanto dinheiro vocẽ tem na carteira? R$'))
    dolar = real / 5.20
    euro = real / 5.53
    print(f'Com R${real} você pode comprar €{euro:.2f}')
    print(f'Com R${real} você pode comprar US${dolar:.2f}')