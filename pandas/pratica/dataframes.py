from numpy.random import randn
import numpy as np
import pandas as pd


# crio um DF com 5 linhas e 4 colunas,usando numeros aleatorios pelo randn, depois indico o index 
# e as columns
df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(' '), columns='W X Y Z'.split(' '))
print(df)

# seleciono apenas uma coluna do meu DF, me mostram ela como um serie
print(df['W'])


# Caso queira vela como um DF de uma coluna basta passar entre 2 colchetes
print(df[['W']])

# seleciono mais de uma coluna
print(df[['W', 'Y']])


# seleciono apenas um um indice no caso a abaixo o index = A
print(df.loc['A'])

#seleciono mais de um index, mais de uma linha.
print(df.loc[['A', 'B']])

# Crio uma nova coluna no meu df e uso como seus valores a soma de outras 2 colunas'
df['new'] = df['W'] + df['Y']
print(df)

df2 = df.drop('new', axis=1) # passo a coluna que quero deletar e a axis=1 para deletar a coluna, axis=0 para deletar a linha
# essa alteração não afeta o df orginal, então para salvar apenas a adciono em uma nova variavel
print(df2)

# Caso deseje realmente fazer uma alteração na coluna original devo adicionar o indice 'inplace=True' e as alterações eram salvas

df = df.drop('new', axis=1, inplace=True) 