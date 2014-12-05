# coding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('你的名字是', validators=[Required()])
    submit = SubmitField('Submit')
