from flask import Flask, render_template,url_for
from employee import employeedata
app=Flask(__name__)


@app.route('/')
@app.route('/home')
def Home():
    return render_template('home.html',title='home.html',page='this is the home page')

@app.route('/about')
def about():
    return render_template('about.html',title='about',page='this is the about page')

@app.route('/evaluation/<int:num>')
def evaluate(num):
    return render_template("evaluate.html",title='evaluation',page='this is the evaluation page',number=num)



@app.route('/employee')
def employee():
    return render_template('employee.html',title='employee data',page='this is to show emp data',emp=employeedata)

if(__name__=='__main__'):
    app.run(debug=True)