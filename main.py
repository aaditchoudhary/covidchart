import pandas as pd
import plotly.express as px
df=pd.read_csv(r"C:/Users/kanis/OneDrive/Mithun-One drive/OneDrive/Desktop/project 103/Copy+of+data+-+data.csv")
fig=px.scatter(df,x="date",y="cases",color="country",)
fig.show()