# ============================================================
# PLACEMENT PREDICTION PROJECT - COMPLETE ML CODE
# ============================================================

# 1. Import Libraries
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_csv("placement.csv")

print("========== DATASET ==========")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# ============================================================
# 3. DATA CLEANING
# ============================================================

# Remove unnecessary index column
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

print("\n========== AFTER CLEANING ==========")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())


# ============================================================
# 4. DATA VISUALIZATION
# ============================================================

# Placement Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='placement', data=df)
plt.title('Placement Distribution')
plt.xlabel('Placement (0 = Not Placed, 1 = Placed)')
plt.ylabel('Number of Students')
plt.show()


# CGPA Distribution
plt.figure(figsize=(7, 4))
sns.histplot(data=df, x='cgpa', bins=10, kde=True)
plt.title('CGPA Distribution')
plt.xlabel('CGPA')
plt.ylabel('Number of Students')
plt.show()


# IQ Distribution
plt.figure(figsize=(7, 4))
sns.histplot(data=df, x='iq', bins=10, kde=True)
plt.title('IQ Distribution')
plt.xlabel('IQ')
plt.ylabel('Number of Students')
plt.show()


# CGPA vs Placement
plt.figure(figsize=(7, 5))
sns.boxplot(x='placement', y='cgpa', data=df)
plt.title('CGPA vs Placement')
plt.xlabel('Placement (0 = Not Placed, 1 = Placed)')
plt.ylabel('CGPA')
plt.show()


# IQ vs Placement
plt.figure(figsize=(7, 5))
sns.boxplot(x='placement', y='iq', data=df)
plt.title('IQ vs Placement')
plt.xlabel('Placement (0 = Not Placed, 1 = Placed)')
plt.ylabel('IQ')
plt.show()


# CGPA vs IQ
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x='cgpa',
    y='iq',
    hue='placement',
    s=80
)
plt.title('CGPA vs IQ - Placement Analysis')
plt.xlabel('CGPA')
plt.ylabel('IQ')
plt.show()


# Correlation Heatmap
plt.figure(figsize=(6, 4))
correlation = df[['cgpa', 'iq', 'placement']].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Correlation Heatmap')
plt.show()


# ============================================================
# 5. SELECT INPUT AND OUTPUT
# ============================================================

X = df[['cgpa', 'iq']]
Y = df['placement']

print("\n========== INPUT AND OUTPUT ==========")
print("Input Features:")
print(X.head())

print("\nTarget:")
print(Y.head())


# ============================================================
# 6. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.1,
    random_state=2
)

print("\n========== TRAIN TEST SPLIT ==========")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("Y_train:", Y_train.shape)
print("Y_test:", Y_test.shape)


# ============================================================
# 7. FEATURE SCALING
# ============================================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nFeature scaling completed.")


# ============================================================
# 8. CREATE LOGISTIC REGRESSION MODEL
# ============================================================

clf = LogisticRegression()

print("\nLogistic Regression model created.")


# ============================================================
# 9. TRAIN MODEL
# ============================================================

clf.fit(X_train_scaled, Y_train)

print("Model training completed.")


# ============================================================
# 10. MAKE PREDICTIONS
# ============================================================

Y_pred = clf.predict(X_test_scaled)

print("\n========== PREDICTIONS ==========")
print(Y_pred)


# ============================================================
# 11. MODEL ACCURACY
# ============================================================

accuracy = accuracy_score(Y_test, Y_pred)

print("\n========== MODEL PERFORMANCE ==========")
print("Model Accuracy:", accuracy)


# ============================================================
# 12. CLASSIFICATION REPORT
# ============================================================

print("\nClassification Report:")
print(classification_report(Y_test, Y_pred))


# ============================================================
# 13. TEST A NEW STUDENT
# ============================================================

student = pd.DataFrame({
    'cgpa': [8.0],
    'iq': [110]
})

student_scaled = scaler.transform(student)

prediction = clf.predict(student_scaled)

print("\n========== NEW STUDENT PREDICTION ==========")
print("CGPA:", student['cgpa'].iloc[0])
print("IQ:", student['iq'].iloc[0])

if prediction[0] == 1:
    print("Prediction: PLACED")
else:
    print("Prediction: NOT PLACED")


# ============================================================
# 14. SAVE MODEL
# ============================================================

with open("model.pkl", "wb") as file:
    pickle.dump(clf, file)

print("\nmodel.pkl saved successfully!")


# ============================================================
# 15. SAVE SCALER
# ============================================================

with open("scaler.pkl", "wb") as file:
    pickle.dump(scaler, file)

print("scaler.pkl saved successfully!")


# ============================================================
# 16. VERIFY SAVED FILES
# ============================================================

import os

print("\n========== SAVED FILES ==========")

if os.path.exists("model.pkl"):
    print("✓ model.pkl")

if os.path.exists("scaler.pkl"):
    print("✓ scaler.pkl")

print("\n========== PROJECT COMPLETED ==========")
print("ML model training and saving completed successfully!")
