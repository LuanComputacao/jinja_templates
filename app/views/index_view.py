from flask import Blueprint, render_template

from app.services.codewars_services import get_codewars_ranking

bp = Blueprint('index_route', __name__)


@bp.route('/')
def index():
    codewars_ranking = get_codewars_ranking()

    page_title = "Hanking Codewars"

    data = {
        "codewars_ranking": codewars_ranking,
        "page_title": page_title
    }

    return render_template('index.html', **data)
