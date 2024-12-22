from dataclasses import dataclass
import datetime

@dataclass
class Cliente:
    nome_usuario: str
@dataclass
class Despesa(Cliente):
    custo_tipo : str 
    custo_data : datetime.date 
    custo_valor : float 
    
@dataclass
class Renda(Cliente):
    renda_tipo : str 
    renda_data : datetime.date 
    renda_valor : float
    








    




    
