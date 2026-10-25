import os
import sys
import winreg


def add_context_menu():
    """
    Fügt 'Mit FileSorter sortieren' zum Windows-Kontextmenü hinzu.
    """
    try:
        script_path = os.path.join(os.path.dirname(__file__), "src", "context_sort.py")
        python_path = sys.executable
        reg_path = r"Software\Classes\Folder\shell\FileSorter"

        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "Sort with FileSorter")
        command_key = winreg.CreateKey(key, "command")

        command = f'"{python_path}" "{script_path}" "%1"'
        winreg.SetValueEx(command_key, "", 0, winreg.REG_SZ, command)

        winreg.CloseKey(command_key)
        winreg.CloseKey(key)

    except Exception:
        sys.exit(1)


def remove_context_menu():
    """
    Entfernt 'Mit FileSorter sortieren' aus dem Windows-Kontextmenü.
    """
    try:
        reg_path = r"Software\Classes\Folder\shell\FileSorter"
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, reg_path + r"\command")
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, reg_path)

    except Exception:
        pass


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--remove":
        remove_context_menu()
    else:
        add_context_menu()
