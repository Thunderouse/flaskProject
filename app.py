from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kollage_secret_key'

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

@app.route('/')
@app.route('/index')
def index():  # put application's code here
    user = "20-КИС-3"
    return render_template('index.html', title="Home Page", username=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    user = '20-КИС-3'
    return f"{user} Успешная авторизация"


if __name__ == '__main__':
    app.run()
