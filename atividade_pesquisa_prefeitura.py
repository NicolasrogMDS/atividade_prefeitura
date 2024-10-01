"""
Turma - 93313

Nome completo dos componentes:
1 - Nicolas Roger Araujo Monteiro da Silva
2 - Leonardo Machado
"""

import os 
os.system ("cls||clear")
from dataclasses import dataclass

@dataclass
class Familia:
    salario : float
    filho : int

def limpar_terminal():
    os.system("cls || clear")

def calcular_media(a):
    quantidade = len(a)
    if quantidade == 0:
        return 0
    else:
        soma = sum(a)
        media = soma / quantidade
        return media

def criando_arquivo(a,b):
    with open(a,"a") as arquivo_dados:
        for familia in b:
            arquivo_dados.write(f"{familia.salario}, {familia.filho}\n")
    arquivo_dados.close()
    print("\n=== Dados Salvos ===\n")

def lendo_arquivo(a):
    list_dados=[]
    with open(a,"r") as arquivo_origem:
        for linha in arquivo_origem:
            salario, filho = linha.strip().split(",")
            list_dados.append(Familia(salario=float(salario), filho=int(filho)))
    arquivo_origem.close()
    return list_dados

while True:
    print("""
    Código | Descrição
    1    |  Adicionar família
    2    |  Exibir resultados
    3    |  Sair
    """)
    opcao = int(input("\nInsira a opção desejada:  "))
    match (opcao):
        case 1:
            lista_familia = []
            familia = Familia(
            salario = float(input("Digite o salário total da família: ")),
            filho = int(input("Informe a quantidade de filhos: "))
            )
            lista_familia.append(familia)
            nome_arquivo = "pesquisa_prefeitura.txt"
            criando_arquivo(nome_arquivo,lista_familia)
            limpar_terminal()
        case 2:
            lista_familia = []
            nome_arquivo = "pesquisa_prefeitura.txt"
            lista_salario=[]
            lista_filhos = []
            lista_familia = lendo_arquivo(nome_arquivo)
            numero_familias = 0

            for familia in (lista_familia):
                numero_familias += 1
                lista_filhos.append(familia.filho)
                lista_salario.append(familia.salario)

            media_filhos = calcular_media(lista_filhos)
            media_salario = calcular_media(lista_salario)
            max_salario=max(lista_salario)
            min_salario=min(lista_salario)

            limpar_terminal()
            print(f"Media de filhos da população: {media_filhos:.2f}")
            print(f"Media salarial da população: {media_salario:.2f}")
            print(f"Maior salário da população: {max_salario:.2f}")
            print(f"Menor salário da população: {min_salario:.2f}")
            print(f"Número de famílias da população: {numero_familias}")

        case 3:
            break

        case _:
            print("Opção inválida. Por favor, tente novamente,")