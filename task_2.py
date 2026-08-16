# Завдання 2: get_cats_info(path)
# Функція приймає шлях до текстового файлу з інформацією про котів
# (кожен рядок: "id,ім'я,вік") і повертає список словників
# виду {"id": ..., "name": ..., "age": ...}.

def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats_info = []
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    cat_id, name, age = line.split(",")
                    cats_info.append({"id": cat_id, "name": name, "age": int(age)})
                except ValueError:
                    print(f"Пропущено некоректний рядок: '{line}'")
        return cats_info
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []
            


if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)
