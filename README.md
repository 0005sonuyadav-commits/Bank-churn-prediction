# Bank Customer Churn Prediction - Streamlit App

This is a machine learning web application that predicts whether a bank customer is likely to churn (leave the bank) based on various customer attributes.

## Features

- Interactive web interface built with Streamlit
- Real-time churn prediction
- Risk assessment and recommendations
- User-friendly input forms
- Probability visualization

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model

Before running the app, you need to train the model:

```bash
python train_model.py
```

This will:
- Load and preprocess the data
- Engineer features
- Train a Random Forest classifier
- Save the trained model and scaler as `model.pkl` and `scaler.pkl`

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository, branch, and main file (app.py)
6. Click "Deploy"

**Important:** Make sure to run `train_model.py` locally first and commit `model.pkl` and `scaler.pkl` to your repository.

### Option 2: Heroku

1. Install Heroku CLI
2. Create `Procfile`:
```
web: sh setup.sh && streamlit run app.py
```

3. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

4. Deploy:
```bash
heroku create your-app-name
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### Option 3: AWS/Azure/GCP

You can deploy this app on any cloud platform that supports Python applications.

## Project Structure

```
Bank_Project/
├── app.py                 # Streamlit application
├── train_model.py         # Model training script
├── Bank.ipynb            # Original Jupyter notebook
├── European_Bank.csv     # Dataset
├── requirements.txt      # Python dependencies
├── model.pkl            # Trained model (generated)
├── scaler.pkl           # Feature scaler (generated)
└── README.md            # This file
```

## Model Information

- **Algorithm:** Random Forest Classifier
- **Features Used:**
  - Credit Score
  - Geography
  - Gender
  - Age
  - Tenure
  - Balance
  - Number of Products
  - Has Credit Card
  - Is Active Member
  - Estimated Salary
  - Engineered features (ratios and interactions)

## Usage

1. Open the app in your browser
2. Input customer information using the sliders and dropdowns
3. Click "Predict Churn" button
4. View the prediction results and risk assessment
5. Get actionable recommendations

## Links

Once deployed, your app will be available at one of these URLs depending on your deployment method:

- **Streamlit Cloud:** `https://your-username-bank-churn-prediction.streamlit.app`
- **Heroku:** `https://your-app-name.herokuapp.com`

## License

This project is open source and available under the MIT License.
