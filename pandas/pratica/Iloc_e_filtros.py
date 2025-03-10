import pandas as pd
from numpy.random import randn
import numpy as np



df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(' '), columns='W X Y Z'.split(' '))

print(df)
# seleciono apenas 2 indices do meu df
print(df.loc[['A', 'B']])


# tbm selecio uma coluna especifica
print(df.loc[['A', 'B'], 'W'])

# ultilizand0 o iloc para selecionar uma linha e uma coluna especifica atraves de cordenadas
# o primeiro valor representa a linha e o segundo a coluna
# lembrando sempre que no python a contagem começa pelo 0

print(df.iloc[1, 2])


# Seleciono todas as linhas exceto a ultima e seleciono a coluna 2 ou seja Y
print(df.iloc[:-1, 2])


#seleciono todas as linhas exceto a primeira e todas as colunas exceto a primeira
print(df.iloc[1:, :2])

# seleciono todas as linhas e todas as colunas
print(df.iloc[:, :])

# seleciono todas as linhas e todas as colunas exceto a primeira
print(df.iloc[:, 1:])

# seleciono todas as linhas exceto a primeira e todas as colunas exceto a ultima
print(df.iloc[1:, :-1])

# seleciono as linhas B, C, D das colunas X, Y
print(df.iloc[1:-1, 1:-1])


# FILTROS SIMPLES
print(df +df)

# peço para me retornar apenas os elementos do data frame que são maiores do que 0,1
print(df > 0,1)

# peço para me retornar os elementos do meu df que são maiores do que 0 aqui sera mostrado os valores do df
print(df[df > 0])

# Peço para meu df me retornar apenas os elementos da coluna Z que seja maior do que 0, ou seja todos os elementos da coluna Z que forem 
# maiores do que 0 terem seus indices retornados, isso e muito valioso imagine que esses valores fossem o salario eu poderia retornar apenas
# os salarios que passassem de um cetro valor e assim o indice deles seria retornado.
print(df[df['Z'] > 0])

# peço para me retornar apenas os elementos da coluna W e X que seja maior do que 0, ou seja, passo 2 condicoes para serem verdadeiras
print(df[(df['W'] > 0) & (df['X'] > 0)])

# OPERAÇÕES COM INDICES
print(df.index)  #vejo os indices do meu df
print(df.columns) # vejo as colunas do meu df

# reseto os indices do meu df, isso fara com que os indices passem a ser enumerados
df.reset_index(inplace=True) # chamo o inplace para aplicar as modificações no arquivo orginal.

print(df)

# retorno para o indice aintigo retirando o numerico que acabei de aplicar no reset_index
df.set_index('index', inplace=True)

# crio novos indices para o meu df
novos_indices =('CA NY WY OR CO ').split()

# defino que df['novos_index'] seja igual aos novos indices, preciso definir isso pos preciso passar a sring
# 'novo_index' para o set_index
df['novos_index'] = novos_indices
print(novos_indices)

# adciono os novos indices ao dataframe usando o set index e ultilizo
# o reset index para guardar os indices antigos
df.reset_index().set_index('novos_index')