import time

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt

# 运行 streamlit run web/web_test.py

# 普通显示
st.write("Hello ,let's learn how to build a streamlit app together1")

# 文本显示 数学表达式
st.title("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# 输入部件
st.checkbox('yes')
st.button('点击可刷新')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick your gender', ['Male', 'Female'])
st.multiselect('choose a planet', ['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)

st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

# 显示进度和状态
# st.balloons()
# st.progress(10)
# with st.spinner('Wait for it...'):
#     time.sleep(10)
#
# st.success("You did it !")
# st.error("Error")
# st.warnig("Warning")
# st.info("It's easy to build a streamlit app")
# st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("标题")
st.sidebar.button("确定")
st.sidebar.radio("选择", ["M", "W"])

# 直方图
rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

# 折线图
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)

# 条形图
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)

# 面积图
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)

# 牛郎星图表
df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
c = alt.Chart(df).mark_circle().encode(x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(c, use_container_width=True)

# 图形对象 流程图
st.graphviz_chart('''digraph {  
    Big_shark -> Tuna        
    Tuna -> Mackerel        
    Mackerel -> Small_fishes        
    Small_fishes -> Shrimp    
}''')

# 显示地图
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [23.23, 111.4], columns=['lat', 'lon'])
st.map(df)
