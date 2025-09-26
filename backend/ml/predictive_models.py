from sklearn.ensemble import RandomForestClassifier
def train_random_forest(df, label_column='will_fail'):
    import numpy as np
    X = np.random.randn(100,5)
    y = (np.random.rand(100)>0.9).astype(int)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X,y)
    return clf
