import random
import string

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = '!#$%&*+-=?@^_.'


def generate_password(length, include_digits, include_uppercase, include_lowercase, include_symbols, exclude_confusing):
    chars = ""

    if include_digits:
        chars += digits
    if include_uppercase:
        chars += uppercase_letters
    if include_lowercase:
        chars += lowercase_letters
    if include_symbols:
        chars += punctuation

    if exclude_confusing:
        chars = chars.translate(str.maketrans('', '', 'il1Lo0O'))

    if not chars:
        print("Выберите хотя бы один тип символов.")
        return None

    return ''.join(random.choice(chars) for _ in range(length))


def main():
    num_passwords = int(input("Введите количество паролей для генерации: "))
    password_length = int(input("Введите длину одного пароля: "))
    include_digits = input("Включать цифры (0123456789)? (Да/Нет): ").lower() == "да"
    include_uppercase = input("Включать прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? (Да/Нет): ").lower() == "да"
    include_lowercase = input("Включать строчные буквы (abcdefghijklmnopqrstuvwxyz)? (Да/Нет): ").lower() == "да"
    include_symbols = input("Включать символы (!#$%&*+-=?@^_)? (Да/Нет): ").lower() == "да"
    exclude_confusing = input("Исключать неоднозначные символы il1Lo0O? (Да/Нет): ").lower() == "да"

    for _ in range(num_passwords):
        password = generate_password(password_length, include_digits, include_uppercase, include_lowercase,
                                     include_symbols, exclude_confusing)
        if password is not None:
            print(password)


if __name__ == "__main__":
    main()

