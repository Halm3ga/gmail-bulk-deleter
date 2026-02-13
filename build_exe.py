import PyInstaller.__main__
import os
import shutil

def build_executable():
    print("Building Gmail Deleter executable...")
    
    # Clean previous builds
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('dist'):
        shutil.rmtree('dist')
        
    PyInstaller.__main__.run([
        'app.py',
        '--name=GmailDeleter',
        '--onefile',
        '--console',
        '--clean',
        '--add-data=credentials.json;.',  # Bundle credentials.json inside EXE
        '--hidden-import=googleapiclient',
        '--hidden-import=google_auth_oauthlib',
    ])
    
    print("\n[SUCCESS] Build complete!")
    print("Executable is located in 'dist/GmailDeleter.exe'")
    print("This is a STANDALONE app. You can move the .exe to any PC and it will work!")

if __name__ == "__main__":
    build_executable()
