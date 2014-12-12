# coding: utf-8
from flask.ext.wtf import Form
from flask.ext.pagedown.fields import PageDownField
from wtforms import StringField, SubmitField, TextAreaField, SelectField,\
    ValidationError, BooleanField
from wtforms.validators import Required, Length, Email
from ..models import Role, User


class EditProfileForm(Form):
    name = StringField(u'姓名', validators=[Length(1, 64)])
    location = StringField(u'地区', validators=[Length(1, 64)])
    about_me = TextAreaField(u'我的简介')
    submit = SubmitField(u'保存')


class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[
        Required(), Length(1, 64), Email()])
    username = StringField(u'用户名', validators=[Required(), Length(1, 128)])
    confirmed = BooleanField(u'激活')
    role = SelectField(u'角色', coerce=int)
    name = StringField(u'姓名', validators=[Length(0, 64)])
    location = StringField(u'地区', validators=[Length(0, 64)])
    about_me = TextAreaField(u'我的简介')
    submit = SubmitField(u'修改')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'该邮箱已被注册！')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'该用户名已经注册！')


class PostForm(Form):
    body = PageDownField(u'输入你想说的话吧', validators=[Required()])
    submit = SubmitField(u'提交')
