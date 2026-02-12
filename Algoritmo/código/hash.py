def funcao_hash(chave,tamanho):
    return hash(chave)%tamanho

class Tabelahash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def inserir(self, chave, valor):
        indice = funcao_hash(chave, self.tamanho)
        self.tabela[indice].append((chave, valor))

    def buscar(self, chave):
        indice = funcao_hash(chave, self.tamanho)
        for k, v in self.tabela[indice]:
            if k == chave:
                return v
        return None

th = Tabelahash()

th.inserir("massa", 5.50)
th.inserir("arroz", 4.20)

print(th.buscar("massa"))