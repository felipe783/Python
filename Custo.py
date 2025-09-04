pessoas=3
salario=5000
meses=6

def Custos_projeto(P, S,M):
    return S*P*M
    """
    aqui a função Custos_projeto vai retornar a equação (S*P*M)
    """

custo_total=Custos_projeto(pessoas,salario,meses)
#Aqui na variavel custo_final vai lançar na função Custos_projeto os valores da variaveis dentro deo parenteses

print(f"O custo é:R${custo_total:,.2f}")
#aqui printa
