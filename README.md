# Sort Files – Windows Context Menu Tool

This is a small Python tool for Windows that adds a **“Sort Files”** option to the right-click context menu, I build it many Years ago but never published it on Git, but now I found it on my PC and Published it :) .

Once installed, you can right-click any folder and automatically sort all files inside it into subfolders based on their file extensions.

Simple idea, big time saver.
 
---
## How it works

After installation, Windows gets a new context menu entry:

**Right click → Sort Files**

When you click it, all files in the selected folder are moved into folders like `Images`, `Documents`, `Audio`, and more, depending on their file type.

---

## Installation

⚠️ **Administrator rights are required**, because this tool modifies the Windows registry.

1. Make sure Python is installed and added to your PATH  
2. Open **PowerShell as Administrator**
3. Navigate to the project directory
4. Run:

```powershell
python setup_context_menu.py


