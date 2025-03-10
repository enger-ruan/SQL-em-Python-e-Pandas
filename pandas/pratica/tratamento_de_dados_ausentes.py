import numpy as np
import pandas as pd

df = pd.DataFrame({
'A': [1,2,np.nan],
'B': [5,np.nan, np.nan],
'C': [1,2,3]
})

# retira os dados nulos do meu df, e retorna somenta as linhas completas
df.dropna()

# retira os dados nulos do meu , e retorna somente as colunas que estão completas
df.dropna(axis=1)

# posso passssar um numero de colunas nulas que não seram permitidas ou seja ela não as retornara
# abaixo defini que se houver mais de 2 valores nulo então a linha não deve ser retornada
# ou seja se outras linhas ou colunas tiverem apenas 1 valor nulo seram retornadas da mesma forma que uma normal
df.dropna(axis=1, thresh=2)


# posso preencher os valore nam(nulo) com algum conteudo numero valor etc
# assim os valores nam seram preenchidos pos algo
df.fillna(0)

# faz a media dos valores da coluna para preencher os espaços vazios
df['A'].mean()

# ultilizando o fillna e depois ultilizando a media dos valores da colunas, eu preencho os valores
# nam com a media dos valores disponiveis na coluna
df['A'].fillna(value=df['A'].mean())

# preencho o valor nam, com o ultimo valor observavel bem util para series temporais.
# ou seja preenche o valor ausente com o ultimo valor disponivel tbm e util para indices que são tempo
df.ffill()

# tbm existe o bfill que pega não o ultimo mas o proximo valor que existe e tras para preencher os que faltam
# ex: e como se pagasse os dados de 2020 para preencher os de 2019
df.bfill