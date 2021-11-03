import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")



df = pd.read_csv("data/house_prices.csv")


df.head()


df.info()


#df.isnull().sum() # 20-30 missing Drop the column, rows
df.count() / len(df) >= 0.7


# Drop column if 30% is missing
df2 = df[[col for col in df if df[col].count() / len(df) >= 0.3]]
del df2['Id']


print("Columns Dropped:", end=" ")
for c in df.columns:
    if c not in df2.columns:
        print(c, end=", ")



round(df2.describe(), 2)


sns.distplot(df['SalePrice'], bins=100, hist_kws={'alpha':0.5});


df_num = df2.select_dtypes(exclude=['O']) # Excluding Objects


df_num.info()


df_num.hist(figsize=(20, 20), bins=50, xlabelsize=10, ylabelsize=10);


df_num_corr = df_num.corr()['SalePrice'][:-1]


sns.heatmap(df_num.corr())


# Strong Correlation with Sale Price
important_feat = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False)


print(f"There are {len(important_feat)} strongly correlated features with Sale Price.")
important_feat


for i in range(0, len(df_num.columns), 5):
    sns.pairplot(data=df_num,x_vars=df_num.columns[i:i+5],
                y_vars=['SalePrice'])


import operator


ind_feat_df = []
for i in range(0, len(df_num.columns)-1):
    temp = df_num[[df_num.columns[i], 'SalePrice']]
    temp = temp[temp[df_num.columns[i]] get_ipython().getoutput("=0 ]")
    ind_feat_df.append(temp)


all_corr = {feat.columns[0]: feat.corr()['SalePrice'][0] for feat in ind_feat_df}


all_corr = sorted(all_corr.items(), key=operator.itemgetter(1))
for (key, value) in all_corr:
    print(f"{key:>15}: {value:>15}")


important_feat = [key for key, value in all_corr if abs(value) >= 0.5]
print(f"There are {len(important_feat)} strongly correlated features with Sale Price.")
important_feat


num_corr = df_num.drop('SalePrice', axis=1).corr()


plt.figure(figsize=(10,10))
sns.heatmap(num_corr[(abs(num_corr)>=0.5)], cmap='viridis', vmax=1, vmin=-1,linewidths=.1, annot=True, square=True);


quant_feats = ['LotFrontage', 'LotArea', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'TotalBsmtSF', '1stFlrSF',
    '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
    'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 
    'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'SalePrice']


quant_df = df2[quant_feats]


quant_df.head()


feat_to_analyze = [f for f in quant_feats if f in important_feat]


feat_to_analyze.append('SalePrice')
print(feat_to_analyze)


fig, ax = plt.subplots(round(len(feat_to_analyze)/3), 3, figsize=(20, 15))

for i, ax in enumerate(fig.axes):
    if i < len(feat_to_analyze) - 1:
        sns.regplot(x=feat_to_analyze[i], y="SalePrice", data=df2[feat_to_analyze], ax=ax);


cat_feat = [c for c in quant_feats[:-1] + df2.columns.tolist() if (c not in quant_feats) or (c not in df2.columns.tolist())]


df_cat = df2[cat_feat]


df_cat.head()


df_cat_not_num = df_cat.select_dtypes(include=['O'])


print(f"There are {len(df_cat_not_num.columns)} non numerical features.")
print(df_cat_not_num.columns.tolist())


df_cat = pd.concat([df_cat, df2['SalePrice']], axis=1)


sns.boxplot(x="MSZoning", y="SalePrice", data=df_cat);


sns.boxplot(x="SaleCondition", y="SalePrice", data=df_cat);



