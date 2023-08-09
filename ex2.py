# REVISÃO (COMENTARIO)
"""COMENTARIO EM BLOCO"""

#ctrl L -> LIMPA O TERMINAL

#type da variavel
a = 10
type(a)
#<class 'int'>

#Tipagem

# int - numeros inteiros sem casas decimais
a = 30
b = -8

# float - numeros com casas decimais
c = 8.90
d = -6.89

# str - caracteres - texto
a = 'Ana'
b = "Alana"
c = """string com varias linhas
1 -
2 -"""
print(c)

# bool - False or True ( valores logicos)
a = True
b = False

#OPERACOES DE CONVERSÃO
a = 1
a = float(a)  #converte para float o 1(int)

b = 2.8
b = int(b)  #converte para int
print(b)

d = 3.6
d = str(d)   #converte para string
print(d)

#OPERAÇOES DE ENTRADA (INPUT) - todos são string
nome = input('')
idade = input('')

idade=int(idade)  #conversão
print(idade)

# INPUT COM TIPAGEM
a = int(input(''))
b = float(input(''))
c = str(input(''))

# OPERAÇÕES DE SAIDA (PRINT)
idade = 30
nome = 'Ana'
print(idade, nome) #virgula da espaço entre as variaveis
print('o seu nome é', nome, 'idade:', idade) # saida formatada
print('o seu nome é: {} idade: {}'.format(nome, idade)) # formatada com format e {}, cada chave tem um variavel na ordem
print(f'o seu nome é: {nome} idade: {idade}') # f string 

#OPERADORES ARITMETICO
print( 10 + 3)
print(10 -7)
print(10 * 3)
print(10 / 3)
print(10 //3) # divisão inteira sem casas decimais
print(10 % 3) # mod - resto da divisão
print(10 ** 3) # potencia

#ORDEM
#1 POTENCIA **
#2 MULTIPLICAÇÃO/DIV/MOD - DA ESQUERDA OARA DIREITA
#3 SOMA/SUBT

#OPERACOES RELACIONAIS (TRUE OR FALSE)
print(10 >3)     #maior
print(5 < 10)    #menor
print(10 == 3)  #iguais
print(10 !=6)    #diferente
print(10 >= 3)  #maior ou igual
print(10 <= 3)  #menor ou igual


#OPERADORES LOGICOS
print(10 > 3 and 10 == 10) #AND - TORNA TRUE SE AS DUAS FOREM VERDADEIROS
print(10 < 3 or 10 == 10) #OR - APENAS UM VALOR VERDADEIRO
print(not 10 == 10) #NOT - INVERTE A OPERAÇÃO

#INTRUCOES CONDICIONAIS (IF ELIF ELSE)
num = int(input(''))
if num % 2 == 0:
    print('o numero é par')
else:
    print('o num é impar')

#positivo /negativo / nulo

if num >0:
    print('positivo')
elif num < 0:
    print('negativo')
else:
    print('zero')


#ESTRUTURA DE SELEÇÃO (MATCH CASE)- Só entra no case se o valor for identico ao do case, comparações de igualdade
num = int(input(''))
match num:
    case 1: #case é apenas um VALOR
        print('num: 1')
    case 2:
        print('num: 2')
    case 1 | 10: #operacao de OR (comparação)
        print('')
    case _:               #case default - caso os case sejam falsos
        print('num diferente')


letra = input('') #match com string
match letra:
    case 'a':
        print('')
    case 'c':
        print('')

#-> MATCH CASE DA PARA USAR COM TRUE E FALSE (BOOL)

#ESTRUTURA DE REPETIÇÃO

#WHILE - QUANDO FOR VERDADEIRA

#exibir numeros de 1 a 10
cont = 1
while cont <=10:
    print(cont)
    cont += 1 #aumenta o valor da variavel

#calculadora
opcao = 0
while opcao != 5:
    print('1 +')
    print('2 -')
    print('3 *')
    print('4 /')
    print('5 - sair')
    opcao = int(input('escolha: '))
    match opcao:
        case 1:
            a = float(input('primeiro:'))
            b = float(input('segundo:'))
            print(f'é: {a +b}')

        case 2:
            a = float(input('primeiro:'))
            b = float(input('segundo:'))
            print(f'é: {a -b}')
        
        case 3:
            a = float(input('primeiro:'))
            b = float(input('segundo:'))
            print(f'é: {a *b}')
    
        case 4:
            a = float(input('primeiro:'))
            b = float(input('segundo:'))
            print(f'é: {a /b}')
        case 5:
            break
        case _:
            print('invalido')

#FOR -> quantidade de vezes definida, sabe os passos

for a in range(1,11): #inicial \ final
    print(a)

for a in range(2,11, 2): #(inicial, final, passo)
    print(a)

for a in range(11): #final
    print(a)

#FUNCAO - USA DEF

def somar(num1, num2): #funcao para somar - (variavel)
    c = num1 + num2
    return c #volta o valor da soma

somar(5,5) #chama funcão

#mostar o resultado
c = somar(5,5)
print(c)
#ou 
print(somar(5,5))


#FUNCAO - USA DEF - usando input.

def somar(num1, num2): #funcao para somar - (variavel)
    c = num1 + num2
    return c #volta o valor da soma, armazena os valores. (SEM RETURN VOLTA NULO)

#não precisa ter o mesmo nome da variavel de func dentro do parametro
a = int(input(''))
b = int(input(''))
print(f'{a} e {b}é: {somar(a,b)}')


