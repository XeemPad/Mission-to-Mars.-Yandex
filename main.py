from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import os
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


class RegisterForm(FlaskForm):
    astronaut_id = StringField('Login / email', validators=[DataRequired()])
    astronaut_password = PasswordField('Password', validators=[DataRequired()])
    commit_password = PasswordField('Repeat Password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit_btn = SubmitField('Submit')


@app.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pass  # Страницы редиректа пока нет
    return render_template('register.html', title='Регистрация', base_css_directory=
                           url_for('static', filename='css/style.css'), form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
