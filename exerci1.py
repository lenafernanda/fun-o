# For loop simples: Crie um loop que percorra os números de 1 a 10.
""" 
numero = 0

contagem < 10:
numero += 1
for numero in range:
    print({numero})

"""
'''Codigo correto a baixo'''
numero = 0

for numero in range(1,11):
    print({numero})
print('\n')
# range é uma função que gera uma sequência de números, sem os guardar todos na memória
'''usar range() sempre que precisares de:
Repetir algo um certo número de vezes
Iterar por uma sequência de números
Contar em ordem crescente ou decrescente'''

# ==============================================
'''2. Loop While: Crie um loop que mostre os números de 10 a 1.'''
print('\n')

contador = 10  #Começa do número certo
while contador >=1: # "Enquanto o valor do contador for maior ou igual a 1
    print(contador)
    contador -=1 # se não diminuir o contador, ele fica preso em 10 para sempre

print('\n')
'''3. Operações em listas: Crie uma lista de números e use um loop para somar todos os elementos.'''
soma = [2,2,2,2] # listas do numero que vou somar
total = 0       # criar uma variavel chamada 'total' que começa do zero pra guardar a soma
for resultado in soma:
    total = total + resultado # Adiciona o valor de 'resultado' (cada número da lista) ao 'total'
    print(total)

# 4. List Comprehension: Crie uma nova lista que contém os quadrados dos números de 1 a 5.
quadrado = [x**2 for x in  range(1, 6)]
    #           for x in range(1, 6)  um laço de repetição (for) dentro da lista.
print(quadrado)

# 5. Identificando pares: Crie um loop que imprima apenas os números pares de uma lista fornecida.
numero = [1,2,3,4,5,6,7,8,9,10]
for lista in numero:
    if lista %2 == 0:
        print(f'numeros pares:{lista}')

# 7. Loop aninhado — Tabuada
numero = int(input('me diga um numero de 1 a 10 para a tabuada:'))
for i  in  range(1, 11): 
    print(f'{numero} x {i} = {numero*i}')