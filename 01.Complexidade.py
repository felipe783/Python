#Exemplo simplificado de estimativa parametrica em Phyton
def estimar_custo_projeto(pontos_da_funcao, custo_por_ponto, fator_complexidade):
    """
    Estima o custo de um projeto de software
    Fator complexidade:1.0 (simples), 1.2(média),1.5 (complexo)
    """
    custo_base=pontos_da_funcao * custo_por_ponto
    custo_final=custo_base * fator_complexidade
    return custo_final

#dados do projeto
pf_estimados=350#ponto da funçao
custo_historico_por_pf= 850.50 #R$
complexidade = 1.2 #media

custo_total_estimado = estimar_custo_projeto(pf_estimados, custo_historico_por_pf,complexidade)
print(f"O custo estimado do projeto é:R${custo_total_estimado:,.2f}")
#saida:o custo estimado do projeto é R$357,210.00
