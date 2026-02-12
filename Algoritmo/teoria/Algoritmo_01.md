# Binary Search

## Definição

A **Binary Search** é um algoritmo de busca que localiza um elemento em uma **lista ordenada**, dividindo repetidamente o espaço de busca pela metade.

Em cada iteração:
- compara-se o elemento central com o valor procurado
- elimina-se metade do espaço de busca

### Complexidade

- **Tempo:** $$O(\log n)$$
- **Espaço:** $$O(1)$$ (versão iterativa)

---

## Por que usar

- Extremamente eficiente para grandes volumes de dados  
- Reduz drasticamente o número de comparações  
- Muito utilizada em estruturas indexadas (bancos de dados, buscas, sistemas)

---

## Como usar

### Pré-requisito fundamental

> **A lista precisa estar ordenada**

```python
def binary_search(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1
```
---

# Decorators

## Definição

Um **Decorator** é um padrão de projeto em Python que permite **modificar ou estender o comportamento de uma função ou método**, **sem alterar o seu código original**.

Formalmente, um decorator é:
> **Uma função que recebe outra função como argumento e retorna uma nova função**

---

## Motivação Conceitual

Em programação, muitas vezes queremos:
- adicionar **logs**
- medir **tempo de execução**
- verificar **permissões**
- validar **entradas**
- contar chamadas de funções

Sem decorators, isso levaria a **código duplicado**.

Decorators resolvem isso aplicando o princípio:
> **Separação de responsabilidades**

---

## Intuição Matemática

Se pensarmos em funções como mapeamentos:

$$
f: X \rightarrow Y
$$

Um decorator é um operador que transforma essa função:

$$
D(f) = f'
$$

Ou seja, ele cria uma **nova função** com comportamento estendido:

$$
f'(x) = g(f(x))
$$

---

## Estrutura Geral de um Decorator

Um decorator possui **três níveis**:

1. Função decorator
2. Função wrapper (envoltório)
3. Execução da função original

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # comportamento antes
        resultado = func(*args, **kwargs)
        # comportamento depois
        return resultado
    return wrapper
```

--- 
# Modules

## Definição

Um **Module** em Python é simplesmente **um arquivo `.py`** que contém:
- funções
- classes
- variáveis
- constantes
- código executável

Formalmente:
> **Um módulo é uma unidade de organização e encapsulamento de código**

---

## Motivação Conceitual

À medida que um sistema cresce, surgem problemas clássicos:
- arquivos muito grandes
- código difícil de manter
- reutilização limitada
- alto acoplamento

Modules resolvem isso aplicando:
- **Modularização**
- **Separação de responsabilidades**
- **Organização lógica do sistema**

---

## Intuição Matemática / Estrutural

Pense em um sistema como um conjunto:

$$
S = \{M_1, M_2, M_3, \dots, M_n\}
$$

Onde cada módulo representa um subconjunto funcional:

$$
M_i = \{f_1, f_2, c_1, v_1\}
$$

O sistema emerge da **composição dos módulos**, não de um único bloco monolítico.

---

## Criando um Módulo

### Arquivo: `operacoes.py`

```python
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

PI = 3.14159
```

---

# Bubble Sort (Ordenação por Bolha)

## Definição

O **Bubble Sort** é um algoritmo de ordenação simples que organiza os elementos de uma lista através de **comparações sucessivas entre pares adjacentes**, trocando-os de posição quando estão fora de ordem.

A cada iteração completa:
- o maior elemento “borbulha” para o final da lista

---

## Ideia Intuitiva

Dada uma lista:

$$
[5, 3, 8, 4]
$$

O algoritmo compara:
- 5 e 3 → troca
- 5 e 8 → não troca
- 8 e 4 → troca

Após uma passagem:

$$
[3, 5, 4, 8]
$$

O maior valor já está corretamente posicionado.

---

## Funcionamento Geral

O algoritmo executa:
- múltiplas **passagens** pela lista
- em cada passagem, compara elementos adjacentes
- reduz o espaço de busca a cada iteração

---

## Pseudocódigo

```text
para i de 0 até n-1:
    para j de 0 até n-i-2:
        se lista[j] > lista[j+1]:
            trocar(lista[j], lista[j+1])
