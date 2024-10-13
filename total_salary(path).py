def total_salary(path):  
    try:
        with open(path, 'r', encoding='utf-8') as file:  
            salaries = []  
            for line in file:  
                name, salary = line.strip().split(',')
                salaries.append(int(salary))  
            total = sum(salaries)  
            average = total / len(salaries)  
            return total, average  
    except FileNotFoundError:  
        print(f"Файл {path} не знайдений.")  
    except Exception as e:  
        print(f"Сталася помилка: {e}")

# Приклад використання функції:
total, average = total_salary("C:/Users/golos/OneDrive/Рабочий стол/Projects/First_repo/Місячні_заробітні_плати_розробників.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
