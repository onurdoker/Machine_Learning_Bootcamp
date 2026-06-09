# %%
# ! Decision Tree
# import libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

# %%
# ! 2. Data Analysis and Visualization

# Data obtained from kaggle 'Telco Customer Churn' by Blastchar

# https://www.kaggle.com/datasets/blastchar/telco-customer-churn

df = pd.read_csv("customer.csv")

df = df.drop("customerID", axis=1)
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")


df_encoded = pd.get_dummies(df, drop_first=True)

# %%
# ! 3. Data Analysis and Preprocessing
X = df_encoded.drop("Churn", axis=1)
y = df_encoded["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=0.25
)

model = DecisionTreeClassifier(max_depth=4, min_samples_split=10)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy: ", accuracy_score(y_test, y_pred))

plt.figure()
plot_tree(model)
plt.show()
