import pandas as pd
import janitor
import plotly.express as px

df = pd.read_csv('Customers.csv')

df_clean = df.clean_names() \
             .remove_empty() \
             .dropna(subset=['profession'])

fig = px.scatter(
    df_clean, 
    x='age', 
    y='annual_income_', 
    color='gender',
    size='spending_score_1_100',
    hover_data=['profession'],
    title='Customer Analysis Report'
)

print(df_clean.head())

fig.show()