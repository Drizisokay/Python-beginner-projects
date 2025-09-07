import pandas as pd

data = {'Month': [1,2,3,4,5,6,7,8], 'Temp': [43.1,56.9,60.3,67.2,76.1,85.8,85.2,86.7]}
df = pd.DataFrame(data, index= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'])

df.to_csv('monthly_mean_temps_texas.csv')

print(df)