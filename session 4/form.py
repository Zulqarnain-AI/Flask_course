from flask_wtf import FlaskForm 
from wtforms import (
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)
from wtforms.validators import (
    DataRequired,
    length,
    Email,
    Optional,
    EqualTo

)

class SignupForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(),length(4,50)]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    gender = SelectField(
        "Gender",
        choices = [("male","male"),( "femal","femal"),("other" ,"other")],
        validators=[Optional()]
    )
    dob=DateField(
        "date of birth",
        validators=[Optional()]
    )
    password=PasswordField(
        "Password",
        validators=[DataRequired(),length(5,10)]
    )
    confirm_password=PasswordField(
        "Confirm Password",
        validators=[DataRequired(),length(5,10),EqualTo("password")]
    )

    submit=SubmitField("Sign Up")



class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    password=PasswordField(
        "Password",
        validators=[DataRequired(),length(5,10)]
    )
    remember_me=BooleanField("remember Me")
    submit=SubmitField("Log in")