"""Adopt a pet application."""

from flask import Flask, render_template, redirect, flash, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap

from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "flyersareawesome"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

bootstrap = Bootstrap(app)
toolbar = DebugToolbarExtension(app)


@app.route("/")
def show_pets():
    """List all pets on home page."""

    pets = Pet.query.all()
    return render_template("index.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        # new_pet = Pet(name=form.name.data, age=form.age.data, ...)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('show_pets'))

    else:
        # re-present form for editing
        return render_template("pet_add_form.html", form=form)
