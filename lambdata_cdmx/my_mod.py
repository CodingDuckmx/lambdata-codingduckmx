#lambdata_cdmx/my_mod.py

from sklearn.model_selection import train_test_split

def my_function(dataframe):

    X = dataframe.iloc[:,:len(dataframe.columns) -1]
    y = dataframe.iloc[:,-1]
        
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42 
    )
    
    return dataframe.isnull(),  X_train.shape, X_test.shape, y_train.shape, y_test.shape  #invoking the function


