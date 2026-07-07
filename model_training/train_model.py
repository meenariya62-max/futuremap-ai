import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset properly - last column is career
rows = []
with open('../dataset/careers_dataset.csv', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) < 2:
            continue
        career = parts[-1].strip()
        skills = ', '.join([s.strip() for s in parts[:-1]])
        if career == 'career':  # skip header
            continue
        rows.append({'skills': skills, 'career': career})

df = pd.DataFrame(rows)
df = df.dropna()
print(f"Dataset: {len(df)} rows, {df['career'].nunique()} unique careers")
print(df['career'].value_counts())

X = df['skills']
y = df['career']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2), max_features=500)),
    ('clf', RandomForestClassifier(n_estimators=200, random_state=42))
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.2f}")

os.makedirs('../backend', exist_ok=True)
joblib.dump(pipeline, '../backend/career_model.pkl')
print("Model saved successfully!")
