from flask import Blueprint, render_template, request
from .utils import *
from .__init__ import send_email

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

    if request.method == "POST":
        contact_form = {}
        try:
            if request.form["name"] == "" or request.form["email"] == "" or request.form["message"] == "":
                return render_template("home/contact.html", mc=mc, error=True)
            contact_form["name"] = request.form["name"]
            contact_form["email"] = request.form["email"].replace(" ", "").lower()
            contact_form["message"] = request.form["message"]
            send_email(contact_form)
        except:
            return render_template("home/contact.html", mc=mc, error=True)
        return render_template("home/contact.html", mc=mc, success=True)

    return render_template("home/contact.html", mc=mc)

@bp.route("/theming-kit")
def theming_kit():
    return render_template("theming_kit.html")