import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

file = 'data/csv_wrang.csv'
df = pd.read_csv(file)
years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

plt.style.use('dark_background')
fig = plt.figure(figsize = (12, 16))
plt.subplots_adjust(left=0.05,
                    bottom=0.1,
                    right=0.8,
                    top=0.85,
                    wspace=0.7,
                    hspace=0.3)
grid = plt.GridSpec(2, 2)
# fig.suptitle(f"Случаи с изнасилованием связанными статьями 120 и 121 на {df_rape['year'].values[0]} год")

def animate(indx):
    fig.clear()

    ax1 = plt.subplot(grid[0, 1])
    ax2 = plt.subplot(grid[1, 0])
    ax3 = plt.subplot(grid[1, 1])
    ax5 = plt.subplot(grid[0, 0])

    #spec = fig.add_gridspec(3, 2)
    df_rape = df[df['ind'] == indx]
    print(df_rape)

    def remove_empty(val,lab):
        val2 = []
        lab2 = []
        for i in range(0, len(val)):
            if val[i] != 0:
                val2.append(val[i])
                lab2.append(lab[i])
        return val2, lab2

    # Chart1:

    total = df_rape['amnt_stop_investigation'].values[0] + df_rape['amnt_opravdonyh'].values[0]  + df_rape['amnt_osuzhden'].values[0] 

    values1 = [df_rape['amnt_stop_investigation'].values[0] + df_rape['amnt_opravdonyh'].values[0] + df_rape['uslov_osuzhd'].values[0], df_rape['total'].values[0]]
    print(values1)
    labels1 = ['Освобожденные', 'Лишенные свободы']

    plt.suptitle(f'''Случаи с изнасилованием связанные с педофилией 
статьями 122 и 124 на {int(df_rape['year'].values[0])} год''', size = 23, fontweight="bold")
    ax1.pie(values1, colors=['#27557b', '#FF0000'], autopct='%1.1f%%')
    ax1.legend(labels1, bbox_to_anchor=(0.85,1.025), loc="upper left", fontsize = 13)
    ax1.set_title(f"Общее количество рассмотренных случаев {int(total)}", size = 17)


    
    values2 = [df_rape['year_less_1'].values[0] + df_rape['year_1_3'].values[0] + df_rape['year_1_5'].values[0],
                df['year_3_5'].values[0],
                  df['year_5_8'].values[0] + df['year_8_10'].values[0],
                    df['year_10_12'].values[0] + df['year_15_20'].values[0],
                      df['year_20_25'].values[0] + df['year_25_30'].values[0],
                      df['death_punish'].values[0],
                      df['forever_jail'].values[0]]
    ttl = df_rape['year_less_1'].values[0] + df_rape['year_1_3'].values[0] + df_rape['year_1_5'].values[0] + df['year_3_5'].values[0] + df['year_5_8'].values[0] + df['year_8_10'].values[0] + df['year_10_12'].values[0] + df['year_15_20'].values[0] + df['year_20_25'].values[0] + df['year_25_30'].values[0] + df['death_punish'].values[0] + df['forever_jail'].values[0] 
    labels2 = [f"до 3 лет {int((df_rape['year_less_1'].values[0] + df_rape['year_1_3'].values[0] + df_rape['year_1_5'].values[0])/ttl*100)}%", 
               f"c 3 до 5 лет {int((df['year_3_5'].values[0])/ttl*100)}%",	
               f"с 5 года до 8 лет {int((df['year_5_8'].values[0] + df['year_8_10'].values[0])//ttl*100)}%",
               f"с 10 года до 20 лет {int((df['year_10_12'].values[0] + df['year_15_20'].values[0])/ttl*100)}%",	
               f"с 20 до 30 лет {int((df['year_20_25'].values[0] + df['year_25_30'].values[0])/ttl*100)}%", 
               f"смертная казнь {int((df['death_punish'].values[0])/ttl*100)}%",	
               f'''пожизненное лишение
свободы {int((df['forever_jail'].values[0])/ttl*100)}%''']
    #values2, labels2 = remove_empty(values2, labels2) 
    ax2.pie(values2,colors=['#FFCCCC', '#FF8080', '#FF0000', '#990000', '#D10000', '#A30000'])
    labs2 = [f'{l}, {s:0.1f}%' for l, s in zip(labels2, values2)]
    ax2.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels2, fontsize = 13)
    ax2.set_title(f'''Общее количество лишенных 
свободы: {int(df_rape['amnt_osuzhden'].values[0])}''', size = 17)



    values3 = [df_rape['by_reconciliation'].values[0], df_rape['by_other_reson'].values[0], df_rape['by_being_crazy'].values[0], df_rape['amnt_opravdonyh'].values[0], df_rape['uslov_osuzhd'].values[0]]
    ttls = df_rape['by_reconciliation'].values[0]+  df_rape['by_other_reson'].values[0]+  df_rape['by_being_crazy'].values[0] + df_rape['amnt_opravdonyh'].values[0]+  df_rape['uslov_osuzhd'].values[0]
    labels3 = [f'''По примирению
сторон {int(df_rape['by_reconciliation'].values[0]/ttls * 100)}%''', f'''По другим 
причинам {int(df_rape['by_other_reson'].values[0]/ttls * 100)}%''', f"По невминяемости {int(df_rape['by_being_crazy'].values[0]/ttls *100)}%", f"Оправданные {int(df_rape['amnt_opravdonyh'].values[0]/ttls * 100)}%", f'''Условно 
осужденные {int(df_rape['uslov_osuzhd'].values[0]/ttls * 100)}%''']
    
    ax3.pie(values3, colors=['#7B5EC6', '#0f2231', '#27557b', '#4288c2', '#8cb6da'])
    labs3 = [f'{l}, {s:0.1f}%' for l, s in zip(labels3, values3)]
    ax3.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels3, fontsize = 13)
    ax3.set_title(f'''Общее количество не лишенных 
сободы: {int(df_rape['amnt_stop_investigation'].values[0] + df_rape['amnt_opravdonyh'].values[0] + df_rape['uslov_osuzhd'].values[0])}''', size = 17)

    df_total = df[df['ind'] <= indx]
    ax5.set_ylim(60, 170)
    ax5.set_xlim(2016, 2023)
    ax5.set_title('Статистика по годам', size = 17)
    ax5.plot(df_total['year_exp'], df_total['totals'])

animation = FuncAnimation(fig,animate, frames=range(df['ind'].min(), df['ind'].max()+1), interval = 5000)
animation.save('smallergif.gif', dpi=100, writer=PillowWriter(fps=200)) # Script for saving
plt.show()