get_ipython().getoutput("apt-get install openjdk-8-jdk-headless -qq > /dev/null")
get_ipython().getoutput("wget -q https://www-us.apache.org/dist/spark/spark-3.0.2/spark-3.0.2-bin-hadoop2.7.tgz")


get_ipython().getoutput("tar xf spark-3.0.2-bin-hadoop2.7.tgz")
get_ipython().getoutput("pip install -q findspark")


import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.0.2-bin-hadoop2.7"


import findspark
findspark.init()


from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("pyspark_basics").getOrCreate()


get_ipython().run_cell_magic("writefile", " user_simple.json", """{"name":"Bob"}
{"name":"Jim", "age":40}
{"name":"Mary", "age": 24}""")


df = spark.read.json("user_simple.json")


df


df.show()


df.printSchema()


df.columns


df.describe()


df.describe().show()


from pyspark.sql.types import StructField, StringType, IntegerType, StructType


data_schema = [StructField("age", IntegerType(), True), StructField("name",StringType(), True)]


final_struc = StructType(fields=data_schema)


df = spark.read.json("user_simple.json", schema=final_struc)


df.printSchema()


df.show()


df['age']


type(df['age'])


df.select("age")


type(df.select("age"))


df.select("age").show()


df.head(2)


df.select(["name","age"])


df.select(["name","age"]).show()


df.withColumn("newAge", df['age']).show()


df.show()


df.withColumnRenamed("name","firstName").show()


df.show()


df.withColumn("agePlusTen", df['age']+10).show()


df.withColumn("age_minus_5", df['age']-5).show()


df.createOrReplaceTempView("custmers")


sql_results = spark.sql("SELECT * from custmers")


sql_results


sql_results.show()


spark.sql("SELECT * FROM custmers WHERE age=24").show()





get_ipython().getoutput("curl https://raw.githubusercontent.com/markumreed/colab_pyspark/main/WMT.csv >> WMT.csv")


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("operations").getOrCreate()
df = spark.read.csv('WMT.csv',inferSchema=True,header=True)


df.printSchema()


df.head(5)


df.filter('Close<62').show()


df.filter('Close<62').select('Open').show()


df.filter('Close<62').select(['Date','Open']).show()


df.filter(df['Close'] < 62).show()


df.filter((df['Close'] < 62) & ~(df['Open'] > 60)).show()


df.filter(df['Open'] == 60.98).show(1)


df.filter(df['Open'] == 60.98).collect()


res =df.filter(df['Open'] == 60.98).collect()


type(res[0])


res[0].asDict()


for item in res[0]:
  print(item)


import pandas as pd


pd.Series(res[0].asDict())





from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("groupbyagg").getOrCreate()


get_ipython().getoutput("curl https://raw.githubusercontent.com/markumreed/colab_pyspark/main/sales_data.csv >> sales_data.csv")


df = spark.read.csv("sales_data.csv", inferSchema=True, header=True)


df.printSchema()


df.show()


df.groupBy("company")


df.groupBy("company").mean().show()


df.groupBy("company").count().show()


df.groupBy("company").min().show()


df.groupBy("company").max().show()


df.groupBy("company").sum().show()


df.agg({"num_sales":"max"}).show()


df.groupBy("company").agg({"num_sales":"mean"}).show()


company_groups = df.groupBy("company")


company_groups.min().show()


from pyspark.sql.functions import countDistinct, avg, stddev


df.select(countDistinct("num_sales")).show()


df.select(avg("num_sales")).show()


df.select(stddev("num_sales")).show()


df.select(countDistinct("num_sales").alias("ANYTHING WE WANT")).show()





from pyspark.sql.functions import format_number


sales_std = df.select(stddev("num_sales").alias("stddev"))


sales_std.show()


sales_std.select(format_number("stddev",2)).show()


df.orderBy("num_sales").show() # Ascending Order


df.orderBy(df['num_sales'].desc()).show()





get_ipython().getoutput("curl https://raw.githubusercontent.com/markumreed/colab_pyspark/main/missing_data.csv >> missing_data.csv")


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("missing_data").getOrCreate()


