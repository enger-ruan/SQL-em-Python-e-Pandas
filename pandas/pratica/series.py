import pandas as pd
import numpy as np

# Series e como se fosse a coluna do meu Dataframe, exemplos abaixo de como criar uma series.


labels = ['a', 'b', 'c']
my_list= [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a':10, 'b':20, 'c':30}

df_l = (pd.Series(labels)) # crio uma series a apartir de uma lista

# Criando uma series ultilizando uma lista como data e index
df_list = pd.Series(data=labels, index=my_list)# crio uma series e defino o index 'my_list' ele será meu indice.



# Series a apartir de dicionarios se casam muito bem, pois a series tranforma as chaves dos dicionarios em index e os valores em data
df_dict = pd.Series(d) # crio uma series a apartir de um dicionario


print(df_dict)

print('\n')

# Crio outra series e defino seu index e data
ser1= pd.Series(data=[1,2,3,4], index=['USA', 'Germany', 'USSR', 'Japan'])

# posso retornar apenas um valor da series ultilizando o index 'USA'
print(ser1['USA'])


# ou retornar uma lista passando varios index

print(ser1[['USA', 'USSR']])

