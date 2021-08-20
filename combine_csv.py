# import necessary libraries
import pandas as pd
import datetime
from glob import glob

files = sorted(glob('*.csv'))
print(files)

df = pd.concat((pd.read_csv(file).assign(filename = file) for file in files), ignore_index = True)
df.drop_duplicates(subset=['text'],inplace=True, ignore_index=True)

current_date = datetime.datetime.now()
filename = str(current_date)

df.to_csv(str(filename + '_combined.csv'),index=False)
