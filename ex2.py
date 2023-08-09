# REVISÃO (COMENTARIO)
"""COMENTARIO EM BLOCO"""

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


