try:
    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime
    import pandas as pd
    print("All modules are imported!")
except Exception as e:
    print(f"Error while importing modules. Error - {type(e).__name__}")


def first_function_execute(**context):
    print("first_function_execute")
    context['ti'].xcom_push(key='mykey', value="'first_function_execute' says, Hello!")


def second_function_execute(**context):
    instance = context.get("ti").xcom_pull(key="mykey")
    data = [{"name": "Peter", "title": "Full Stack Software Engineer"},
            {"name": "Parker", "title": "Mechanical Engineer"}]
    df = pd.DataFrame(data=data)
    print('@' * 66)
    print(df.head())
    print('@' * 66)
    print(f"I am in 'second_function_execute' got value :{instance} from 'first_function_execute'")


dag_default_args = {"owner": "airflow",
                    "retries": 1,
                    "retry_delay": timedelta(minutes=5),
                    "start_date": datetime(2023, 5, 10)}

dag = DAG(dag_id="dag1", schedule_interval="@daily", default_args=dag_default_args, catchup=False)

task1 = PythonOperator(task_id="first_function_execute",
                       dag=dag,
                       python_callable=first_function_execute,
                       provide_context=True)

task2 = PythonOperator(task_id="second_function_execute",
                       dag=dag,
                       python_callable=second_function_execute,
                       provide_context=True)

task1 >> task2
