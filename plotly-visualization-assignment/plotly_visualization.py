import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Epochs" : range(1,11),
    "Training Loss Value" : [0.9, 0.8, 0.75, 0.7, 0.65, 0.6, 0.58, 0.55, 0.52, 0.5]
})

fig = px.line(
    df,
    x = "Epochs",
    y = "Training Loss Value",
    title="Training Loss Over Epochs"
)

fig.add_annotation(
    x=6.5,
    y=0.59,
    text="Loss Stablizing",
    showarrow=True,
    arrowhead= 6
)

fig.show()