# Maternal Health Risk Dashboard

An interactive Streamlit project for exploring the Maternal Health Risk dataset through descriptive analysis and machine learning-based risk prediction.

## Project Contents

- `app.py`: Descriptive dashboard for exploring the dataset.
- `pages/`: Additional pages for population distributions, risk-level comparisons, and feature correlations.
- `prediction_app.py`: Interactive dashboard for predicting maternal health risk using trained machine learning models.
- `models/`: Saved machine learning models and associated mapping files.
- `data_preprocessing.ipynb`: Data assessment, preprocessing, model development, and evaluation.
- `Maternal Health Risk Data Set.csv`: Dataset used in the project.
- `requirements.txt`: Required Python packages.

## Run the Dashboard

### 1. Clone the repository

```bash
git clone https://github.com/BingerLiang77/maternal_risk.git
cd maternal_risk
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### Descriptive Dashboard

Start the descriptive dashboard:

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`.

### Predictive Dashboard

Open a separate terminal, enter the project folder, activate the same virtual environment, and run:

```bash
streamlit run prediction_app.py --server.port 8502
```

The predictive dashboard will be available at `http://localhost:8502`.

To stop a dashboard, press `Ctrl+C` in the corresponding terminal.

## Disclaimer

This project is intended for educational demonstration only. Model-predicted probabilities may be uncalibrated and should not be interpreted as actual clinical outcome probabilities. The dashboard is not a substitute for professional medical assessment.
