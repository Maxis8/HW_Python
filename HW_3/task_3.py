# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import re
txt = 'Первое государство русского народа Киевская Русь просуществовала около 300 лет. \
Это была федерация княжеств, которой управлял совместно род Рюриковичей. Развитие феодальных отношений и усиление \
самостоятельности отдельных городов привело к политическому дроблению Киевской Руси. В конце тридцатых годов XIII в.\
на Русь обрушились монголо-татары, и она почти на 250 лет попала в зависимость от Золотой Орды.\
Иго ускорило процесс дробления Руси, но вместе с тем по мере возрождения экономики и культуры превращалось в стимул \
к объединению. В силу ряда факторов на место политического лидера в начале XIV в. выдвинулась Москва, \
что объясняется ее выгодным географическим положением, и дальновидной политикой ее князей.'
words = txt.split()


def get_clean_word(word: str) -> str:
    word = word.lower()
    word = re.sub('[^a-zа-яё0-9]', '', word, flags=re.IGNORECASE)
    word = word.strip('-')
    return word


all_list = [get_clean_word(word) for word in words]


def words_counter(text: str) -> list[str]:
    count_words = {}
    LIMIT = 10
    sorted_dictionary = {}
    lst_words = all_list
    for word in lst_words:
        counter = lst_words.count(word)
        count_words[word] = counter
    sorted_values = sorted(count_words.values())[::-1]
    for i in sorted_values:
        for k in count_words.keys():
            if count_words[k] == i:
                sorted_dictionary[k] = count_words[k]
    return list(sorted_dictionary.items())[0: LIMIT]


print(words_counter(txt))

