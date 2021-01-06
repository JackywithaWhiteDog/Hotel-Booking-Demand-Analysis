import pandas as pd
from HTML.config import month_number, nominal, ordinal, meaningless
from HTML import config as Config

def parse_date(year, month, date):
    return '{:04d}-{:02d}-{:02d}'.format(year, month_number[month], date)

def add_arrival_date(x):
    date = [None] * len(x)
    for i, row in x[['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month']].iterrows():
        date[i] = parse_date(row[0], row[1], row[2])
    x['arrival_date'] = date
    return x

"""
RETURN: train (m*k matrix), test (n*k matrix), train_index, test_index
- m: # of training examples
- n: # of testing examples
- k: # of features + label (for training set, at the last column)
- train_index, test_index: list of string, indicate arrival date
"""
def get_mean_data():
  x_train = pd.read_csv(Config.train_path)
  N = x_train.shape[0]
  x_test = pd.read_csv(Config.test_path)
  X = add_arrival_date(pd.concat((x_train, x_test), ignore_index=True))

  dummies = pd.get_dummies(
    data=X.drop(columns=meaningless),
    columns=nominal+ordinal,
    drop_first=True,
    dummy_na=True)
  dummies = dummies.fillna(dummies.mean())

  x_train_processed = dummies.iloc[:N,:].groupby('arrival_date').mean()
  x_test_processed = dummies.iloc[N:,:].groupby('arrival_date').mean()

  y_train = pd.read_csv(Config.train_label_path)
  y_test = pd.read_csv(Config.test_nolabel_path)

  train = x_train_processed.merge(y_train, left_index=True, right_on='arrival_date')
  test = x_test_processed.merge(y_test, left_index=True, right_on='arrival_date')

  train_index = train['arrival_date']
  test_index = test['arrival_date']

  train = train.drop(columns=['arrival_date']).to_numpy(dtype=float)
  test = test.drop(columns=['arrival_date']).to_numpy(dtype=float)

  return train, test, train_index, test_index
