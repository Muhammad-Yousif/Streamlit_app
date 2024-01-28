# import essential libraries
import streamlit as st 
from PIL import Image
import pandas as pd
import numpy as np 
import plotly.express as px 

# title
st.title(":green[Rainfall In Pakistan Since 1901-2016]")
st.markdown(" ### :green[Data Source : Kaggle]")
#image 
image = Image.open('rain.png')
resized_image = image.resize([700,300])
st.image(resized_image)

# Creating multiple tabs
intro, insight, author, = st.tabs(["Introduction","Insights","Author"])

#Introduction section
#Description
intro.markdown("### :green[Description]")
intro.write(''':green[ Welcome to Rainfall Explorer: Discover Pakistan's Precipitation Patterns!
Embark on a fascinating journey through Pakistan's meteorological history with Rainfall Explorer. This interactive data science application, meticulously crafted using Streamlit, invites you to explore over a century of rainfall data spanning from 1901 to 2016. Our app offers a streamlined yet comprehensive tool for delving into the intricacies of Pakistan's climatic trends.
Uncover the story behind each raindrop as you navigate through decades of meteorological records. From the lush monsoon seasons to the parched spells of drought, Rainfall Explorer provides a captivating window into the dynamic interplay of weather phenomena that have shaped Pakistan's landscapes and livelihoods.
Through intuitive visualizations and powerful analytics tools, you can dissect the data with precision, identifying trends, anomalies, and correlations that offer invaluable insights into Pakistan's rainfall patterns. Whether you're a seasoned data scientist, a curious student, or simply an enthusiast of weather dynamics, our app empowers you to conduct exploratory data analysis (EDA) with ease and efficiency.
Join us as we unravel the mysteries of Pakistan's rainfall, one data point at a time. Let Rainfall Explorer be your compass as you navigate through the rich tapestry of historical weather data, illuminating the past to inform the future. Welcome aboard this voyage of discovery, where every rainfall tells a story waiting to be told.
               ]''', )


#Insights Section
#reading dataset
df = pd.read_csv('rainfall_1901_2016_pak.csv')
insight.markdown(" ### :green[Insights With Visualizaton]")
insight.subheader(':green[View Dataset]')
insight.write(df)

#plot_1
insight.subheader(":green[Monthly Rainfal in MM]")
monthly_plot = px.line(data_frame=df,x='Month',y='Rainfall - (MM)')
insight.plotly_chart(monthly_plot)

#plot_2
insight.subheader(":green[Yearly Rainfal in MM]")
yearly = px.line(data_frame=df,x=' Year',y='Rainfall - (MM)')
insight.plotly_chart(yearly)

#plot_3
insight.subheader(":green[Maximum Rainfall Years]")
max_rain = df['Rainfall - (MM)'].nlargest(n=10).groupby(by=df[' Year']).max()
insight.write(max_rain)
max_rain_plot = px.line(max_rain)
insight.plotly_chart(max_rain_plot)

# plot_4
insight.subheader(":green[Minimum Rainfall Years]")
min_rain = df['Rainfall - (MM)'].nsmallest(n=10).groupby(by=df[' Year']).min()
insight.write(min_rain)
min_rain_plot = px.line(min_rain)
insight.plotly_chart(min_rain_plot)


#Author section
author.title(':green[Muhammad Yousif]')
author.subheader(':green[Data Science & Machine Learning Practitionner]')

author.subheader(":green[Contact Us]")

author.write(":green[Have questions or feedback? Feel free to reach out to us through the following channels:]")


#links
author.markdown(":green[- Email: [hellomyousif@gmail.com](mailto:hellomyousif@gmail.com)]")
author.markdown(":green[- Twitter: [Muhammad Yousif](https://x.com/MUHAMMADYO19867?t=n9xjcZRhv-0lIhy6cJUmeA&s=08)]")
author.markdown(":green[- LinkedIn: [Muhammad Yousif](https://www.linkedin.com/in/muhammad-yousif-b78b722a5?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)]")
