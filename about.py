from flask import Flask, url_for, redirect, render_template, request, Blueprint

about = Blueprint("about", __name__, static_folder="static", template_folder="templates")

@about.route("/")
def intro():
    return render_template("aboutme.html")