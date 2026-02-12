# Regular Expressions (Expressões Regulares)

## Definição

Uma **Regular Expression (Regex)** é uma **sequência de caracteres** que define um **padrão de busca** em um texto.

Formalmente:
> Uma regex descreve um **conjunto de strings** que obedecem a uma determinada regra sintática.

Ela é amplamente usada para:
- busca de padrões (`find`)
- substituição de texto (`find and replace`)
- validação de entrada
- análise léxica
- pré-processamento de dados

---

## Intuição Conceitual

Dado um texto:

$$
T = \text{"email: usuario@email.com"}
$$

Uma regex define **o que queremos reconhecer**, não *como* procurar.

Por exemplo:
- queremos reconhecer **um email**
- queremos extrair **números**
- queremos validar **formatos**

Regex trabalha no nível de **padrões abstratos**, não de caracteres individuais isolados.

---

## Visão Formal (Teoria)

Do ponto de vista teórico, expressões regulares pertencem à **Teoria dos Autômatos**.

Uma regex descreve uma **linguagem regular**:

$$
L \subseteq \Sigma^*
$$

onde:
- $$\Sigma$$ é o alfabeto
- $$\Sigma^*$$ é o conjunto de todas as strings possíveis
- $$L$$ é o subconjunto aceito pela regex

---

## Estrutura Básica de uma Regex

Uma regex é construída a partir de:

- **literais**
- **metacaracteres**
- **quantificadores**
- **classes de caracteres**
- **âncoras**

---

## Caracteres Literais

Correspondem exatamente ao caractere informado:

```text
abc
````


# Iterators (Iteradores)

## Definição

Um **Iterator** é um objeto que contém um **número contável de valores** e permite **percorrer esses valores um por um**, de forma sequencial.

Formalmente em Python:
> Um iterador é um objeto que implementa o **iterator protocol**, isto é, os métodos  
> `__iter__()` e `__next__()`.

---

## Motivação Conceitual

Muitas estruturas de dados:
- listas
- tuplas
- strings
- arquivos
- streams de dados

não precisam ser acessadas de uma vez só.

Iterators resolvem isso permitindo:
- **processamento incremental**
- **uso eficiente de memória**
- **percursos controlados**

---

## Intuição Matemática

Considere um conjunto ordenado finito:

$$
S = \{x_1, x_2, \dots, x_n\}
$$

Um iterador define uma função de avanço:

$$
I(k) = x_k \quad \text{para } k = 1, 2, \dots, n
$$

Quando $$k > n$$, o iterador sinaliza o **fim da sequência**.

---

## Iterator Protocol em Python

Um objeto é um iterador se:

1. Possui o método `__iter__()`
2. Possui o método `__next__()`
3. Lança `StopIteration` ao final

Formalmente:

```python
    
    obj.__iter__()
    obj.__next__()
```

# Variable Scope (Escopo de Variáveis)

## Definição

**Variable Scope** refere-se à **região de um programa** onde uma determinada variável pode ser **acessada** e **modificada**.

O escopo define:
- **visibilidade** da variável
- **tempo de vida** (lifetime)
- onde ela **existe logicamente** no código

> Compreender escopo é essencial para evitar conflitos de nomes e erros lógicos.

---

## Motivação Conceitual

Em programas reais:
- funções reutilizam nomes
- módulos diferentes coexistem
- estados locais e globais se misturam

Sem regras claras de escopo:
- variáveis sobrescrevem outras
- bugs silenciosos aparecem
- o código perde previsibilidade

---

## Intuição Estrutural

Podemos pensar no programa como um conjunto de regiões:

$$
P = \{S_1, S_2, \dots, S_n\}
$$

Cada variável pertence a **uma região específica**:

$$
v \in S_i \quad \text{mas} \quad v \notin S_j
$$

Isso define **onde** a variável é válida.

---

## Tipos de Escopo em Python (Regra LEGB)

Python resolve nomes seguindo a regra **LEGB**:

1. **L**ocal  
2. **E**nclosing  
3. **G**lobal  
4. **B**uilt-in  

---

## Escopo Local

Variáveis definidas **dentro de uma função**.

```python
def func():
    x = 10
    print(x)

func()
# print(x)  # Erro
```




