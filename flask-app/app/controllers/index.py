
from flask import request, jsonify, render_template, redirect
from app import app, get_db_connection

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SelectField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    nome = StringField('Usuario', validators=[DataRequired()],id='iptnome')
    senha = PasswordField('Senha', validators=[DataRequired()],id='iptnome')
    protocol = SelectField(choices=[('usu', 'Usuario'), ('for', 'Fornecerdor'), ('cli', 'Cliente')])
    remember = BooleanField('Remember')


@app.route('/<user>', methods=['GET', 'POST'])
@app.route('/', defaults={'user':None}, methods=['GET', 'POST'])
def index(user):
    form = MyForm()
    if form.validate_on_submit():
        user = form.nome
        #return redirect(f'/{form.name}')
    return render_template('/html/index.html', user=user,form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('/html/login.html')