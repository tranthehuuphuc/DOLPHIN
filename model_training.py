import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

def train_and_evaluate_model(features_df: pd.DataFrame, unseen_data_path=None):
    # Separate features and labels
    X = features_df.drop('label', axis=1)
    y = features_df['label']
    
    # Create a pipeline for scaling and classification
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            class_weight='balanced',
            max_depth=10,
            min_samples_split=5
        ))
    ])
    
    # Perform 5-fold cross-validation
    cross_val_scores = cross_val_score(pipeline, X, y, cv=5)
    print("Cross-validation scores:", cross_val_scores)
    print("Average cross-validation score:", np.mean(cross_val_scores))
    
    # Train-test split for final evaluation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    
    # Detailed metrics
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # FPR and FNR
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    fpr = fp / (fp + tn)
    fnr = fn / (tp + fn)
    print(f"\nAccuracy: {accuracy:.4f}")
    print(f"False Positive Rate (FPR): {fpr:.4f}")
    print(f"False Negative Rate (FNR): {fnr:.4f}")
    
    # Feature importance
    rf_classifier = pipeline.named_steps['classifier']
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': rf_classifier.feature_importances_
    }).sort_values(by='importance', ascending=False)
    print("\nFeature Importance:")
    print(feature_importance)
    
