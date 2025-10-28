# Import libraries

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Medals Visualization", layout="wide")
st.title("Medals Visualization")

# Dropdown menu
medal = st.selectbox("Medal type", ["gold",'silver','bronze'])

# checkboxes

show_bar = st.checkbox("Show Bar Chart",value=True)
show_pie = st.checkbox("Show Pie Chart",value=True)

# two-col structure

col1, col2 = st.columns(2)

# load the medal wide dataset
df = px.data.medals_wide()

# plot the bar chart

if show_bar:
  fig_bar = px.bar(
      df,
      x="nation",
      y=f"{medal}",
      title = "Medals count"
  )

  fig_bar.update_layout(
      title_x=0.5,
      xaxis_title="Country",
      yaxis_title="Count",
      height = 300
  )

  col1.plotly_chart(fig_bar, use_container_width=True)


if show_pie:
  fig_pie = px.pie(
      df,
      names="Country",
      values=f"{medal}",
      title = "Medals count"
  )

  fig_pie.update_layout(
      title_x = 0.5,
      height = 300
  )

  col2.plotly_chart(fig_pie, use_container_width=True)
  
