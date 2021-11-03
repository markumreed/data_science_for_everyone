import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")


df = pd.read_csv("data/house_prices.csv")
df.head()


df.info()


# Remove ID, Remove col with 30% or less NaN Values
df_2 = df[[col for col in df if df[col].count() / len(df) >= .3]]
del df_2['Id']


print("List of dropped columns:", end=" ")
for c in df.columns:
    if c not in df_2.columns:
        print(c, end=", ")
print("\n")


df = df_2 # Because I'm lazy 


# House price distribution
df['SalePrice'].describe()


plt.figure(figsize=(10, 10))
sns.distplot(np.log(df['SalePrice']), color="g", bins=100, hist_kws={'alpha':0.4});


list(set(df.dtypes.tolist()))


df_num = df.select_dtypes(include=['float64','int64'])


df_num.head()


df_num.hist(figsize=(16,20), bins=50, xlabelsize=8, ylabelsize=8);


df_num_corr = df_num.corr()['SalePrice'][:-1]
important_feature_list = df_num_corr[abs(df_num_corr)>0.5].sort_values(ascending=False)
print(f"""
There are {len(important_feature_list)} that strongly correlate with the sales price. 
The correlations are below:
{important_feature_list}
""")


for i in range(0, len(df_num.columns), 5):
    sns.pairplot(data=df_num,
                x_vars=df_num.columns[i:i+5],
                y_vars=['SalePrice'])


import operator


ind_features_df = []
for i in range(0, len(df_num.columns)-1): # Drop SalePrice Column with the -1
    tempDF = df_num[[df_num.columns[i], 'SalePrice']]
    tempDF = tempDF[tempDF[df_num.columns[i]] get_ipython().getoutput("= 0]")
    ind_features_df.append(tempDF)


all_corr  = {feature.columns[0]: feature.corr()['SalePrice'][0] for feature in ind_features_df}
all_corr = sorted(all_corr.items(), key=operator.itemgetter(1))
for (key, value) in all_corr:
    print(f"{key:>15}: {value:>15}")


important_feature_list = [key for key, value in all_corr if abs(value) >= .5]
print(f"""
There are {len(important_feature_list)} that strongly correlate with the sales price. 
The correlations are below:
{important_feature_list}
""")


corr_not_price = df_num.drop('SalePrice', axis=1).corr()


plt.figure(figsize=(10, 10))
sns.heatmap(corr_not_price[(corr_not_price>=0.5) | (corr_not_price <=-.4)],
           cmap='viridis',vmax=1.0, vmin=-1.0, linewidths=0.1,
           annot=True, annot_kws={'size':8}, square=True);


quantitative_features_list = ['LotFrontage', 'LotArea', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'TotalBsmtSF', '1stFlrSF',
    '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
    'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 
    'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'SalePrice']


df_quant_values = df[quantitative_features_list]
df_quant_values.head()


feat_to_analyze = [x for x in quantitative_features_list if x in important_feature_list]
feat_to_analyze.append('SalePrice')
feat_to_analyze


fig, ax = plt.subplots(round(len(feat_to_analyze) / 3), 3, figsize=(20, 15))

for i , ax in enumerate(fig.axes):
    if i < len(feat_to_analyze) - 1:
        sns.regplot(x=feat_to_analyze[i], y='SalePrice', data=df[feat_to_analyze], ax=ax);


cat_feat = [a for a in quantitative_features_list[:-1] + df.columns.tolist() \
            if (a not in quantitative_features_list[:-1]) or (a not in df.columns.tolist())]


cat_df = df[cat_feat]
cat_df.head()


df_not_num = cat_df.select_dtypes(include=['O'])


print(f"There is {len(df_not_num.columns)} non numerical features including:\n{df_not_num.columns.to_list()}")


plt.figure(figsize=(10, 10))
ax = sns.boxplot(x="BsmtExposure", y="SalePrice", data=cat_df)
plt.setp(ax.artists, alpha=0.5, linewidth=2, edgecolor="k")
plt.xticks(rotation=45);


plt.figure(figsize=(15, 10))
ax = sns.boxplot(x="SaleCondition", y="SalePrice", data=cat_df)
plt.setp(ax.artists, alpha=0.5, linewidth=2, edgecolor="k")
plt.xticks(rotation=45);


fig, axes = plt.subplots(round(len(df_not_num.columns) / 3), 3, figsize=(15, 30))

for i, ax in enumerate(fig.axes):
    if i < len(df_not_num.columns):
        ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)
        sns.countplot(x=df_not_num.columns[i], alpha=0.7, data=df_not_num, ax=ax)
fig.tight_layout();



