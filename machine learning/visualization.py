import plotly.express as px

fig = px.scatter(df, 
                 x='Age', 
                 y='Annual Income ($)', 
                 color='Gender',
                 title='Age vs Annual Income by Gender')
fig.show()