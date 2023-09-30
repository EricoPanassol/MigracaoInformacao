import numpy as np
from collections import defaultdict

# +***************************************+
# |     Author: Érico Riess Panazzolo     |
# |     Registration: 212012290-8         |
# |     Date: 09/20/2023 - 10/02/2023     |
# +***************************************+


# Seleção do arquivo
# ====================================================================
file = input("Digite o nome do arquivo que deseja carregar: ./")
 

# Salva as informações dos arquivos em listas para serem manipuladas
# ====================================================================
old_ladies_list = [] # lista inicial das velhinhas

with open(file) as f:
    lines = [line.strip() for line in f.readlines()]
    for ladie in lines:
        ladies = ladie.split(":")
        numeros = [int(num) for num in ladies[1].split()]

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
        old_ladies_list.append([int(ladies[0]), numeros_combinados])
    
    
# Salva as informações das probabilidades de cada velhinha
# ====================================================================
probs = []    
for lady in old_ladies_list:
    friends = lady[1]
    prob = (1 / len(friends))  * 0.9
    # print(f"Velha: {lady[0]}\nAmigas: {lady[1]}\nProbabilidade: {prob}\n")
    probs.append([friends, prob, lady[0]])


# Cria uma lista com probabilidades de contar para cada uma
# ====================================================================
equation = []
for lady in probs:
    for amiga in lady[0]:
        equation.append([lady[2], lady[1], amiga])
    

# Dict para agrupar as probabilidades
# ====================================================================
agrupadas = defaultdict(list)

for item in equation:
    chave = item[2] 
    probabilidade = item[1]
    velhinha_origem = item[0]  
    agrupadas[chave].append([velhinha_origem, probabilidade])

lista_agrupada = [[chave, probabilidades] for chave, probabilidades in agrupadas.items()]


# Cria a matriz das probabilidades com a diagonal toda -1
# ====================================================================
num_velhinhas = max([item[0] for item in lista_agrupada])
prob_matrix = np.eye(num_velhinhas) * (-1)


# Monta a matriz com as probabilidades
# ====================================================================
for item in lista_agrupada:
    velhinha_destino = item[0]
    probabilidades = item[1]
    
    for prob in probabilidades:
        velhinha_origem = prob[0]
        probabilidade = prob[1]
        
        if velhinha_destino != velhinha_origem:
            prob_matrix[velhinha_destino - 1, velhinha_origem - 1] = probabilidade


# Método de Gauss para resolver o sistema
# ====================================================================
def gauss_elimination(matrix, b):
    n = matrix.shape[0]
    augmented_matrix = np.hstack((matrix, b.reshape(-1, 1)))

    for i in range(n):
        pivot_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]
        pivot = augmented_matrix[i, i]
        augmented_matrix[i] /= pivot
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i]
            augmented_matrix[j] -= factor * augmented_matrix[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:-1], x[i+1:])

    return x


# Resolve o sistema
# ====================================================================
b = -np.ones(num_velhinhas) # vetor b com todos os valores -1 para multiplicar a matriz
gossips = gauss_elimination(prob_matrix, b)


# Printa todas as velhinhas com suas fofocas
# ====================================================================
# for i, gossip_count in enumerate(gossips, 1):
#     print(f"Velhinha {i} recebeu {gossip_count:.6f} fofocas.")


# Encontra a velhinha que mais recebeu fofoca
# ====================================================================
most_gossiped_lady = np.argmax(gossips) + 1
most_gossips = gossips[most_gossiped_lady - 1]
print(f"Velhinha {most_gossiped_lady} recebeu a maior quantidade de fofocas: {most_gossips:.6f}")