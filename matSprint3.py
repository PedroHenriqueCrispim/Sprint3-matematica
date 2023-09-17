#Função de tempo de resposta (exemplo fictício)
def tempo_resposta(posicao):
    return posicao**2 - 10*posicao + 25 #(pode ser alterado)

#Encontrando o mínimo (onde o tempo de resposta é minimizado)
def encontrar_minimo():
    minimo = float('inf')
    posicao_minima = None

    for posicao in range(101):
        tempo = tempo_resposta(posicao)
        if tempo < minimo:
            minimo = tempo
            posicao_minima = posicao

    return posicao_minima, minimo

#Função de precificação
def calcula_preco_mensal(qtd_escolas):
    custo_fixo = 1000  #Custo fixo mensal(pode ser alterado)
    custo_variavel = 200  #Custo variável por escola(pode ser alterado)
    preco = custo_fixo + custo_variavel * qtd_escolas
    return preco

#Simulação de precificação
melhor_lucro = 0
melhor_qtd_escolas = 0

for qtd_escolas in range(1, 101):
    preco = calcula_preco_mensal(qtd_escolas) #Calcula o preço mensal
    lucro = qtd_escolas * (10000 - preco)  #Calcula o lucro com base no preço e no lucro por escola

    if lucro > melhor_lucro:
        melhor_lucro = lucro
        melhor_qtd_escolas = qtd_escolas

posicao_minima, tempo_minimo = encontrar_minimo()

print(f"Posição da maçaneta para tempo mínimo: {posicao_minima}")
print(f"Tempo mínimo de resposta: {tempo_minimo}")
print(f"Para obter o maior lucro, a empresa deve ter {melhor_qtd_escolas} escolas aderentes.")
print(f"Lucro máximo: ${melhor_lucro}")
