# lambdata_cdmx/my_script.py

import pandas as pd
from lambdata_cdmx.my_mod import my_function


df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data', 
index_col=False, names=['ages','workclass','fnlwgt','education','education-num','marital-status',
 'occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income'])




print('------------')


print(df.head())
print(' ')
print(my_function(df))


