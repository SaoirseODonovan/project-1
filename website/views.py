from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Quiz, User
from . import db

views = Blueprint('views', __name__)

@views.route('/form', methods=['GET', 'POST'])
@login_required
def form():
    if request.method == 'POST':
        username = request.form.get('username')
        quesOne = request.form.get('qusOne')
        quesTwo = request.form.get('qusTwo')
        quesThree = request.form.get('qusThree')
        quesFour = request.form.get('qusFour')
        quesFive = request.form.get('qusFive')
        quesSix = request.form.get('qusSix')

        userExists = User.query.filter_by(username=username).first()

        if userExists:
            if username == current_user.username:
                print("Username is:", username)
                print("Selected answer 1:", quesOne)
                print("Selected answer 2:", quesTwo)
                print("Selected answer 3:", quesThree)
                print("Selected answer 4:", quesFour)
                print("Selected answer 5:", quesFive)
                print("Selected answer 6:", quesSix)

                

                quiz = Quiz(username=username, qusOne=quesOne, qusTwo=quesTwo, qusThree=quesThree, qusFour=quesFour, qusFive=quesFive, qusSix=quesSix)

                db.session.add(quiz)
                db.session.commit()
                flash('Answers submitted!', category='success')

                return redirect(url_for('views.submission'))
            else:
                flash('The username provided is not yours, please try again with your username.', category='error')
        else:
            flash('That username does not exist!', category='error')

    return render_template('form.html', user=current_user)

@views.route('/submission')
@login_required
def submission():
    return render_template('submission.html', user=current_user)

@views.route('/', methods=['GET', 'POST'])
@login_required
def welcome():
    return render_template("welcome.html", user=current_user)

@views.route('/group', methods=['GET', 'POST'])
@login_required
def group():
    return render_template("group.html", user=current_user)

