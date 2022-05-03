import json
import exceptions
import logging


def reading_posts(path):
    """
    Загружает файл с постами
    :param path: Путь к файлу
    :return: Список постов
    """
    with open(path, "r", encoding="UTF-8") as posts:
        posts_list = json.load(posts)

    return posts_list


def search_posts(s, posts_list):
    """
    Поиск постов по вхождению слова
    :param posts_list: Список всех постов
    :param s: Слово для поиска
    :return: Список постов
    """

    result = []
    if s:
        for post in posts_list:
            if s.lower() in post["content"].lower():
                result.append(post)

    return result
