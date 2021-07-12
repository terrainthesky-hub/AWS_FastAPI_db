"""Data visualization functions"""

from fastapi import APIRouter

router = APIRouter()

import plotly.express as px

# dataframe = px.data.gapminder().rename(columns={
#     'year': 'Year', 
#     'lifeExp': 'Life Expectancy', 
#     'pop': 'Population', 
#     'gdpPercap': 'GDP Per Capita'
# })


# @router.get('/worldviz')
# async def worldviz(metric, country):
#     """
#     Visualize world metrics from Gapminder data

#     ### Query Parameters
#     - `metric`: 'Life Expectancy', 'Population', or 'GDP Per Capita'
#     - `country`: [country name](https://www.gapminder.org/data/geo/), case sensitive

#     ### Response
#     JSON string to render with react-plotly.js
#     """
#     subset = dataframe[dataframe.country == country]
#     fig = px.line(subset, x='Year', y=metric, title=f'{metric} in {country}')
#     return fig.to_json()