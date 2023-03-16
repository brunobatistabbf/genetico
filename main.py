import random

# alfabeto e a frase alvo
alfabeto = "abcdefghijklmnopqrstuvwxyz "
alvo = "ciencia da computacao"

# Tamanho da população e número máximo de gerações
tam_pop = 200
max_geracoes = 1000


def fitness(individuo):
    #Função de avaliação.
    return sum(1 for a, b in zip(individuo, alvo) if a == b)

# Cria uma população de indivíduos aleatórios
populacao = [''.join(random.choice(alfabeto) for _ in range(len(alvo))) for _ in range(tam_pop)]

for geracao in range(max_geracoes):

    # Avalia cada indivíduo e ordena por fitness
    avaliacoes = [(individuo, fitness(individuo)) for individuo in populacao]
    avaliacoes.sort(key=lambda x: x[1], reverse=True)

    # Se um indivíduo atinge a solução, termina a execução
    if avaliacoes[0][0] == alvo:
        print(f"Melhor solução encontrada na geração {geracao}: {avaliacoes[0][0]}")
        break

    # Seleciona os pais para a próxima geração
    pais = [avaliacoes[i][0] for i in range(tam_pop // 2)]

    # Cria novos indivíduos através do cruzamento de dois pais aleatórios
    filhos = []
    for i in range(tam_pop - len(pais)):
        pai = random.choice(pais)
        mae = random.choice(pais)
        ponto_corte = random.randint(1, len(alvo) - 1)
        filho = pai[:ponto_corte] + mae[ponto_corte:]
        filhos.append(filho)

    # Realiza uma mutação aleatória  em alguns filhos
    for i in range(len(filhos)):
        if random.random() < 0.01:
            filho = list(filhos[i])
            filho[random.randint(0, len(alvo) - 1)] = random.choice(alfabeto)
            filhos[i] = ''.join(filho)

    populacao = pais + filhos
    print(populacao)



