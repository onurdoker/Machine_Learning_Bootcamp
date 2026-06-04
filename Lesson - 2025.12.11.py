# %%
import pandas as pd

# Read data from an CSV file
df = pd.read_csv(
    "titanic.csv",
    sep=",",
    header=0,
    usecols=["Passengerid", "Age", "Sex", "Fare"],
    nrows=100,
)
print(df)

# Read data from an Excel file
df_excel = pd.read_excel("raw_data.xlsx", sheet_name=0)
print(df_excel)


# Fill missing values in 'Price' column with 0
df_excel["Price"] = df_excel["Price"].fillna(0)
print(df_excel)


# Create a new column 'Total_Price' as the product of 'Price' and 'Quantity'
df_excel["Total_Price"] = df_excel["Price"] * df_excel["Quantity"]
print(df_excel)


# Filter rows where 'Total_Price' is greater than 100
df_filtered = df_excel[df_excel["Total_Price"] > 100].copy()
print(df_filtered)


# Save the filtered DataFrame to a new Excel file with default index
df_filtered.to_excel("filtered_data.xlsx", sheet_name="Data")

# Save the filtered DataFrame to a new Excel file without default index
df_filtered.to_excel("filtered_data.xlsx", sheet_name="Data", index=False)

# %%
# ! SQL Server

import sqlalchemy as sa

SERVER = "SERVER_NAME"  # Replace with your server name to learn server => name SELECT @@SERVERNAME
DATABASE = "DATABASE_NAME"  # Replace with your database name
USERNAME = "USER_NAME"  # Replace with your username
PASSWORD = "PASSWORD"  # Replace with your password
DRIVER = "DRIVER"  # Replace with your driver name

conn_str = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver= {DRIVER}"

try:
    engine = sa.create_engine(conn_str)
    engine.connect()
    print("Connected to SQL Server")
except Exception as e:
    print(f"Error connecting to SQL Server: {e}")

# Query data from a SQL Server table
query = "SELECT * FROM YourTableName"  # Replace with your table name

df_sql = pd.read_sql(query, engine)
print(df_sql)

students = pd.DataFrame(
    {"Name": ["John", "Alice", "Bob", "Eva"], "Marks": [85, 92, 78, 90]}
)

new_students = pd.DataFrame(
    {
        "Name": ["David", "Sophia"],
        "Marks": [88, 95],
    }
)

# Write data to a SQL Server table
students.to_sql(name="Students", con=engine, index=False, if_exists="replace")

# Append data to an existing table
new_students.to_sql(name="Students", con=engine, index=False, if_exists="append")

# Append data in chunks to an existing table
new_students.to_sql(
    name="Students", con=engine, index=False, if_exists="append", chunksize=2
)
