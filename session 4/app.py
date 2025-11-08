
from flask import Flask,render_template,redirect,url_for,flash
from form import SignupForm,LoginForm

app=Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = 'THIS_IS_A_KEY'
@app.route('/')
def home():
    return render_template('home.html', title='Home')


@app.route('/signup',methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"dear, {form.username.data}! your account is created successfully")
        return redirect(url_for('home'))
    return render_template('signup.html', title='signup',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"dear, your are loged in successfully")
        return redirect(url_for('home'))

    return render_template('login.html', title='login',form=form)

if(__name__=='__main__'):
    app.run(debug=True)