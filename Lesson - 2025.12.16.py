# %%
# importing libraries
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# %%
# Load the "tips" dataset from seaborn
df = sns.load_dataset("tips")

df.head()

# %%
# * Scatter Plot
plt.figure(figsize=(10, 8))
plt.scatter(df["total_bill"], df["tip"], color="red", alpha=0.5)
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Scatter Plot of Total Bill vs Tip")
plt.show()

# %%
# * Histogram

plt.figure(figsize=(10, 8))
plt.hist(df["total_bill"], bins=40, color="green", alpha=0.5)
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.title("Histogram of Total Bill")
plt.show()

# %%
# * Bar plot
summarized_data = df.groupby("day")["total_bill"].sum()
plt.figure(figsize=(10, 8))
plt.bar(summarized_data.index, summarized_data.values, color="orange", alpha=0.5)
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.title("Average Total Bill by Day")
plt.show()

# %%
# * Line plot
# Create a line plot of total_bill over time (using the index as a proxy for time)
sorted_data = df.sort_values("total_bill").reset_index()

plt.figure(figsize=(10, 8))
plt.plot(
    df.index,
    sorted_data["total_bill"],
    color="green",
    marker="o",
    linestyle="-",
    linewidth=2,
    markersize=5,
)
plt.title("Total Bill Over Time")
plt.xlabel("Index")
plt.ylabel("Total Bill")
plt.show()

# %%
# ! SeaBorn
# * Scatter Plot
plt.figure(figsize=(10, 8))
sns.scatterplot(
    data=df, x="total_bill", y="tip", s=100, hue="day", palette="magma", alpha=0.7
)
plt.title("Scatter Plot of Total Bill vs Tip by Day")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend(title="Day")
plt.show()


# %%
plt.figure(figsize=(10, 8))
my_pallette = {"Male": "blue", "Female": "red"}
sns.scatterplot(
    data=df, x="total_bill", y="tip", s=100, hue="sex", palette=my_pallette, alpha=0.5
)
plt.title("Scatter Plot of Total Bill vs Tip by Sex")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend(title="Sex")
plt.show()

# %%
# * Bar plot
plt.figure(figsize=(10, 8))
sns.barplot(data=df, x="total_bill", y="day", hue="day", estimator="sum")
plt.title("Bar Plot of Total Bill by Day")
plt.xlabel("Total Bill")
plt.ylabel("Day")
plt.show()

# %%
# ! Plotly
# * Scatter Plot

fig = px.scatter(
    df,
    x="total_bill",
    y="tip",
    color="sex",
    size="size",
    title="Scatter Plot of Total Bill vs Tip by Sex",
    labels={"total_bill": "Total Bill", "tip": "Tip"},
)
fig.show(renderer="browser")

# %%
"""
Graph objects are the building blocks of Plotly visualizations. They represent individual elements of a plot, such as lines, bars, markers, etc. Each graph object has specific properties that can be customized to create a desired visualization.

import plotly.graph_objects as go

fig.add_trace(go.Scatter(
    x=df[df['sex'] == 'Female']['total_bill'],
    y=df[df['sex'] == 'Female']['tip'],
    mode='markers',
    name='Female'
))

fig.add_trace(go.Scatter(
    x=df[df['sex'] == 'Male']['total_bill'],
    y=df[df['sex'] == 'Male']['tip'],
    mode='markers',
    name='Male'
))

"""
