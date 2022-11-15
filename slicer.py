import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#path ='/Users/ryszard/Desktop/Si_patterns/PCScan_20kv dd180.ebsp — rough.txt'
#path ='C:/Users/Ryszard/Desktop/Si_patterns/PCScan__10kv.ebsp.txt'
path = '/Users/ryszard/Downloads/PCScan_20kv sim2 - 2056px_2.txt'


''' subplots'''
def subplotter(df, rows, cols, count):
    plt.subplot(rows, cols, count, aspect='equal', adjustable='box')
    plt.scatter(df_filtered['PCx'], df_filtered['PCy'], c=df_filtered['sigma range'], vmin=0, vmax=0.2, cmap='jet_r')
    plt.yticks(np.arange(df['PCy'].min(), df['PCy'].max(), 0.05))
    plt.xticks(np.arange(df['PCx'].min(), df['PCx'].max(), 0.05))
    plt.colorbar()
    plt.title("PCz =" + str(row.PCz), fontweight='bold')
    return None

'''plot prep'''
ax = plt.subplots(figsize=(18,9))
pcz_limits = [0.424, 0.434]
#matplotlibFonts(4,4,8)
cols, rows = 6, 4

def importer(path):
    columns = ['PCx', 'PCy', 'PCz', 'sigma range', '# of bands for sigma range', '2sigma range', '# of bands for 2sigma']
    df = pd.read_csv(path, sep=';', skiprows=2, names=columns, encoding='utf-16 le')
    df = df.astype(float)
    return df

'''get data'''
df = importer(path)

'''iterate over the dataframe rows, get only unique PCz values to get 
   slices through PC space, then plot with variable as color scale'''
check = []
count = 0
for row in df.itertuples():
    if row.PCz not in check and row.PCz >= pcz_limits[0] and row.PCz <= pcz_limits[1]:
        count += 1
        check.append(row.PCz)
        df_filtered = df.loc[df['PCz'] == row.PCz]
        subplotter(df_filtered, rows, cols, count)
        
        #find_extremes(df_filtered)
        print(df_filtered.loc[df_filtered['sigma range'] == df_filtered['sigma range'].min()])
    else:
        continue 

plt.tight_layout()    

plt.show()
