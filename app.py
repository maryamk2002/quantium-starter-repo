# 1. IMPORTS
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)


df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.groupby(["date","region"], as_index=False)["sales"].sum()
df = df.sort_values(by="date")







app.layout = html.Div(style={'backgroundColor': "#FFFBFB", 'fontFamily': 'sans-serif', 'padding': '20px'}, children=[
    html.H1(
        children="Pink Morsel Visualiser",
        style={'textAlign': 'center', 'color': "#000000"}
    ),
    

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
            {"label": "All", "value": "all"}
        ],
        value="all",
       
        style={
            'color': '#f8fafc', 
            'padding': '10px', 
            'fontSize': '18px', 
            'display': 'flex', 
            'justifyContent': 'center', 
            'gap': '20px'
        }
    ),
    
    # 2. The Empty Graph Component
    dcc.Graph(
        id="sales-line-chart"
        
    )
])
@app.callback(
    Output("sales-line-chart", "figure"),   
    Input("region-filter", "value")         
)
def update_graph(selected_region):
 
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]
    
    # 2. Rebuild the line chart with the filtered data
    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales",
        color="region" if selected_region == "all" else None,
        labels={"sales": "Sales ($)", "date": "Date", "region": "Region"},
        title=f"Sales Performance ({selected_region.upper()})",
        
    )
   
    fig.update_layout(
        plot_bgcolor='#111111',   
        paper_bgcolor='#111111',  
        font_color='#ffffff',    
        margin=dict(l=40, r=40, t=40, b=40)
    )
    

    return fig

if __name__ == "__main__":
    app.run(debug=True)