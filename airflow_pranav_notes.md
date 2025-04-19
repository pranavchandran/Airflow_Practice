
# 📘 Apache Airflow — Pranav's Learning Summary

## ✅ What is Apache Airflow?
Airflow is an open-source tool for **workflow automation** and **orchestration**.  
It helps schedule and manage complex data pipelines using **DAGs** (Directed Acyclic Graphs).

---

## 🧱 Core Concepts

| Term | Description |
|------|-------------|
| **DAG** | A Directed Acyclic Graph – defines your workflow |
| **Task** | A unit of work – usually a Python function or shell command |
| **Operator** | A wrapper that runs tasks (e.g. PythonOperator, BashOperator) |
| **Scheduler** | Triggers DAG runs based on time or condition |
| **Executor** | Executes the tasks (Local, Celery, Kubernetes, etc.) |
| **Web UI** | Dashboard to manage, trigger, and monitor DAGs |

---

## 🧑‍💻 DAG Skeleton Example

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def my_task():
    print("Hello Airflow!")

default_args = {
    'start_date': datetime(2025, 4, 10),
    'retries': 1
}

with DAG('my_first_dag',
         schedule_interval='@daily',
         default_args=default_args,
         catchup=False
         ) as dag:

    task = PythonOperator(
        task_id='say_hello',
        python_callable=my_task
    )
```

---

## ⚙️ Important DAG Configs (`default_args`)

| Key | Use |
|-----|-----|
| `start_date` | When DAG starts running |
| `retries` | Number of retry attempts for failed task |
| `retry_delay` | Time between retries |
| `catchup` | If `True`: runs all missed DAGs since `start_date` |
| `depends_on_past` | If `True`: only runs if previous run was successful |
| `execution_timeout` | Kills task if it runs too long |
| `email_on_failure` | Sends email if task fails |

---

## 📅 catchup: True vs False

- `True`: Backfills missed DAG runs since `start_date`
- `False`: Only runs current/new scheduled runs

✅ Use `context['execution_date']` inside your function to get the logical run date.

---

## ⚠️ `datetime.now()` vs `execution_date`

| Code | Output |
|------|--------|
| `datetime.now()` | Actual current system time |
| `context['execution_date']` | Airflow’s logical time for that run |

---

## 🔄 Retrying Tasks

```python
'retries': 3,
'retry_delay': timedelta(minutes=5)
```

This will retry the task 3 times with a 5-minute gap if it fails.

---

## 🔧 max_active_runs

Limits how many **parallel DAG runs** are allowed.

- `max_active_runs = 1`: ensures only one DAG run happens at a time.
- Useful to avoid data overlap or overload.

---

## 📈 Logs & Monitoring

- Use **logging.info()** inside tasks to track output.
- View logs via **UI → DAG → Run → Task → Log**.

---

## ✅ Final Task Used for Validation

```python
def print_exec_date(**context):
    execution_date = context['execution_date']
    print(f"Execution date: {execution_date}")
```

Used with `catchup=True` to simulate real-world backfill logic.

---

## 🛠️ Tools & Setup

- Used **WSL (Ubuntu)** on Windows for running Airflow
- Ran commands:
  - `airflow db init`
  - `airflow webserver --port 8080`
  - `airflow scheduler`
- Created DAGs in: `~/airflow/dags/`
- Used VS Code + WSL to edit DAG files

---

## ✅ Conclusion

Pranav successfully learned:
- DAG structure & scheduling
- Task dependencies (`t1 >> t2`)
- Logging & retries
- Handling backfills using `execution_date`
- Realistic Airflow use cases

🎉 You are now Airflow-ready for real-world projects!
