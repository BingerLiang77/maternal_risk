import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Maternal Health Risk Data Set")

# Load data
df = pd.read_csv("Maternal Health Risk Data Set.csv")

# 1. Dataset introduction

st.header("About the dataset")

st.write("""
This dataset contains demographic and clinical measurements
collected from pregnant women. Data has been collected from 
different hospitals, community clinics, maternal health cares 
from the rural areas of Bangladesh through the IoT based risk 
monitoring system.

""")

# 2. Dataset summary

st.header("Dataset summary")

col1, col2, col3 = st.columns(3)

col1.metric("Number of patients", len(df))
col2.metric("Number of features", (len(df.columns)-1))
col3.metric("Risk categories", df["RiskLevel"].nunique())


# 3. Dataset preview

st.header("Dataset preview")

st.write("A preview of the dataset is shown below.")

st.dataframe(
    df.head(10),
    use_container_width=True
)

# 4. Dataset preview

st.header("Risk Group Distribution")

fig, ax = plt.subplots(figsize=(8, 5))

sns.countplot(
    data=df,
    x="RiskLevel",
    order=["high risk", "mid risk", "low risk"],
    ax=ax
)

ax.set_title("Distribution of Risk Groups")
ax.set_xlabel("Risk Level")
ax.set_ylabel("Number of Patients")

plt.tight_layout()
st.pyplot(fig)