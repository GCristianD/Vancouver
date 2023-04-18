import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

st.title('Sample of Vancouver rentals')

df1 = pd.read_csv('dataset.csv')
feat = ['price','livingArea','bedrooms','bathrooms','url','address/zipcode','address/streetAddress','latitude','longitude']
df1 = df1[feat]
#df1 = df1[df1['price']<8000]
#df1 = df1[df1['livingArea']<4000]

#st.write(df1)

#maxbedrooms = st.slider('hour', 0, 6, 3) # min: 0, max: 3, default: 3


col1, col2 = st.columns([2,2])

maxprice = col1.slider('Max price:', 1500, 12000, 8000) # min: 1500, max: 12000, default: 8000
maxarea = col1.slider('Max living area:', 300, 5000, 2000)

df = df1[df1['price'] <= maxprice]
df = df[df['livingArea'] <= maxarea]
df["bedrooms"] = df["bedrooms"].astype(str)
fig = px.scatter(df, x="livingArea", y="price",color="bedrooms", trendline="ols",color_discrete_sequence=px.colors.qualitative.Antique,trendline_scope="overall")

#fig = px.scatter(df1, x="livingArea", y="price",color="bedrooms", trendline="ols",color_discrete_sequence=px.colors.qualitative.Antique,trendline_scope="overall")
col1.plotly_chart(fig,theme=None)


if col2.checkbox('Show map'):
    #st.subheader('Map of Vancouver rentals')
    col2.map(df)

