
from flask import request, jsonify, render_template, redirect,url_for
from app import app, get_db_connection

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField,SelectField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired()])
    senha = PasswordField('Senha:', validators=[DataRequired()])    
    remember = BooleanField('Manter logado:')
    #protocol = SelectField(choices=[('usu', 'Usuario'), ('for', 'Fornecerdor'), ('cli', 'Cliente')])
    recaptcha = RecaptchaField()
    #resp_cap = StringField('resp_cap',validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()    
    if form.validate_on_submit():
        #captcha_response = request.form['g-recaptcha-response']
        
        print(f'email::  {form.email.data}')
        print(f'senha::  {form.senha.data}')
        print(f'remember::  {form.remember.data}')
        #print(f'recaptcha::  {form.recaptcha}')
        #print(f'resp_cap::  {captcha_response}')
        #return redirect(url_for(f'/{user.data}'))
    return render_template('/html/index.html',form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()    
    if form.validate_on_submit():
        #captcha_response = request.form['g-recaptcha-response']
        
        print(f'email::  {form.email.data}')
        print(f'senha::  {form.senha.data}')
        print(f'remember::  {form.remember.data}')
        #print(f'recaptcha::  {form.recaptcha}')
        #print(f'resp_cap::  {captcha_response}')
        #return redirect(url_for(f'/{user.data}'))
    return render_template('/html/login.html',form=form)