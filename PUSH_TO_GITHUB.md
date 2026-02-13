# Push Email Deleter to GitHub

## Step 1: Create Repository
1. Go to **[GitHub New Repo](https://github.com/new)**
2. Name: `gmail-bulk-deleter`
3. **Do not** initialize with README/gitignore
4. Click **Create repository**

## Step 2: Push Code
Run these commands in PowerShell:

```powershell
cd c:\Users\Me\Desktop\Files\Python\EmailDelete

# Add remote (Change Halm3ga to your username if different)
git remote add origin https://github.com/Halm3ga/gmail-bulk-deleter.git

# Set branch name
git branch -M main

# Push
git push -u origin main
```

## Step 3: Releases (Optional)
You can upload the `GmailDeleter.exe` file from the `dist` folder to GitHub Releases to share it easily!
