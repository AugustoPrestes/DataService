# %%
import pandas as pd
from datetime import date

tabela = pd.read_csv("./extract/22-03-2024.csv", sep=';')

# %% 
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

datahoje = date.today()

# %% 
tabela.columns = tabela.columns.str.lower()

# %% 
tabela = tabela.set_index('ticker')

# %% 
tabela['data'] = date.today().strftime('%d-%m-%y')

# %% 
tabela.head()

# %%
tabela.to_json(f'saves/{datahoje}.json', orient='index')
