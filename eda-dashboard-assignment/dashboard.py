import pandas as pd
import requests
import plotly.express as px
import streamlit as st

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)

df = df.rename(columns={"userId" : "user_id"})
df = df.drop(columns="id")

post_count = df.groupby("user_id").size()
print(post_count)

df["post_length"] = df["body"].apply(len)
print(df.head())

st.title("Posts Dataset Preview")
st.write("Posts Data")
st.dataframe(df.head(50))

st.subheader("Posts Per User Chart")
st.bar_chart(post_count)

st.subheader("Posts Length Distribution")
fig = px.histogram(df, x="post_length")
st.plotly_chart(fig)