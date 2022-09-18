##telco churn

import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("D:\Windows10\Dekstop\Miuul Makine Öğrenmesi Yaz Kampı\Feature Engineering\Projeler\Telco-Customer-Churn.csv/Telco-Customer-Churn.csv")

df.head()
df.shape
#21 değişken 7043 satır veri

def grab_col_names(dataframe, cat_th=10, car_th=20):

    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == 'O']
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != 'O']

    num_but_cat = [col for col in num_cols if dataframe[col].nunique() < cat_th]

    cat_but_car = [col for col in cat_cols if dataframe[col].nunique() > car_th]

    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    cat_cols = cat_cols + num_but_cat
    num_cols = [col for col in num_cols if col not in num_but_cat]
    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)


#numerik değişken analizi

def num_summary(dataframe, col):
    quartile = [0, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[col].describe(quartile).T)

for i in num_cols:
    num_summary(df, i)

#kategorik değişken analizi

def cat_summary(dataframe, col):
    a = pd.DataFrame