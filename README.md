# Maternal Health Risk Dashboard

An interactive Streamlit dashboard for exploring the Maternal Health Risk dataset, together with the data preprocessing and machine learning analysis.

## Run the Dashboard

1. Clone the repository and enter the project folder:

```bash
git clone <repository-url>
cd maternal_risk
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Start the Streamlit dashboard:

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`.

To stop the dashboard, press `Ctrl+C` in the terminal.

## Project Structure

```text
maternal_risk/
├── app.py
├── pages/
├── data_preprocessing.ipynb
├── requirements.txt
└── README.md
```

- `app.py` — Streamlit dashboard
- `pages/` — dashboard pages
- `data_preprocessing.ipynb` — data processing and machine learning analysis
- `requirements.txt` — required Python packages
