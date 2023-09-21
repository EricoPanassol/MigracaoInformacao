# 0: velhinha
# 1: quantas fofocas recebeu
# 2: lista das amigas
# estrutura: [int, int, [int]]

import time
import random
import os


# Leitura dos arquivos do diretorio e seleção do arquivo
# ====================================================================
path = './'  # Substitua pelo caminho do seu diretório-

# Lista todos os arquivos do diretório
files_dir = os.listdir(path)

# Lista apenas arquivos
files = [file for file in files_dir if os.path.isfile(os.path.join(path, file))]

print("Arquivos:\n")
for file in files:
    print(file)
print("\n")

file = input("Digite o nome do arquivo que deseja carregar: ./")
# ====================================================================
 

# Salva as informações dos arquivos em listas para serem manipuladas
# ====================================================================
old_ladies_list = [] # lista inicial das velhinhas
old_ladies_queue = [] # fila das velhinhas que faltam fofocar

with open(file) as f:
    lines = [line.strip() for line in f.readlines()]
    for ladie in lines:
        ladies = ladie.split(":")
        numeros = [int(num) for num in ladies[1].split()]
        old_ladies_queue.append(int(ladies[0])) # adiciona as velhinhas com fofocas na fila (todas começam com 0 fofocas)

        # Unir os números adjacentes
        numeros_combinados = []
        i = 0
        while i < len(numeros):
            if i + 1 < len(numeros) and numeros[i] == 1 and numeros[i + 1] == 0:
                numeros_combinados.append(10)  # Combina 1 e 0 em 10
                i += 1
            else:
                numeros_combinados.append(numeros[i])
            i += 1

        # Atualiza a lista original com os números combinados
        old_ladies_list.append([int(ladies[0]), 0, numeros_combinados])
# ====================================================================


# Print de controle para o usuário
# ====================================================================
print("Queue antes:", old_ladies_queue)
print("Lista antes:", old_ladies_list)
print("\n\nVelhinhas com as fofocas e lista de amigas")
# ====================================================================


# Variaveis usadas (probabilidade de esquecer e limitador de tempo)
# ====================================================================
FORGET_PROB = 0.10  # 10%
start_time = time.time()
one_min = 60
# ====================================================================


# Loop que itera sobre todas as velhinhas e contabiliza as fofocas
# ====================================================================
while(len(old_ladies_queue) > 1 and ((time.time() - start_time) < one_min)):
    actualLady = old_ladies_queue.pop(0) - 1

    if random.random() <= 1 - FORGET_PROB: # checa se a velhinha esqueceu de contar
        friends = len(old_ladies_list[actualLady][2])
        probability = 1.0 / friends  # divide igualmente entre as amigas

        gossiped = False # checa se a fofoca ja foi contada

        while not gossiped: # checa se a velhinha ja fofocou
            escolha = random.choice(old_ladies_list[actualLady][2]) # escolhe uma amiga
            if random.random() <= probability: # probabilidade de contar para a amiga escolhida
                old_ladies_queue.append(escolha)
                old_ladies_list[escolha-1][1] += 1
                gossiped = True
    else:
        # print(f"esqueceu de contar: {actualLady+1}")  
        continue
    # print(f"\nvelhinha: {actualLady+1} \nfila: {old_ladies_queue}")
    # print(f"probabilidade de escolher qualquer amiga: {probability}")
    # print(f"contou para: {escolha} (+1 nas fofocas {old_ladies_list[escolha-1]})")
    # print(f"Lista das velhinhas: {old_ladies_list}")
# ====================================================================


# Procura a velhinha que recebeu mais fofocas
# ====================================================================
total_gossip = 0
final_lady = 0
 
for old_lady in old_ladies_list:
    print(old_lady)
    bigger = old_lady[1]  
    if bigger > total_gossip:
        total_gossip = bigger
        final_lady = old_lady[0]
# ====================================================================


# Finaliza o programa
# ====================================================================
print(f"\nVelhinha que mais recebeu fofoca foi a {final_lady} e foram {total_gossip}.\n")  
# print(f"Velhinha: {final_lady} \nFofocas: {bigger}")
# ====================================================================





# executa até que a fila de velhinhas acabe ou até que o tempo zere (1min)
# remove a primeira velhinha da fila, 
# while(len(old_ladies_queue) > 1 and ((time.time() - start_time) < one_min)):
#     actualLady = old_ladies_queue.pop(0) - 1 
#     print(f"\nvelhinha: {actualLady+1} \nfila: {old_ladies_queue}")
    
#     if random.random() <=  1 - FORGET_PROB:
#         escolha = random.choice(old_ladies_list[actualLady][2]) # escolhe uma amiga baseado na probabilidade
#         print(f"contou para: {escolha}")
#         old_ladies_queue.append(escolha)
#         old_ladies_list[escolha-1][1] += 1 # contador de fofocas da velhinha escolhida
#         print(f"veia escolhida {escolha} aumenta 1 no contador de fofocas: {old_ladies_list[escolha-1]}")
#     else:
#         print(f"esqueceu de contar: {actualLady+1}")
#         continue