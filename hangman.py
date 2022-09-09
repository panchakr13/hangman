import random


def get_word(list1):
    return random.choice(list1).upper()


def display_hangman(tries, difficult):
    stages = ['''Осталось 0 попыток, Вы проиграли!
                    ________
                    |      |
                    |     \\o/
                    |      |
                    |     / \\
                    |
                    -''',
              '''Осталась 1 попытка:
              ________
              |      |
              |     \\o/
              |      |
              |     / 
              |
              -''',
              '''Осталось 2 попытки:
              ________
              |      |
              |     \\o/
              |      |
              |
              |
              -''',
              '''Осталось 3 попытки:
              ________
              |      |
              |     \\o
              |      |
              |
              |
              -''',
              '''Осталось 4 попытки:
              ________
              |      |
              |      o
              |      |
              |
              |
              -''',
              '''Осталось 5 попыток:
              ________
              |      |
              |      o
              |      
              |
              |
              -''',
              '''Осталось 6 попыток:
              ________
              |      |
              |
              |
              |
              |
              -''']

    stages_long = ['''Осталось 0 попыток, Вы проиграли!
                    ________
                    |      |
                    |     \\o/
                    |      |
                    |    _/ \\_
                    |
                    -''',
                   '''Осталась 1 попытка:
                   ________
                   |      |
                   |     \\o/
                   |      |
                   |    _/ \\
                   |
                   -''',
                   '''Осталось 2 попытки:
                   ________
                   |      |
                   |     \\o/
                   |      |
                   |     / \\
                   |
                   -''',
                   '''Осталось 3 попытки:
                   ________
                   |      |
                   |     \\o/
                   |      |
                   |     / 
                   |
                   -''',
                   '''Осталось 4 попытки:
                   ________
                   |      |
                   |     \\o/
                   |      |
                   |
                   |
                   -''',
                   '''Осталось 5 попыток:
                   ________
                   |      |
                   |     \\o
                   |      |
                   |
                   |
                   -''',
                   '''Осталось 6 попыток:
                   ________
                   |      |
                   |      o
                   |      |
                   |
                   |
                   -''',
                   '''Осталось 7 попыток:
                   ________
                   |      |
                   |      o
                   |      
                   |
                   |
                   -''',
                   '''Осталось 8 попыток:
                   ________
                   |      |
                   |
                   |
                   |
                   |
                   -''']

    stages_very_long = ['''Осталось 0 попыток, Вы проиграли!
                    ________
                    |      |
                    |     \\o/
                    |      |
                    |    _/ \\_
                    |
                    -''',
                        '''Осталась 1 попытка:
                        ________
                        |      |
                        |     \\o/
                        |      |
                        |    _/ \\
                        |
                        -''',
                        '''Осталось 2 попытки:
                        ________
                        |      |
                        |     \\o/
                        |      |
                        |     / \\
                        |
                        -''',
                        '''Осталось 3 попытки:
                        ________
                        |      |
                        |     \\o/
                        |      |
                        |     / 
                        |
                        -''',
                        '''Осталось 4 попытки:
                        ________
                        |      |
                        |     \\o/
                        |      |
                        |
                        |
                        -''',
                        '''Осталось 5 попыток:
                        ________
                        |      |
                        |     \\o
                        |      |
                        |
                        |
                        -''',
                        '''Осталось 6 попыток:
                        ________
                        |      |
                        |      o
                        |      |
                        |
                        |
                        -''',
                        '''Осталось 7 попыток:
                        ________
                        |      |
                        |      o
                        |      
                        |
                        |
                        -''',
                        '''Осталось 8 попыток:
                        ________
                        |      |
                        |
                        |
                        |
                        |
                        -''',
                        '''Осталось 9 попыток:
                        ________
                        |      
                        |
                        |
                        |
                        |
                        -''',
                        '''Осталось 10 попыток:

                        |      
                        |
                        |
                        |
                        |
                        -''',
                        '''Осталось 11 попыток:''']
    if difficult == 3:
        return stages[tries]
    elif difficult == 2:
        return stages_long[tries]
    else:
        return stages_very_long[tries]


