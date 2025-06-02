ls
cd
pwd
cd .. 
ls
exit
ls
cd
cd /
ls
cd opt
ls -a
cd spark/
ls -a
cd /etc
ls
cd spark
exit
/opt/spark/bin/spark-submit ingest.py 
spark-submit   --packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.3.0 ingest.py 
/opt/spark/bin/spark-submit --packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.3.0 \ ingest.py
exit
ls
/opt/spark/bin/spark-submit --packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.3.0 \ ingest.py
/opt/spark/bin/spark-submit --packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.3.0 ingest.py
    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions     --conf spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkSessionCatalog     --conf spark.sql.catalog.spark_catalog.type=hive     --conf spark.sql.catalog.local=org.apache.iceberg.spark.SparkCatalog     --conf spark.sql.catalog.local.type=hadoop     --conf spark.sql.catalog.local.warehouse=$PWD/warehouse \
/opt/spark/bin/spark-submit --packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.3.0 ingest.py
/opt/spark/bin/spark-submit --packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.5.0,org.apache.hadoop:hadoop-aws:3.3.4,software.amazon.awssdk:s3:2.17.106 ingest.py
/opt/spark/bin/spark-submit --packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.5.0,org.apache.hadoop:hadoop-aws:3.3.4,software.amazon.awssdk:s3:2.17.106 ingest.py
clear
/opt/spark/bin/spark-submit --packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.5.0,org.apache.hadoop:hadoop-aws:3.3.4,software.amazon.awssdk:s3:2.17.106 ingest.py
./submit_ingest.sh 
cd .. 
ls
ls
cd .. 
ls
cd .. 
ls
cd conf
cd spark
cd home
ls
cd spark
ls
cd
./submit_ingest.sh 
clear
./submit_clean.sh
./submit_clean.sh
./submit_ingest.sh 
./submit_ingest.sh 
./submit_ingest.sh 
./submit_ingest.sh 
./submit_ingest.sh 
./submit_ingest.sh 
./submit_clean.sh
./submit_clean.sh
pyspark clean.py
/opt/spark/bin/pyspark clean.py
pyspark clean.py
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
./submit_clean.sh
cleả
clear
exit 
cd
ls
./submit_transform.sh 
./submit_transform.sh 
./submit_transform.sh 
pyspark --packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.5.0,org.apache.hadoop:hadoop-aws:3.3.4,software.amazon.awssdk:s3:2.17.106
/opt/spark/bin/pyspark --packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.5.0,org.apache.hadoop:hadoop-aws:3.3.4,software.amazon.awssdk:s3:2.17.106
exit
/
submit_transform
./submit_transform.sh 
echo $SPARK_HOME
ls
cd $SPARK_HOME
ls
cd
./submit_transform.sh 
./submit_transform.sh 
exit
ls
./submit_load.sh
./submit_load.sh
spark.jars.packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.5.0,org.apache.hadoop:hadoop-aws:3.3.4,software.amazon.awssdk:s3:2.17.106, \
echo $SPARK_CONF_DIR
exit
./spark_submit
./submit_load.sh 
./submit_load.sh 
./submit_transform.sh 
./submit_clean.sh 
./submit_load.sh 
./submit_load.sh 
./submit_load.sh 
./submit_load.sh 
exit
./submit_load.sh 
./submit_load.sh 
./submit_load.sh 
./submit_load.sh 
./submit_load.sh 
exit
ls
ssh clickhouse
exit
./submit_load.sh 
exit
