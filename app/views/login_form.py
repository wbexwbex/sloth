from flask.ext.wtf import Form
from wtforms import TextField, StringField, BooleanField, TextAreaField, SelectField, SubmitField
from wtforms.validators import Required, DataRequired, Length
from flask.ext.babel import gettext


class LoginForm(Form):
    account = StringField('account', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class UserForm(Form):
    account = StringField('account', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    group = SelectField('group', coerce=unicode, validators=[DataRequired()])
    submit = SubmitField('submit')
