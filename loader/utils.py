import json
from main.utils import reading_posts
from config import POST_PATH, UPLOAD_FOLDER
import exceptions


def save_file(picture):
    f"""
    Сохраняет картинку поста в {UPLOAD_FOLDER}
    :param picture: Загруженная картинка
    :return: Путь к картинке
    """
    allowed_type = ["png", "gif", "webp", "jpeg", "jpg"]
    filename = picture.filename
    picture_type = filename.split(".")[-1]
    if picture_type not in allowed_type:
        raise exceptions.WrongImgType(f"Неверный формат файла, допустимы только: {', '.join(allowed_type)}")
    path = f"{UPLOAD_FOLDER}/{filename}"
    picture.save(path)

    return path


def save_post(post):
    f"""
    Сохраняет пост в файл {POST_PATH}
    :param post: Загруженный пост
    """
    posts_list = reading_posts(POST_PATH)
    posts_list.append(post)
    with open(POST_PATH, "w", encoding="UTF-8") as posts:
        json.dump(posts_list, posts, indent=2, ensure_ascii=False)
