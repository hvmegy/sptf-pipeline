from airflow import DAG
from datetime import datetime
from datetime import timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator

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
        start = DummyOperator(task_id='start')
        
        create_bucket = BashOperator( 
            task_id="init_buckets",
            bash_command=scripts_path + "create_bucket.sh ",                            
        )
        
        ingest = BashOperator( 
            task_id="ingest",
            bash_command=scripts_path + "ingest.sh "
        )
        
        clean = BashOperator( 
            task_id="clean", 
            bash_command=scripts_path + "clean.sh "                     
        )
        
        start >> create_bucket >> ingest >> clean 