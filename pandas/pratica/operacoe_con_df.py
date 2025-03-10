import pandas as pd

df = pd.DataFrame({'col1': [1,2,3,4], 'col2':[444, 555, 666, 444], 'col3':['abc', 'def','ghi', 'xyz']})

# Me retornar as informações sobre as colunas exemplo seu tipo de dado
df.info()

# Me permite ver o tamanho de cada coluna, o quanto de memoria ela ocupa
df.memory_usage()

# retorna apenas os dados que são unicos no df.
df['col2'].unique()

# retorna o numero de dados unicos de uma coluna
df['col2'].nunique()

# retorna o numero de vezes que um dado aparece em uma coluna e tbm qual dado é.
df.value_counts('col2')

# crio uma função 
def comp(x):
    return x ** 2 

# Aplica uma função a uma coluna, a função e aplicada em cada linha da coluna.
df['col1'].apply(comp)

# poderia ultilizar o lambda para funções mais simples

df['col1'].apply(lambda x: x ** 2)

# faz a soma de todos os valore da coluna
df['col1'].sum() 

# media
df['col1'].mean()

# desvio padrao
df['col1'].std()

# retorna o numero de linhas
df['col1'].count()

# retorna o menor valor
df['col1'].min()

# retorna o maior valor
df['col1'].max()

# retorna em qual indice a o valor maximo
df['col1'].idxmax()

# defino um filtro na 'col2' e indico que caso tenha um valor 444 na mesma, deve se aplicar uma soma
# na coll1 no qual os valores correspondem '444'
df[df['col2'] == 444]['col1'].sum()

# ordeno meu df apartir da ordem de alguma coluna especifica.
df.sort_values('col2')

data = {'A':['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
'B':['one', 'one', 'two', 'two', 'one', 'one'],
'C': ['x', 'y', 'x', 'y', 'x', 'y'],
'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)

# indico para meu df que caso ele veja o valor 'one' ele subistiua por 1 e caso veja o 'two' ele substitua por 2
dict_map ={'one': 1, 'two': 2}

# defino que a coluna 'E' seja igual a coluna 'B' e ultilizo o map para fazer aplicar a troca do das strings por int
df['E'] = df['B'].map(dict_map)

# ultilizo o pivot table para agrupar os dados e fazer uma media das colunas
df.pivot_table()









































