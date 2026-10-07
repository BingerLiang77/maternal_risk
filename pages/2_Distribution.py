import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Risk-Level Comparisons")

st.write("""
Compare the distributions of demographic and clinical characteristics across maternal health risk levels.
""")

# Load data
df = pd.read_csv("Maternal Health Risk Data Set.csv")

# Features
features = [
    "Age",
    "SystolicBP",
    "DiastolicBP",
    "BS",
    "BodyTemp",
    "HeartRate"
]

# Let the user select a variable
variable = st.selectbox(
    "Select a variable",
    features
)

# Risk level order
risk_order = ["high risk", "mid risk", "low risk"]

# Create boxplot
fig, ax = plt.subplots(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="RiskLevel",
    y=variable,
    ax=ax,
    order=risk_order
)

ax.set_title(f"Distribution of {variable} by Risk Level")
ax.set_xlabel("Risk Level")
ax.set_ylabel(variable)

plt.tight_layout()

st.pyplot(fig)



# Distribution summary
st.subheader("Distribution Summary")

summary = (
    df.groupby("RiskLevel")[variable]
    .agg(
        Min="min",
        Q1=lambda x: x.quantile(0.25),
        Median="median",
        Q3=lambda x: x.quantile(0.75),
        Max="max"
    )
    .reindex(risk_order)
)

# Calculate IQR
summary["IQR"] = summary["Q3"] - summary["Q1"]

# Reorder columns
summary = summary[
    [ "Median","Q1", "Q3", "Max","Min", "IQR"]
]

# Display table
st.dataframe(
    summary.round(2),
    use_container_width=True
)

