from dataclasses import dataclass

@dataclass
class Veiculo:
    codigo_veiculo: int
    modelo: str
    ano: int
    cor: str
    preco: float