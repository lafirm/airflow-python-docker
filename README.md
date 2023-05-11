# Airflow w/ Python and Docker

Follow either the steps mentioned in this [page](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) or the steps below.

- Download the official **`docker-compose yaml`** file using the command below inside your project repo:

```shell
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.6.0/docker-compose.yaml'
```
- Create folder in your repo to synchronize between your computer and the container namely
dags, logs and plugins
- Create a Dockerfile with base image as `apache/airflow:2.6.0-python3.10` and install  the dependencies using `requirements.txt`
- Edit the downloaded file **`docker-compose yaml`**
  * Comment this line `image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.6.0}` and uncomment this line `build: .`, 
if you want to use your custom image using Dockerfile using `apache/airflow:2.6.0-python3.10`
  * Change `CeleryExecutor` to `LocalExecutor`
  * Comment lines corresponding to `CeleryExecutor` and `Redis` services (Redis is used with `CeleryExecutor`)
  * Comment services like `airflow-worker` and `airflow-flower`
- Run the command `docker-compose up -d`
- Use this url `http://localhost:8080/` to see airflow UI (it takes some time to start all the services)
- username = **airflow** and password = **airflow**
- Now, you can see the list of DAGs you created


## Useful Resources:
- [Airflow Docker Image](https://hub.docker.com/r/apache/airflow)
- [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
- [Airflow Docs](https://airflow.apache.org/docs/apache-airflow/2.0.1/)
- [Python Operator in Airflow](https://hevodata.com/learn/python-operator-in-airflow/)
- [Simple Airflow Docker Script](https://github.com/soumilshah1995/Learn-Apache-Airflow-in-easy-way-/)