# 1. IMPORTS
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)


df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.groupby(["date", "region"], as_index=False)["sales"].sum()
df = df.sort_values(by="date")


fig = px.line(
    df, 
    x="date", 
    y="sales", 
    color="region",
    title="Sales Timeline",
    labels={"sales": "Sales ($)", "date": "Timeline", "region": "Region"}
)


app.layout = html.Div(children=[
    html.H1(children="Sales Dashboard"),
    
    html.P(children="This dashboard shows the sales of pink morsel over time."),
    
    dcc.Graph(
        id="sales-line-chart",
        figure=fig  
    )
])


if __name__ == "__main__":
    app.run(debug=True)