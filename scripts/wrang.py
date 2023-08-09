import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

file = 'archive/data_imp.csv'
df = pd.read_csv(file)
df_2 = df[df['type_of_punish']=='child']
df_2.reset_index(inplace=True, drop=True)
df_2['totals'] = df_2['amnt_stop_investigation'] + df_2['amnt_opravdonyh']  + df_2['amnt_osuzhden']
# df_1 = df_2 
# df_1.index = df_2.index*25
# last_idx = df_1.index[-1]+1
# df_expanded = df_1.reindex(range(last_idx))
df_2['year_exp'] = df_2['year']
# df_expanded['year'] = df_expanded['year'].fillna(method='ffill')
# df_expanded['type_of_punish'] = df_expanded['type_of_punish'].fillna(method='ffill')
# df_expanded = df_expanded.interpolate()
# df_expanded['year'] = df_expanded['year'].astype('int')
# df_expanded['year_exp'] = df_expanded['year_exp']
# df_expanded['year_exp'] = df_expanded['year_exp']
df_2['ind'] = range(1, len(df_2) + 1)
print(df_2)
df_2.to_csv('data/csv_wrang.csv')