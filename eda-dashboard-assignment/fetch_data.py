import pandas as pd
import requests
import matplotlib.pyplot as plt

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)

df = df.rename(columns={"userId" : "user_id"})
df = df.drop(columns="id")

post_count = df.groupby("user_id").count()
print(post_count)

df["post_length"] = df["body"].apply(len)
print(df.head())

post_count.plot.bar()
plt.title("Posts Per User")
plt.xlabel("User Id")
plt.ylabel("Number of Posts")
plt.show()

df["post_length"].plot.hist()
plt.title("Distribution of post length")
plt.xlabel("Characters")
plt.ylabel("Frequency")
plt.show()