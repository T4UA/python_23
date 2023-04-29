class Cev:
  def __init__(self):
    pass

  def desafio011(self):
    larg = float(input('Largura da parede: '))
    altu = float(input('Altura da parede: '))
    area = larg * altu
    print(f'Sua parede tem a dimensão de {larg}x{altu} e sua área é de {area}m².')
    print(f'Para pintar essa parede, você precisará de {area/2}l de tinta.')

  def desafio012(self):
    preco = float(input('Qual o preço do produto? R$'))
    desc = preco - (preco * 5 / 100)
    print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${desc:.2f}')

  def desafio013(self):
    salario = float(input('Qual é o salário do funcionário? R$'))
    reaj = salario + (salario * 15 / 100)
    print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${reaj:.2f}')

  def desafio014(self):
    grau = float(input('Informe a temperatura em C: '))
    fah = grau * 1.8 + 32
    print(f'A temperatura de {grau}C corresponde a {fah}F!')

  def desafio015(self):
    km = float(input('Quantidade de quilometros percorridos: '))
    dias = int(input('Quantos dias alugados: '))
    custo_d = 60 * dias
    custo_k = 0.15 * km
    preco = custo_d + custo_k
    print(f'O total a pagar é de R${preco:.2f}')

  def desafio016(self):
    from math import trunc
    num = float(input('Digite um valor: '))
    print(f'O valor digitado foi {num} e a sua porção inteira é {num:.0f}')
    print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')
    print(f'O valor digitado foi {num} e a sua porção interia é {int(num)}')

  def desafio017(self):
    '''from math import hypot'''
    cat_op = float(input('Comprimento do cateto oposto: '))
    cat_ad = float(input('Comprimento do cateto adjacente: '))
    hipo = (cat_op * cat_op) + (cat_ad * cat_ad)
    '''hipo = hypot(cat_op, cat_ad)'''
    print(f'A hipotenusa vai medir {hipo**(1/2):.2f}')

  def desafio018(self):
    from math import radians, sin, cos, tan
    ang = float(input('Digite o ângulo que você deseja: '))
    print(f'O ângulo de {ang} tem o SENO de {sin(radians(ang)):.2f}')
    print(f'O ângulo de {ang} tem o COSSENO de {cos(radians(ang)):.2f}')
    print(f'O ângulo de {ang} tem a TANGENTE de {tan(radians(ang)):.2f}')

  def desafio019(self):
    from random import choice
    a1 = input('Primeiro aluno: ')
    a2 = input('Segundo aluno: ')
    a3 = input('Terceiro aluno: ')
    a4 = input('Quarto aluno: ')
    lista = [a1,a2,a3,a4]
    escolhido = choice(lista)
    print(f'O aluno escolhido foi {escolhido}')

  def desafio020(self):
    from random import shuffle
    a1 = input('Primeiro aluno: ')
    a2 = input('Segundo aluno: ')
    a3 = input('Terceiro aluno: ')
    a4 = input('Quarto aluno: ')
    lista = [a1,a2,a3,a4]
    shuffle(lista)
    print(f'A ordem de apresentação será {lista}')