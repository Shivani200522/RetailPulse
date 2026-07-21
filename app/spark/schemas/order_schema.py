from pyspark.sql.types import *

order_schema = StructType([
    StructField("event_id", StringType(), True),
    StructField("event_type", StringType(), True),
    StructField("event_timestamp", StringType(), True),
    StructField("source", StringType(), True),

    StructField("order_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("product_id", StringType(), True),
    StructField("store_id", StringType(), True),

    StructField("quantity", IntegerType(), True),
    StructField("unit_price", DoubleType(), True),
    StructField("discount_percent", DoubleType(), True),
    StructField("final_price", DoubleType(), True),

    StructField("payment_method", StringType(), True),
    StructField("payment_status", StringType(), True)
])