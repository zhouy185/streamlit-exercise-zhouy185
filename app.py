import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Medals Explorer",layout="wide")
st.title("Medals Explorer (Plotly + Streamlit)")

medal = st.selectbox("Medal type", ["gold", "silver", "bronze"])
show_bar = st.checkbox("Show Bar Chart", value=True)
show_pie = st.checkbox("Show Pie Chart", value=True)


col1, col2 = st.columns(2)


df = px.data.medals_wide()

if show_bar:
    fig_bar = px.bar(
        df, 
        x="nation", 
        y=f"{medal}", 
        title=f"Medals count({medal})"
        )
    fig_bar.update_layout(title_x=0.5, yaxis_title="Count", xaxis_title="Nation", height=300)
    col1.plotly_chart(fig_bar, use_container_width=True)

if show_pie:
    fig_pie = px.pie(df, names="nation", values=f"{medal}",
                     title=f"Medal Share ({medal})")
    fig_pie.update_traces(textinfo="percent+label")
    fig_pie.update_layout(title_x=0.5, height=300)
    col2.plotly_chart(fig_pie, use_container_width=True)
