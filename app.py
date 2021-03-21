"""Adopt a pet application."""

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap

from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "flyersareawesome"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

bootstrap = Bootstrap(app)
toolbar = DebugToolbarExtension(app)


@app.route("/")
def show_pets():
    """List all pets on home page."""

    pets = Pet.query.all()
    return render_template("index.html", pets=pets)
