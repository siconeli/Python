#--------------------------------------------
#Atalhos do VS Code:

#Selecionar a palavra, depois Ctrl + H, digitar a nova palavra, depois Ctrl + Alt + Enter = Sunstituir palavras iguais por outra palavra
#Ctrl + D = Selecionar palavras iguais
#Ctrl + F = Pesquisar
#Ctrl + ; = Comentar linhas de código
#Shift + Alt + Seta para baixo = Duplicar linha
#Alt + Seta para baixo ou para cima = Movimentar linha
#Ctrl + L = Seleciona a linha inteira
#Alt + Z = Adapta o comprimento da linha de código de acordo com a tela
#Ctrl + G = Localiza a linha de código desejada

#--------------------------------------------

#Print na mesma linha:
#print('Henrique Siconeli', end=' ')
#print('Francisco')

#Quebra de linha no print:
#print('Teste de quebra de linha \nquebrou')

#--------------------------------------------

#Mostrar sucessor e antessesor de um número informado:

# n = int(input('Digite um número: '))

# ant = n - 1
# suc = n + 1

# print(f'O número digitado foi o {n}, seu sucessor é o número {suc} e o antecessor é o número {ant}')

#---------------------------------------------

#Calcular dobro, triplo e raiz quadrada de um número informado:

# n = int(input('Digite um número: '))

# dob = n * 2
# trip = n * 3
# raiz = round(n **(1/2))

# print(f'O número digitado foi o {n}, o dobro desse número é {dob}, o triplo desse número é {trip} e a raiz quadrada é {raiz}')

#---------------------------------------------

#Ler duas notas e mostrar a média:

# n1 = float(input('Digite sua primeira nota: '))
# n2 = float(input('Digite sua segunda nota: '))

# m = (n1 + n2) / 2

# print(f'1º nota: {n1}, 2º nota: {n2} \nSua média é: {m}')
#---------------------------------------------

#Como dar espaçamentos dentro do print:

#g = input('Digite qualquer coisa: ')n

#print('Você digitou ({:!^20})'.format(g))

#---------------------------------------------

#Converter metros em centimetros e milímetros:

# m = int(input('Digite a quantidade de metros: '))

# ce = m * 100
# mi = m * 1000

# print('Você informou {m} metros, que equivale à {ce} centímetros ou {mi} milímetros')

#---------------------------------------------

#Ler um número inteiro qualquer e mostrar sua tabuada:

# n = int(input('Digite um número: '))

# v1 = n * 1
# v2 = n * 2
# v3 = n * 3
# v4 = n * 4
# v5 = n * 5
# v6 = n * 6
# v7 = n * 7
# v8 = n * 8
# v9 = n * 9
# v10 = n * 10

# print(f'{n} x 1 = {v1} \n{n} x 2 = {v2} \n{n} x 3 = {v3} \n{n} x 4 = {v4} \n{n} x 5 = {v5} \n{n} x 6 = {v6} \n{n} x 7 = {v7} \n{n} x 8 = {v8} \n{n} x 9 = {v9} \n{n} x 10 = {v10}')

#---------------------------------------------

#Ler quanto dinheiro uma pessoa tem na carteira e mostrar quantos dólares ela pode comprar:

# carteira = float(input('Informe, qual o valor que possui em sua carteira: '))

# dolares = carteira / 3.27
# arredondamento = round(dolares, 2)

# print(f'Você possui R${carteira} reais em sua carteira, pode comprar US${arredondamento} dólares')

#---------------------------------------------

#Ler a largura e altura de uma parede em metros, calcular a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²:

# largura = int(input('Digite a largura da parede: '))
# altura = int(input('Digite a altura da parede: '))

# tinta = (largura * altura) / 2

# print(f'Para uma parede com {largura} m de largura e {altura} m de altura, é necessário {tinta} litros de tinta')

#---------------------------------------------

#Ler o preço e o desconto de um produto e mostrar o novo preço com desconto.

# preco = int(input('Digite o preço do produto: '))
# valordesconto = int(input('Digite a porcentagem de desconto: '))

# desconto = preco * valordesconto/100

# novopreco = preco - desconto

# print(f'O preço do produto com desconto de {valordesconto}% é R${novopreco} reais')

#---------------------------------------------

#Ler o salário de um funcionário e mostrar o novo salário com 15% de aumento.

# salario = int(input('Digite seu salário: '))

# aumento = salario * 15/100

