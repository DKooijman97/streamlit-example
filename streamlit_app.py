import streamlit as st
from mathModel import linearFunction
import plotly.express as px

st.write(""""
#My First app
*Hello *world!*
""")

a = st.number_input('Enter a number for the slope', value = 1)
b = st.number_input('Enter a number for the intercept', value = 0)
step = st.number_input('Enter a number for the step', value = 1)

values = st.slider('Select a range of values',0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

df = linearFunction(b=b, a=a, gridInfo = [values[0], values[1] +1, step])
fig = px.scatter(df, x="x", y="y", trendline="ols")

st.plotly_chart(fig)