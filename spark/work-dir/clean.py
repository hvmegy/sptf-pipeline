from pyspark.sql import SparkSession
from pyspark.sql import functions as fn
from pyspark.sql.functions import col, sum as spark_sum

# Khởi tạo SparkSession với hỗ trợ Iceberg và S3
spark = (
    SparkSession.builder
    .appName("Clean Data")
    .config("spark.sql.catalog.bronze", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.bronze.type", "hadoop")
    .config("spark.sql.catalog.bronze.warehouse", "s3a://bronze/")
    .config("spark.hadoop.fs.s3a.bucket.bronze.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.bucket.bronze.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.bucket.bronze.secret.key", "admin123") \
        
    .config("spark.hadoop.fs.s3a.bucket.silver.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.bucket.silver.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.bucket.silver.secret.key", "admin123") \
    .config("spark.sql.catalog.silver", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.silver.type", "hadoop")
    .config("spark.sql.catalog.silver.warehouse", "s3a://silver/")
    
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .getOrCreate()
)

df = spark.read.table("bronze.raw.streaming_history")

df = df.select('incognito_mode', 'ip_addr', 'master_metadata_album_album_name', 'master_metadata_album_artist_name', 'master_metadata_track_name', 'ms_played', 'offline', 'platform', 'reason_end', 'reason_start', 'shuffle', 'skipped', 'spotify_track_uri', 'ts')

clean_df = df.na.drop()

clean_df.writeTo("silver.cleaned.streaming_history") \
  .using("iceberg") \
  .createOrReplace()

spark.stop()


