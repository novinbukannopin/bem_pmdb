import matplotlib.pyplot as plt
import numpy as np  # import np
import pandas as pd  # import pd
import plotly.express as px  # import chart
import plotly.graph_objects as go
import streamlit as st
import altair as alt
import math



@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv('clean_pmdb.csv')


laptop = get_data()

value_counts = laptop.groupby(['bidangminat']).size().sort_values(ascending=False).reset_index(name='count')
fig = px.bar(data_frame=value_counts,x='bidangminat', y='count', color='bidangminat')
# st.table(value_counts)
st.plotly_chart(fig, use_container_width=False)

bidang_seni = laptop.groupby(['bidangseni']).size().sort_values(ascending=False).reset_index(name='count')
fig = px.bar(data_frame=bidang_seni,x='bidangseni', y='count', color='bidangseni')
st.plotly_chart(fig, use_container_width=False)

bidang_agama = laptop.groupby(['bidangagama']).size().sort_values(ascending=False).reset_index(name='count')
fig = px.bar(data_frame=bidang_agama,x='bidangagama', y='count', color='bidangagama')
st.plotly_chart(fig, use_container_width=False)

bidang_inggris = laptop.groupby(['bidanginggris']).size().sort_values(ascending=False).reset_index(name='count')
fig = px.bar(data_frame=bidang_inggris,x='bidanginggris', y='count', color='bidanginggris')
st.plotly_chart(fig, use_container_width=False)

bidang_penelitian = laptop.groupby(['bidangpenelitian']).size().sort_values(ascending=False).reset_index(name='count')
fig = px.bar(data_frame=bidang_penelitian,x='bidangpenelitian', y='count', color='bidangpenelitian')
st.plotly_chart(fig, use_container_width=False)
#%%
