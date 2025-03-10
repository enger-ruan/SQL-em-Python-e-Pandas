import pandas as pd

# dataframe

#crio um dicionario
data = {'Classe':['Júnior','Júnior','Pleno','Pleno','Señor','Señor'],
        'Nome':['Jorge','Carlos', 'Roberta','Patricia','Bruno','Vera'],
        'Venda':[200, 120, 340, 124, 243, 350]}


# Crio um dataframe apartir de um dicionario
df = pd.DataFrame(data)

# Faço um group by e agrupo os dados com base na coluna Classe, em seguida pesso para fazer a soma
# dos valores das colunas 'Classes' que forem iguais, sum passei a coluna que queria somar.
sum_df = df.groupby('Classe').sum('Venda')

# faço um group by e agrupo os dados com base na coluna Classe, em seguida pesso para fazer a media
avg_df = df.groupby('Classe').mean('Venda')

# separo por grupo e pego os valores minimos de cada classe, sem especificar a coluna que quero o min, ele além
# de trazer o min tbm me traz os valores da coluna  nome me mostrando o valor nome de quem vendeu menos.
min_df = df.groupby('Classe').min()

# defino que o meu df2 seja uma copia do df assim não modificara o df original
df2 = df.copy()

# defino que a coluna vendas do df2 e igual a ela mesma, so que multiplicado por 0.5 ou seja 50 % do valor total.
df2['Venda'] = df2['Venda'] * 0.5


# crio um df3 e concateno o df com o df2 ou seja junto as informações dos 2 dfs sem somar mas concatenando
df3 = pd.concat([df, df2])

# Ultilizo o order by para não so agrupar por classe mas tbm por nome, e peço para somar os valores da coluna
# dessa maneira terei os nomes agrupados tbm o que somara todos os valores dos nomes iguais.
df3.groupby(['Classe', 'Nome']).sum()