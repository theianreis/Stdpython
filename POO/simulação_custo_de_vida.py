from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Item:
    nome: str
    categoria: str
    preco: float
    quantidade: float = 1.0

    def custo(self) -> float:
        return self.preco * self.quantidade

    def aplicar_variacao_percentual(self, pct: float) -> None:
        self.preco *= (1.0 + pct)


class Cesta:
    def __init__(self, itens: List[Item]):
        self.itens = itens

    def total(self) -> float:
        return sum(i.custo() for i in self.itens)

    def por_categoria(self) -> Dict[str, float]:
        d: Dict[str, float] = {}
        for i in self.itens:
            d[i.categoria] = d.get(i.categoria, 0.0) + i.custo()
        return d

    def aplicar_inflacao(self, inflacao_por_categoria: Dict[str, float]) -> None:
        for i in self.itens:
            i.aplicar_variacao_percentual(inflacao_por_categoria.get(i.categoria, 0.0))


@dataclass
class Evento:
    mes: int
    variacao_pct: float  # decimal
    categoria: Optional[str] = None
    nome_item: Optional[str] = None

    def aplica(self, item: Item) -> bool:
        if self.nome_item is not None:
            return item.nome == self.nome_item
        if self.categoria is not None:
            return item.categoria == self.categoria
        return False


class ModeloInflacao:
    def __init__(self, inflacao_mensal_por_categoria: Dict[str, float]):
        self.inflacao = inflacao_mensal_por_categoria

    def taxa_no_mes(self, mes: int) -> Dict[str, float]:
        return dict(self.inflacao)

class SimuladorCustoDeVida:
    def __init__(
        self,
        cesta: Cesta,
        modelo_inflacao: ModeloInflacao,
        eventos: List[Evento],
        salario_mensal: float = 0.0,
        saldo_inicial: float = 0.0,
    ):
        self.cesta = cesta
        self.modelo = modelo_inflacao
        self.eventos = eventos
        self.salario = salario_mensal
        self.saldo = saldo_inicial

        self.eventos_por_mes: Dict[int, List[Evento]] = {}
        for e in eventos:
            self.eventos_por_mes.setdefault(e.mes, []).append(e)

    def rodar(self, meses: int) -> List[Dict]:
        resultados: List[Dict] = []

        for mes in range(1, meses + 1):
            infl = self.modelo.taxa_no_mes(mes)
            self.cesta.aplicar_inflacao(infl)

            for e in self.eventos_por_mes.get(mes, []):
                for item in self.cesta.itens:
                    if e.aplica(item):
                        item.aplicar_variacao_percentual(e.variacao_pct)

            total = self.cesta.total()
            self.saldo += (self.salario - total)

            resultados.append({
                "mes": mes,
                "custo_total": total,
                "custo_por_categoria": self.cesta.por_categoria(),
                "salario": self.salario,
                "saldo_acumulado": self.saldo,
            })

        return resultados

if __name__ == "__main__":
    cesta = Cesta([

        Item("Arroz", "Alimentos", 8.00, 4),
        Item("Feijão", "Alimentos", 9.50, 4),
        Item("Frango", "Alimentos", 18.00, 6),

        Item("Gasolina", "Transporte", 6.00, 80),

        Item("Aluguel", "Moradia", 1200.00, 1),
        Item("Energia", "Moradia", 180.00, 1),
        Item("Internet", "Moradia", 110.00, 1),

        Item("Farmácia", "Saúde", 120.00, 1),

        Item("Streaming", "Lazer", 55.00, 1),
    ])

    inflacao = ModeloInflacao({
        "Alimentos": 0.015,
        "Transporte": 0.010,
        "Moradia": 0.008,
        "Saúde": 0.012,
        "Lazer": 0.006,
    })

    eventos = [
        Evento(mes=3, categoria="Transporte", variacao_pct=0.15),
        Evento(mes=12, nome_item="Aluguel", variacao_pct=0.08),
    ]

    simulador = SimuladorCustoDeVida(
        cesta=cesta,
        modelo_inflacao=inflacao,
        eventos=eventos,
        salario_mensal=3500.0,
        saldo_inicial=0.0,
    )

    resultados = simulador.rodar(meses=12)


    for r in resultados:
        mes = r["mes"]
        total = r["custo_total"]
        saldo = r["saldo_acumulado"]
        cats = r["custo_por_categoria"]

        top2 = sorted(cats.items(), key=lambda x: x[1], reverse=True)[:2]
        print(
            f"M{mes:02d} | custo: R$ {total:,.2f} | saldo acumulado: R$ {saldo:,.2f} | "
            f"top: {top2[0][0]}=R$ {top2[0][1]:,.2f}, {top2[1][0]}=R$ {top2[1][1]:,.2f}"
        )
