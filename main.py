import streamlit as st
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split

#mining data
df = pd.read_csv('Thousand youtubers.csv')
st.title("data analysis")

#df1 =df.drop(['ID','Year','Category','Product','UnitPrice','TotalPrice'], axis='columns')
#st.write(df1)
#st.map(df1)

if st.button('load dataset'):
    st.write(df)

if st.button('load description'):
    st.write(df.describe())

#a1 = pd.DataFrame(df['Year'], df['Total Price'])
#st.line_chart(df['Year'], df['Total Price'])

fig = plt.figure(figsize=(10,8))
plt.bar(df['Visits'], df['Likes'])
st.pyplot(fig)

col1,col2,col3 = st.columns(3)
col1.metric(st.write(df))
col2.metric(st.write(df.describe))


