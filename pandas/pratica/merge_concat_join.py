import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1','A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3'],
'C': ['C0', 'C1', 'C2', 'C3'],
'D': ['D0', 'D1', 'D2', 'D3']},
index=[0,1,2,3])

df2 = pd.DataFrame({'A': ['A4', 'A5','A6', 'A7'],
'B': ['B4', 'B5', 'B6', 'B7'],
'C': ['C4', 'C5', 'C6', 'C7'],
'D': ['D4', 'D5', 'D6', 'D7']},
index=[4,5,6,7])

df3 = pd.DataFrame({'A': ['A8', 'A9','A10', 'A11'],
'B': ['B8', 'B9', 'B10', 'B11'],
'C': ['C8', 'C9', 'C10', 'C11'],
'D': ['D8', 'D9', 'D10', 'D11']},
index=[8,9,10,11])

# Concat

# faço a concatenação dos df nesse caso de linhas e quisesse conactenar as colunas deveria ultilizar o axis=1
# no caso de colunas para concatenar o python esperar que elas tenham indices iguia e não colunas.
pd.concat([df1,df2,df3])

# Merge
esquerda = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3']})

direita = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
'C': ['C0', 'C1', 'C2', 'C3'],
'D': ['D0', 'D1', 'D2', 'D3']})

# Ultilizando o Merge para mesclar os DFs esquerda e direita, suas colunas e inidices são diferentes 
# e o merge vai mesclar as colunas e os indices porém eu preciso passar um parametro para poder juntar os DFs
# então ultilizo a coluna 'key' para juntar os DFs ja que a key nos 2 dfs são iguais, e como se eu juntasse 2 
# tabelas diferentes e ultilizasse a chave pk para mesclar as colunas em uma certa ordem e logica.

pd.merge(esquerda,direita, on ='key')

esquerda = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
'key2': ['K0', 'K1', 'K0', 'K1'],
'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3']})

direita = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
'key2': ['K0', 'K0', 'K0', 'K0'],
'C': ['C0', 'C1', 'C2', 'C3'],
'D': ['D0', 'D1', 'D2', 'D3']})

# a merge mescla as colunas e indices com base na chave 'key1' e 'key2' ou seja ele vai procurar uma
# logica baseada na key1 e key2 e olhara na tabela da direita os dados que se encaixem na tabela da esquerda
# e os que corresponderem a essa logica seram juntados os que não correspoderem serao retirados
pd.merge(esquerda, direita, on=['key1', 'key2'])


# segue a mesma logica do exemplo acima porem eu passo mais um parametro o how='outer'por padrão ele e inner
# porem colocando como outer, os valores que não atenderam a logica não seram cortados mas constados como nam.
pd.merge(esquerda, direita,how='outer', on=['key1', 'key2'])

esquerda = pd.DataFrame({'A': ['A0', 'A1','A2'],
'B': ['B0', 'B1', 'B2']},
index=['K0', 'K1', 'K2'])

direita = pd.DataFrame({'C': ['C0', 'C2','C3'],
'D': ['D0', 'D2', 'D3']},
index=['K0', 'K2', 'K3'])

# funciona como um left join no sql pega todos os indices da tabela da esquerda e me traz os dados que correspondem a cada linha da tabela da direita
# os indices da tabela da direita que não forem encontrados na tabela da esquerda serao cortados.
esquerda.join(direita)

# Me retornar todos os dados das 2 tabelas unindo os que correspondem e colocando como nam os valores não encontrados
esquerda.join(direita, how='outer')