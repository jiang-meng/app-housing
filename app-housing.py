import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990) by JiangMeng')
df = pd.read_csv('housing.csv')

#add a slider
price_filter = st.slider('Median Housing Price',0.0,500001.0,200000.0)

# create a multi select
location_filter = st.sidebar.multiselect(
     'Chooose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique()) # defaults
     
# filter by house value
df = df[df.median_house_value <= price_filter]
#filter by location
df = df[df.ocean_proximity.isin(location_filter)]

# use a button to filter by income
income = st.sidebar.radio(
    "Choose income level",
    ('low', 'median', 'high'))

if income == 'low':
    df = df[df.median_income <= 2.5]
elif income == 'median':
   df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income == 'high':
    df = df[df.median_income > 4.5]

#show on map
st.markdown('### See more filters in the sidebar :')
st.map(df)

# draw a histogram
st.markdown('### Histogram of the Median House Value')
fig,ax=plt.subplots()
ax.hist(df.median_house_value,bins=30)
st.pyplot(fig)