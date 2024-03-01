import streamlit as st


st.set_page_config(
    page_title="Your App Title",
    page_icon=None,
    layout="wide",  # 如果你希望使用宽屏布局
    initial_sidebar_state="collapsed",  # 这里设置侧边栏默认隐藏
    menu_items=None,
)

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
