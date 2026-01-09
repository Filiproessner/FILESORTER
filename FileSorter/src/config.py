import os

EXTENTIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

WATCH_DIRECTORY = os.path.expanduser("~/Downloads")