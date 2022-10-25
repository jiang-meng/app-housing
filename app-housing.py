import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990) by JiangMeng')
df = pd.read_csv('housing.csv')

#add a slider
pop_slider = st.slider('Median Housing Price',0,500001,200000)
df = df[df.median_house_value >= pop_slider]

# create a multi select
location_filter = st.sidebar.multiselect(
     'Chooose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique()) # defaults

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
st.write('See more filters in the sidebars')
st.map(df)

# draw a histogram
st.write('Histogram of The Median Housing Value')
fig, ax = plt.subplots()
s = df.median_house_value
s.plot.hist(ax=ax,bins=30)
st.pyplot(fig)