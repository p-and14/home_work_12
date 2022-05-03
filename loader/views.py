from flask import Blueprint, render_template, request, send_from_directory
from loader.utils import save_file, save_post
import exceptions
import logging

loader_blueprint = Blueprint("loader_blueprint", __name__)
logging.basicConfig(filename="logger.log", level=logging.INFO)


@loader_blueprint.route("/post", methods=["GET"])
def page_post_form():
    logging.info("Открытие страницы поиска постов")
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    logging.info("Загрузка поста на сервер")
    picture = request.files.get("picture")
    content = request.form.get("content")

    if not picture or not content:
        logging.error("Ошибка загрузки, отсутсвует картинка или текст")
        return "Ошибка загрузки, отсутсвует картинка или текст"

    try:
        path = save_file(picture)
    except exceptions.WrongImgType:
        logging.error("Неверный формат изображения")
        return "Неверный формат изображения"

    post = {"pic": path, "content": content}

    try:
        save_post(post)
    except exceptions.FileUploadError:
        logging.error("Ошибка загрузки файла")
        return "Ошибка загрузки файла"

    logging.info(f"Пост {post} успешно загружен")
    return render_template("post_uploaded.html", post=post)


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
