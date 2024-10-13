def total_salary(path):  # Cкладаємо функцію яка аналізує файл
    try:
        with open(path, 'r', encoding='utf-8') as file:  # Використовуємо менеджер контексту with для читання файлів
            salaries = []  
            for line in file:  
                name, salary = line.strip().split(',') # Для розділення даних у кожному рядку застосуємо метод split                salaries.append(int(salary))  #
            total = sum(salaries)  # Обраховуємо загальну суму заробітної плати
            average = total / len(salaries)  # Обраховуємо середню зарплату
            return total, average  # Повертаємо значення total та average
    except FileNotFoundError:  # Опрацьовуємо похибку у випадку не знайдення файлу
        print(f"Файл {path} не знайдений.")  
    except Exception as e:  
        print(f"Сталася помилка: {e}")  # # Опрацьовуємо інші похибки

# Приклад використання функції:
total, average = total_salary("C:/Users/golos/OneDrive/Рабочий стол/Projects/First_repo/Місячні_заробітні_плати_розробників.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
