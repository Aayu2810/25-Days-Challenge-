from tkinter import filedialog, Tk
from collections import Counter
import os
from dataclasses import dataclass


# 1. Create a model for the data
@dataclass
class Stats:
    folder: str
    num_files: int
    total_size_mb: float
    most_common_types: list[tuple[str, int]]


# 2. Create a function that analyses the folder
def analyse_folder() -> Stats | None:
    # Hide main tkinter window
    root: Tk = Tk()
    root.withdraw()
    folder_path: str = filedialog.askdirectory(title='Select folder to analyze')

    # If the user doesn't select a folder
    if not folder_path:
        print('No folder selected.')
        return None

    # The stats we care about
    file_count: int = 0
    total_size: int = 0
    extension_counter: Counter[str] = Counter()

    # Walk through all directories and subdirectories
    for current_dir, subdirs, filenames in os.walk(folder_path):
        for filename in filenames:
            file_count += 1

            # Get full path to the file
            full_path: str = os.path.join(current_dir, filename)

            try:
                # Get file size in bytes
                file_size: int = os.path.getsize(full_path)
                total_size += file_size
            except OSError:
                # Skip files that can't be accessed (permissions, etc.)
                continue

            # Get file extension (everything after the last dot)
            name, extension = os.path.splitext(filename)
            if extension:  # Only count files with extensions
                extension_counter[
                    extension.lower()
                ] += 1  # Increase the count for that extension

    # Convert bytes to megabytes
    total_size_mb: float = round(total_size / (1024 * 1024), 2)
    most_common_extensions: list[tuple[str, int]] = extension_counter.most_common(5)

    return Stats(
        folder=os.path.abspath(folder_path),
        num_files=file_count,
        total_size_mb=total_size_mb,
        most_common_types=most_common_extensions,
    )


def main() -> None:
    stats: Stats | None = analyse_folder()

    if stats:
        print(f'Folder: {stats.folder}')
        print(f'Number of files: {stats.num_files}')
        print(f'Total size (MB): {stats.total_size_mb}')
        print('Most common file types:')
        for ext, count in stats.most_common_types:
            print(f'  {ext}: {count} files')


if __name__ == '__main__':
    main()

# Homework:
# 1. The "analyse_folder()" is huge! Try splitting this function into smaller functions
# to everything far more re-usable.
