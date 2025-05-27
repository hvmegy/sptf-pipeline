from pyspark.sql import SparkSession

# Khởi tạo SparkSession với hỗ trợ Iceberg và S3
spark = (
    SparkSession.builder
    .appName("JSON to Iceberg on MinIO")
    .config("spark.sql.catalog.bronze", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.bronze.type", "hadoop")
    .config("spark.sql.catalog.bronze.warehouse", "s3a://bronze/")
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.bucket.bronze.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.bucket.bronze.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.bucket.bronze.secret.key", "admin123") \
    .getOrCreate()
)

input_path = "./data/"
df = spark.read.option("multiline", "true").json(input_path + "*.json")

df.printSchema()
df.show(5, truncate=False)

df.writeTo("bronze.raw.streaming_history") \
  .using("iceberg") \
  .createOrReplace()

spark.stop()
