import sys  # Імпортуємо модуль sys для роботи з аргументами командного рядка
import os  # Імпортуємо модуль os для роботи з операційною системою
from pathlib import Path  # Імпортуємо Path з модуля pathlib для роботи з шляхами
from colorama import init, Fore, Style  # Імпортуємо необхідні функції та класи з модуля colorama

# Ініціалізація colorama
init(autoreset=True)  # Ініціалізуємо colorama для автоматичного скидання кольорів після кожного виводу

def print_directory_structure(path, indent=""):  # Визначаємо функцію для виводу структури директорії
    try:
        for item in sorted(path.iterdir()):  # Ітеруємося по всіх елементах у директорії, сортуємо їх
            if item.is_dir():  # Якщо елемент є директорією
                print(f"{indent}{Fore.BLUE}{item.name}/")  # Виводимо ім'я директорії синім кольором
                print_directory_structure(item, indent + "    ")  # Рекурсивно викликаємо функцію для піддиректорії
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")  # Виводимо ім'я файлу зеленим кольором
    except PermissionError:
        print(f"{indent}{Fore.RED}Permission denied: {item}")  # Виводимо повідомлення про відмову в доступі червоним кольором

def main():  # Основна функція
    if len(sys.argv) != 2:  # Перевіряємо, чи передано рівно один аргумент командного рядка
        print("Usage: python hw03.py <directory_path>")  # Виводимо повідомлення про правильне використання скрипта
        sys.exit(1)  # Завершуємо виконання скрипта з кодом 1 (помилка)

    directory_path = Path(sys.argv[1])  # Отримуємо шлях до директорії з аргументу командного рядка
    if not directory_path.exists() or not directory_path.is_dir():  # Перевіряємо, чи існує шлях і чи є він директорією
        print(f"{Fore.RED}Error: The path '{directory_path}' does not exist or is not a directory.")  # Виводимо повідомлення про помилку
        sys.exit(1)  # Завершуємо виконання скрипта з кодом 1 (помилка)

    print_directory_structure(directory_path)  # Викликаємо функцію для виводу структури директорії

if __name__ == "__main__":  # Перевіряємо, чи запущено скрипт напряму
    main()  # Викликаємо основну функцію
