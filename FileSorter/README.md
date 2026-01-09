Sort Files – Windows Context Menu Tool

This is a small Python tool for Windows that adds a “Sort Files” option to the right-click context menu.

Once installed, you can right-click any folder and automatically sort all files inside it into subfolders based on their file extensions.

Simple idea, huge time saver.

How it works

After installation, Windows gets a new context menu entry:

Right click → Sort Files

When you click it, all files in the selected folder are moved into folders like Images, Documents, Audio, and so on, depending on their file type.

Installation

⚠️ Administrator rights are required, because this tool modifies the Windows registry.

Make sure Python is installed and added to your PATH

Open PowerShell as Administrator

Navigate to the project folder

Run:

python setup_context_menu.py


That’s it. The context menu entry is now installed.

Usage

Open File Explorer

Right-click on any folder

Click Sort Files

The files inside the folder will be sorted automatically

No GUI, no extra windows, it just works.

File Categories

Files are sorted using the following rules:

EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}


Each category becomes its own folder inside the selected directory.

Files with extensions that are not listed are left untouched.

Requirements

Windows

Administrator permissions (for installation only)

Notes

Existing files are moved, not copied

Existing folders with the same name are reused

The script only affects the folder you right-clicked on

License

Free to use, modify, and improve.
If you extend it, feel free to open a pull request.