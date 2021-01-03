import pandas as pd 
from HTML import config as Config 


def drop_na_data(df, column_name):
    return df.loc[df[column_name].notna()]

def fill_na(df):
    # fill the na entries with 'None'
    return df.fillna('None')

def preprocessing(df):
    # The only invalid NA is in 'children' column
    return fill_na(drop_na_data(df, 'children')).reset_index(drop=True)

# x_train = pd.read_csv(Config.train_path)
# df1 = drop_na_data(x_train, 'children')
# df2 = fill_na(df1)
# print(df2.isna().sum())
# print(df2.loc[1])

