import pandas as pd
from matplotlib import pyplot as plt

'''import data to pandas dataframe'''
#path = '/Users/user/Desktop/PCScan_si_sim.txt'
path ='/Users/ryszard/Desktop/PCScan_si_sim.txt'
columns = ['PCx', 'PCy', 'PCz', 'sigma range', '# of bands for sigma range', '2sigma limit', '# of bands for 2sigma']
df = pd.read_csv(path, sep=';', skiprows=2, names=columns, encoding='utf-16 le')
df = df.astype(float)

'''plot with variable as color scale'''
ax = plt.subplot(projection='3d')
p = ax.scatter(df['PCx'], df['PCy'], df['PCz'], c=df['sigma range'], cmap='viridis_r')
plt.colorbar(p)
plt.show()