df = spark.read.csv("missing_data.csv", header=True, inferSchema=True)


df.show()


df.printSchema()


df.na.drop().show()


df.na.drop(thresh=2).show()


df.na.drop(subset=['sales']).show()


df.na.drop(how='any').show()


df.na.drop(how='all').show()


df.na.fill('SOME VALUE').show()


df.na.fill(999).show()


df.na.fill("Missing Name", subset=["name"]).show()


from pyspark.sql.functions import mean


mean_value = df.select(mean(df['sales'])).collect()


mean_sales_value = mean_value[0][0]


df.na.fill(mean_sales_value, ["sales"]).show()


# DON'T DO THIS
df.na.fill(df.select(mean(df['sales'])).collect()[0][0] ,['sales']).show() # NOT EASY TO READ


get_ipython().getoutput("curl https://raw.githubusercontent.com/markumreed/colab_pyspark/main/WMT.csv >> WMT.csv")


spark = SparkSession.builder.appName('walmart_dates').getOrCreate()


df = spark.read.csv('WMT.csv', header=True, inferSchema=True)


df.show()


from pyspark.sql.functions import format_number, dayofmonth, hour, dayofyear, month, year, weekofyear, date_format


df.select(dayofmonth(df['Date'])).show()


df.select(hour(df['Date'])).show()


df.select(dayofyear(df['Date'])).show()


df.select(month(df['Date'])).show()


df.select(month(df['Date'])).show()


df.withColumn("Month", month(df['Date'])).show()


df2 = df.withColumn("Month", month(df['Date']))


df2.groupBy("Month").mean()[['avg(Month)', 'avg(Close)']].show()


res = df2.groupBy("Month").mean()[['avg(Month)', 'avg(Close)']]
res = res.withColumnRenamed("avg(Month)", "Month")
res = res.select("Month", format_number('avg(Close)',2).alias("Mean Close")).show()


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("walmart_stock").getOrCreate()


df = spark.read.csv("walmart_stock.csv", header=True, inferSchema=True)


df.columns


df.printSchema()


df.head(5)


df.describe().show()


df.describe().printSchema()


from pyspark.sql.functions import format_number


res = df.describe()


df.describe().columns


res.select(res["summary"],
             format_number(res['Open'].cast('float'), 2).alias('Open'),
             format_number(res['High'].cast('float'), 2).alias('High'),
             format_number(res['Low'].cast('float'), 2).alias('Low'),
             format_number(res['Close'].cast('float'), 2).alias('Close'),
             res['Volume'] .cast('int').alias('Volume')
             ).show()


# High vs Volume
df2 = df.withColumn("HV Ratio", df['High']/df['Volume'])


df2.show()


df2.select('HV Ratio').show()


df.orderBy(df['High'].desc()).head(1)[0][0]


from pyspark.sql.functions import mean
df.select(mean('Close')).show()


from pyspark.sql.functions import max, min


df.select(max('Volume'), min('Volume')).show()


df.filter("Close < 60").count()


from pyspark.sql.functions import count


res = df.filter('Close < 60')
res.select(count('Close')).show()


(df.filter('High > 80').count() * 1.0/df.count()) * 100


from pyspark.sql.functions import corr


df.select(corr('High', 'Volume')).show()


from pyspark.sql.functions import year
yeardf = df.withColumn("Year", year(df['Date']))


max_df = yeardf.groupBy('Year').max()


max_df.select('Year', 'max(High)').show()


max_df.show()


from pyspark.sql.functions import month


monthdf = df.withColumn("Month", month("Date"))
monthavgs = monthdf.select("Month", "Close").groupBy("Month").mean()
monthavgs.select("Month", "avg(Close)").orderBy('Month').show()


get_ipython().getoutput("curl https://raw.githubusercontent.com/markumreed/colab_pyspark/main/appl_stock.csv >> apple_stock.csv")


get_ipython().getoutput("curl https://raw.githubusercontent.com/apache/spark/master/data/mllib/sample_linear_regression_data.txt >> sample_linear_regression_data.txt")


from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("lr_ex").getOrCreate()


from pyspark.ml.regression import LinearRegression


