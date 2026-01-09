import os
import shutil
from config import EXTENTIONS, WATCH_DIRECTORY


def get_file_category(file_extension):
    """
    Bestimmt die Kategorie einer Datei basierend auf ihrer Erweiterung.
    
    Args:
        file_extension (str): Die Dateiendung (z.B. '.jpg')
    
    Returns:
        str: Die Kategorie oder 'Others' wenn nicht gefunden
    """
    file_extension = file_extension.lower()
    
    for category, extensions in EXTENTIONS.items():
        if file_extension in extensions:
            return category
    
    return "Others"


def sort_files(source_directory):
    """
    Sortiert Dateien in einem Verzeichnis in Unterordner nach Dateityp.
    
    Args:
        source_directory (str): Der Pfad zum Verzeichnis mit den zu sortierenden Dateien
    """
    if not os.path.exists(source_directory):
        print(f"Fehler: Verzeichnis '{source_directory}' existiert nicht.")
        return
    
    if not os.path.isdir(source_directory):
        print(f"Fehler: '{source_directory}' ist kein Verzeichnis.")
        return
    
    files_found = False
    categories_created = set()
    
    # Iteriere durch alle Dateien im Verzeichnis
    try:
        for filename in os.listdir(source_directory):
            file_path = os.path.join(source_directory, filename)
            
            # Überspringe Verzeichnisse
            if os.path.isdir(file_path):
                continue
            
            files_found = True
            
            # Bestimme die Kategorie der Datei
            file_extension = os.path.splitext(filename)[1]
            
            # Ignoriere versteckte oder Systemdateien
            if not file_extension:
                print(f"Überspringe Datei ohne Extension: {filename}")
                continue
            
            category = get_file_category(file_extension)
            print(f"Datei: {filename} -> Kategorie: {category} (Extension: {file_extension})")
            
            # Erstelle das Zielverzeichnis falls es nicht existiert
            target_directory = os.path.join(source_directory, category)
            
            if not os.path.exists(target_directory):
                try:
                    os.makedirs(target_directory, exist_ok=True)
                    categories_created.add(category)
                    print(f"  ✓ Ordner erstellt: {category}/")
                except Exception as e:
                    print(f"  ✗ Fehler beim Erstellen von {category}/: {e}")
                    continue
            
            # Verschiebe die Datei
            target_path = os.path.join(target_directory, filename)
            
            try:
                shutil.move(file_path, target_path)
                print(f"  ✓ Datei verschoben: {filename}")
            except Exception as e:
                print(f"  ✗ Fehler beim Verschieben von {filename}: {e}")
    
    except Exception as e:
        print(f"Fehler beim Lesen des Verzeichnisses: {e}")
    
    if not files_found:
        print("Keine Dateien zum Sortieren gefunden.")
    else:
        print(f"Sortierung abgeschlossen. {len(categories_created)} Ordner erstellt.")


def sort_watch_directory():
    """
    Sortiert die Dateien im WATCH_DIRECTORY.
    """
    print(f"Starte Sortierung des Verzeichnisses: {WATCH_DIRECTORY}")
    sort_files(WATCH_DIRECTORY)
    print("Sortierung abgeschlossen!")


if __name__ == "__main__":
    sort_watch_directory()
