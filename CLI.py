def parse_input(user_input):
    # Розбиваємо введений рядок на команду та аргументи
    cmd, *args = user_input.split()
    # Видаляємо зайві пробіли та переводимо команду в нижній регістр
    cmd = cmd.strip().lower()
    # Повертаємо команду та аргументи
    return cmd, args

def add_contact(args, contacts):
    # Розпаковуємо аргументи в ім'я та номер телефону
    if len(args) != 2:
        return "Invalid command. Usage: add [username] [phone]"
    name, phone = args
    # Додаємо контакт у словник
    contacts[name] = phone
    # Повертаємо повідомлення про успішне додавання контакту
    return "Contact added."

def change_contact(args, contacts):
    # Розпаковуємо аргументи в ім'я та новий номер телефону
    if len(args) != 2:
        return "Invalid command. Usage: change [username] [new_phone]"
    name, new_phone = args
    # Перевіряємо, чи існує контакт з таким ім'ям
    if name in contacts:
        # Оновлюємо номер телефону
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    # Перевіряємо, чи введено ім'я
    if len(args) != 1:
        return "Invalid command. Usage: phone [username]"
    name = args[0]
    # Перевіряємо, чи існує контакт з таким ім'ям
    if name in contacts:
        # Повертаємо номер телефону
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    # Перевіряємо, чи є контакти у словнику
    if not contacts:
        return "No contacts found."
    # Виводимо всі контакти з номерами телефонів
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    # Створюємо порожній словник для зберігання контактів
    contacts = {}
    print("Welcome to the assistant bot!")
    
    # Основний цикл програми, який буде працювати до введення команди "close" або "exit"
    while True:
        # Отримуємо введення користувача
        user_input = input("Enter a command: ")
        # Розбираємо введення на команду та аргументи
        command, args = parse_input(user_input)

        # Виконуємо відповідні дії залежно від команди
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "welcome":
            print("Welcome to the assistant bot!")
        else:
            print("Invalid command.")

# Перевіряємо, чи цей файл запущено як основний
if __name__ == "__main__":
    main()
