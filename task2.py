def get_cats_info(path):
    """
    Зчитує файл з інформацією про котів та повертає список.

    """

    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue  # пропускаємо порожні рядки

                try:
                    cat_id, name, age = line.split(",")

                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }

                    cats.append(cat_info)

                except ValueError:
                    print(f"Неправильний формат рядка: {line}")
                    continue

        return cats

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)