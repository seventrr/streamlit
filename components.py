# -*- ecoding: utf-8 -*-
# @ModuleName: app
# @Author: wk
# @Email: 306178200@qq.com
# @Time: 2024/1/8 16:08
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import time

# Sidebar Components
sidebar_input = st.sidebar.text_input("在这里输入内容")
sidebar_slider = st.sidebar.slider("选择一个数值", 0, 100)

# Cachin
@st.cache_data
def load_data():
    # Replace 'large_dataset.csv' with a real file path or another source of data
    data = pd.DataFrame({
        "a": range(100),
        "b": range(100, 200)
    })
    return data

data = load_data()
st.write("Cached Data:", data)

# File Uploader
uploaded_file = st.file_uploader("选择一个文件")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

# Matplotlib Integration
fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [1, 2, 3])
st.pyplot(fig)

# Plotly Integration
df = pd.DataFrame({
    "x": [1, 2, 3, 4],
    "y": [10, 11, 12, 13]
})
fig = px.line(df, x="x", y="y")
st.plotly_chart(fig)

# Layout Control
tab1, tab2 = st.tabs(["第一标签", "第二标签"])
with tab1:
    st.header("这是第一个标签的内容")
with tab2:
    st.header("这是第二个标签的内容")

# Custom Styles
st.markdown(
    """
    <style>
    .big-font {
        font-size:50px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<p class="big-font">这是大号字体</p>', unsafe_allow_html=True)

# Progress Bar and Status
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.1)
st.success("任务完成！")