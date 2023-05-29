
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
boston = load_boston()
data = pd.DataFrame(boston.data)
data.head()
data.columns = boston.feature_names

data['PRICE'] = boston.target
data.head(n=10)