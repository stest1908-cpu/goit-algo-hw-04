# Завдання 3 (опційне): візуалізація структури директорії з кольоровим виводом
# Запуск: python hw03.py /шлях/до/директорії

import sys
import pathlib
from colorama import Fore, Style, init

init(autoreset=True)


def print_directory_structure(path: pathlib.Path, indent: str = "") -> None:
    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + Style.BRIGHT + f"[DIR] {item.name}")
            print_directory_structure(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + f"[FILE] {item.name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python hw03.py <шлях_до_директорії>")
        sys.exit(1)

    directory_path = pathlib.Path(sys.argv[1])

    if not directory_path.exists() or not directory_path.is_dir():
        print(Fore.RED + f"Помилка: '{directory_path}' не існує або не є директорією.")
        sys.exit(1)

    print_directory_structure(directory_path)
