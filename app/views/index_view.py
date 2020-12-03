from flask import Blueprint, render_template

bp = Blueprint('index_route', __name__)


@bp.route('/')
def index():
    data = {
        "resultado": 1 + 3,
        "nome": "João Cardoso"
    }

    return render_template('index.html', **data)
