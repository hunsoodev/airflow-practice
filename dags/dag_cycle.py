import airflow.utils.dates
from airflow import DAG
from airflow.operators.dummy import DummyOperator

dag = DAG(
    dag_id="dag_cycle_test",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval=None,
)

t1 = DummyOperator(task_id="t1", dag=dag)
t2 = DummyOperator(task_id="t2", dag=dag)
t3 = DummyOperator(task_id="t3", dag=dag)
t4 = DummyOperator(task_id="t4", dag=dag)

t1 >> t2 >> t3 >> t4
