def caesar_cipher(text, shift, direction, language):
    result = ""
    alphabet = ""
    if language == 'русский':
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    elif language == 'английский':
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    else:
        print("Неподдерживаемый язык алфавита.")
        return None

    if direction == 'дешифрование':
        shift *= -1

    for char in text:
        if char.lower() in alphabet:
            index = (alphabet.index(char.lower()) + shift) % len(alphabet)
            if char.isupper():
                result += alphabet[index].upper()
            else:
                result += alphabet[index]
        else:
            result += char

    if direction == 'дешифрование':
        shift *= -1

    return result


def main():
    direction = input("Выберите направление (шифрование/дешифрование): ").lower()
    language = input("Выберите язык алфавита (русский/английский): ").lower()
    shift = int(input("Введите шаг сдвига (целое число): "))

    if direction not in ['шифрование', 'дешифрование'] or language not in ['русский', 'английский']:
        print("Некорректный ввод.")
        return

    text = input("Введите текст: ")

    result = caesar_cipher(text, shift, direction, language)

    if result is not None:
        print("Результат:", result)


if __name__ == "__main__":
    main()
