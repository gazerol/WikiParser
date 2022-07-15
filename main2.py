import requests
from bs4 import BeautifulSoup


def add_in_dict_animals(url):
    """ Парсим ссылку и добавляем животных в словарь.
    Аргументы:
    url - ссылка по которой парсим названия животных
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.select("#mw-pages .mw-category-group ul")               # Получаем элементы названий животных.
    next_page = soup.select("#mw-pages a")[1]["href"]                       # Получаем ссылку на следущую страницу.

    for element in elements:
        for animal in element.text.split("\n"):
            if animal[0] == 'A':        # Если встречаем слово, начинающееся на латинскую "A", выходим из функции.
                return
            if animal[0] == 'H':        # На https://ru.wikipedia.org/ в русском списке названий животных под
                continue                # буквой "Д" встречается "Helobdella nununununojensis" - его мы пропускаем.

            if dict_animals.get(animal[0]) is None:       # Проверяем, есть ли список по ключу, если нет - создаём.
                dict_animals[animal[0]] = []
            dict_animals[animal[0]] += [animal]           # Добавляем название животного в список.
    add_in_dict_animals(SITE + next_page)


def output_dict(selected_dict):
    """ Вывод содержимого словаря  в формате:
    А: колличество животных
    """
    for char in ALPHABET:
        if char in selected_dict:
            print(f'{char}: {len(selected_dict[char])}')

    # for char, list_animals in sorted(dict_animals.items()):                 # Рабочий вариант, но при сортировке
    #     print(f'{char}: {len(list_animals)}')                               # выводит первую букву "Ё"


if __name__ == "__main__":
    SITE = 'https://ru.wikipedia.org/'
    ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    start_url = SITE + 'w/index.php?title=Категория%3AЖивотные_по_алфавиту&from=А'  # Cтартовая буква "А" кирилицей.
    dict_animals = {}
    add_in_dict_animals(start_url)
    output_dict(dict_animals)
