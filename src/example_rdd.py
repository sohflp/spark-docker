from pyspark.sql import SparkSession

appName = "RDD and MapReduce example"

# Get Spark Session
spark = SparkSession \
    .builder \
    .appName(appName) \
    .getOrCreate()

# Get Spark Context from Spark Session
sc = spark.sparkContext

# Generate random data from list
data = [1, 2, 3, 4, 5]

# Create a RDD (Resilient Data Distribution)
distData = sc.parallelize(data)

# Apply a reduce function on top of the original RDD
reducedData = distData.reduce(lambda a, b: a + b)

print("Reduced Data = {}".format(reducedData))
