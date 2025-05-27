from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("JSON to Iceberg on MinIO") \
    .config("spark.sql.catalog.my_catalog", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.my_catalog.type", "hadoop") \
    .config("spark.sql.catalog.my_catalog.warehouse", "s3a://my-bucket/warehouse") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "admin123") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()

# Đọc tất cả JSON trong thư mục
df = spark.read.json("/data/json/")

# Ghi vào Iceberg (s3a://my-bucket/warehouse/my_db.my_table)
df.writeTo("my_catalog.my_db.my_table").createOrReplace()
