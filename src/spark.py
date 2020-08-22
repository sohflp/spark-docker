from pyspark.sql import SparkSession
# from pyspark import SparkContext, SparkConf

appName = "Python Spark SQL basic example"


spark = SparkSession \
    .builder \
    .appName(appName) \
    .getOrCreate()

# spark is an existing SparkSession
df = spark.read.json("./test/data/people.jsonl")

# Displays the content of the DataFrame to stdout
df.show()

#########################################
# NOT NEEDED ANYMORE
# SparkContext is part of SparkSession
#########################################
# conf = SparkConf().setAppName(appName)
# sc = SparkContext(conf=conf)
#########################################

sc = spark.sparkContext

data = [1, 2, 3, 4, 5]

# distData is an RDD (Resilient Data Distribution)
distData = sc.parallelize(data)

reducedData = distData.reduce(lambda a, b: a + b)

print("Reduced Data = {}".format(reducedData))
