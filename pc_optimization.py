import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

#path ='/Users/ryszard/Downloads/PCScan_20kv sim2 - 128px.txt'
#path='/Users/ryszard/Downloads/PCScan_20kv sim2 - 256px.txt'
##path = '/Users/ryszard/Downloads/PCScan_20kv sim2 - 2056px.txt'
path = '/Users/ryszard/Downloads/PCScan_20kv sim2 - 2056px_2.txt'


def importer(path):
    columns = ['PCx', 'PCy', 'PCz', 'sigma range', '# of bands for sigma range', '2sigma range', '# of bands for 2sigma']
    df = pd.read_csv(path, sep=';', skiprows=2, names=columns, encoding='utf-16 le')
    df = df.astype(float)
    return df

def find_scale_limits(df):
    PCx_scale_limits = df['PCx'].min(), df['PCx'].max()
    PCy_scale_limits = df['PCy'].min(), df['PCy'].max()
    PCz_scale_limits = df['PCz'].min(), df['PCz'].max()
    return {'PCx': PCx_scale_limits, 'PCy': PCy_scale_limits, 'PCz': PCz_scale_limits}

def find_min_deviation(df):
    min_sigma = df.loc[df['sigma range'] <= df['sigma range'].min()*1.01]
    min_2sigma = df.loc[df['2sigma range'] <= df['2sigma range'].min()*1.01]
    return min_sigma, min_2sigma

def plotter_3d(df, marker_size, scale_limits):
    ax = plt.subplot(projection='3d')
    #p = ax.scatter(df['PCx'], df['PCy'], df['PCz'], c=df['sigma range'], cmap='jet_r', vmin=0, vmax=0.1, s=marker_size, alpha=1)
    p = ax.scatter(df['PCx'], df['PCy'], df['PCz'], c=df['sigma range'], cmap='jet_r', s=marker_size, alpha=1)
    ax.set_xlim3d(scale_limits['PCx'])
    ax.set_ylim3d(scale_limits['PCy'])
    ax.set_zlim3d(scale_limits['PCz'])
    ax.set_xlabel('PCx')
    ax.set_ylabel('PCy')
    ax.set_zlabel('PCz')
    plt.colorbar(p)
    plt.tight_layout()
    #plt.savefig('C:/Users/ryszard/Desktop/fig.png', dpi=300)
    return None

def subplotter(df, count, PCz_min):
    plt.subplots(figsize=(18,9))
    cols, rows = 5, 3
    plt.subplot(rows, cols, count, aspect='equal', adjustable='box')
    #plt.scatter(df['PCx'], df['PCy'], c=df['sigma range'], vmin=0, vmax=0.1, cmap='jet_r')
    plt.scatter(df['PCx'], df['PCy'], c=df['sigma range'], cmap='jet_r')
    plt.colorbar()
    plt.title("PCz =" + str(rows.PCz), fontweight='bold')
    return None

df = importer(path)
df_raw = importer(path)
min_deviation = find_min_deviation(df)[0]
df = df[df['sigma range'] <= min_deviation['sigma range'].min()*1.02]
#df = df[df['PCx'] == 0.531]
print(min_deviation[min_deviation['sigma range'] == min_deviation['sigma range'].min()])
PCz_min = min_deviation['PCz'].mean()
scale_limits = find_scale_limits(df)
#plotter_3d(df, 1, scale_limits)
subplotter(df, 1, 2)
plt.show()