training = spark.read.format("libsvm").load("sample_linear_regression_data.txt")


training.show()


lr = LinearRegression(featuresCol="features", labelCol="label", predictionCol="prediction")


lrModel = lr.fit(training)


print("Coefficients:", str(lrModel.coefficients))
print("Intercept:", str(lrModel.intercept))


trainSummary = lrModel.summary


print("MAE: ", trainSummary.meanAbsoluteError)
print("MSE: ", trainSummary.meanSquaredError)
print("RMSE: ", trainSummary.rootMeanSquaredError)
print("R2: ", trainSummary.r2)
print("Adj R2: ", trainSummary.r2adj)



df = spark.read.format("libsvm").load("sample_linear_regression_data.txt") # FULL DATASET


train_data, test_data = df.randomSplit([0.7, 0.3], seed=42)


test_data.show()


unlabeled_data = test_data.select('features')


corrected_model = lr.fit(train_data) 


res = corrected_model.evaluate(test_data)


print("MAE: ", res.meanAbsoluteError)
print("MSE: ", res.meanSquaredError)
print("RMSE: ", res.rootMeanSquaredError)
print("R2: ", res.r2)
print("Adj R2: ", res.r2adj)


predictions = corrected_model.transform(unlabeled_data)


predictions.show()


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('data_transformer').getOrCreate()


df = spark.read.csv('customers.csv', inferSchema=True, header=True)


df.printSchema()


df.show()


from pyspark.ml.feature import StringIndexer

df2 = spark.createDataFrame(
    [(0,"a"), (1, "b"), (2, "c"), (3, "a"), (4, "b"), (5, "c")],
    ["user_id", "category"]
)


df2.show()


indexer = StringIndexer(inputCol="category", outputCol="categoryIndex")


indexed = indexer.fit(df2).transform(df2)


indexed.show()


from pyspark.ml.linalg import Vectors 
from pyspark.ml.feature import VectorAssembler


df3 = spark.createDataFrame(
    [(0, 18, 1.0, Vectors.dense([0.0, 10.0, 0.5]), 1.0)],
    ["id", "hour", "mobile", "userFeatures", "clicked"]
)
df3.show()


assembler = VectorAssembler(
    inputCols = ["hour", "mobile", "userFeatures"],
    outputCol = "features"
)
output = assembler.transform(df3)


output.select("features", "clicked").show()


df.show()


indexer = StringIndexer(inputCol="Group", outputCol="groupIndex")
indexed = indexer.fit(df).transform(df)
indexed.show()


assembler = VectorAssembler(
    inputCols = ["Phone", "groupIndex"],
    outputCol = "features"
)
output = assembler.transform(indexed)
output.select("Name", "features").show()





from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("lin_reg").getOrCreate()


df = spark.read.csv("Ecommerce_Customers.csv", inferSchema=True, header=True)


df.printSchema()


df.show()


df.head()


from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler


df.columns


assembler = VectorAssembler(inputCols=['Avg Session Length', 'Time on App',
                                       'Time on Website','Length of Membership'],
                            outputCol='features')


output = assembler.transform(df)


output.select("features").show()


final_data = output.select("features", "Yearly Amount Spent")


train_data, test_data = final_data.randomSplit([0.7, 0.3])


train_data.describe().show()


test_data.describe().show()


from pyspark.ml.regression import LinearRegression


lr = LinearRegression(labelCol='Yearly Amount Spent')


model = lr.fit(train_data)


import pandas as pd


pd.DataFrame({"Coefficients":model.coefficients}, index=['Avg Session Length', 'Time on App',
                                       'Time on Website','Length of Membership'])


res = model.evaluate(test_data)


res.residuals.show()


unlabeled_data = test_data.select("features")


predictions = model.transform(unlabeled_data)


predictions.show()


print("MAE:", res.meanAbsoluteError)
print("MSE:", res.meanSquaredError)
print("RMSE:", res.rootMeanSquaredError)
print("R2", res.r2)
print("Adj R2", res.r2adj)





from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("log_reg").getOrCreate()


get_ipython().getoutput("curl https://raw.githubusercontent.com/apache/spark/master/data/mllib/sample_libsvm_data.txt >> sample_libsvm_data_2.txt")


