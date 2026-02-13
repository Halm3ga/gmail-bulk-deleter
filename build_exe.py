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
        '--hidden-import=googleapiclient',
        '--hidden-import=google_auth_oauthlib',
    ])
    
    print("\n✅ Build complete!")
    print("Executable is located in 'dist/GmailDeleter.exe'")
    print("\n⚠️ IMPORTANT: You must copy 'credentials.json' to the same folder as the exe!")

if __name__ == "__main__":
    build_executable()