# novosalario = salario + aumento

# print(f'O seu salário de R${salario} reais com 15% de aumento é R${novosalario}')

#---------------------------------------------
#Ler o nome completo de uma pessoa e mostrar: O nome com todas as letras maiúsculas, com todas minúsculas, quantas letras ao todo e quantas letras tem o primeiro nome.

# nome = str(input('Digite seu nome completo: '))

# maiusculas = nome.upper()

# minusculas = nome.lower()

# quantidade = len(nome)

# pnome = nome.split()

# pnome = len(pnome[0])

# print(f'{nome} / {maiusculas} / {minusculas} / {quantidade} / {pnome}')

#---------------------------------------------
#Ler um número de 0 a 9999 e mostrar na tela sua Unidade, dezena, centena e milhar:
# num = int(input('Digite um número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10

# print(f'Analisando o número: {num}, Unidade: {u}, Dezena: {d}, Centena: {c} e Milhar: {m}')

#---------------------------------------------
#Ler o nome de uma cidade e dizer se ela começa ou não com o nome "Santo":
# cidade = str(input('Digite o nome de uma cidade: ')).strip().title()

# divide = cidade.split()

# busca = divide[0].find('Santo')

# if busca == 0:
#     print(f'A cidade digitada foi: {cidade}, O nome da cidade começa com Santo')
# else:
#     print(f'A cidade digitada foi: {cidade}, O nome da cidade não começa com Santo')

#---------------------------------------------
#Ler o nome de uma pessoa e dizer se ela tem "Silva" no nome:

# nome = str(input('Digite seu nome: ')).strip().title()

# contem = 'Silva' in nome

# if contem == True:
#     print('Contem Silva em seu nome')
# else:
#     print('Não contem Silva em seu nome')  

#---------------------------------------------
#Ler uma frase e mostrar quantas vezes aparece a letra "a", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez:

# frase = str(input('Digite uma frase aleatória: ')).strip().lower()

# vezes = frase.count('a')

# primeira = frase.find('a') + 1

# ultima = frase.rfind('a') + 1

# print(f'A letra A aparece {vezes} vezes na frase. \nA primeira letra A apareceu na posição {primeira}. \nA última letra A apareceu na posição {ultima}.')

#---------------------------------------------
#Ler o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente:

# nome = str(input('Digite seu nome completo: ')).strip()

# divide = nome.split()

# primeiro = divide[0]

# ultimo = divide[-1]

# print(f'Seu nome é {nome} \nPrimeiro nome é {primeiro} \nÚltimo nome é {ultimo}')

#---------------------------------------------
# Condição ELIF
# nome = str(input('Qual o seu nome? '))

# if nome == 'henrique':
#     print('Seu nome é lindo!')
# elif nome == 'pedro' or nome== 'tadeu' or nome == 'allison':
#     print('Seu nome é bem popular no Brasil!')
# else:
#     print('Seu nome é bem normal!')
# print('Abraço!')

#---------------------------------------------
# Aprovação de empréstimo mobiliário:

# vcasa = float(input('Qual é o valor da casa? '))
# salario = float(input('Qua é o seu salário? '))
# anos = int(input('Em quantos anos deseja pagar? '))

# prestacao = vcasa / (anos*12)
# aprovacao = salario * (30/100)

# if prestacao > aprovacao:
#     print(f'Para uma casa no valor de R${vcasa}, a prestação fica R${prestacao} mensal, não se adequando ao valor do seu salário, então o empréstimo foi negado.')
   
# else:
#     print(f'Para uma casa no valor de R${vcasa}, a prestação fica R${prestacao} mensal, sendo este o valor, cabe no seu salário, o empréstimo foi aprovado.')

#---------------------------------------------
# Conversão de bases:

# num = int(input('Digite um número inteiro: '))
# base = int(input('''Escolha qual será a base de conversão: 
# [ 1 ] - Converter para Binario 
# [ 2 ] - Converter para Octal 
# [ 3 ] - Converter para Hexadecimal
# Opção: '''))

# if base == 1:
#     print(f'O número {num} convertido para binário é {bin(num) [2:]}')
# elif base == 2:
#     print(f'O número {num} convertido para octal é {oct(num)} [2:]')
# elif base == 3:
#     print(f'O número {num} convertido para hexadecimal é {hex(num) [2:]}')

#---------------------------------------------
# Comparação de valores:

