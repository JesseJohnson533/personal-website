import json
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

@bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        response = request.get_json()
        contact_form = {}
        try:
            if response.form["name"] == "" or response.form["email"] == "" or response.form["subject"] == "" or response.form["message"] == "":
                return {"success": 0}
            contact_form["name"] = request.form["name"]
            contact_form["email"] = request.form["email"].replace(" ", "").lower()
            contact_form["subject"] = request.form["subject"]
            contact_form["message"] = request.form["message"]
            send_email(contact_form)
        except:
            return {"success": 0}
        return {"success": 1}

    return render_template("home/contact.html")

@bp.route("/theming-kit")
def theming_kit():
    return render_template("./theming_kit.html")