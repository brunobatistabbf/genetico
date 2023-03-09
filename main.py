import random

# Define o alfabeto e a frase alvo
alfabeto = "abcdefghijklmnopqrstuvwxyz "
alvo = "ciencia da computacao"

# Define o tamanho da população e número máximo de gerações
tam_pop = 200
max_geracoes = 2000


# Define a função de fitness
def fitness(individuo):
    return sum(1 for a, b in zip(individuo, alvo) if a == b)


# Gera a população inicial
populacao = [''.join(random.choice(alfabeto) for _ in range(len(alvo))) for _ in range(tam_pop)]

# Evolui a população por um número máximo de gerações
for geracao in range(max_geracoes):
    # Avalia o fitness de cada indivíduo
    avaliacoes = [(individuo, fitness(individuo)) for individuo in populacao]

    # Ordena a população pelo fitness, do maior para o menor
    avaliacoes.sort(key=lambda x: x[1], reverse=True)

    # Verifica se a frase alvo foi encontrada
    if avaliacoes[0][0] == alvo:
        print(f"Encontrado na geração {geracao}")
        break

    # Seleciona os indivíduos mais aptos para reprodução
    pais = [avaliacoes[i][0] for i in range(tam_pop // 2)]

    # Realiza o crossover para gerar novos indivíduos
    filhos = []
    for i in range(tam_pop - len(pais)):
        pai = random.choice(pais)
        mae = random.choice(pais)
        ponto_corte = random.randint(1, len(alvo) - 1)
        filho = pai[:ponto_corte] + mae[ponto_corte:]
        filhos.append(filho)
        print(filho)


    # Mutação em uma taxa de 5%
    for i in range(len(filhos)):
        if random.random() < 0.01:
            filho = list(filhos[i])
            filho[random.randint(0, len(alvo) - 1)] = random.choice(alfabeto)
            filhos[i] = ''.join(filho)


    # Nova população é a união dos pais com os filhos
    populacao = pais + filhos



