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

## Step 3: Configure Consent Screen (New UI)

1.  **Click `Branding`** (Left Menu)
    *   **App name**: Enter `GmailCleaner`
    *   **User support email**: Select your email
    *   **Developer contact email**: Enter your email
    *   Click **SAVE**

2.  **Click `Data Access`** (Left Menu)
    *   Click **ADD OR REMOVE SCOPES**
    *   Search for `gmail.modify`
    *   Check: `https://www.googleapis.com/auth/gmail.modify`
    *   Click **UPDATE** → **SAVE**

3.  **Click `Audience`** (Left Menu)
    *   Scroll down to **Test users**
    *   Click **ADD USERS**
    *   Enter your Gmail address
    *   Click **SAVE**

## Step 4: Create Credentials

1.  **Click `Clients`** (Left Menu)
    *   Click **CREATE CLIENT**
    *   **Application type**: `Desktop app`
    *   **Name**: `GmailCleaner Desktop`
    *   Click **CREATE**

2.  **Download JSON**
    *   Click the **Download JSON** icon (⬇️) next to the new client
    *   Rename file to: **`credentials.json`**
    *   Move to project folder: `c:\Users\Me\Desktop\Files\Python\EmailDelete\`

---

## 🚀 That's it!
Now the app can log in and clean your emails.
The first time you run it, a browser window will open asking for permission.
