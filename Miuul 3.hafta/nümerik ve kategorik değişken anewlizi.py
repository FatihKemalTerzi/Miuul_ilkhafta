import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
#df = pd.read_csv("D:\Windows10\Dekstop\diabetes.csv\diabetes.csv")
df = sns.load_dataset("titanic")

def grabColNames(dataFrame, catTh=10, carTh=30):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri
    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi
    Notes
    ------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.
    """
    catCols = [col for col in df.columns if str(df[col].dtype) in ['object', 'category', "bool"]]
    numButCat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
    catButCar = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    catCols = catCols + numButCat
    catCols = [col for col in catCols if col not in catButCar]
    numCols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    numCols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    numCols = [col for col in numCols if col not in catCols]
    print(f"Observations: {dataFrame.shape[0]}")
    print(f"Variables: {dataFrame.shape[1]}")
    print(f'cat_cols: {len(catCols)}')
    print(f'num_cols: {len(numCols)}')
    print(f'cat_but_car: {len(catButCar)}')
    print(f'num_but_cat: {len(numButCat)}')

    return catCols, numCols, catButCar

print(grabColNames(df))

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("D:\Windows10\Dekstop\diabetes.csv\diabetes.csv")

def catchcolnames(df):

    """

    :return: nümerik ve kategorik değişkenleri döndürecek
    """

    catcatch = [col for col in df.columns if str(df[col].dtype) in ['object', 'category', "bool"]]
    numeric = [col for col in df.columns if df[col].dtypes in ["int", "float"]]

    return catcatch, numeric
catchcolnames(df)
