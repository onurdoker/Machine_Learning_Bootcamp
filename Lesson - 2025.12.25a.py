# %%
# ! Logistic Regressions
# import libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# %%
# ! 2. Data Analysis and Visualization

# Data obtained from kaggle 'Pima Indians Diabetes Database' by UCI Machine Learning
# https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

df = pd.read_csv("diabetes.csv")

# Display basic information about the dataset.
print(f"Head: \n{df.head(5)}\n")

print(f"Info:\n {df.info}\n")

print(f"Describe: \n{df.describe()}\n")

print(df["Outcome"].value_counts())

# %%
# Visualize data
df.corr()
plt.figure()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

# %%
# ! 3. Data Analysis and Preprocessing
coltofix = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

for col in coltofix:
    df[col] = df[col].replace(0, df[col].mean())

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=0.30
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

# %%
# ! 4. Model training
model = LogisticRegression(C=1, solver="liblinear", random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

print(classification_report(y_test, y_pred))
"""
Precision : TP / (TP + FP)
Recall    : TP / (TP + FN)
F1 Score  : 2 * ((precision * recall) / (precision + recall))
"""
