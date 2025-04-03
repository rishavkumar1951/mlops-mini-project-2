import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/rishavkumar1951/mlops-mini-project-2.mlflow')
dagshub.init(repo_owner='rishavkumar1951', repo_name='mlops-mini-project-2', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)