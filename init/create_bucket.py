from minio import Minio
from minio.error import S3Error

# Khởi tạo client MinIO
client = Minio(
    "minio:9000",
    access_key="admin",
    secret_key="admin123",
    secure=False  # Nếu bạn không dùng https
)

bucket_list = ["bronze", "silver", "gold"] 

for bucket in bucket_list: 
    try:
        if not client.bucket_exists(bucket):
            client.make_bucket(bucket)
            print(f"Bucket '{bucket}' đã được tạo.")
        else:
            print(f"Bucket '{bucket}' đã tồn tại.")
    except S3Error as err:
        print(f"Error: {err}")

