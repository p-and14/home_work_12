from flask import Blueprint, render_template, request
from main.utils import search_posts, reading_posts
import logging
from config import POST_PATH

main_blueprint = Blueprint('main_blueprint', __name__)
logging.basicConfig(filename="logger.log", level=logging.INFO)


@main_blueprint.route("/")
def main_page():
    logging.info("Открытие главной страницы")
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    logging.info("Открытие страницы поиска")
    s = request.args.get("s", "")
    try:
        posts_list = reading_posts(POST_PATH)
        new_posts_list = search_posts(s, posts_list)
    except FileNotFoundError:
        logging.error(f"Файл {POST_PATH} отсутсвует или не хочет превращаться в список")
        return f"Файл {POST_PATH} отсутсвует или не хочет превращаться в список"

    return render_template("search.html", s=s, posts=new_posts_list)
