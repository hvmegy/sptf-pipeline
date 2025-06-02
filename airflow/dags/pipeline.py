from airflow import DAG
from datetime import datetime
from datetime import timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

scripts_path = "$HOME/scripts/"

with DAG(
    'pipeline',
    default_args={
        "depends_on_past": False,
        "retries": 5,
        "retry_delay": timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function, # or list of functions
        # 'on_success_callback': some_other_function, # or list of functions
        # 'on_retry_callback': another_function, # or list of functions
        # 'sla_miss_callback': yet_another_function, # or list of functions
        # 'on_skipped_callback': another_function, #or list of functions
        # 'trigger_rule': 'all_success'
        "start_date": datetime(2024, 1, 1),
    },
    description='A DAG to manage and interact with containers in Docker Compose',
    schedule=timedelta(days=1),
    catchup=False,
) as dag:
        start = EmptyOperator(task_id='start')
        
        init = EmptyOperator(task_id='init')
        pipeline = EmptyOperator(task_id='pipeline')
        
        create_bucket = BashOperator( 
            task_id="init_buckets",
            bash_command=scripts_path + "create_bucket.sh ",                            
        )
        
        init_clickhouse = BashOperator(
            task_id="init_clickhouse",
            bash_command=scripts_path + "init_clickhouse.sh "
        )
        
        ingest = BashOperator( 
            task_id="ingest",
            bash_command=scripts_path + "ingest.sh "
        )
        
        clean = BashOperator( 
            task_id="clean", 
            bash_command=scripts_path + "clean.sh "                     
        )
        
        transform = BashOperator( 
            task_id="transform",
            bash_command=scripts_path + "transform.sh "
        )
        load = BashOperator( 
            task_id="load",
            bash_command=scripts_path + "load.sh "
        )
        finish = BashOperator(
            task_id="finish",
            bash_command=scripts_path + "finish.sh "
        )
        
        start >> init 
        init >> [create_bucket, init_clickhouse]
        [create_bucket, init_clickhouse] >> pipeline
        pipeline >> ingest >> clean >> transform >> load >> finish
        
        