# Eduardo Bambulim - RM 573228
# Flavio Junior Carvalho Silva - RM 571924 (REPRESENTANTE)

# listas para guardar as informacoes
tipos = []
paises = []
regioes = []
cidades = []
areas = []
intensidades = []
ocorrencias = []

# pede a quantidade total de eventos
while True:
    try:
        qtd = int(input("Insira a quantidade de eventos: "))
        if qtd > 0:
            break
        print("A quantidade de eventos deve ser maior que zero!")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")

# loop para preencher os dados de cada evento
for i in range(qtd):
    print(f"\n--- Evento {i + 1} ---")
    
    # valida se o tipo nao esta vazio
    while True:
        tipo = input("Tipo: ").strip()
        if len(tipo) > 0:
            break
        print("O tipo do evento não pode ser vazio!")
        
    # valida o pais
    while True:
        pais = input("País: ").strip()
        if pais != "":
            break
        print("O país não pode ser vazio!")
        
    # valida a regiao
    while True:
        regiao = input("Região: ").strip()
        if regiao:
            break
        print("A região não pode ser vazia!")
        
    # valida a cidade
    while True:
        cidade = input("Cidade: ").strip()
        if len(cidade) > 0:
            break
        print("A cidade não pode ser vazia!")
        
    # valida a area (tem que ser maior que 0)
    while True:
        try:
            area = float(input("Área: "))
            if area <= 0:
                print("A área deve ser maior que zero!")
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido para a área.")
            
    # valida intensidade (de 1 ate 10)
    while True:
        try:
            intensidade = int(input("Intensidade: "))
            if intensidade < 1 or intensidade > 10:
                print("A intensidade deve estar entre 1 e 10!")
            else:
                break
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro para a intensidade.")
            
    # valida quantidade de ocorrencias (minimo 1)
    while True:
        try:
            ocorrencia = int(input("Ocorrências: "))
            if ocorrencia >= 1:
                break
            print("O número de ocorrências deve ser pelo menos 1!")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro para as ocorrências.")

    # adiciona tudo nas listas
    tipos.append(tipo)
    paises.append(pais)
    regioes.append(regiao)
    cidades.append(cidade)
    areas.append(area)
    intensidades.append(intensidade)
    ocorrencias.append(ocorrencia)

# comeca a fazer as analises
total = len(tipos)

# a. soma total de todas as areas
soma_areas = 0
for a in areas:
    soma_areas += a

# b. calcula a media de intensidade
soma_int = 0
for val in intensidades:
    soma_int += val

if total > 0:
    media_int = soma_int / total
else:
    media_int = 0.0

# c. acha a regiao com maior quantidade de ocorrencias
regs_unicas = []
ocor_reg = []

for i in range(total):
    reg = regioes[i]
    oco = ocorrencias[i]
    if reg not in regs_unicas:
        regs_unicas.append(reg)
        ocor_reg.append(oco)
    else:
        pos = regs_unicas.index(reg)
        ocor_reg[pos] += oco

# pega a regiao com mais ocorrencias usando max e index
max_oco = max(ocor_reg)
idx_max = ocor_reg.index(max_oco)
reg_mais_ocorr = regs_unicas[idx_max]

# d. densidade media de ocorrencias (ocorrencias / area)
total_oc = 0
for o in ocorrencias:
    total_oc += o

if soma_areas > 0:
    densidade = total_oc / soma_areas
else:
    densidade = 0.0

# e. quantidade de eventos com intensidade acima da media
acima_media = 0
for x in intensidades:
    if x > media_int:
        acima_media += 1

# f. acha o evento mais critico (desempata por area se intensidade for igual)
pos_critico = 0
for i in range(1, total):
    if intensidades[i] > intensidades[pos_critico]:
        pos_critico = i
    elif intensidades[i] == intensidades[pos_critico] and areas[i] > areas[pos_critico]:
        pos_critico = i

# tira o decimal se for numero inteiro (para o print ficar igual ao exemplo)
soma_areas_str = str(int(soma_areas)) if soma_areas == int(soma_areas) else str(soma_areas)

area_crit = areas[pos_critico]
area_critica_str = str(int(area_crit)) if area_crit == int(area_crit) else str(area_crit)

# imprime o relatorio final bonitinho
print()
print("========================================")
print("        RELATÓRIO DE ANÁLISE")
print("========================================")
print()
print(f"Total de eventos registrados: {total}")
print()
print("----------------------------------------")
print("Resumo Geral")
print("----------------------------------------")
print(f"Área total afetada: {soma_areas_str} km²")
print(f"Média de intensidade: {media_int:.1f}")
print()
print("----------------------------------------")
print("Análises")
print("----------------------------------------")
print(f"Região com maior número de ocorrências: {reg_mais_ocorr}")
print(f"Quantidade de eventos acima da média de intensidade: {acima_media}")
print(f"Densidade média de ocorrências: {densidade:.2f} ocorrências/km²")
print()
print("----------------------------------------")
print("Evento Mais Crítico")
print("----------------------------------------")
print(f"Tipo: {tipos[pos_critico]}")
print(f"Local: {cidades[pos_critico]}, {regioes[pos_critico]}, {paises[pos_critico]}")
print(f"Intensidade: {intensidades[pos_critico]}")
print(f"Área afetada: {area_critica_str} km²")
print()
print("========================================")
print(f"Total de desastres registrados: {total}")
