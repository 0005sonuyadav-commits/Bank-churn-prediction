import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

print("Loading data...")
df = pd.read_csv("European_Bank.csv")

# Data preprocessing
print("Preprocessing data...")
# Remove non-informative features
cols_to_drop = [col for col in ['CustomerId', 'Surname', 'Year'] if col in df.columns]
df = df.drop(columns=cols_to_drop)

# Handle missing values
df = df.dropna()

# Feature Engineering
print("Engineering features...")
df['Balance_To_Salary_Ratio'] = df['Balance'] / (df['EstimatedSalary'] + 1)
df['Product_Density'] = df['NumOfProducts'] / (df['Tenure'] + 1)
df['Engagement_Product_Interaction'] = df['IsActiveMember'] * df['NumOfProducts']
df['Age_Tenure_Interaction'] = df['Age'] * (df['Tenure'] + 1)
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 30, 45, 60, 100], 
                          labels=['Young', 'Middle_Aged', 'Senior', 'Elderly'])

# Encode categorical variables
print("Encoding categorical variables...")
categorical_cols = ['Geography', 'Gender', 'Age_Group']
df_encoded = pd.get_dummies(df, columns=[col for col in categorical_cols if col in df.columns], drop_first=True)

# Separate features and target
X = df_encoded.drop('Exited', axis=1)
y = df_encoded['Exited']

# Split data
print("Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scale features
print("Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
print("Training Random Forest model...")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train_scaled, y_train)

# Evaluate model
train_score = model.score(X_train_scaled, y_train)
test_score = model.score(X_test_scaled, y_test)

print(f"\nModel Training Complete!")
print(f"Training Accuracy: {train_score:.4f}")
print(f"Testing Accuracy: {test_score:.4f}")

# Save model and scaler
print("\nSaving model and scaler...")
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

with open('scaler.pkl', 'wb') as file:
    pickle.dump(scaler, file)

print("Model and scaler saved successfully!")
print("\nFeature names:")
print(X.columns.tolist())
