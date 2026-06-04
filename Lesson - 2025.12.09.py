# %%
# ! Polymorphism


class Dog:
    def do_sound(self):
        print("Wof wof")


dog1 = Dog()
dog1.do_sound()


class Cat:
    def do_sound(self):
        print("Meow Meow")


cat1 = Cat()
cat1.do_sound()


class Cow:
    def do_sound(self):
        print("Moo Moo")


cow1 = Cow()
cow1.do_sound()

# %%
# ! Abstraction
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


# %%
# ! Data Analysis and Virtualization
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print("Array: ", arr1)  # Array:  [1 2 3 4 5]

vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
matrix = vector.reshape(4, 3)
print("Reshaped Matrix: \n", matrix)

# Attributes
print("Matrix shape: ", matrix.shape)  # Matrix shape:  (4, 3)
print("Matrix dimensions: ", matrix.ndim)  # Matrix dimensions:  2
print("Matrix data type: ", matrix.dtype)  # Matrix data type:  int64
print("Matrix size: ", matrix.size)  # Matrix size:  12
print("Matrix item size: ", matrix.itemsize)  # Matrix item size:  8


print("Array1: ", arr1)  # Array1:  [1 2 3 4 5]
print("Array1 data type: ", arr1.dtype)  # Array1 data type:  int64

arr2 = np.array([1, 2, 3, 4, 5, "a"])
print("Array2: ", arr2)  # Array2:  ['1' '2' '3' '4' '5' 'a']
print("Array2 data type: ", arr2.dtype)  # Array2 data type:  <U21

# Special Matrix
# Matrix with zeros
zeros_matrix = np.zeros((3, 3))
print("Zeros Matrix: \n", zeros_matrix)

# Matrix with random numbers
random_matrix = np.random.rand(3, 3)
print("Random Matrix: \n", random_matrix)

#
lin_matrix = np.linspace(0, 10, 5)
print("Linear Matrix: \n", lin_matrix)


#  Basic Operations
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

sum = a + b
diff = a - b
prod = a * b
div = a / b  # Element-wise division, results in float values
div_int = a // b  # Element-wise integer division, results in integer values
print("Sum: \n", sum)
print("Diff: \n", diff)
print("Prod: \n", prod)
print("Div: \n", div)


# Transpose of matrix
trans_matrix = matrix.T
print("Transpose matrix: \n", trans_matrix)

# Statistical Operations
print("Max number of matrix: ", matrix.max())  # Max number of matrix:  12
print("Min number of matrix: ", matrix.min())  # Min number of matrix:  1
print("Sum of matrix elements: ", matrix.sum())  # Sum of matrix elements:  78
print("Mean of matrix elements: ", matrix.mean())  # Mean of matrix elements:  6.5
print("Index of max element: ", matrix.argmax())  # Index of max element:  11
print("Index of min element: ", matrix.argmin())  # Index of min element:  0
print("Standard deviation of matrix elements: ", matrix.std())
# Standard deviation of matrix elements:  3.452052529534663


# Slicing
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
matrix[0, 1]  # Accessing element at first row and second column, output: 2
matrix[2, 2]  # Accessing element at third row and third column, output: 11
matrix[1:3, 0:2]  # Slicing rows 1 to 2 and columns 0 to 1, output: [[5 6], [9 10]]


# Stacking
vector1 = np.array([1, 2])
vector2 = np.array([3, 4])

vertical_vector = np.hstack((vector1, vector2))  # Stack vectors vertically
print("Vertical Stack: \n", vertical_vector)

horizontal_vector = np.vstack((vector1, vector2))  # Stack vectors horizontally
print("Horizontal Stack: \n", horizontal_vector)

dot_product = np.dot(vector1, vector2)  # Calculate dot product
print("Dot Product: ", dot_product)

cross_product = np.cross(vector1, vector2)  # Calculate cross product
print("Cross Product: ", cross_product)


array_d = np.array([1, 2, 3, 4])

array_e = array_d
array_e[0] = 10
print("Array D: ", array_d)
print("Array E: ", array_e)
# Both array_d and array_e will reflect the change since they reference the same data in memory.

array_f = array_d.copy()
array_f[0] = 20

print("Array D: ", array_d)
print("Array F: ", array_f)
# array_d and array_f will not reflect the change since they reference different data in memory.

# %%
# ! Pandas
import pandas as pd

series_A = pd.Series([10, 20, 30, 40, 50])
letters = pd.Series(["a", "b", "c", "d", "e"])
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

df = pd.DataFrame(data)

print(df.head())  # Display first 5 rows
print(df.head())  # Display first 5 rows
print(df.tail(2))  # Display last 2 rows
print(df.sample(2))  # Display 2 random rows

print(df.dtypes)  # Display data types of each column
print(df.columns)  # Display column names
print(df.shape)  # Display number of rows and columns
print(df.describe())  # Display summary statistics


print(df.loc[3])  # Access row with index 1
print(df.iloc[2])  # Access row at position 2

# ! Insert new row
df.loc[4] = ["Eve", 28, "Miami"]  # Add new row
df.loc[-1] = ["Eve", 28, "Miami"]  # You can't use negative index to reach the last row
print(df)

df.loc[len(df)] = [
    "Eve",
    28,
    "Miami",
]  # to reach the last row you can use len(df) function
print(df)

# ! Delete row
df["Salary"] = 50000  # Add a new column 'Salary'
print(df)
df.drop("Salary", axis=1, inplace=True)  # Delete column with name 'Salary'
print(df)
df.drop(-1, axis=0, inplace=True)  # Drop row with name -1
print(df)

# %%
# ! Merge and Joining DataFrames
df_workers = pd.DataFrame(
    {
        "WorkerID": [101, 102, 103, 104],
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "DepartmentId": [1, 1, 5, 3],
    }
)

df_departments = pd.DataFrame(
    {
        "DepartmentId": [1, 2, 3, 4],
        "Department": ["HR", "IT", "Finance", "IT"],
    }
)

# merge two dataframes based on DepartmentId column
inner_join_df = pd.merge(df_workers, df_departments, on="DepartmentId", how="inner")
print(inner_join_df)

# left join
left_join_df = pd.merge(df_workers, df_departments, on="DepartmentId", how="left")
print(left_join_df)

# right join
right_join_df = pd.merge(df_workers, df_departments, on="DepartmentId", how="right")
print(right_join_df)

# outer join
outer_join_df = pd.merge(df_workers, df_departments, on="DepartmentId", how="outer")
print(outer_join_df)


# %%
# ! Concatenate DataFrames
df1 = pd.DataFrame({"Number": [1, 2, 3]})
df2 = pd.DataFrame({"Number": [4, 5, 6]})

pd.concat(
    [df1, df2]
)  # Concatenate along rows (axis=0) by default without specifying axis
pd.concat([df1, df2], axis=0)  # Concatenate along rows (axis=0) by specifying axis
pd.concat(
    [df1, df2], axis=0, ignore_index=True
)  # Concatenate along rows and reset index
pd.concat([df1, df2], axis=1)  # Concatenate along columns (axis=1)
pd.concat(
    [df1, df2], axis=1, ignore_index=True
)  # Concatenate along columns and reset index
