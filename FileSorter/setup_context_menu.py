import os
import winreg
import sys


def add_context_menu():
    """
    Fügt 'Mit FileSorter sortieren' zum Windows-Kontextmenü hinzu.
    """
    try:
        # Pfad zum context_sort.py Skript (liegt im src Ordner)
        script_path = os.path.join(os.path.dirname(__file__), "src", "context_sort.py")
        python_path = sys.executable
        
        # Registry-Pfad für Ordner-Kontextmenü
        reg_path = r"Software\Classes\Folder\shell\FileSorter"
        
        # Öffne oder erstelle Registry-Schlüssel
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
        
       
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "Sort with FileSorter")
        command_key = winreg.CreateKey(key, "command")
        
        # Kommando mit Pfad als Argument
        command = f'"{python_path}" "{script_path}" "%1"'
        winreg.SetValueEx(command_key, "", 0, winreg.REG_SZ, command)
        
        winreg.CloseKey(command_key)
        winreg.CloseKey(key)
        
        print("✓ Kontextmenü erfolgreich integriert!")
        print("Du kannst jetzt in jedem Ordner Rechtsklick machen und")
        print("'Sort with FileSorter' auswählen.")

    except Exception as e:
        print(f"✗ Fehler beim Registrieren: {e}")
        print("Starte dieses Skript als Administrator!")
        sys.exit(1)


def remove_context_menu():
    """
    Entfernt 'Mit FileSorter sortieren' aus dem Windows-Kontextmenü.
    """
    try:
        reg_path = r"Software\Classes\Folder\shell\FileSorter"
        
        # Lösche den Registry-Schlüssel
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, reg_path + r"\command")
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, reg_path)
        
        print("✓ Kontextmenü erfolgreich entfernt!")
        
    except Exception as e:
        print(f"✗ Fehler beim Entfernen: {e}")


if __name__ == "__main__":
    print("=" * 50)
    print("FileSorter - Kontextmenü Installation")
    print("=" * 50)
    print()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--remove":
        remove_context_menu()
    else:
        add_context_menu()
    
    print()
    input("Drücke Enter zum Beenden...")
