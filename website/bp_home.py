from flask import (
    Blueprint, render_template
)
from .utils import *

bp = Blueprint("bp_home", __name__)

@bp.route("/")
def index():
    mc = set_menu("home")
    return render_template("home/index.html", mc=mc)

@bp.route("/portfolio")
def portfolio():
    mc = set_menu("portfolio")
    return render_template("home/portfolio.html", mc=mc)

@bp.route("/contact")
def contact():
    mc = set_menu("contact")
    return render_template("home/contact.html", mc=mc)