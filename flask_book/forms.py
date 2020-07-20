from flask import Flask, request, render_template, redirect, url_for, session, flash

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'this is secret key'


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form1 = NameForm()
    if session.get('name'):
        print(session['name'])
    else:
        print('nothing')
    if request.method == 'POST':
        if form1.validate_on_submit():
            name = form1.name.data
            if name != session.get('name'):
                flash(f'You changed your name from {session["name"]} to {name}')
            
            # print(dir(form1))
            # print(dir(form1.name))
            print(form1.name.data)
            session['name'] = form1.name.data
            # form1.name.data = ''
            return redirect(url_for('index'))
    return render_template('forms.html', form=form1)

