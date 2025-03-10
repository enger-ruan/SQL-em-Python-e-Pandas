import pandas as pd

df_gas_completo = pd.read_csv('exercicios/gasolina_completo.csv', sep=';', index_col=0)
print(df_gas_completo.loc[[2], 'DATA INICIAL'])

df_gas_completo['DATA INICIAL'] = pd.to_datetime(df_gas_completo['DATA INICIAL'], errors='coerce')

df_gas_completo['DATA FINAL'] = pd.to_datetime(df_gas_completo['DATA FINAL'], errors='coerce')

print(df_gas_completo.loc[[2], 'DATA INICIAL'])


df_gas_completo['ANO FINAL'] = df_gas_completo['DATA FINAL'].dt.year

df_gas_completo['MES FINAL'] = df_gas_completo['DATA FINAL'].dt.month

df_gas_completo.to_csv('exercicios/gasolina_completo.csv', sep=';', decimal='.')

df_gas_completo[['MES FINAL', 'DATA FINAL']]

df_gas_completo.loc['GASOLINA COMUM', :]

df.loc['GASOLINA COMUM', :]

gasolina_comum =df_gas_completo.loc[df_gas_completo['PRODUTO'] == 'GASOLINA COMUM', :]