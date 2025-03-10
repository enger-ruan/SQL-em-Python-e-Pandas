import pandas as pd

# lendo arquivo csv, primeiro passo o caminho do arquivo e depois o separador dos elementos do arquivo
# no caso abaix estão separados por virgula, neese arquivo posso passar tbm o parametro decimal e indicar qual 
# pontuação e usada para separar o decimal nesse caso e o ponto final '.'
df1 = pd.read_csv("pratica/exemplo.csv", sep=',', decimal='.')

# posso ultilizar um .info para verificar se os dados recebidos são o tipo que e apresentado
df1.info()


# Para exportar os dados em um arquivo csv, posso passar o separador e o decimal que desejar

df1.to_csv("pratica/exemplo.csv", sep=';', decimal='.')