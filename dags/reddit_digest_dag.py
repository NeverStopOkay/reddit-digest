# dags/reddit_digest_dag.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'you',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'reddit_digest_daily',
    default_args=default_args,
    description='Generate Reddit Digest daily',
    schedule_interval='0 7 * * *',  # 7 AM daily
    start_date=datetime(2025, 11, 11),
    catchup=False,
    tags=['digest', 'reddit'],
) as dag:

    generate_post = BashOperator(
        task_id='generate_substack_post',
        bash_command='cd /app && python generate_substack_post.py',
    )

    generate_post