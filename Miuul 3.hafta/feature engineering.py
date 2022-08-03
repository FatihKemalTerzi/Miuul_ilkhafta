import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import missingno as msno
from datetime import date
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

df = pd.read_csv('D:\Windows10\Dekstop\diabetes.csv\diabetes.csv')
df.head()

#Görev 1: Keşifçi veri analizi

#Genel Resim

def check_df(dataframe, head=5):
    print("######Shape#####")
    print(dataframe.shape)
    print("######Types#####")
    print(dataframe.dtypes)
    print("######Head#####")
    print(dataframe.head(head))
    print("######Tail#####")
    print(dataframe.tail(head))
    print("######NA#####")
    print(dataframe.isnull().sum)
    print("######Quantiles#####")
    print(dataframe.quantile([0, 0.05, 0.5, 0.95, 0.99, 1]).T)

check_df(df)

#Nümerik ve kategorik değişkenlerin yakalanması
#############################################

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Not: Kategorik değişkenlerin içerisinde numerik görünümlü kategorik değişkenler de dahildir.

    :param dataframe: Değişken isimleri alınmak istenilen dataframe
    :param cat_th: int, optional
                numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    :param car_th: int,optional
                kategorik fakat kardinal değişkenler için sınıf eşik değeri
    :return:
        cat_cols :list
            kategorik değişkenlerin listesi
        num_cols: list
            numerik değişkenlerin listesi
        cat_but_car: list
            Kategorik görünümlü kardinal değişken listesi
    Notes:
        cat_cols + num_cols + cat_but_car = toplam değişken sayısı
        num_but_cat cat_cols'un içerisinde
    """

    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if
                   dataframe[col].nunique() < cat_th and dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if
                   dataframe[col].nunique() > car_th and dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)

cat_cols
num_cols
cat_but_car


##################################
# KATEGORİK DEĞİŞKENLERİN ANALİZİ
##################################

#cat
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()

cat_summary(df, "Outcome")


##################################
# NUMERİK DEĞİŞKENLERİN ANALİZİ
##################################

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist(bins=20)
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show()


for col in num_cols:
    num_summary(df, col, plot=True)
