from pyspark.sql import SparkSession

appName = "Data Frame load from JSON"

# Get Spark Session
spark = SparkSession \
    .builder \
    .appName(appName) \
    .getOrCreate()

# spark is an existing SparkSession
df = spark.read.json("./data/people.jsonl")

# Displays the content of the DataFrame to stdout
df.show()