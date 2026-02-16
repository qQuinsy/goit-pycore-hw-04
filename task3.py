import sys
from pathlib import Path
from colorama import init, Fore


init(autoreset=True)


def print_directory(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + item.name)
            print_directory(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + item.name)


def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії.")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + "Шлях не існує.")
        sys.exit(1)

    if not path.is_dir():
        print(Fore.RED + "Це не директорія.")
        sys.exit(1)

    print(Fore.BLUE + path.name)
    print_directory(path)


if __name__ == "__main__":
    main()
