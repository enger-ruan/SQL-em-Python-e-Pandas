import pandas as pd
from numpy.random import randn

# ultilizando o lista zip eu faço a junção de duas listas ele encaixa os elementos um com o outro em forma de tupla

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]

# ultilizo o zip para juntar as listas e defino o como multiindice
hier_index = pd.MultiIndex.from_tuples(zip(outside, inside))
print(hier_index)

# crio o df ultilizando o zip para inidices e defino sua colunas 
df = pd.DataFrame(randn(6, 2), index = hier_index,columns= ['A', 'B'])

# Defino nomes para ser exibidos em cima dos indices
df.index.names = ['Groups', 'num']


# essa funcionalidade e interessante pos classifica os indices em uma hierarquia primeiro g1 ou g2 depois se 1, 2 ou 3.

print(df)

# pego apenas os indices 'G1' que são os primeiros da hierarquia
df.loc['G1']

# seleciono o indice '1' do indice 'G1'
df.loc['G1'].loc[1]

# seleciono todos os elmentos de indice '1' no level 'num' ou seja ele não se baseara na hirarquia 'G1'
# ele vai se basear no nome que dei para os indices, como chamel o level 2 de num então especifico que quero
# o indice '1' do level 'num', assim terei os indices 1 tanto do G1 quanto do G2
df.xs(1, level='num')