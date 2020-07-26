from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

# spark is an existing SparkSession
df = spark.read.json("./test/data/people.jsonl")

# Displays the content of the DataFrame to stdout
df.show()
