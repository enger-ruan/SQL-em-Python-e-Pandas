import pandas as pd
import datetime

# crio um df com o index Datetime
numero_de_dias = 100

# Cria um intervalo de datas começando de 1/1/2024 ate 100 dias depois dessa data que e oque defini na outra variavel
datas = pd.date_range(start='1/1/2024', periods=numero_de_dias)


# crio um df ultilizando o range e defino o index e a coluna
df = pd.DataFrame(range (numero_de_dias), columns=['numeros'], index=datas)

# visualizo informações de algum dia especifico
df.index[0].day

# Do mes
df.index[0].month

# Do ano
df.index[0].year

# Da hora
df.index[0].hour

# pego todos as linhas do mes 1 
df[df.index.month == 1]

# pego todos as linhas dos dados que sejam dia 5
df[df.index.day == 5]