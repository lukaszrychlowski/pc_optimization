import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

'''import data to pandas dataframe'''
#path = '/Users/user/Desktop/PCScan_si_sim.txt'
path ='/Users/ryszard/Desktop/PCScan_si_sim.txt'
columns = ['PCx', 'PCy', 'PCz', 'sigma range', '# of bands for sigma range', '2sigma limit', '# of bands for 2sigma']
df = pd.read_csv(path, sep=';', skiprows=2, names=columns, encoding='utf-16 le')
df = df.astype(float)

'''get min and max sigma values'''
sigma_min=df['sigma range'].min()
sigma_max=df['sigma range'].max()

'''iterate over the dataframe rows, get only unique
   PCz values to get slices through PC space, then 
   plot with variable as color scale'''
check = []
for row in df.itertuples():
    if row.PCz not in check:
        check.append(row.PCz)
        plt.figure()
        df_filtered = df.loc[df['PCz'] == row.PCz]
        ax = plt.subplot()
        p = ax.scatter(df_filtered['PCx'], df_filtered['PCy'], c=df_filtered['sigma range'], vmin=sigma_min, vmax=sigma_max, cmap='viridis_r')
        plt.yticks(np.arange(df['PCy'].min(), df['PCy'].max(), 0.02))
        plt.xticks(np.arange(df['PCx'].min(), df['PCx'].max(), 0.02))
        plt.title("PCz =" + str(row.PCz))
        plt.colorbar(p)        
    else:
        continue 
    
plt.show()
