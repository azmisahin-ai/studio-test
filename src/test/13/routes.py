from flask import Blueprint, render_template

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/")
def index():
    return render_template("index.html")

@routes_bp.route("/about")
def about():
    return render_template("about.html")

@routes_bp.route("/contact")
def contact():
    return render_template("contact.html")