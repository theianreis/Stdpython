#%%
# Arrays e Linked Lists

## Definição Geral

**Arrays** e **Linked Lists** são estruturas de dados fundamentais usadas para armazenar **coleções de elementos**.  
A principal diferença entre elas está na **forma como os dados são organizados na memória**.

Essa diferença estrutural determina:
- eficiência de acesso
- custo de inserção e remoção
- uso de memória
- adequação ao problema

---

## Arrays

### Definição

Um **Array** armazena elementos em **posições contíguas de memória**.

Isso significa que:
- todos os elementos estão lado a lado
- o endereço de qualquer elemento pode ser calculado diretamente

---

### Modelo de Memória

Se o primeiro elemento está no endereço $$A_0$$, então o elemento de índice $$i$$ está em:

$$
A_i = A_0 + i \cdot s
$$

onde $$s$$ é o tamanho do tipo de dado.

---

### Consequência Direta

- **Acesso direto** em tempo constante:
  
$$
O(1)
$$

```python
array = [10, 20, 30, 40]
print(array[2])  # acesso direto
```

---

# HashMaps (Tabelas Hash)

## Definição

**HashMap**, **HashTable**, **Map**, **Dictionary** ou **Associative Array** são nomes diferentes para a **mesma estrutura de dados**.

Formalmente:
> Uma HashMap é uma estrutura de dados que implementa o **Abstract Data Type (ADT) Map**,  
> isto é, uma estrutura que **mapeia chaves (keys) para valores (values)**.

---

## Modelo Abstrato

O comportamento lógico de uma HashMap pode ser descrito como uma função:

$$
M : K \rightarrow V
$$

onde:
- $$K$$ é o conjunto de chaves
- $$V$$ é o conjunto de valores
- cada chave é **única**

---

## Operações Fundamentais

Uma HashMap suporta, conceitualmente:

- Inserção: `put(k, v)`
- Busca: `get(k)`
- Remoção: `remove(k)`

Com complexidade média:

$$
O(1)
$$

---

## Ideia Central: Função Hash

Uma **função hash** transforma uma chave em um índice:

$$
h : K \rightarrow \{0, 1, \dots, n-1\}
$$

Esse índice indica onde o valor será armazenado internamente.

---

## Estrutura Interna (Visão Simplificada)

Internamente, uma HashMap usa:
- um **array**
- associado a uma função hash

```text
índice → [ (chave, valor) ]
```

# Stacks, Queues e Heaps

Essas três estruturas de dados controlam **a ordem de acesso aos elementos**, cada uma com uma política diferente.  
Elas são fundamentais para algoritmos, sistemas operacionais, compiladores e arquiteturas de software.

---

## Stack (Pilha)

### Definição

Uma **Stack** é uma estrutura de dados que opera segundo o princípio **LIFO** (*Last In, First Out*).

> O último elemento inserido é o primeiro a ser removido.

---

### Operações Fundamentais

- `push(x)` → insere um elemento
- `pop()` → remove o elemento do topo
- `peek()` → consulta o topo

---

### Modelo Conceitual

$$
x_1 \rightarrow x_2 \rightarrow x_3
$$

Se $$x_3$$ foi o último a entrar, então:

$$
\text{pop}(S) = x_3
$$

---

### Implementação

Uma stack pode ser implementada com:
- **array**
- **linked list**

Exemplo em Python:

```python
stack = []

stack.append(1)   # push
stack.append(2)
stack.append(3)

topo = stack.pop()  # pop
```
---
# Sorting Algorithms (Algoritmos de Ordenação)

## Definição

**Sorting** é o processo de **organizar dados** segundo uma determinada **ordem**.

Um **Sorting Algorithm** especifica:
- como os elementos devem ser comparados
- como devem ser rearranjados
- qual política de ordenação é aplicada

As ordens mais comuns são:
- **numérica**
- **lexicográfica**

---

## Modelo Abstrato

Dado um conjunto de dados:

$$
A = \{a_1, a_2, \dots, a_n\}
$$

um algoritmo de ordenação produz:

$$
A' = \{a_{\pi(1)}, a_{\pi(2)}, \dots, a_{\pi(n)}\}
$$

tal que:

$$
a_{\pi(1)} \le a_{\pi(2)} \le \dots \le a_{\pi(n)}
$$

onde $$\pi$$ é uma **permutação** dos índices.

---

## Importância da Ordenação

A ordenação é crucial porque:

- melhora a eficiência de buscas
- reduz complexidade computacional
- organiza dados para processamento posterior
- é base para muitos algoritmos avançados

---

## Relação com Algoritmos de Busca

Quando os dados estão ordenados, algoritmos como **Binary Search** passam de:

$$
O(n) \rightarrow O(\log n)
$$

Isso representa um ganho **exponencial** de eficiência.

---

## Classificação dos Algoritmos de Ordenação

### 1. Por Complexidade

- **Quadráticos:** $$O(n^2)$$
- **Logarítmicos:** $$O(n \log n)$$
- **Lineares (casos específicos):** $$O(n)$$

---

### 2. Por Uso de Memória

- **In-place:** usam memória constante
- **Out-of-place:** usam memória adicional

---

### 3. Por Estabilidade

- **Estáveis:** mantêm a ordem relativa de elementos iguais
- **Não estáveis:** podem alterar essa ordem

---

## Algoritmos Mais Comuns

### Bubble Sort

- Complexidade: $$O(n^2)$$
- Estável
- Didático

---

### Insertion Sort

- Complexidade: $$O(n^2)$$
- Muito eficiente para listas pequenas
- Estável

---

### Selection Sort

- Complexidade: $$O(n^2)$$
- Não estável
- Poucas trocas

---

### Merge Sort

- Complexidade: $$O(n \log n)$$
- Estável
- Usa memória extra

---

### Quick Sort

- Complexidade média: $$O(n \log n)$$
- Pior caso: $$O(n^2)$$
- In-place
- Muito rápido na prática

---

### Heap Sort

- Complexidade: $$O(n \log n)$$
- Não estável
- Baseado em Heap

---

## Tabela Comparativa

| Algoritmo | Tempo Médio | Estável | Memória |
|---------|------------|--------|--------|
| Bubble | $$O(n^2)$$ | Sim | $$O(1)$$ |
| Insertion | $$O(n^2)$$ | Sim | $$O(1)$$ |
| Selection | $$O(n^2)$$ | Não | $$O(1)$$ |
| Merge | $$O(n \log n)$$ | Sim | $$O(n)$$ |
| Quick | $$O(n \log n)$$ | Não | $$O(\log n)$$ |
| Heap | $$O(n \log n)$$ | Não | $$O(1)$$ |

---

## Ordenação como Transformação Estrutural

Ordenar é impor uma **relação de ordem total**:

$$
\le : A \times A \rightarrow \{0,1\}
$$

Isso transforma um conjunto não estruturado em um conjunto **navegável e pesquisável**.

---

## Quando Ordenar

- Antes de buscas frequentes
- Para análise estatística
- Para deduplicação
- Para visualização de dados
- Para algoritmos dependentes de ordem

---

## Conclusão

Sorting Algorithms são:
- fundamentais na ciência da computação
- essenciais para eficiência algorítmica
- base para buscas, índices e sistemas

> **Ordenar dados não é um fim — é um acelerador de tudo que vem depois**
---
