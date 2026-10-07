import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Feature Correlations")

st.write("""
Explore relationships between demographic
and clinical variables in the maternal health population.
""")

# Load data
df = pd.read_csv("Maternal Health Risk Data Set.csv")


features = [
    "Age",
    "SystolicBP",
    "DiastolicBP",
    "BS",
    "BodyTemp",
    "HeartRate"
]

risk_order = ["high risk", "mid risk", "low risk"]


# -----------------------------
# 1. Overall correlation matrix
# -----------------------------

st.header("Overall Feature Correlation")

corr = df[features].corr()

fig, ax = plt.subplots(figsize=(9, 7))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    ax=ax
)

ax.set_title("Feature Correlation")

plt.tight_layout()

st.pyplot(fig)


# -----------------------------
# 2. Explore individual relationships
# -----------------------------

st.header("Explore a Relationship")

st.write("""
Select two variables to explore their relationship.
Points are coloured according to maternal health risk level.
""")

col1, col2 = st.columns(2)

with col1:
    x_variable = st.selectbox(
        "Select X variable",
        features,
        index=0
    )

with col2:
    y_variable = st.selectbox(
        "Select Y variable",
        features,
        index=1
    )


correlation = df[x_variable].corr(df[y_variable])

risk_palette = {
    "high risk": "red",
    "mid risk": "orange",
    "low risk": "green"
}

fig, ax = plt.subplots(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x=x_variable,
    y=y_variable,
    hue="RiskLevel",
    palette=risk_palette,
    alpha=1,
    ax=ax
)

ax.set_title(f"{x_variable} vs {y_variable}")
ax.set_xlabel(x_variable)
ax.set_ylabel(y_variable)

plt.tight_layout()

st.pyplot(fig)


st.metric(
    "Pearson correlation",
    f"{correlation:.2f}"
)