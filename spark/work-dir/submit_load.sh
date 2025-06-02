/opt/spark/bin/spark-submit \
--packages \
org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.5.0,\
org.apache.hadoop:hadoop-aws:3.3.4,\
software.amazon.awssdk:s3:2.17.106,\
com.clickhouse:clickhouse-jdbc:0.6.0 \
/opt/spark/work-dir/load.py