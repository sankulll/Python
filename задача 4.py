import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

one_hot = pd.get_dummies(data['whoAmI'])
data_one_hot = pd.concat([data, one_hot], axis=1)
data_one_hot.drop('whoAmI', axis=1, inplace=True)

data_one_hot.head()