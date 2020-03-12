#lambdata_cdmx/my_mod.py
import pandas as pd
import numpy as np
import random

# from sklearn.model_selection import train_test_split

# def my_function(dataframe):

#     X = dataframe.iloc[:,:len(dataframe.columns) -1]
#     y = dataframe.iloc[:,-1]
        
#     X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42 
#     )
    
#     return dataframe.isnull(),  X_train.shape, X_test.shape, y_train.shape, y_test.shape  #invoking the function


class Split_Dates:

    def __init__(self,dtfr):
        self.dt  = dtfr

    def split_columns(self):
        self.dt = (self.dt.iloc[:,0]).str.split('-', expand=True)



class Train_split:
    def __init__(self,X,testsize=0.8,randstate=42):
        self.X = X
        self.testsize = testsize
        self.randstate = randstate

    def split_sample(self):
        random.seed(self.randstate)
        size = int(len(self.X) * self.testsize)
        sel_index = random.sample(self.X.index.tolist(),size)
        X_train = self.X.iloc[sel_index,:]
        X_test = self.X.iloc[self.X.index.drop(sel_index),:]   
        return X_train, X_test




