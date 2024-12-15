# model_training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

def train_and_evaluate_model(features_df: pd.DataFrame):
    """
    Train and evaluate a machine learning model on the extracted features.
    
    Args:
        features_df (pd.DataFrame): DataFrame containing extracted features and labels
    """
    # Separate features and labels
    X = features_df.drop('label', axis=1)
    y = features_df['label']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Random Forest Classifier
    rf_classifier = RandomForestClassifier(
        n_estimators=100, 
        random_state=42, 
        class_weight='balanced'
    )
    rf_classifier.fit(X_train_scaled, y_train)
    
    # Predictions
    y_pred = rf_classifier.predict(X_test_scaled)
    
    # Print detailed evaluation metrics
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': rf_classifier.feature_importances_
    }).sort_values('importance', ascending=False)
    print("\nFeature Importance:")
    print(feature_importance)
    
    return rf_classifier, scaler