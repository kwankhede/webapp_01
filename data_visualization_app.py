import streamlit as st
import plotly_express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go



# webapp layout 
st.set_page_config(layout="centered")

#title of the app 
st.title("ANALYSIS OF SANGHAMITRA.STORE'S SALES")
st.subheader("(From start to Jan 2022)")


    
#table for category wise sales
st.title("TOTAL SALES OF SANGHAMITRA")
st.subheader("(Category wise)")
data = pd.read_csv("categories.csv")
st.write(data)
st.write("Net sale Total:",data[['Net sales']].sum())


# Let's use some visualization (bar plot) 
st.subheader("Bar Plot")
fig_1 = px.bar(data, 'Category','Items sold',text='Items sold')
st.plotly_chart(fig_1, use_container_width=True)


#pie chart
st.subheader("Pie Chart")
fig2 = px.pie(data, values='Items sold', names='Category',
             title='TOTAL SALES OF SANGHAMITRA IN PERCENTAGES')
fig2.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig2, use_container_width=True)


#add a sidebar 
st.sidebar.subheader("Visualization settigs")
#Configuration
st.set_option('deprecation.showfileUploaderEncoding', False)
    
#Setup file upload 
uploaded_file = st.sidebar.file_uploader(label= "Upload Excel or csv", type = ['csv','xlsx'])
#global df
if uploaded_file is not None:
    print(uploaded_file)
    print('HELLO') 
    
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)
        
try:
    st.write(df)
except Exception as e:
    print(e)
    #st.write("please upload file to the application.")
    
    
    
 
#import datetime

#st.title("Date range")

#min_date = datetime.datetime(2022,1,30)
#max_date = datetime.date(2025,1,1)

#a_date = st.date_input("Pick a date", min_value=min_date, max_value=max_date)

##this uses streamlit 'magic'!!!! 
##"The date selected:", a_date
#"""

#Import packages for map pinnning 
from streamlit_folium import folium_static
import folium 
    
# get latitude and longitude for all the districts(748) in India 
codes = pd.read_csv("cities.csv")

# load the customer information 
data = pd.read_csv("~jan_2022.csv")

# get the latitude and logitude for customer's cities. 
cities_with_cordinates = pd.merge(codes, data, on='City')
df = cities_with_cordinates[["City","Latitude","Longitude"]]

loc_center = [df['Latitude'].mean(), df['Longitude'].mean()]

st.title("Our custemer locations")

map1 = folium.Map(location = loc_center, tiles='Openstreetmap', 
                  zoom_start = 5, control_scale=True)
for index, loc in df.iterrows():
    folium.CircleMarker([loc['Latitude'], loc['Longitude']],     
                        radius=2, weight=5, popup=loc['City']).add_to(map1)
folium.LayerControl().add_to(map1)
folium_static(map1)
st.write(df)




#https://towardsdatascience.com/how-to-create-a-map-from-geospatial-data-in-python-f4bb7d11ddad
