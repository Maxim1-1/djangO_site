from pandas import read_csv, DataFrame
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# from sklearn.cross_validation import train_test_split

# просмотр данных
dataset = read_csv('../data/car_col.csv', sep=';')
# print(dataset.head())

# CorrKoef = dataset
#
# CorField = []
# for i in CorrKoef:
#     for j in CorrKoef.index[CorrKoef[i] > 0.9]:
#         if i != j and j not in CorField and i not in CorField:
#             CorField.append(j)
#             print(f"{i}-->{j}: r^2={CorrKoef[i][CorrKoef.index==j].values[0]}")

# print(np.corrcoef(dataset))
print(dataset.corr())
