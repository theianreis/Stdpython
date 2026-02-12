'''
Funções Lambdas: Inicialmente anônimas, mas quando associada as uma
                 var deixam de ser
                - São Ideias para operações simples e unicas
'''

# soma simples
f_soma = lambda x,y:x+y
resultado = f_soma(x=1,y=3)
print(resultado)

# utilização do filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))

# utilização do map
fruits = ['apple', 'banana', 'cherry']
lengths = list(map(lambda x: len(x), fruits))
print(lengths)

