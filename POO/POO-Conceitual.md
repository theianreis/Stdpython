## Conceitos Iniciais de Programação Orientada a Objetos (POO)

### Objeto
Um **objeto** é uma **instância de uma classe** criada em tempo de execução.  
Ele representa uma entidade concreta do sistema e possui identidade própria, estado e comportamento.

---

### Classe
Uma **classe** é um **molde estrutural** que define:
- quais dados um objeto possui
- quais comportamentos esse objeto pode executar

A classe não é executável por si só; ela serve como definição para a criação de objetos.

---

### Atributo
Um **atributo** é uma **variável definida dentro de uma classe** que representa os dados internos de um objeto.

Os atributos armazenam o **estado** do objeto e não devem ser acessados diretamente sem controle.

---

### Método
Um **método** é uma **função definida dentro de uma classe** que descreve o comportamento do objeto.

Os métodos:
- operam sobre os atributos
- implementam regras de negócio
- controlam mudanças de estado

---

### Construtor
O **construtor** é um método especial responsável por:
- criar o objeto
- inicializar seus atributos
- garantir que o objeto seja criado em um estado válido

Ele prepara o objeto para uso imediato após a instanciação.

---

### Getters
**Getters** são métodos de acesso utilizados para **consultar valores de atributos** de forma controlada.

Eles fazem parte da interface pública da classe e ajudam a manter o encapsulamento.

---

### Setters
**Setters** são métodos utilizados para **modificar valores de atributos** de forma controlada.

Eles permitem:
- validação de dados
- aplicação de regras
- proteção do estado interno do objeto

---

### Estado
O **estado** de um objeto corresponde ao **conjunto atual de valores de seus atributos**.

A mudança de estado deve ocorrer exclusivamente por meio de métodos, garantindo previsibilidade e segurança.

---

### Escopo
**Escopo** define a **região do código onde uma variável é visível e acessível**.

O escopo controla:
- tempo de vida da variável
- isolamento de dados
- previsibilidade do comportamento do sistema

---

### Passagem de Parâmetros
A **passagem de parâmetros** descreve a forma como dados ou referências a objetos são transferidos para métodos.

Em POO, essa passagem permite a **interação entre objetos**, viabilizando colaboração entre componentes do sistema.

---

## Tipos de Variáveis em POO

### Variável de Instância
A **variável de instância** pertence a um objeto específico.

Cada objeto possui sua própria cópia dessa variável, que representa parte de seu estado interno.

---

### Variável Local
A **variável local** existe apenas dentro de um método.

Ela é criada durante a execução do método e destruída ao final, não fazendo parte do estado do objeto.

---

## Abstração

### Definição
**Abstração** é o princípio que consiste em **selecionar apenas os aspectos relevantes** de uma entidade e ignorar detalhes desnecessários para o contexto do sistema.

Ela aproxima o código da **forma humana de modelar problemas**, focando no *o que* o objeto faz, não em *como* ele faz.

---

### Semântica
- **Semântica gramatical**: estrutura correta do código
- **Semântica computacional**: significado e comportamento real do código no sistema

A abstração conecta essas duas camadas.

---

## Modificadores de Acesso (Visibilidade)

### Public
Elementos **públicos** podem ser acessados por qualquer parte do sistema.

Usados para definir a interface exposta da classe.

---

### Protected
Elementos **protegidos** podem ser acessados pela própria classe e por suas subclasses.

Utilizados para extensões controladas via herança.

---

### Private
Elementos **privados** só podem ser acessados dentro da própria classe.

Essenciais para proteção do estado interno e encapsulamento.

---

## Encapsulamento

### Definição
**Encapsulamento** é o princípio que protege os dados internos do objeto, permitindo acesso apenas por meio de métodos controlados.

Ele garante:
- integridade dos dados
- redução de acoplamento
- segurança de modificações internas

---

## Relacionamentos entre Classes

### Associação
A **associação** representa uma relação genérica entre classes, onde objetos podem se conhecer ou interagir.

Não implica dependência de ciclo de vida.

---

### Agregação
A **agregação** é uma forma fraca de associação.

Um objeto contém outro, mas o objeto contido pode existir independentemente.

---

### Composição
A **composição** é uma forma forte de associação.

O ciclo de vida do objeto contido depende do objeto que o contém.

---

### Herança
A **herança** permite que uma classe derive de outra, reutilizando atributos e métodos.

Ela estabelece uma relação de especialização, mas deve ser usada com cautela no mercado para evitar acoplamento excessivo.

---

### Dependência
A **dependência** ocorre quando uma classe utiliza outra temporariamente, geralmente como parâmetro ou variável local.

Mudanças na classe dependida podem impactar a classe dependente.

---

## Interface

### Definição
Uma **interface** define um conjunto de métodos que uma classe deve implementar, sem especificar como.

Ela estabelece contratos claros, fundamentais para:
- arquitetura de software
- desacoplamento
- desenvolvimento em equipe
- frameworks e APIs
