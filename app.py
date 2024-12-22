from classes_main import classes
from utilities import functions
from datetime import datetime

clin1 = classes.Cliente(
    nome_usuario = [""],
)
desp = classes.Despesa(
    nome_usuario=[""],
    custo_tipo = [""],
    custo_data = [datetime.date],
    custo_valor = [0.0],  
)
ren1 = classes.Renda(
    nome_usuario=[""],
    renda_tipo = [" "],
    renda_data = [datetime.date],
    renda_valor = [0.0],
   
)

#Code here!
functions.cadastro_menu()
