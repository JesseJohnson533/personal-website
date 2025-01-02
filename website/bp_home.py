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
        response = json.loads(request.data)
        try:
            if response["name"] == "" or response["email"] == "" or response["subject"] == "" or response["message"] == "":
                return {"success": 0}, 400
            send_email(response)
        except:
            return {"success": 0}
    return render_template("home/contact.html")