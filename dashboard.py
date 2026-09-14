import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("My Live Dashboard")

data = pd.DataFrame({
    "x": range(20),
    "y": np.random.randint(1, 100, 20)
})

st.metric("Current Value", data["y"].iloc[-1])

fig = px.line(data, x="x", y="y", title="Live Chart")
st.plotly_chart(fig, use_container_width=True)
