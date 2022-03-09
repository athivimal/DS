import matplotlib.pyplot as plt
import pandas as pd

# load the csv file (Monthly average air temperatures of the city of Barcelona since 1780) into a pandas data frame
df_temperature = pd.read_csv('bar1.csv', encoding='utf-8')

print(df_temperature.info())
df_temperature.set_index('Any', inplace=True)

df_temperature.index.name = 'year'

# calculate the yearly average air temperature
df_temperature['average_temperature'] = df_temperature.mean(axis=1)

# drop columns containing monthly values
df_temperature = df_temperature[['average_temperature']]

# visualize the first 5 columns
df_temperature.head()

plt.style.use('seaborn')

# line plot - the yearly average air temperature in Barcelona
df_temperature.plot(color='green', linewidth=3, figsize=(12,6))

# modify ticks size
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend('')

# title and labels
plt.title('The  average Count ', fontsize=20)
plt.xlabel('Days', fontsize=16)
plt.ylabel('Count x 10', fontsize=16)