df = spark.read.format("libsvm").load("sample_libsvm_data.txt")


df.printSchema()


from pyspark.ml.classification import LogisticRegression


lr = LogisticRegression()

model = lr.fit(df)

summary = model.summary


summary.predictions.show()


from pyspark.mllib.evaluation import MulticlassMetrics


model.evaluate(df)


pred_and_labels = model.evaluate(df)


pred_and_labels.predictions.show()


pred_and_labels = pred_and_labels.predictions.select("label", "prediction")


pred_and_labels.show()


from pyspark.ml.evaluation import BinaryClassificationEvaluator, MulticlassClassificationEvaluator


eval = BinaryClassificationEvaluator(rawPredictionCol="prediction", labelCol="label")


eval_multi = MulticlassClassificationEvaluator(predictionCol="prediction", 
                                               labelCol="label", 
                                               metricName="accuracy")


acc = eval.evaluate(pred_and_labels)


acc


get_ipython().getoutput("curl https://raw.githubusercontent.com/markumreed/colab_pyspark/main/titanic.csv >> titanic_2.csv")


from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("titanic").getOrCreate()


df = spark.read.csv("titanic.csv", inferSchema=True, header=True)


df.printSchema()


df.columns


data = df.select([
 'Survived',
 'Pclass',
 'Sex',
 'Age',
 'SibSp',
 'Parch',
 'Fare',
 'Embarked'])


data.head()


data_final = data.na.drop()


from pyspark.ml.feature import (VectorAssembler, VectorIndexer,
                                OneHotEncoder, StringIndexer)


gender_indexer = StringIndexer(inputCol="Sex", outputCol="SexIndex")
gender_ecoder = OneHotEncoder(inputCol="SexIndex", outputCol="SexVec")

embark_indexer = StringIndexer(inputCol="Embarked", outputCol="EmbarkIndex")
embark_ecoder = OneHotEncoder(inputCol="EmbarkIndex", outputCol="EmbarkVec")



assembler = VectorAssembler(inputCols=["Pclass", "SexVec", "Age", "SibSp",
                                       "Parch", "Fare", "EmbarkVec"],
                            outputCol="features")


from pyspark.ml.classification import LogisticRegression


from pyspark.ml import Pipeline


lr = LogisticRegression(featuresCol='features', labelCol="Survived")


pipeline = Pipeline(stages=[
                            gender_indexer,embark_indexer,
                            gender_ecoder,embark_ecoder,
                            assembler, lr
])


train, test = data_final.randomSplit([0.7, 0.3], seed=42)


model_fit = pipeline.fit(train)
res = model_fit.transform(test)


from pyspark.ml.evaluation import BinaryClassificationEvaluator


eval = BinaryClassificationEvaluator(rawPredictionCol='prediction',
                                     labelCol='Survived')


res.select('Survived', 'prediction').show()


auc = eval.evaluate(res)


auc


get_ipython().getoutput("curl https://raw.githubusercontent.com/apache/spark/master/data/mllib/sample_kmeans_data.txt >> sample_kmeans_data.txt")


get_ipython().getoutput("curl https://archive.ics.uci.edu/ml/machine-learning-databases/00236/seeds_dataset.txt >> seeds_dataset.txt")


from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("sample_cluster").getOrCreate()


from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator


df = spark.read.format("libsvm").load("sample_kmeans_data.txt")


df.show()


kmeans = KMeans().setK(2).setSeed(42)
model = kmeans.fit(df)


pred = model.transform(df)


eval = ClusteringEvaluator()


silhouette = eval.evaluate(pred)
print(f"Silhouette with squared euclidean distance: {silhouette}")


centers = model.clusterCenters()
print("Cluster Centers:")
print("=================")
for center in centers:
  print(center)


from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("seeds").getOrCreate()


from pyspark.ml.clustering import KMeans


df = spark.read.csv("seeds_dataset.csv", header=True, inferSchema=True)


df.show()


df.describe().show()


from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler


df.columns


assembler = VectorAssembler(inputCols=df.columns, outputCol='features')


