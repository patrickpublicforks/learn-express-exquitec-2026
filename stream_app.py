import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("My Datascience Project")

st.write("**:red[My first page]**")

val = st.text_input("enter your name")

df = pd.DataFrame({
    val: [1,2,3],
    "name": ["ase", "ade", "remi"],
    "y": [100, 150, 129] 
})

df

fig, ax = plt.subplots()
ax.plot(df[val], df["y"], label="Sine Wave")
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Sine Wave')
ax.legend()

# 3. Display the plot in Streamlit using st.pyplot()
st.pyplot(fig)