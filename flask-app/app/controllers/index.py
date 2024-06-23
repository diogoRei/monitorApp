
from flask import request, jsonify, render_template, redirect
from app import app, get_db_connection

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField,SelectField
from wtforms.validators import DataRequired
#RECAPTCHA_PUBLIC_KEY = '6LevsP8pAAAAALGrywJHNLMn8fnu99ZMNuZ9FOcC'
#RECAPTCHA_PRIVATE_KEY = '6LevsP8pAAAAAOZZfu-NOaw8dijsX0aa9xyp8iRJ'
#RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}

class MyForm(FlaskForm):
    nome = StringField('Usuario', validators=[DataRequired()],id='iptnome')
    senha = PasswordField('Senha', validators=[DataRequired()],id='iptnome')    
    remember = BooleanField('Remember')
    #protocol = SelectField(choices=[('usu', 'Usuario'), ('for', 'Fornecerdor'), ('cli', 'Cliente')])
    recaptcha = RecaptchaField()

@app.route('/<user>', methods=['GET', 'POST'])
@app.route('/', defaults={'user':None}, methods=['GET', 'POST'])
def index(user):
    form = MyForm()    
    if form.validate_on_submit():
        user = form.nome
        #print(f'nome::  {user.data}')
        #return redirect(f'/{user.data}')
    return render_template('/html/index.html', user=user,form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('/html/login.html')