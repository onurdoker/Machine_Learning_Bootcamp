# %%
# import libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# %%
# ! 2. Data Analysis and Visualization

# Data obtained from kaggle 'Medical Cost Personal Datasets' by Miri Choi
# https://www.kaggle.com/datasets/mirichoi0218/insurance

df = pd.read_csv("insurance.csv")

# Display basic information about the dataset.
print(f"Info:\n {df.info()}\n")

print(f"Describe: \n{df.describe()}\n")

print(f"Head: \n{df.head(5)}\n")

# %%
# Visualize data
plt.figure()
sns.barplot(data=df, x="smoker", y="charges")
plt.show()

plt.figure()
sns.boxplot(data=df, x="smoker", y="charges")
plt.show()

# %%
# ! 3. Data Analysis and Preprocessing

# Feature Engineering => Encoding => One-Hot Encoding
df_encoding = pd.get_dummies(df, columns=["sex", "smoker", "region"], drop_first=True)

X = df_encoding.drop("charges", axis=1)
Y = df_encoding["charges"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# %%
# ! 4. Model training
model = LinearRegression()  # Create a linear regression model.
model.fit(X_train, Y_train)  # Train the model.
Y_pred = model.predict(X_test)  # Predict on the test set.

# %%
# ! 5. Evaluation
r2 = r2_score(Y_test, Y_pred)
mse = mean_squared_error(Y_test, Y_pred)
print(f"R^2 score: {r2:.4f}")
print(f"MSE: {mse:.2f}")

# %%
# ! 6. Deployment
new_customer = pd.DataFrame([[25, 30, 1, 0, 0, 1, 0, 0]], columns=X_train.columns)

new_customer_prediction = model.predict(new_customer)

print(f"New Customer Prediction: {new_customer_prediction[0]:.2f}")

# %%
# ! 7. Improve model
df_encoding_new = pd.get_dummies(
    df, columns=["sex", "smoker", "region"], drop_first=True
)

df_encoding_new["bmi_smoker"] = df_encoding_new["bmi"] * df_encoding_new["smoker_yes"]
df_encoding_new["is_obese"] = df_encoding_new["bmi"].apply(lambda x: 1 if x > 30 else 0)

X_new = df_encoding_new.drop("charges", axis=1)
Y_new = df_encoding_new["charges"]

X_train_new, X_test_new, Y_train_new, Y_test_new = train_test_split(
    X_new, Y_new, test_size=0.2
)

model_new = LinearRegression()  # Create a linear regression model.
model_new.fit(X_train_new, Y_train_new)  # Train the model.
Y_pred_new = model_new.predict(X_test_new)  # Predict on the test set.

r2_new = r2_score(Y_test_new, Y_pred_new)
mse_new = mean_squared_error(Y_test_new, Y_pred_new)
print(f"R^2 score: {r2_new:.4f}")
print(f"MSE: {mse_new:.2f}")

# %%
