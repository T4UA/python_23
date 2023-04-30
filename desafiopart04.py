class Cev:
  def __init__(self):
    pass

  def desafio031(self):
    dist = float(input('Qual a distancia da sua viagem? '))
    print(f'Você está prestes a começar uma viagem de {dist}Km.')
    if dist <= 200:
      valor = dist * 0.50
      print(f'E o preço da sua passagem será de R${valor:.2f}')
    else:
      valor = dist * 0.45
      print(f'E o preço da sua passagem será de R${valor:.2f}')

  def desafio032(self):
    from datetime import date
    ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
    if ano == 0:
      ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
      print(f'O ano {ano} é bissexto')
    else:
      print(f'O ano de {ano} não é bissexto')

  def desafio033(self):
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    num3 = int(input('Terceiro número: '))

    if num1 > num2 and num1 > num3 and num2 > num3:
      print(f'Maior valor é {num1}')
      print(f'Menor valor é {num3}')
    elif num2 > num1 and num2 > num3 and num1 > num3:
      print(f'Maior valor é {num2}')
      print(f'Menor valor é {num3}')
    elif num3 > num1 and num3 > num2 and num1 > num2:
      print(f'Maior valor é {num3}')
      print(f'Menor valor é {num2}')
    elif num1 > num2 and num1 > num3 and num3 > num2:
      print(f'Maior valor é {num1}')
      print(f'Menor valor é {num2}')
    elif num2 > num1 and num2 > num3 and num3 > num1:
      print(f'Maior valor é {num2}')
      print(f'Menor valor é {num1}')
    else:
      print(f'Maior valor é {num3}')
      print(f'Menor valor é {num1}')

  def desafio034(self):
    salario = float(input('Digite seu salario: R$'))
    if salario <= 1250:
      aumento = (salario * (15/100)) + salario
    else:
      aumento = (salario * (10/100)) + salario
      
    print(f'Seu novo salário é de R${aumento:.2f}')

  def desafio035(self):
    pri = float(input('Primeiro segmento: '))
    seg = float(input('Segundo segmento: '))
    ter = float(input('Terceiro segmento: '))
    if pri + seg >= ter and seg + ter >= pri and ter + pri >= seg:
      print('Os segmentos acima PODEM FORMAR um triângulo')
    else:
      print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

  def desafio036(self):
    valor_casa = float(input('Valor da casa: R$'))
    salario = float(input('Seu salário: R$'))
    anos = int(input('Em quantos anos irá pagar: '))

    prestacao = (valor_casa / anos) / 12
    porc = salario * 30 / 100
    if prestacao > porc:
      print(f'Com esse valor de R${prestacao:.2f} das prestações, não podemos conceder o empréstimo')
    else:
      print(f'O valor de R${prestacao:.2f} por mês está dentro do seu limite, emprestimo concedido')

  def desafio037(self):
    num = int(input('Digite um número inteiro: '))
    print('[1] converter para BINARIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL')
    opcao = int(input('Sua Opção: '))
    if opcao == 1:
      bn = bin(num)
      print(f'{num} convertido para BINÁRIO é igual a {bn[2:]}')
    elif opcao == 2:
      oc = oct(num)
      print(f'{num} convertido para OCTAL é igual a {oc[2:]}')
    elif opcao == 3:
      hx = hex(num)
      print(f'{num} convertido para HEXADECIMAL é igual a {hx[2:]}')
    else:
      print('Opção Inválida')

  def desafio038(self):
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    if num1 > num2:
      print('O PRIMEIRO número é maior')
    elif num1 == num2:
      print('Os valores são IGUAIS')
    else:
      print('O SEGUNDO número é maior')

  def desafio039(self):
    from datetime import date
    ano = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano
    print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
    if idade < 18:
      diferenca_idade = 18 - idade
      ano_alistamento = atual + diferenca_idade
      print(f'Ainda faltam {diferenca_idade} anos para o alistamento\nSeu alistamento será em {ano_alistamento}')
    elif idade == 18:
      print('Você deveria se alistar IMEDIATAMENTE')
    else:
      diferenca_idade = idade - 18
      ano_alistamento = atual - diferenca_idade
      print(f'Você ja deveria ter se alistado há {diferenca_idade} anos\nSeu alistamento foi em {ano_alistamento}')

  def desafio040(self):
    nota_1 = float(input('Primeira nota: '))
    nota_2 = float(input('Segunda nota: '))
    media = (nota_1 + nota_2) / 2
    print(f'Tirando {nota_1} e {nota_2}, a média do aluno é {media:.1f}')
    if media >= 7:
      print('O aluno está APROVADO')
    elif 4 <= media < 7:
      print('O aluno está em RECUPERAÇÃO')
    else:
      print('O aluno está REPROVADO')