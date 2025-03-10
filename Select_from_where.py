# IMPORTANTE so posso usar o read_sql quando for ultilizar o select

import sqlite3
import pandas as pd

# crio um banco de dados sua conexão com o python
conn = sqlite3.connect('web.db')

# crio um cursor ele serve para executar as instruções sql 
c = conn.cursor()

query = "SELECT A,B,C FROM data WHERE A > 200 AND B > 100"
sql_df = pd.read_sql(query, conn)
sql_df.index = sql_df.index.rename('index_name')
print(sql_df)
conn.commit()
c.close()
conn.close()

#
#c.execute('''SELECT A,B,C FROM data
#           WHERE A > 200 AND B > 100
#          ''')
#sql_df = pd.DataFrame(c.fetchall())
#print(sql_df)
#
