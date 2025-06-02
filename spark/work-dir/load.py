from pyspark.sql import SparkSession
from pyspark.sql import functions as fn
from pyspark.sql.functions import col, sum as spark_sum

# Khởi tạo SparkSession với hỗ trợ Iceberg và S3
spark = (
    SparkSession.builder
    .appName("Load Data") \
    .config("spark.hadoop.fs.s3a.bucket.gold.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.bucket.gold.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.bucket.gold.secret.key", "admin123") \
    .config("spark.sql.catalog.gold", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.gold.type", "hadoop") \
    .config("spark.sql.catalog.gold.warehouse", "s3a://gold/") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .getOrCreate()
)

url = "jdbc:clickhouse://clickhouse:8123/streaming_history"
user = "root" 
password = "root"  
driver = "com.clickhouse.jdbc.ClickHouseDriver"


dim_album = spark.read.table("gold.structured.dim_album")
dim_artist = spark.read.table("gold.structured.dim_artist")
dim_track = spark.read.table("gold.structured.dim_track")
dim_platform = spark.read.table("gold.structured.dim_platform")
fact_stream = spark.read.table("gold.structured.fact_stream")

tables = [
    (dim_album, "dim_album"),
    (dim_artist, "dim_artist"),
    (dim_track, "dim_track"),
    (dim_platform, "dim_platform"),
    (fact_stream, "fact_stream")
]

for df, table_name in tables:
    print(f"Writing {table_name} to ClickHouse...")
    df.write \
        .format("jdbc") \
        .option("url", url) \
        .option("dbtable", f"streaming_history.{table_name}") \
        .option("driver", driver) \
        .option("user", user) \
        .option("password", password) \
        .mode("append") \
        .save()

