import os
import shutil
from config import EXTENTIONS, WATCH_DIRECTORY


def get_file_category(file_extension):
    file_extension = file_extension.lower()

    for category, extensions in EXTENTIONS.items():
        if file_extension in extensions:
            return category

    return "Others"


def _unique_target_path(target_directory, filename):
    target_path = os.path.join(target_directory, filename)
    if not os.path.exists(target_path):
        return target_path

    stem, extension = os.path.splitext(filename)
    counter = 1
    while True:
        candidate = os.path.join(target_directory, f"{stem}_{counter}{extension}")
        if not os.path.exists(candidate):
            return candidate
        counter += 1


def sort_files(source_directory):
    files_found = False
    categories_created = set()

    try:
        for filename in os.listdir(source_directory):
            file_path = os.path.join(source_directory, filename)

            if os.path.isdir(file_path):
                continue

            file_extension = os.path.splitext(filename)[1].lower()
            if not file_extension:
                continue

            files_found = True
            category = get_file_category(file_extension)
            target_directory = os.path.join(source_directory, category)

            if not os.path.exists(target_directory):
                os.makedirs(target_directory, exist_ok=True)
                categories_created.add(category)

            target_path = _unique_target_path(target_directory, filename)
            shutil.move(file_path, target_path)

    except Exception:
        pass

    return {
        "files_found": files_found,
        "categories_created": len(categories_created),
    }


def sort_watch_directory():
    """
    Sortiert die Dateien im WATCH_DIRECTORY.
    """
    return sort_files(WATCH_DIRECTORY)


if __name__ == "__main__":
    sort_watch_directory()
