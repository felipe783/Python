import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Dados de tarefas (exemplo de cronograma)
data = {
'Tarefa': ['Design UI', 'Codificação Backend', 'Testes'],
'Início': ['2025-09-01 7:00', '2025-09-02 9:00', '2025-09-04 13:00'],
'Fim': ['2025-09-02 9:00', '2025-09-03 11:00', '2025-09-05 14:00']
}

df = pd.DataFrame(data)
df['Início'] = pd.to_datetime(df['Início'])
df['Fim'] = pd.to_datetime(df['Fim'])
df['Duração_dias'] = (df['Fim'] - df['Início']).dt.total_seconds() / 86400.0
fig, ax = plt.subplots(figsize=(20, 3))
ax.barh(df['Tarefa'], df['Duração_dias'], left=mdates.date2num(df['Início']))

# limitar o eixo X ao intervalo útil (com 1 hora de "margem")
start = df['Início'].min() - pd.Timedelta(hours=1)
end   = df['Fim'].max() + pd.Timedelta(hours=1)
ax.set_xlim(mdates.date2num(start), mdates.date2num(end))

# ticks por hora (ajusta interval pra 1, 2, 6 etc conforme precisar)
ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # só hora:minuto
fig.autofmt_xdate()
plt.tight_layout()
plt.title('Cronograma (horas)')
plt.show()