def play(word, vrnt, lett):
    print('Давайте играть в угадайку слов!')
    if vrnt == '3':
        trs = 6
    elif vrnt == '2':
        trs = 8
    else:
        trs = 11
    print(display_hangman(trs, vrnt))
    history = []
    if lett == '1':
        word_completion = word[0] + '_' * (len(word) - 2) + word[-1]
    else:
        word_completion = '_' * len(word)
    print(f'Загаданное слово содержит {len(word)} букв:', word_completion)
    while trs > 0:
        while True:
            vvod = input('Введите букву или слово целиком: \n>>> ').upper()
            if vvod in history:
                print('Вы уже вводили это, будьте внимательнее.\n>>>')
            elif (len(vvod) == 1 or len(vvod) == len(word)) \
                    and (vvod in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                         or vvod in word):
                history.append(vvod)
                break
            else:
                print('Ввод некорректен, попробуйте еще раз.\n>>>')
        if len(vvod) == 1 and vvod in word:
            word_completion_n = ''
            for ind, val in enumerate(word):
                if val == vvod:
                    word_completion_n += vvod
                else:
                    word_completion_n += word_completion[ind]
            word_completion = word_completion_n
            print('Есть такая буква в этом слове!')
            print(display_hangman(trs, vrnt))
            print(f'Загаданное слово содержит {len(word)} букв:',
                  word_completion)
            if '_' not in word_completion:
                print('Поздравляем, вы угадали слово!')
                break
        elif len(vvod) == 1 and vvod not in word:
            trs -= 1
            print('Нет такой буквы в этом слове!')
            print(display_hangman(trs, vrnt))
            print(f'Загаданное слово содержит {len(word)} букв:',
                  word_completion)
        elif len(vvod) == len(word) and vvod != word:
            trs -= 1
            print('Вы не угадали слово!')
            print(display_hangman(trs, vrnt))
            print(f'Загаданное слово содержит {len(word)} букв:',
                  word_completion)
        else:
            print('Поздравляем, вы угадали слово! Вы победили')
            break
    if trs == 0:
        print(display_hangman(trs, vrnt))
        print('Загаданное слово:', word)


animals = ['бегемот', 'черепаха', 'выхухоль', 'крокодил', 'муравьед',
           'пантера', 'соболь', 'горностай', 'тюлень', 'дельфин', 'корова',
           'лошадь', 'барсук', 'леопард', 'ягуар', 'носорог', 'сурикат',
           'дикобраз', 'лисица', 'ондатра', 'росомаха', 'медведь', 'кролик',
           'бурундук', 'обезьяна', 'антилопа', 'собака', 'кенгуру', 'утконос']

birds = ['пингвин', 'страус', 'попугай', 'тетерев', 'глухарь', 'рябчик',
         'ворона', 'ястреб', 'синица', 'воробей', 'голубь', 'курица', 'сорока',
         'журавль', 'лебедь', 'зяблик', 'соловей', 'иволга', 'жаворонок',
         'скворец', 'кукушка', 'ласточка', 'колибри', 'трясогузка', 'пеликан',
         'куропатка', 'перепел', 'коршун', 'снегирь', 'фламинго']

cities = ['Киев', 'Харьков', 'Одесса', 'Днепр', 'Донецк', 'Запорожье', 'Львов',
          'Кривой Рог', 'Севастополь', 'Николаев', 'Мариуполь', 'Луганск',
          'Винница', 'Макеевка', 'Симферополь', 'Херсон', 'Чернигов',
          'Полтава', 'Хмельницкий', 'Черкассы', 'Черновцы', 'Житомир', 'Сумы',
          'Ровно', 'Ивано-Франковск', 'Тернополь', 'Кропивницкий', 'Луцк',
          'Ужгород', 'Кременчуг']
while True:
    variant = input('''Выберите сложность игры:
1 - Легкая (11 попыток)
2 - Средняя (8 попыток)
3 - Сложная (6 попыток)
>>> ''')
    if variant == '1' or variant == '2' or variant == '3':
        break
    else:
        print('Вы ошиблись при вводе, попробуйте еще раз.')

while True:
    letters = input('''Хотите открыть первую и последнюю буквы?
1 - Да, откройте.
2 - Нет, не нужно.
>>> ''')
    if letters == '1' or letters == '2':
        break
    else:
        print('Вы ошиблись при вводе, попробуйте еще раз.')

while True:
    category = input('''Хотите узнать, из какой категории выбранное слово?
1 - Да, покажите подсказку.
2 - Нет, не нужно.
>>> ''')
    if category == '1' or category == '2':
        break
    else:
        print('Вы ошиблись при вводе, попробуйте еще раз.')
if category == '1':
    words_list = random.choice([animals, birds, cities])
    if words_list == animals:
        print('Выбранное слово из категории "Звери".')
    elif words_list == birds:
        print('Выбранное слово из категории "Птицы".')
    else:
        print('Выбранное слово из категории "Города Украины".')
else:
    words_list = animals + birds + cities


play(get_word(words_list), variant, letters)
