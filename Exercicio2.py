'''Elabore um algoritmo com implementação em Python que leia respostas para uma enquete 
até que uma condição de parada seja informada. 
Ao final, deverão ser apresentados o total de participantes na enquete 
e o percentual de votos recebidos para cada opção de resposta. 
O programa deverá permitir configurar o tema da enquete e as opções de resposta 
através de um arquivo de configuração (hard coded) a ser importado ou de forma interativa no início da execução.'''

# bibliotecas padrão
import os
import json

# constantes
CONFIG = 'config.json'

# dicionario vazio (padrão)
enquete = {
    '1 - Qual a Sua liguagem preferida?':{
        '1 - Python': 0,
        '2 - C#': 0,
        '3 - Java': 0,
        '4 - C++': 0,
        '5 - Ruby': 0,
        '0 - Nenhuma das Três': 0
    },
    '2 - Qual marca de Celular vc prefere?': {
        '1 - iPhone': 0,
        '2 - Samsung': 0,
        '3 - Motorola': 0,
        '4 - Xiaomi': 0,
        '5 - Sony': 0,
        '0 - Nenhuma das Três': 0,
    }
}

# chamada pra escolher a enquete
def escolher_enquete():
    print("----------------------------------------------------")
    print("Qual enquete vc quer escolher?")
    for x in enquete.keys():
        print(x)
    print("----------------------------------------------------")
    res = input("Opção: [q para Sair] ")

    if res == 'q':
        quit()

    for x in enquete.keys():
        if res in str(x).split(' - ')[0]:
            return x

# chamada que salva o dicionário em um arquivo JSON
def salvar_JSON():
    with open(CONFIG, 'w') as arq:
        json.dump(enquete, arq, indent=4)

    print(f"Enquete salva em {CONFIG}")

# chamada que carrega o dicionário a partir do arquivo JSON
def carregar_JSON():
    try:
        with open(CONFIG, 'r') as arq:
            return json.load(arq)
    except FileNotFoundError:
        input("Arquivo não criado. Será carregado um dicionario vazio")
        return enquete

# chamada que desenha o menu carregado a partir de um dicionario
def menu(_enquete):
    soma = total(_enquete)
    for key, value in enquete.items():
        if _enquete in key:
            print(f"Enquete: {key}")
            print(f"Respostas: {soma}")
            print("----------------------------------------------------")
            for j in value:
                print(j)
            print("----------------------------------------------------")

# chamada somatória
def total(_enquete):
    soma = 0

    for key, value in enquete.items():
        if _enquete in key:
            for j in value:    
                soma += value[j]

    return soma

# chamada que mostra resultados
def mostrar_resultados(_enquete):
    soma = total(_enquete)
    print("----------------------------------------------------")
    print("Resumo da enquete")
    print(f"{_enquete}")
    print("----------------------------------------------------")
    for key, value in enquete.items():
        if _enquete in key:
            for j in value:    
                valor = value[j]
                print(f"{j}: {valor} respostas. Percentual de {float((valor/soma) * 100):.2f} %")

    print("----------------------------------------------------")
    print(f"Total de Participantes: {soma}")
    print("----------------------------------------------------")

# chamada principal
def main():
    op = escolher_enquete()
    while True:
        os.system("cls" if os.name == 'nt' else "clear")
        menu(op)
            
        res = input("Resposta: [q para sair] ").strip()

        # sai do programa
        if res == 'q':
            break

        # resposta deve ser menor que o tamanho do dicionario
        if int(res) > (len(enquete[op]) - 1):
            input("Opção Incorreta")
        else:
        # laço para achar a resposta
            for key, value in enquete.items():
                if op in key:
                    for j in value:
                        if res in str(j).split(' - ')[0]:
                            enquete[op][j] += 1

    mostrar_resultados(op)
    salvar_JSON()
    print("Fim do Programa")

if __name__ == "__main__":
    enquete = carregar_JSON()
    main()
