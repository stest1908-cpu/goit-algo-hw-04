# Завдання 1: total_salary(path)
# Функція приймає шлях до текстового файлу із зарплатами розробників
# (кожен рядок: "Ім'я,зарплата") і повертає кортеж (загальна_сума, середня_сума).

def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, salary = line.split(",")
                    total += float(salary)
                    count += 1
                except ValueError:
                    print(f"Пропущено некоректний рядок: '{line}'")
            average = 0
            if count > 0:
                average = total / count 
        return total, average
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return 0, 0


if __name__ == "__main__":
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
