import os 
from dataclasses import dataclass
os.system ("cls||clear")

@dataclass
class Dados:
    salario : float
    filhos : int

def criando_arquivo(a,b):
    with open(a,"a") as arquivo_dados:
        for dado in b:
            arquivo_dados.write(f"{dado.usuario}, {dado.senha}\n")
    arquivo_dados.close()
    print("\n=== Dados Salvos ===\n")

def lendo_arquivo(a):
    list_dados=[]
    with open(a,"r") as arquivo_origem:
        for linha in arquivo_origem:
            usuario, senha = linha.strip().split(",")
            list_dados.append(Dados(usuario=usuario, senha=int(senha)))
    arquivo_origem.close()
    return list_dados