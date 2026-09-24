from datetime import datetime, timedelta

from airflow.sdk import DAG, task
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig

from config.config import BIGQUERY_TABLES


DBT_PROJECT_PATH = "/usr/local/airflow/dbt"
DBT_EXECUTABLE_PATH = "/usr/local/airflow/dbt_venv/bin/dbt"
DBT_PROFILES_PATH = "/usr/local/airflow/.dbt/profiles.yml"


with DAG(
    dag_id="dataplatform_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args={
        "retries":2,
        "retry_delay":timedelta(minutes=2),
    },
) as dag:

    @task
    def ingest(table):
        from ingestion.bigquery.run import ingest_table

        ingest_table(table)

    ingestion_tasks = [
        ingest.override(task_id=f"ingest_{table}")(table)
        for table in BIGQUERY_TABLES
    ]

    dbt_transformation = DbtTaskGroup(
        group_id="dbt_transformation",

        project_config=ProjectConfig(
            dbt_project_path=DBT_PROJECT_PATH,
        ),

        profile_config=ProfileConfig(
            profile_name="transformation_dbt",
            target_name="dev",
            profiles_yml_filepath=DBT_PROFILES_PATH,
        ),

        execution_config=ExecutionConfig(
            dbt_executable_path=DBT_EXECUTABLE_PATH,
        ),

        operator_args={
            "install_deps": True,
        },
    )

    ingestion_tasks >> dbt_transformation