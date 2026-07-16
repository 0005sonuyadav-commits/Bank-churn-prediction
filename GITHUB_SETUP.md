# 🔗 GitHub Setup - Get Your Repository URL

## Step-by-Step Guide to Create GitHub Repository and Get URL

---

## 📋 Prerequisites

- A GitHub account (if you don't have one, create at https://github.com/join)
- Git installed on your computer

---

## ✅ Step 1: Check if Git is Installed

Open Terminal and run:

```bash
git --version
```

**If you see a version number** (like `git version 2.x.x`):
✅ Git is installed! Continue to Step 2.

**If you see "command not found":**
❌ Install Git:
- Mac: `brew install git` (or download from https://git-scm.com/)
- Windows: Download from https://git-scm.com/

---

## 🌐 Step 2: Create GitHub Repository

### Option A: Via GitHub Website (Recommended)

1. **Go to GitHub:**
   - Visit: https://github.com/new

2. **Fill in Repository Details:**
   - **Repository name:** `bank-churn-prediction`
   - **Description:** `Bank Customer Churn Prediction using Machine Learning and Streamlit`
   - **Visibility:** Public ✅ (Required for free Streamlit deployment)
   - **DON'T check:** ❌ Add a README file
   - **DON'T check:** ❌ Add .gitignore
   - **DON'T check:** ❌ Choose a license

3. **Click:** "Create repository" button

4. **Copy Your Repository URL:**
   
   You'll see a page with commands. Look for the HTTPS URL:
   
   ```
   https://github.com/YOUR_USERNAME/bank-churn-prediction.git
   ```
   
   **COPY THIS URL!** You'll need it in Step 3.

---

## 💻 Step 3: Initialize Git in Your Project

Open Terminal and run these commands one by one:

```bash
# Navigate to your project
cd "/Users/sonuyadav/Desktop/Prime folder/Bank_Project"

# Check current directory (should show your project folder)
pwd

# Initialize Git repository
git init

# Configure Git (replace with YOUR info)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Check Git status
git status
```

---

## 📦 Step 4: Commit Your Files

```bash
# Add all files to Git
git add .

# Check what will be committed
git status

# Commit with a message
git commit -m "Initial commit: Bank Churn Prediction App"

# Verify commit
git log --oneline
```

---

## 🔗 Step 5: Connect to GitHub

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/bank-churn-prediction.git

# Verify remote
git remote -v
```

You should see:
```
origin  https://github.com/YOUR_USERNAME/bank-churn-prediction.git (fetch)
origin  https://github.com/YOUR_USERNAME/bank-churn-prediction.git (push)
```

---

## 🚀 Step 6: Push to GitHub

```bash
# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

**You'll be asked for credentials:**

### Option A: Personal Access Token (Recommended)

1. **Create Token:**
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token" → "Generate new token (classic)"
   - Give it a name: "Bank Churn App"
   - Select scopes: ✅ repo (all)
   - Click "Generate token"
   - **COPY THE TOKEN** (you won't see it again!)

2. **Use Token as Password:**
   - Username: Your GitHub username
   - Password: **Paste the token** (not your GitHub password!)

### Option B: SSH (Advanced)

Follow GitHub's SSH guide: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

---

## ✅ Step 7: Verify on GitHub

1. **Go to Your Repository:**
   ```
   https://github.com/YOUR_USERNAME/bank-churn-prediction
   ```

2. **You should see:**
   - All your files listed
   - README.md displayed at bottom
   - Green "Code" button
   - Your commit message

---

## 🎯 Your GitHub URL

Your repository URL is:

```
https://github.com/YOUR_USERNAME/bank-churn-prediction
```

**Write your actual URL here:**

```
https://github.com/_______________/bank-churn-prediction
```

---

## 📝 Quick Reference: All Commands in Order

```bash
# 1. Navigate to project
cd "/Users/sonuyadav/Desktop/Prime folder/Bank_Project"

# 2. Initialize Git
git init

# 3. Configure Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 4. Add files
git add .

# 5. Commit
git commit -m "Initial commit: Bank Churn Prediction App"

# 6. Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/bank-churn-prediction.git

# 7. Push
git branch -M main
git push -u origin main
```

---

## 🔄 Future Updates

After making changes to your code:

```bash
# Add changes
git add .

# Commit with message
git commit -m "Description of changes"

# Push to GitHub
git push
```

Streamlit Cloud will automatically redeploy! 🎉

---

## 🐛 Troubleshooting

### Problem: "remote origin already exists"

**Solution:**
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/bank-churn-prediction.git
```

### Problem: "failed to push some refs"

**Solution:**
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Problem: Authentication failed

**Solutions:**
1. Use Personal Access Token (not password)
2. Create token at: https://github.com/settings/tokens
3. Use token as password when pushing

### Problem: "src refspec main does not match any"

**Solution:**
```bash
git branch -M main
git push -u origin main
```

---

## 🎯 Next Steps

Now that your code is on GitHub:

1. ✅ Your GitHub URL is ready
2. 🚀 Go to Streamlit Cloud: https://share.streamlit.io/
3. 🔗 Connect your GitHub repository
4. 🌐 Deploy your app!

Follow **START_HERE.md** Step 5 for Streamlit deployment.

---

## 📱 Share Your Repository

Your GitHub repository URL to share:
```
https://github.com/YOUR_USERNAME/bank-churn-prediction
```

Once deployed on Streamlit, you'll also get an app URL:
```
https://YOUR_USERNAME-bank-churn-prediction-app-xxxxx.streamlit.app
```

---

## ✨ GitHub Repository Checklist

- [ ] Repository created on GitHub
- [ ] Git initialized locally
- [ ] Files committed
- [ ] Remote added
- [ ] Pushed to GitHub
- [ ] Files visible on GitHub website
- [ ] URL copied for Streamlit deployment

---

## 💡 Pro Tips

1. **Keep README Updated:** Your README.md shows on GitHub homepage
2. **Write Good Commits:** Use descriptive commit messages
3. **Push Often:** Regular pushes = backup + deployment
4. **Check Status:** Use `git status` frequently
5. **View History:** Use `git log` to see commits

---

## 🎓 Learn More About Git

- **Git Basics:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com/
- **Interactive Tutorial:** https://learngitbranching.js.org/

---

## 🎉 Congratulations!

Your code is now on GitHub! 

**Your Repository URL:**
```
https://github.com/YOUR_USERNAME/bank-churn-prediction
```

Use this URL to deploy on Streamlit Cloud! 🚀
