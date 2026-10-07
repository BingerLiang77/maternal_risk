import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Maternal Health Risk Data Set.csv")


# -----------------------------
# 1. Histogram
# -----------------------------

st.header("Population Distributions")

st.write("Explore the overall distribution of demographic and clinical characteristics in the maternal health population.")

variable = st.selectbox(
    "Select a variable",
    ["Age", "SystolicBP", "DiastolicBP",
     "BS", "HeartRate", "BodyTemp"]
)

fig, ax = plt.subplots()

ax.hist(df[variable].dropna(), bins=20)

ax.set_xlabel(variable)
ax.set_ylabel("Number of patients")
ax.set_title(f"Distribution of {variable}")

st.pyplot(fig)

# -----------------------------
# 2. Calculate skewness
# -----------------------------

skewness = df[variable].skew()

st.metric(
    "Skewness",
    f"{skewness:.2f}"
)