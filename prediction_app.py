import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Maternal Risk Prediction",
    page_icon="🩺",
    layout="centered"
)

# Load trained model
MODEL_PATH = Path(__file__).parent / "models" / "cleaned.joblib"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()


# Initialize session state
if "validated" not in st.session_state:
    st.session_state.validated = False

if "validated_values" not in st.session_state:
    st.session_state.validated_values = None


# Model introduction
st.title("Maternal Health Risk Prediction")

st.markdown("""
This dashboard uses a **Decision Tree classification model**
to explore maternal health risk categories based on selected
demographic and physiological measurements.

Enter the measurements below, validate your inputs, and obtain
the model's predicted risk category.
""")

st.divider()


# User inputs
st.caption("Enter patient measurements below.")
st.subheader("Patient Measurements")


age = st.number_input(
    "Age (years)",
    min_value=0,
    max_value=100,
    value=None,
    step=1
)

glucose = st.number_input(
    "Blood Glucose (mmol/L)",
    min_value=0.0,
    max_value=60.0,
    value=None,
    step=0.1
)

systolic = st.number_input(
    "Systolic BP (mmHg)",
    min_value=0,
    max_value=350,
    value=None,
    step=1
)

diastolic = st.number_input(
    "Diastolic BP (mmHg)",
    min_value=0,
    max_value=250,
    value=None,
    step=1
)

temperature = st.number_input(
    "Body Temperature (°F)",
    min_value=80.0,
    max_value=115.0,
    value=None,
    step=0.1
)

heart_rate = st.number_input(
    "Heart Rate (bpm)",
    min_value=0,
    max_value=300,
    value=None,
    step=1
)


# Validation ranges
limits = {
    "Age": (10, 70),
    "Blood glucose": (1, 36),
    "Systolic BP": (50, 300),
    "Diastolic BP": (20, 200),
    "Body temperature": (91.4, 107.6),
    "Heart rate": (1, 250),
}


values = {
    "Age": age,
    "Blood glucose": glucose,
    "Systolic BP": systolic,
    "Diastolic BP": diastolic,
    "Body temperature": temperature,
    "Heart rate": heart_rate,
}


# Reset validation if any input changes
current_values = tuple(values.values())

if (
    st.session_state.validated
    and st.session_state.validated_values != current_values
):
    st.session_state.validated = False
    st.session_state.validated_values = None


# Validate inputs
st.divider()

if st.button(
    "Proceed",
    type="primary",
    use_container_width=True
):
    invalid = []

    for name, value in values.items():
        lower, upper = limits[name]

        if value is None:
            invalid.append(name)
            st.error(f"{name}: Please enter a value.")

        elif not lower <= value <= upper:
            invalid.append(name)
            st.error(
                f"{name}: Value {value} is outside the "
                f"validation range ({lower}–{upper}). "
                "Please verify the measurement, unit, and entry."
            )

    # Check consistency between systolic and diastolic BP
    if systolic is not None and diastolic is not None:
        if systolic <= diastolic:
            invalid.append("Blood pressure relationship")
            st.error(
                "Systolic BP should be higher than diastolic BP. "
                "Please verify both measurements."
            )

    if invalid:
        st.session_state.validated = False
        st.session_state.validated_values = None
    else:
        st.session_state.validated = True
        st.session_state.validated_values = current_values


# Clinical warnings
if st.session_state.validated:
    st.divider()
    st.subheader("Clinical Warnings")

    warnings = []

    # Blood glucose warnings
    if glucose < 3.0:
        warnings.append(
            "Very low blood glucose: below 3.0 mmol/L. "
            "Prompt clinical assessment may be needed."
        )
    elif glucose < 3.9:
        warnings.append(
            "Low blood glucose: below 3.9 mmol/L."
        )
    elif glucose >= 11.1:
        warnings.append(
            "High glucose: interpretation depends on the "
            "measurement context and may require clinical confirmation."
        )

    # Blood pressure warnings
    if systolic >= 180 or diastolic >= 110:
        warnings.append(
            "Severe-range high blood pressure: urgent clinical assessment "
            "is required, especially during pregnancy."
        )
    elif systolic >= 140 or diastolic >= 90:
        warnings.append(
            "Elevated blood pressure: clinical assessment is recommended."
        )
    elif systolic < 90 or diastolic < 60:
        warnings.append(
            "Low blood pressure: assess symptoms and clinical context."
        )

    # Temperature warnings
    if temperature >= 100.4:
        warnings.append(
            "Elevated temperature: 100.4°F (38°C) or above."
        )
    elif temperature < 95.0:
        warnings.append(
            "Low temperature: verify the measurement and assess clinically."
        )

    # Heart rate warnings
    if heart_rate >= 120:
        warnings.append(
            "High heart rate: assess symptoms and clinical context."
        )
    elif heart_rate < 30:
        warnings.append(
            "Very low heart rate. Prompt clinical assessment may be needed."
        )
    elif heart_rate < 50:
        warnings.append(
            "Low heart rate: assess symptoms and clinical context."
        )

    if warnings:
        for warning in warnings:
            st.warning(warning)
    else:
        st.success("No warnings triggered by the configured rules.")


# Prediction

st.divider()
st.subheader("Risk Prediction")

if not st.session_state.validated:
    st.info("Please enter patient measurements and click Proceed.")

else:
    if st.button(
        "Predict Risk Level",
        type="primary",
        use_container_width=True
    ):
        # Prepare input using the model's expected feature names
        input_data = pd.DataFrame([{
            "Age": age,
            "SystolicBP": systolic,
            "DiastolicBP": diastolic,
            "BS": glucose,
            "BodyTemp": temperature,
            "HeartRate": heart_rate
        }])

        # Predict risk category without displaying probabilities
        predicted_class = model.predict(input_data)[0]

        st.divider()
        st.subheader("Prediction Results")

        st.metric(
            label="Predicted Risk Level",
            value=str(predicted_class).title()
        )

        st.caption(
            "This model is intended for educational demonstration only. "
            "Its predictions are not clinically validated and should not "
            "be used as a substitute for professional clinical assessment."
        )

