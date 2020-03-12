# lambdata_cdmx/my_script.py

import pandas as pd
import numpy as np
# from my_mod import my_function
# from my_mod import My_class


# df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])




# print('------------')


# print(df.head())
# print(' ')
# print(my_function(df))


from my_mod import Split_Dates
from my_mod import Train_split

 
         

df1  = pd.DataFrame(np.array([['1-2-2003'], ['4-5-2006'], ['7-8-2009']]), columns=['full date'])

print(df1)

# df_splited = df['full date'].str.split('-')

# print(df_splited)

my_split = Split_Dates(df1)
my_split.split_columns()
print(my_split.dt)


df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])             



train_splited = Train_split(df2)
X_train, X_test = train_splited.split_sample()

print(X_train)