# Deployment Guide

## Quick Deployment to Streamlit Cloud

### Step 1: Prepare Your Repository

1. **Install dependencies** (in your local environment):
```bash
pip install -r requirements.txt
```

2. **Train the model locally**:
```bash
cd "/Users/sonuyadav/Desktop/Prime folder/Bank_Project"
python train_model.py
```

This will create `model.pkl` and `scaler.pkl` files.

### Step 2: Push to GitHub

1. **Initialize Git** (if not already done):
```bash
cd "/Users/sonuyadav/Desktop/Prime folder/Bank_Project"
git init
```

2. **Create .gitignore**:
```bash
echo "*.pyc
__pycache__/
.DS_Store
.ipynb_checkpoints/
*.log" > .gitignore
```

3. **Add and commit files**:
```bash
git add .
git commit -m "Initial commit: Bank Churn Prediction App"
```

4. **Create a new repository on GitHub** (via web browser):
   - Go to https://github.com/new
   - Name it: `bank-churn-prediction`
   - Don't initialize with README (you already have one)
   - Click "Create repository"

5. **Push to GitHub**:
```bash
git remote add origin https://github.com/YOUR_USERNAME/bank-churn-prediction.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**:
   - Visit: https://share.streamlit.io/

2. **Sign in with GitHub**:
   - Click "Sign in with GitHub"
   - Authorize Streamlit

3. **Create New App**:
   - Click "New app" button
   - Select your repository: `YOUR_USERNAME/bank-churn-prediction`
   - Branch: `main`
   - Main file path: `app.py`
   - Click "Deploy"

4. **Wait for Deployment**:
   - Streamlit will install dependencies
   - Build and deploy your app
   - This usually takes 2-5 minutes

5. **Get Your Link**:
   - Once deployed, you'll get a URL like:
   - `https://YOUR_USERNAME-bank-churn-prediction-app-xxxxx.streamlit.app`

### Step 4: Share Your App

Your app is now live! Share the URL with anyone.

## Alternative: Local Testing

Before deploying, test locally:

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Troubleshooting

### Issue: ModuleNotFoundError

**Solution**: Make sure all dependencies are in `requirements.txt` and installed:
```bash
pip install -r requirements.txt
```

### Issue: Model files not found

**Solution**: Run the training script:
```bash
python train_model.py
```

Make sure `model.pkl` and `scaler.pkl` are committed to Git:
```bash
git add model.pkl scaler.pkl
git commit -m "Add trained model files"
git push
```

### Issue: App not loading on Streamlit Cloud

**Solutions**:
1. Check the logs in Streamlit Cloud dashboard
2. Verify `requirements.txt` has all dependencies
3. Make sure `model.pkl` and `scaler.pkl` are in the repository
4. Check that `app.py` doesn't have any syntax errors

## App URL

After successful deployment, your app will be accessible at:
```
https://YOUR_USERNAME-bank-churn-prediction-app-xxxxx.streamlit.app
```

## Notes

- The free tier of Streamlit Cloud is perfect for this app
- Your app will sleep after inactivity but wake up when visited
- You can redeploy anytime by pushing changes to GitHub
- Streamlit Cloud automatically rebuilds when you push updates

## Customization

You can customize the app appearance by editing `.streamlit/config.toml`:
- Change theme colors
- Modify fonts
- Adjust layout settings

## Support

If you encounter issues:
1. Check Streamlit documentation: https://docs.streamlit.io
2. Visit Streamlit Community forum: https://discuss.streamlit.io
3. Check GitHub Issues for similar problems
