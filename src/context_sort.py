import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from sorter import sort_files


def main():
    """
    Sortiert den übergebenen Pfad.
    Wird vom Windows-Kontextmenü aufgerufen.
    """
    if len(sys.argv) < 2:
        print("Fehler: Kein Pfad angegeben.")
        sys.exit(1)
    
    path = sys.argv[1]
    
    if not os.path.exists(path):
        print(f"Fehler: Pfad '{path}' existiert nicht.")
        sys.exit(1)
    
    print(f"Sortiere Verzeichnis: {path}")
    sort_files(path)
    print("Sortierung abgeschlossen!")
    


if __name__ == "__main__":
    main()