df_final = assembler.transform(df)


df_final.show()


from pyspark.ml.feature import StandardScaler


scaler = StandardScaler(inputCol='features',outputCol='scaledFeatures', withStd=True, withMean=False)


scaledModel = scaler.fit(df_final)


df_final = scaledModel.transform(df_final)


df_final.show()


kmeans = KMeans(featuresCol='scaledFeatures', k=3)
model = kmeans.fit(df_final)


pred = model.transform(df_final)


from pyspark.ml.evaluation import ClusteringEvaluator


eval = ClusteringEvaluator()


silhouette = eval.evaluate(pred)
print(f"Silhouette with squared euclidean distance: {silhouette}")


centers = model.clusterCenters()
print("Cluster Centers:")
for center in centers:
  print(center)





from pyspark.ml import Pipeline
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("rf").getOrCreate()


df = spark.read.format("libsvm").load("sample_libsvm_data.txt")


df.show()


(train, test) = df.randomSplit([0.7, 0.3], seed=42)


test.show()


train.printSchema()


rf = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=20,seed=42)


model = rf.fit(train)


pred = model.transform(test)


pred.printSchema()


pred.select("prediction", "label", "features").show(5)


eval = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")


acc = eval.evaluate(pred)


print("Test Error = get_ipython().run_line_magic("g"", " % (1.0 - acc))")


model.featureImportances


from pyspark.ml.classification import GBTClassifier


gbt = GBTClassifier(labelCol="label", featuresCol="features", maxIter=10, seed=42)


model = gbt.fit(train)


pred = model.transform(test)


pred.select("prediction", "label", "features").show(5)


eval = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
acc = eval.evaluate(pred)
print("Test Error = get_ipython().run_line_magic("g"", " % (1.0 - acc))")


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("trees").getOrCreate()


df = spark.read.csv("College.csv", inferSchema=True, header=True)


df.printSchema()


df.head(2)


df.columns


# "label", "features"
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler


df.printSchema()


df.columns


assembler = VectorAssembler(
    inputCols=['Apps',
 'Accept',
 'Enroll',
 'Top10perc',
 'Top25perc',
 'F_Undergrad',
 'P_Undergrad',
 'Outstate',
 'Room_Board',
 'Books',
 'Personal',
 'PhD',
 'Terminal',
 'S_F_Ratio',
 'perc_alumni',
 'Expend',
 'Grad_Rate'          
    ],
    outputCol="features"
)


output = assembler.transform(df)


from pyspark.ml.feature import StringIndexer


indexer = StringIndexer(inputCol="Private", outputCol="PrivateIndexer")
output_fixed = indexer.fit(output).transform(output)


df_final = output_fixed.select("features", "PrivateIndexer")


train, test = df_final.randomSplit([0.7, 0.3], seed=42)


from pyspark.ml.classification import DecisionTreeClassifier, RandomForestClassifier, GBTClassifier
from pyspark.ml import Pipeline


dtc = DecisionTreeClassifier(labelCol="PrivateIndexer", featuresCol="features")
rfc = RandomForestClassifier(labelCol="PrivateIndexer", featuresCol="features")
gbt = GBTClassifier(labelCol="PrivateIndexer", featuresCol="features")


dtc_model = dtc.fit(train)
rfc_model = rfc.fit(train)
gbt_model = gbt.fit(train)


dtc_pred = dtc_model.transform(test)
rfc_pred = rfc_model.transform(test)
gbt_pred = gbt_model.transform(test)


from pyspark.ml.evaluation import MulticlassClassificationEvaluator


evaluator = MulticlassClassificationEvaluator(labelCol="PrivateIndexer", predictionCol="prediction", metricName="accuracy")


dtc_acc = evaluator.evaluate(dtc_pred)
rfc_acc = evaluator.evaluate(rfc_pred)
gbt_acc = evaluator.evaluate(gbt_pred)


print("-"*10)
print(f"DT Acc: {dtc_acc}")
print("-"*10)
print(f"RFC Acc: {rfc_acc}")
print("-"*10)
print(f"GBT Acc: {gbt_acc}")
print("-"*10)



