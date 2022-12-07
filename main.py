import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config("UFO Reporting Analysis")

path = "notebooks:csv/UFO_cleaned.csv"

df = pd.read_csv(path)

df = df.drop(columns=df.columns[0])

# Data

st.header("Data")
st.dataframe(df)

st.header("Analyses")
st.header("")

# Top Years

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
years = df.Date.dt.year.value_counts()
histo = px.histogram(years,
                    title='Years with most Sightings',
                    x=years.index, y=years,
                    labels={'index':'years'})
st.plotly_chart(histo)

# Top 10 States

top_ten_state = df['State'].value_counts().head(10)

pie_chart = px.pie(top_ten_state,
            title='Top 10 States with the most UFO sightings and their percentile makeup',
            values='State',
            names=top_ten_state.index)


histo = px.histogram(top_ten_state,
                    x=top_ten_state.index, y=top_ten_state,
                    labels={'index':'States'})

st.plotly_chart(pie_chart, use_container_width=True)
st.plotly_chart(histo)

# Top 10 Cities

top_ten_cities = df['City'].value_counts().head(10)

pie_chart = px.pie(top_ten_cities,
            title='Top 10 Cities with the most UFO sightings and their percentile makeup',
            values='City',
            names=top_ten_cities.index)

histo = px.histogram(top_ten_cities,
                    x=top_ten_cities.index, y=top_ten_cities,
                    labels={'index':'Cities'})

st.plotly_chart(pie_chart)
st.plotly_chart(histo)

# Top 10 Shapes

shape = df['Shape'].value_counts().head(10)

pie_chart = px.pie(shape,
            title='Top 10 Shapes seen during the sighting and their percentile makeup',
            values='Shape',
            names=shape.index)

histo = px.histogram(shape,
                    x=shape.index, y=shape,
                    labels={'index':'Shape'})

st.plotly_chart(pie_chart)
st.plotly_chart(histo)

# Time Periods

time = df['Time'].value_counts()

pie_chart = px.pie(time,
            title='Most common time (Military time) the sightings occurred and their percentile makeup',
            values='Time',
            names=time.index)

histo = px.histogram(time,
                    x=time.index, y=time,
                    labels={'index':'Shape'})

st.plotly_chart(pie_chart)
st.plotly_chart(histo, use_container_width=True)

# Most Common Day of the month

day = df['Date'].dt.day.value_counts()

pie_chart = px.pie(day,
            title='Most common day of the month the sightings occurred and their percentile makeup',
            values='Date',
            names=day.index)

histo = px.histogram(day,
                    x=day.index, y=day,
                    labels={'index':'Day of the month'})

st.plotly_chart(pie_chart)
st.plotly_chart(histo, use_container_width=True)

# Most Common Month

month = df['Date'].dt.month_name().value_counts()

pie_chart = px.pie(month,
            title='Most common month of the year the sightings occurred and their percentile makeup',
            values='Date',
            names=month.index)

histo = px.histogram(month,
                    x=month.index, y=month,
                    labels={'index':'Month of the year'})

st.plotly_chart(pie_chart)
st.plotly_chart(histo, use_container_width=True)


# Worldclouds

img = Image.open('img/data_eight.png')
img2 = Image.open('img/data_nine.png')
st.header("WordClouds")
st.header("")
st.header("Most common word(s) used to describe sighting")
st.image(img)
st.header("Most common word(s) used to describe how long the interaction lasted")
st.image(img2)
