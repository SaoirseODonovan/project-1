from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

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

        print("Username is:", username)
        print("Selected answer 1:", quesOne)
        print("Selected answer 2:", quesTwo)
        print("Selected answer 3:", quesThree)
        print("Selected answer 4:", quesFour)
        print("Selected answer 5:", quesFive)
        print("Selected answer 6:", quesSix)

        return redirect(url_for('views.thank_you'))

    return render_template('form.html', user=current_user)

@views.route('/thank_you')
@login_required
def thank_you():
    return render_template('thank_you.html', user=current_user)

@views.route('/', methods=['GET', 'POST'])
@login_required
def welcome():
    return render_template("welcome.html", user=current_user)

