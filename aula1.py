'''sintax: é o conjunto de regras que define como escrever 
o código corretamente para que o Python entenda e execute.
Exemplo correto: '''
print('olá Mundo')
'''O comando print() está escrito corretamente, com parênteses e uma string entre aspas.

exemplo incorreto :
print "Olá, mundo!"
 * é obrigatório usar parênteses no print '''

'''COMENTÁRIOS'''
# Comentários são usados para explicar o código e não são executados pelo Python. São muito úteis para lembrar o que cada parte do código faz.
# Este é um comentário
print("Isso será exibido agora o que está comentado não vai aparecer")

''' Erro comum: Aspas duplas sozinhas ("texto") não são comentários, são strings. Para comentários, use # ou aspas triplas """.'''

'''VARIÁVEIS

Variáveis guardam informações que você quer usar no código. Você escolhe o nome e atribui um valor com o sinal =
Exemplo correto:
'''
Nome = "Milena"
idade = 20
altura = 1.50

#  Regras para nomes de variáveis:
#1 Devem começar com letra ou underscore _
#2 Não podem começar com números
#3 Não podem usar palavras reservadas do Python (ex: print, if, for...)

'''Exemplos incorretos:'''
'''1nome = "Milena"   #  começa com número
altura@ = 1.70     #  caractere inválido (@)
def = "função"     #  palavra reservada
'''

