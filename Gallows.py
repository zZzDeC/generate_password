import random

word_list = ["PYTHON", "JAVA", "PROGRAMMING", "DEVELOPER", "HANGMAN", "CODING"]

def get_word():
    return random.choice(word_list)

# функция получения текущего состояния
def display_hangman(tries):
    stages = [
        # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        guess = input('Введите букву или слово: ').upper()

        if guess.isalpha():
            if guess in guessed_letters or guess in guessed_words:
                print('Вы уже называли эту букву или слово. Попробуйте еще раз.')
            elif len(guess) == 1:
                guessed_letters.append(guess)
                if guess in word:
                    print('Отлично! Вы угадали букву.')
                    for i in range(len(word)):
                        if word[i] == guess:
                            word_completion = word_completion[:i] + guess + word_completion[i + 1:]
                else:
                    print('Буквы нет в слове.')
                    tries -= 1
            elif len(guess) == len(word) and guess.isalpha():
                guessed_words.append(guess)
                if guess == word:
                    guessed = True
                else:
                    print('Неверное слово. Попробуйте еще раз.')
                    tries -= 1
            else:
                print('Некорректный ввод. Попробуйте еще раз.')
        else:
            print('Пожалуйста, введите букву или слово.')

        print(display_hangman(tries))
        print(word_completion)

        if '_' not in word_completion:
            guessed = True
            print('Поздравляем, вы угадали слово! Вы победили!')
        elif tries == 0:
            print(f'Извините, вы проиграли. Загаданное слово было: {word}')

if __name__ == "__main__":
    while True:
        word_to_guess = get_word().upper()
        play(word_to_guess)

        play_again = input('Хотите сыграть еще раз? (Да/Нет): ').lower()
        if play_again != 'да':
            break

