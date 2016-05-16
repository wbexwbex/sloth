from flask.ext.wtf import Form
from wtforms import TextField, StringField, BooleanField, TextAreaField, SelectField, SubmitField
from wtforms.validators import Required, DataRequired, Length
from flask.ext.babel import gettext


class UserForm(Form):
    domain = SelectField('sdomain', coerce=unicode)
    server = SelectField('sserver', coerce=unicode)
    roleid = StringField('roleid')
    name = StringField('name')
    submit = SubmitField('submit')