# num1 = int(input('Informe um número: '))
# num2 = int(input('Informe outro número: '))

# if num1 > num2:
#     print(f'O PRIMEIRO valor ({num1}) é MAIOR que o segundo valor ({num2})')
# elif num1 < num2:
#     print(f'O SEGUNDO valor ({num2}) é MAIOR que o primeiro valor ({num1})')
# elif num1 == num2:
#     print('Não existe valor maior, os dois são IGUAIS!')

#---------------------------------------------
# Calcular o alistamento ao exército:

# nasc = int(input('Informe o seu ano de nascimento: '))
# calc = 2023 - nasc
# faltam = nasc - 2005
# passou = calc - 18

# if calc < 18:
#     print(f'Você ainda não atingiu a idade de alistamento, faltam {faltam} anos')
# elif calc == 18:
#     print(f'Você tem {calc} anos, essa é a hora certa de se alistar!')
# elif calc > 18:
#     print(f'A hora certa de se alistar já passou, você está {passou} anos atrasado!')

#---------------------------------------------
# Calcular a média de duas notas e classificar a situação do aluno :

# n1 = float(input('Informe sua nota 1: '))
# n2 = float(input('Informe sua nota 2: '))

# media = (n1 + n2) / 2

# if media < 5:
#     print(f'Sua média é {media}, está a baixo de 5.0, você foi REPROVADO!')
# elif media == 5 or media <= 6.9:
#     print(f'Sua média é {media}, você está de RECUPERAÇÃO!')
# elif media >= 7:
#     print(f'Sua média é {media}, está dentro do esperado, você foi APROVADO!')    

#---------------------------------------------
# Classificar a categoria de um aluno de natação, de acordo com seu ano de nascimento:

# nasc = int(input('''
# [ Classificação ] 

# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

# Informe seu ano de nascimento: '''))

# idade = 2023 - nasc

# if idade == 1 or idade <= 9:
#     print(f'O atleta tem {idade}, é da categoria [MIRIM]')
# elif idade == 10 or idade <= 14:
#     print(f'O atleta tem {idade}, é da categoria [INFANTIL]')
# elif idade == 14 or idade <= 19:
#     print(f'O atleta tem {idade}, é da categoria [JUNIOR]')
# elif idade == 19 or idade  <=20:
#     print(f'O atleta tem {idade},  é da categoria [SÊNIOR]')
# elif idade > 20:
#     print(f'O atleta tem {idade}, é da categoria [MASTER]')

#---------------------------------------------
# Cálculo IMC:

# peso = float(input('Informe seu peso (Kg): '))
# altura = float(input('Informe sua altura (M): '))

# imc = peso / (altura**2)

# if imc < 18.5:
#     print(f'Seu IMC é {imc}, você está abaixo do peso!')
# elif imc >= 18.5 and imc < 25:
#     print(f'Seu IMC é {imc}, você está no peso ideal!')
# elif imc >= 25 and imc < 30:
#     print(f'Seu IMC é {imc}, você está com sobrepeso!')
# elif imc >= 30 and imc < 40:
#     print(f'Seu IMC é {imc}, você está com obesidade')
# elif imc >= 40:
#     print(f'Seu IMC é {imc}, você tem obesidade mórbita!')

#---------------------------------------------
# Valor a ser pago por um produto de acordo com a condição de pagamento.

# valor = float(input('Informe o valor do produto: R$ '))
# dinheirooucheque = valor - (valor * 10/100)
# umanocartao = valor - (valor * 5/100)
# tresnocartao = valor + (valor * 20/100)

# print('''
# 1 - À vista - Dinheiro/Cheque: 10% de desconto
# 2 - À vista - Cartão: 5% de desconto
# 3 - Em até 2x - Cartão: preço normal
# 4 - Em até 3x - Cartão: 20% de juros
# ''')

# condicao = int(input('Informe a condição de pagamento: '))

# if condicao == 1:
#     print(f'O valor do produto é {valor}, com a condição de pagamento escolhida fica: R${dinheirooucheque}')
# elif condicao == 2:
#     print(f'O valor do produto é {valor}, com a condição de pagamento escolhida fica: R${umanocartao}')
# elif condicao == 3:
#     print(f'O valor do produto é {valor}, com a condição de pagamento escolhida fica: R${valor}')
# elif condicao == 4:
#     print(f'O valor do produto é {valor}, com a condição de pagamento escolhida fica: R${tresnocartao}')

#---------------------------------------------
