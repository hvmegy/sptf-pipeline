from pyspark.sql import SparkSession
from pyspark.sql import functions as fn
from pyspark.sql.functions import col, sum as spark_sum

# Khởi tạo SparkSession với hỗ trợ Iceberg và S3
spark = (
    SparkSession.builder
    .appName("Transform Data") \
    .config("spark.sql.catalog.silver", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.silver.type", "hadoop") \
    .config("spark.sql.catalog.silver.warehouse", "s3a://silver/") \
    .config("spark.hadoop.fs.s3a.bucket.silver.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.bucket.silver.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.bucket.silver.secret.key", "admin123") \
        
    .config("spark.sql.catalog.gold", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.gold.type", "hadoop") \
    .config("spark.sql.catalog.gold.warehouse", "s3a://gold/") \
    .config("spark.hadoop.fs.s3a.bucket.gold.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.bucket.gold.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.bucket.gold.secret.key", "admin123") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .getOrCreate()
)

df = spark.read.table("silver.cleaned.streaming_history")

dim_artist = (
    df.select("master_metadata_album_artist_name")
    .distinct()
    .withColumnRenamed("master_metadata_album_artist_name", "artist_name")
    .withColumn("artist_id", fn.monotonically_increasing_id())
)

dim_album = (
    df.select("master_metadata_album_album_name")
    .distinct()
    .withColumnRenamed("master_metadata_album_album_name", "album_name")
    .withColumn("album_id", fn.monotonically_increasing_id())
)

dim_track = (
    df.select(
        "spotify_track_uri",
        "master_metadata_track_name",
        "master_metadata_album_album_name",
        "master_metadata_album_artist_name"
    )
    .distinct()
    .join(dim_album, df.master_metadata_album_album_name == dim_album.album_name, "left")
    .join(dim_artist, df.master_metadata_album_artist_name == dim_artist.artist_name, "left")
    .select(
        "spotify_track_uri",
        fn.col("master_metadata_track_name").alias("track_name"),
        "album_id",
        "artist_id"
    )
    .withColumn("track_id", fn.monotonically_increasing_id())
)

dim_platform = (
    df.select("platform")
    .distinct()
    .withColumn("platform_id", fn.monotonically_increasing_id())
)

fact_df = (
    df
    .join(dim_track, df.spotify_track_uri == dim_track.spotify_track_uri, "left")
    .join(dim_platform, "platform", "left")
    .select(
        "ts", "ms_played", "skipped", "offline", "incognito_mode",
        "reason_start", "reason_end", "shuffle",
        "track_id", "platform_id"
    )
)


dim_platform.writeTo("gold.structured.dim_platform").createOrReplace()
dim_track.writeTo("gold.structured.dim_track").createOrReplace()
dim_album.writeTo("gold.structured.dim_album").createOrReplace()
dim_artist.writeTo("gold.structured.dim_artist").createOrReplace()
fact_df.writeTo("gold.structured.fact_stream").createOrReplace()
