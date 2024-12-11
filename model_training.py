# Handles training and evaluation of models

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_and_evaluate_model(features):
    """
    Trains and evaluates a Random Forest model.

    Args:
        features (pd.DataFrame): Features and labels.

    Returns:
        RandomForestClassifier: Trained model.
    """
    X = features.drop(columns=["label"])
    y = features["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))

    return model