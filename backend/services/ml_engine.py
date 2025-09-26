from ml.anomaly_detection import run_isolation_forest
from ml.predictive_models import train_random_forest
def run_ml_pipeline(df):
    anomalies = run_isolation_forest(df)
    model = train_random_forest(df)
    return anomalies, model
