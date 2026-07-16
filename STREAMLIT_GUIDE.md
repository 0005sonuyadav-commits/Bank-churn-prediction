# 🎈 Complete Streamlit Usage Guide

## What is Streamlit?

Streamlit is a Python framework that turns data scripts into shareable web apps in minutes. No frontend experience required!

---

## 🚀 Installing Streamlit

### Step 1: Install Streamlit

Open Terminal and run:

```bash
pip install streamlit
```

### Step 2: Verify Installation

```bash
streamlit --version
```

You should see something like: `Streamlit, version 1.28.1`

---

## 💻 Running Streamlit Apps

### Method 1: Run Your App

```bash
cd "/Users/sonuyadav/Desktop/Prime folder/Bank_Project"
streamlit run app.py
```

**What happens:**
- Terminal shows: "You can now view your Streamlit app in your browser"
- Browser automatically opens to `http://localhost:8501`
- App loads with your interface

### Method 2: Specific Port

```bash
streamlit run app.py --server.port 8502
```

### Method 3: Disable Auto-Open Browser

```bash
streamlit run app.py --server.headless true
```

---

## 🛑 Stopping Streamlit

In the terminal where Streamlit is running:

```bash
Press: Ctrl + C
```

The app will stop and terminal returns to normal.

---

## 🎨 Basic Streamlit Commands (Used in Your App)

### 1. **Display Text**

```python
import streamlit as st

st.title("🏦 My App")                    # Large title
st.header("Section Header")              # Section header
st.subheader("Subsection")               # Smaller header
st.text("Plain text")                    # Plain text
st.markdown("**Bold** and *italic*")     # Markdown formatting
```

### 2. **Input Widgets**

```python
# Slider
age = st.slider("Select Age", 18, 100, 35)

# Number input
balance = st.number_input("Balance", 0, 300000, 50000)

# Selectbox (dropdown)
country = st.selectbox("Country", ["USA", "UK", "India"])

# Radio buttons
choice = st.radio("Pick one", ["Yes", "No"])

# Checkbox
agree = st.checkbox("I agree")

# Text input
name = st.text_input("Enter name")

# Date input
date = st.date_input("Select date")
```

### 3. **Buttons**

```python
# Regular button
if st.button("Click Me"):
    st.write("Button was clicked!")

# Primary button (styled)
if st.button("Submit", type="primary"):
    st.success("Submitted!")
```

### 4. **Display Results**

```python
# Success message (green)
st.success("✅ Success message")

# Error message (red)
st.error("❌ Error message")

# Warning (yellow)
st.warning("⚠️ Warning message")

# Info (blue)
st.info("ℹ️ Info message")

# Display any data
st.write("Hello", "World", 123, [1, 2, 3])
```

### 5. **Layout - Columns**

```python
col1, col2 = st.columns(2)

with col1:
    st.header("Left Column")
    st.write("Content in left column")

with col2:
    st.header("Right Column")
    st.write("Content in right column")
```

### 6. **Display Data**

```python
import pandas as pd

# DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
st.dataframe(df)

# Metrics
st.metric("Temperature", "70°F", "1.2°F")

# JSON
st.json({"name": "John", "age": 30})
```

### 7. **Charts** (Optional)

```python
# Line chart
st.line_chart(df)

# Bar chart
st.bar_chart(df)

# Area chart
st.area_chart(df)
```

---

## 🔄 How Streamlit Works

### Key Concept: **Reruns from Top to Bottom**

- Every time user interacts with widget, **entire script reruns**
- Streamlit is smart: only updates what changed
- This is why buttons work instantly!

### Example:

```python
import streamlit as st

st.title("Counter App")

# Initialize counter in session state
if 'count' not in st.session_state:
    st.session_state.count = 0

# Button increments counter
if st.button("Increment"):
    st.session_state.count += 1

# Display counter
st.write(f"Count: {st.session_state.count}")
```

---

## 📦 Caching (Important for Performance)

### Why Cache?

If you load data or train models, you don't want to reload every time!

### How to Cache:

```python
import streamlit as st

@st.cache_data  # Cache data (DataFrames, lists, etc.)
def load_data():
    df = pd.read_csv("data.csv")
    return df

@st.cache_resource  # Cache resources (models, connections)
def load_model():
    model = pickle.load(open('model.pkl', 'rb'))
    return model

# Use them
df = load_data()        # Loads once, then cached
model = load_model()    # Loads once, then cached
```

**In your app:**
```python
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model
```

This loads model **once**, not on every user interaction!

---

## 🎯 Your App Explained

Let me break down your `app.py`:

### Part 1: Setup
```python
import streamlit as st
import pandas as pd
# ... other imports

st.set_page_config(
    page_title="Bank Customer Churn Prediction",
    page_icon="🏦",
    layout="wide"
)
```
**What it does:** Configures page title, icon, and layout

### Part 2: Load Model
```python
@st.cache_resource
def load_model():
    # Load model and scaler
    ...
```
**What it does:** Loads model once and caches it

