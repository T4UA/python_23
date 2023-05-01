class Cev:
  def __init__(self):
    pass

  def desafio041(self):
    from datetime import date
    ano_nasc = int(input('Ano de Nascimento: '))
    atual = date.today().year
    idade = atual - ano_nasc
    print(f'Com {idade} anos')
    if idade <= 9:
      print('Você está na categoria MIRIM')
    elif idade <= 14:
      print("Você está na categoria INFANTIL")
    elif idade <= 19:
      print('Você está na categoria JUNIOR')
    elif idade <= 25:
      print('Você está na categoria SẼNIOR')
    else:
      print('Você está na categoria MASTER')

  def desafio042(self):
    seg_1 = float(input('Primeiro Segmento: '))
    seg_2 = float(input('Segundo Segmento: '))
    seg_3 = float(input('Terceiro Segmento: '))
    if seg_1 + seg_2 > seg_3 and seg_2 + seg_3 > seg_1 and seg_3 + seg_1 > seg_2:
      if seg_1 != seg_2 != seg_3 != seg_1:
        print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO")
      elif seg_1 == seg_2 == seg_3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILATERO')
      else:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')
    else:
      print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

  def desafio043(self):
    peso = float(input('Qual é seu peso? (Kg) '))
    altura = float(input('Qual é sua altura? (m) '))
    imc = peso / (altura**2)
    print(f'O IMC dessa pessoa é de {imc:.1f}, classificada com', end=' ')
    if imc <= 18.5:
      print('BAIXO PESO')
    elif 18.6 <= imc <= 24.9:
      print('PESO NORMAL')
    elif 25 <= imc <= 29.9:
      print('SOBREPESO')
    elif 30 <= imc <= 34.9:
      print('OBESIDADE GRAU I')
    elif 35 <= imc <= 39.9:
      print('OBESIDADE GRAU II')
    else:
      print('OBESIDADE GRAU III')

  def desafio044(self):
    preco = float(input('Qual o preço do produto? R$ '))
    print('[1] À vista dinheiro\n[2] Transferencia Pix\n[3] Em até 2x no cartão\n[4] 3x ou mais no cartão')
    pagamento = int(input('Qual a forma de pagamento? [1,2,3,4]: '))
    if pagamento == 1 or pagamento == 2 or pagamento == 3:
      print(f'Sua compra de R${preco:.2f} vai custar no final R$', end='')
    if pagamento == 1:
      print(f'{preco:.2f}')
    elif pagamento == 2:
      desconto = preco - (preco * 10 / 100)
      print(f'{desconto:.2f}')
    elif pagamento == 3:
      juros = preco + (preco * 5 / 100)
      parcela = juros / 2
      print(f'{juros:.2f}, logo será pago 2 parcelas de R${parcela:.2f}')
    elif pagamento == 4:
      juros = preco + (preco * 20 / 100)
      totparc = int(input('Quantas parcelas: '))
      parcela = juros / totparc
      print(f'Sua compra de R${preco:.2f} vai custar no final R${juros:.2f}, logo será pago {totparc} parcelas de R${parcela:.2f}')
    else:
      print('Opção Inválida')

  def desafio045(self):
    from time import sleep
    from random import randint
    print('Suas opções\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
    jogador = int(input('Qual é a sua jogada? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    computador = randint(0,2)
    print('-=-' * 11)
    if jogador == 0 and computador == 2:
      print('Computador jogou Tesoura\nJogador jogou Pedra\n\nJOGADOR VENCE')
    elif jogador == 1 and computador == 0:
      print('Computador jogou Pedra\nJogador jogou Papel\n\nJOGADOR VENCE')
    elif jogador == 2 and computador == 1:
      print('Computador jogou Papel\nJogador jogou Tesoura\n\nJOGADOR VENCE')
    elif jogador == 0 and computador == 1:
      print('Computador jogou Pedra\nJogador jogou Papel\n\nCOMPUTADOR VENCE')
    elif jogador == 1 and computador == 2:
      print('Computador jogou Papel\nJogador jogou Tesoura\n\nCOMPUTADOR VENCE')
    elif jogador == 2 and computador == 0:
      print('Computador jogou Tesoura\nJogador jogou Pedra\n\nCOMPUTADOR VENCE')
    else:
      if jogador == 2 == computador:
        print('Computador jogou Tesoura\nJogador jogou Tesoura\n\nEMPATE!!')
      elif jogador == 0 == computador:
        print('Computador jogou Pedra\nJogador jogou Pedra\n\nEMPATE!!')
      elif jogador == 1 == computador:
        print('Computador jogou Papel\nJogador jogou Papel\n\nEMPATE!!')
      else:
        print('OPÇÃO INVÁLIDA')
    print('-=-' * 11)

  def desafio046(self):
    from time import sleep
    for cont in range(10,-1,-1):
      print(cont)
      sleep(1)
    print("BUM! BUM! BUM!")

  def desafio047(self):
    for cont in range(1, 51):
      if cont % 2 == 0:
        print(cont, end=' ')
    print('ACABOU')

  def desafio048(self):
    soma = acum = 0
    for cont in range(1,501,2):
      if cont % 3 == 0:
        soma += cont
        acum += 1
    print(soma, acum)

  def desafio049(self):
    num = int(input('A tabuada de qual número você deseja saber? '))
    for c in range(1,11):
      print(f'{num} x {c:2} = {num*c}')

  def desafio050(self):
    soma = 0
    for c in range(0,6):
      num = int(input('Digite um valor: '))
      if num % 2 == 0:
        soma += num
    print(f'A soma dos números pares é {soma}')