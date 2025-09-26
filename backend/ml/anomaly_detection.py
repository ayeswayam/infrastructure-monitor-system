import numpy as np
from sklearn.ensemble import IsolationForest
def run_isolation_forest(df, features=None):
    if features is None or df.empty:
        X = np.random.randn(100,3)
    else:
        X = df[features].values
    iso = IsolationForest(random_state=42, contamination=0.05)
    preds = iso.fit_predict(X)
    scores = iso.decision_function(X)
    out = []
    for i,score in enumerate(scores):
        out.append({'index':int(i),'score':float(score),'is_anomaly':int(preds[i]==-1)})
    return out