### Part 3: User Inputs
```python
col1, col2 = st.columns(2)

with col1:
    credit_score = st.slider("Credit Score", 300, 850, 650)
    age = st.slider("Age", 18, 100, 35)
    ...
```
**What it does:** Creates two columns with input widgets

### Part 4: Prediction
```python
if st.button("🔮 Predict Churn", type="primary"):
    # Process inputs
    # Make prediction
    # Display results
```
**What it does:** When button clicked, runs prediction

### Part 5: Display Results
```python
st.success("✅ Customer is likely to STAY")
st.metric("Churn Probability", "35.2%")
```
**What it does:** Shows prediction results with colors and metrics

---

## 🌐 Deploying on Streamlit Cloud

### Why Streamlit Cloud?

- ✅ **FREE** for public apps
- ✅ Automatic deployment from GitHub
- ✅ Built-in authentication (optional)
- ✅ Custom domains (optional)
- ✅ Resource management

### How to Deploy:

**Step 1:** Push to GitHub
```bash
git init
git add .
git commit -m "My Streamlit app"
git push
```

**Step 2:** Go to Streamlit Cloud
- Visit: https://share.streamlit.io/
- Sign in with GitHub
- Click "New app"

**Step 3:** Configure
- Repository: Your GitHub repo
- Branch: main
- Main file: app.py

**Step 4:** Deploy!
- Click "Deploy"
- Wait 2-3 minutes
- Get your public URL!

---

## 🔧 Streamlit Configuration

### Config File: `.streamlit/config.toml`

```toml
[theme]
primaryColor = "#FF4B4B"        # Button/link color
backgroundColor = "#FFFFFF"      # Page background
secondaryBackgroundColor = "#F0F2F6"  # Sidebar background
textColor = "#262730"            # Text color
font = "sans serif"              # Font family

[server]
headless = true                  # Don't open browser
port = 8501                      # Port number
enableCORS = false               # CORS settings
```

---

## 💡 Pro Tips

### 1. **Hot Reload**
- When you save `app.py`, Streamlit auto-reloads
- Click "Always rerun" for automatic updates

### 2. **Debug Mode**
- Use `st.write()` to debug variables
- Check terminal for error messages

### 3. **Session State**
- Store data across reruns
```python
st.session_state.my_variable = "value"
```

### 4. **Secrets Management**
- Never commit passwords/API keys
- Use `secrets.toml`:

```toml
# .streamlit/secrets.toml
[api]
key = "your-secret-key"
```

Access in code:
```python
api_key = st.secrets["api"]["key"]
```

### 5. **Performance**
- Use `@st.cache_data` for data
- Use `@st.cache_resource` for models
- Avoid expensive operations in main body

---

## 🐛 Common Issues & Solutions

### Issue 1: Port Already in Use

**Error:** "Address already in use"

**Solution:**
```bash
# Find and kill process
lsof -ti:8501 | xargs kill -9

# Or use different port
streamlit run app.py --server.port 8502
```

### Issue 2: Module Not Found

**Error:** "ModuleNotFoundError: No module named 'X'"

**Solution:**
```bash
pip install X
# or
pip install -r requirements.txt
```

### Issue 3: App Not Updating

**Solution:**
- Press 'R' in browser to rerun
- Click "Always rerun" in top-right menu
- Clear cache: Press 'C' in browser

### Issue 4: Slow Performance

**Solution:**
- Add caching decorators
- Reduce data size
- Optimize computations

---

## 📚 Learn More

### Official Resources:
- **Docs:** https://docs.streamlit.io/
- **Gallery:** https://streamlit.io/gallery
- **Forum:** https://discuss.streamlit.io/
- **Cheat Sheet:** https://docs.streamlit.io/library/cheatsheet

### Your Next Steps:
1. ✅ Run your app locally
2. ✅ Experiment with widgets
3. ✅ Deploy to Streamlit Cloud
4. ✅ Share your URL!

---

## 🎓 Quick Practice

Try this simple app:

```python
import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("What's your name?")
age = st.slider("How old are you?", 0, 100, 25)

if st.button("Submit"):
    st.write(f"Hello {name}! You are {age} years old.")
    st.balloons()  # Fun celebration!
```

Save as `test.py` and run:
```bash
streamlit run test.py
```

---

## ✨ For Your Bank Churn App:

### To Run:
```bash
cd "/Users/sonuyadav/Desktop/Prime folder/Bank_Project"
streamlit run app.py
```

### To Test:
1. Enter customer details
2. Click "Predict Churn"
3. See results instantly!

### To Deploy:
Follow **START_HERE.md** or **DEPLOYMENT_GUIDE.md**

---

## 🎉 You're Ready!

Now you know:
- ✅ How to run Streamlit apps
- ✅ Basic Streamlit commands
- ✅ How your app works
- ✅ How to deploy online
- ✅ Common troubleshooting

**Go ahead and run your app!**

```bash
streamlit run app.py
```

🚀 Happy Streamlit-ing!
