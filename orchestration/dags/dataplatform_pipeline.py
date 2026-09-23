from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig


DBT_PROJECT_PATH = "/usr/local/airflow/dbt"
DBT_EXECUTABLE_PATH = "/usr/local/airflow/dbt_venv/bin/dbt"
DBT_PROFILES_PATH = "/usr/local/airflow/.dbt/profiles.yml"


dbt_dag = DbtDag(
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

    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    dag_id="dbt_transformation",
)