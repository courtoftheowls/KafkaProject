from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import json


def stream_data():
    import finnhub
    finnhub_client = finnhub.Client(api_key="cqm5d4hr01qoqqs7vlp0cqm5d4hr01qoqqs7vlpg")
    res = finnhub_client.quote('AAPL')
    print(json.dumps(res, indent=3))


default_args = {
    'owner': 'airflow',
    'start': datetime(2024,9,1,10,00)
}

# with DAG('user_automation',
#          default_args=default_args,
#          schedule_interval='@daily',
#          catchup=False) as dag:
    
#     streaming_task = PythonOperator(
#         task_id='streaming_data',
#         python_callable=stream_data
#     )

stream_data()