def get_cats_info(path): # Створюємо функцію get_cats_info(path)
    cats = [] # Створюємо порожній список для зберігання інформації про котів
    try:
        with open(path, 'r', encoding='utf-8') as file: # Відкриваємо файл для читання з кодуванням utf-8
            for line in file: # Проходимо по кожному рядку у файлі
                line = line.strip() # Видаляємо зайві пробіли і символи переносу рядка
                cat_id, cat_name, cat_age = line.split(',') # Розділяємо рядок на частини по комах
                cat_info = {"id": cat_id, "name": cat_name, "age":cat_age}  # Створюємо словник з інформацією про кожного кота
                cats.append(cat_info)  # Додаємо словник до списку
    except Exception as e: # Перевіряємо на помилки
        print(f"Помилка зчитування файлу: {e}") # Виводимо повідомлення про помилку
    return cats # Повертаємо інформацію про котів

# Приклад використання функції
cats_info = get_cats_info(r"C:\Users\golos\OneDrive\Рабочий стол\Projects\First_repo\goit-pycore-hw-04\Інформація_про_котів.txt")
print(cats_info)              
            
            
        
    