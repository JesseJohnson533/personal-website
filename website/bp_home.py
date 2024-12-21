from flask import Blueprint, render_template, request
from .utils import *
from .__init__ import send_email

bp = Blueprint("bp_home", __name__)

@bp.route("/")
def index():
    return render_template("home/index.html")

@bp.route("/about-me")
def about_me():
    return render_template("home/about_me.html")

@bp.route("/portfolio")
def portfolio():
    return render_template("home/portfolio.html")

@bp.route("/contact")
def contact():

    if request.method == "POST":
        contact_form = {}
        try:
            if request.form["name"] == "" or request.form["email"] == "" or request.form["message"] == "":
                return render_template("home/contact.html", error=True)
            contact_form["name"] = request.form["name"]
            contact_form["email"] = request.form["email"].replace(" ", "").lower()
            contact_form["message"] = request.form["message"]
            send_email(contact_form)
        except:
            return render_template("home/contact.html", error=True)
        return render_template("home/contact.html", success=True)

    return render_template("home/contact.html")

@bp.route("/theming-kit")
def theming_kit():
    return render_template("./theming_kit.html")