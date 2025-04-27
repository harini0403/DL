import os
import pandas as pd
import xgboost as xgb
import joblib

def train_difficulty_model(df):
    """
    Train and save the difficulty prediction model.
    """
    features = [col for col in df.columns if col != 'next_difficulty']
    X = df[features]
    y = df['next_difficulty']

    # Train the model
    xgb_model = xgb.XGBClassifier(eval_metric="mlogloss")
    xgb_model.fit(X, y)

    # Save the model
    os.makedirs('../model', exist_ok=True)
    joblib.dump(xgb_model, '../model/next_difficulty_model.pkl')
    print("✅ Difficulty model trained and saved.")

