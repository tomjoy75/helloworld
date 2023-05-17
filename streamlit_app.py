import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

st.header("st.write")
    
st.write("Hello, *World!* :sunglasses:")

st.write(1234)

df = pd.DataFrame({
    "première colonne" : [1 ,2 ,3 ,4],
    "deuxième colonne" : [10, 20, 30, 40]
})
st.write(df)

st.write("Ci-dessous se trouve un DataFrame :", df, "Ci-dessus se trouve un DataFrame")

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=["a", "b", "c"])
c = alt.Chart(df2).mark_circle().encode(
    x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
st.write(df2)
st.write(c)
# if st.button("say hello"):
#     st.write("why hello?")
# else:
#     st.write("goodbye")