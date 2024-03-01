import streamlit as st
import pandas as pd
import numpy as np
import pickle  # to load a saved modelimport base64  #to open .gif files in streamlit app

"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
