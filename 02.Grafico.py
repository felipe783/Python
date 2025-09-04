import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Dados de tarefas (exemplo de cronograma)
#aqui é o dicionario pra printar e onde fica as infos
data = {
'Tarefa': ['Design UI', 'Codificação Backend', 'Testes'],
'Início': ['2025-09-01 7:00', '2025-09-02 9:00', '2025-09-04 13:00'],
'Fim': ['2025-09-02 9:00', '2025-09-03 11:00', '2025-09-05 14:00']
}

df = pd.DataFrame(data) #aqui os bagulho do dicionario vira colunas
df['Início'] = pd.to_datetime(df['Início']) #matplot não entende str então aqui as colunas "Inicio/Fim" pra datetime
df['Fim'] = pd.to_datetime(df['Fim'])
df['Duração_dias'] = (df['Fim'] - df['Início']).dt.total_seconds() / 86400.0
#o dt.total converte a diferença de dias e horas pra segundos
# e o 86400.0 é o tantos de segundos tem um dia
#o AX é um eixo
fig, ax = plt.subplots(figsize=(19, 6)) #aqui muda as dimensões do grafico
ax.barh(df['Tarefa'], df['Duração_dias'], left=mdates.date2num(df['Início']))
#df(tarefa) é no eixo Y,df(duração dias) é o comprimento da barra
#left=mdates.date2num(df['Início']) → define onde a barra começa no eixo X

# limitar o eixo X ao intervalo útil (com 1 hora de "margem")
start = df['Início'].min() - pd.Timedelta(hours=1)
end   = df['Fim'].max() + pd.Timedelta(hours=1)
#Ele pega a menor data/hora de início e a maior data/hora de fim.
#E adiciona uma folga de 1 hora antes e 1 hora depois, só pra o gráfico não ficar colado na borda.
ax.set_xlim(mdates.date2num(start), mdates.date2num(end))
#define o limite do eixo X(start e end)
#mdates.date2num transforma a data (datetime) num número que o matplotlib entende

# ticks por hora (ajusta interval pra 1, 2, 6 etc conforme precisar)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2)) #Define os ticks principais do eixo X (as marquinhas que aparecem no gráfico).
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # só hora:minuto aqui define como os ticks vão ser exibidos
fig.autofmt_xdate() #aqui define as datas pra elas ficarem inclinadas quando aparecerem
# se quiser 90 graus é  plt.xticks(rotation=90) gira em 90 graus o eixo
#esse rotation ce pode escolher quantos graus quer mexer
plt.tight_layout() #aqui não corta nenhum texto
plt.title('Cronograma (horas)') #coloca titulo
plt.show() #exibe o grafico


#datetime é um tipo de dado usado em Python (e em várias linguagens) pra representar datas e horários de forma organizada.
