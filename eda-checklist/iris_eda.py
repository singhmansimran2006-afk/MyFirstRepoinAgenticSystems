import plotly.express as px
import pandas as pd

df = pd.read_csv("iris.csv")

#inspect the dataset structure
print(df.head())
print(df.shape)

#check column information and missing values
print(df.info(),"\n")
print(df.describe(),"\n")
print(df.isnull())   #check missing values

#analyze the distribution of one feature
fig = px.histogram(
    df['petal_length'],
    title="Distribution of Petal Length"
)
fig.show()

#identify possible outliers in the dataset
out = px.box(
    df['petal_length'],
    title="Outliers"
)
out.show()

#analyze relationships between variables
corr = df[['petal_length','petal_width']].corr(numeric_only=True)

relation = px.imshow(
    corr,
    title="Petal Length VS Petal width"
)
relation.show()