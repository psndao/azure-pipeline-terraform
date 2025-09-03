from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, lit
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

spark = SparkSession.builder.appName("WeatherTransform").getOrCreate()

raw_path = "abfss://raw-data@pape2025datalake.dfs.core.windows.net/weather/raw/"
df = spark.read.text(raw_path)

schema = StructType([
    StructField("name", StringType(), True),
    StructField("main", StructType([
        StructField("temp", DoubleType(), True),
        StructField("humidity", DoubleType(), True),
    ]), True),
    StructField("weather",
        StructType([
            StructField("description", StringType(), True)
        ]), True)
])

df_parsed = df.select(from_json(col("value"), schema).alias("data"))
df_final = df_parsed.select(
    col("data.name").alias("city"),
    col("data.main.temp").alias("temperature"),
    col("data.main.humidity").alias("humidity"),
    col("data.weather.description").alias("description"),
    lit("Dakar").alias("source_city")
)

df_final.write.mode("overwrite").parquet(
    "abfss://transformed@pape2025datalake.dfs.core.windows.net/weather/"
)
