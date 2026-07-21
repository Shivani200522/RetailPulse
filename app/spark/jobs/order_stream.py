from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json

from app.spark.schemas.order_schema import order_schema

spark = (
    SparkSession.builder
    .appName("RetailPulse-Streaming")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "host.docker.internal:9092")
    .option("subscribe", "retail-orders")
    .load()
)

json_df = df.selectExpr("CAST(value AS STRING)")

orders = (
    json_df
    .select(
        from_json(
            col("value"),
            order_schema
        ).alias("data")
    )
    .select("data.*")
)

query = (
    orders.writeStream
    .format("console")
    .outputMode("append")
    .option("truncate", False)
    .start()
)

query.awaitTermination()