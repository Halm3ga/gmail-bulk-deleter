# How to Get `credentials.json` for Gmail API

You MUST enable the Gmail API and download `credentials.json` for this app to work. Follow these exact steps:

---

## Step 1: Create a Project
1. Go to **[Google Cloud Console](https://console.cloud.google.com/)**
2. Click the project dropdown (next to logo) → **New Project**
3. Name it `GmailCleaner` and click **Create**
4. Wait for it to be created, then **Select Project**

## Step 2: Enable Gmail API
1. In the search bar at the top, type `Gmail API`
2. Select **Gmail API** from the results
3. Click **ENABLE**

## Step 3: Configure OAuth Consent Screen
1. Go to **APIs & Services** → **OAuth consent screen** (left menu)
2. Choose **External** → Click **Create**
3. **App Information**:
   - App name: `GmailCleaner`
   - User support email: (Select your email)
   - Developer contact email: (Type your email)
4. Click **SAVE AND CONTINUE**
5. **Scopes**: Click **ADD OR REMOVE SCOPES**
   - Search for `gmail.modify`
   - Check the box for `https://www.googleapis.com/auth/gmail.modify`
   - Click **UPDATE**, then **SAVE AND CONTINUE**
6. **Test Users**: Click **ADD USERS**
   - Enter your Gmail address (and any others you want to clean)
   - Click **ADD**, then **SAVE AND CONTINUE**

## Step 4: Create Credentials
1. Go to **APIs & Services** → **Credentials**
2. Click **+ CREATE CREDENTIALS** → **OAuth client ID**
3. **Application type**: Select **Desktop app**
4. Name: `GmailCleaner Desktop`
5. Click **CREATE**

## Step 5: Download the File
1. A popup will show "OAuth client created"
2. Click **DOWNLOAD JSON**
3. Rename the file to **`credentials.json`**
4. Move it to the project folder:
   `c:\Users\Me\Desktop\Files\Python\EmailDelete\`

---

## 🚀 That's it!
Now the app can log in and clean your emails.
The first time you run it, a browser window will open asking for permission.
