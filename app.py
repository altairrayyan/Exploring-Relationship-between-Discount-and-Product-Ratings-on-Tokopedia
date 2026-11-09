from pathlib import Path
import pandas as pd
import json
import numpy as np
import plotly.graph_objects as go
import streamlit as st

params = json.load(open(Path(__file__).parent / "m3_params.json"))
st.title("Discount and Rating Tokopedia Products")

diskon = st.checkbox("Discount")
review = st.slider("Number of Reviews", 0, 5000, 10)
price = st.number_input("Harga sebelum diskon (Rp)", min_value=1000, value=100000)

z = (params["Intercept"]
     + params["has_discount"] * int(diskon)
     + params["n_log_reviews"] * np.log10(review + 1)
     + params["log_pricelist"] * np.log10(price))
p = 1 / (1 + np.exp(-z))
st.metric("Chance of getting 5.0 rating", f"{p:.0%}")

grid = np.linspace(0, np.log10(5001), 100)

fig = go.Figure()
for d, nama in [(0, "Tanpa diskon"), (1, "Diskon")]:
    z_grid = (params["Intercept"]
          + params["has_discount"] * d
          + params["n_log_reviews"] * grid
          + params["log_pricelist"] * np.log10(price))
    fig.add_trace(go.Scatter(x=grid, y=1 / (1 + np.exp(-z_grid)), mode="lines", name=nama))

fig.add_trace(go.Scatter(x=[np.log10(review + 1)], y=[p], mode="markers", name="Input kamu"))
fig.update_layout(xaxis_title="log10(jumlah review + 1)", yaxis_title="Peluang rating 5.0", yaxis_range=[0, 1])
st.plotly_chart(fig)



