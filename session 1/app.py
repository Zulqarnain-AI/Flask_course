from flask import Flask

app=Flask(__name__)

@app.route('/')
def Home():
    return "<h1>this is the home page</h1>"

@app.route('/about')
def about():
    return "this is the about page ok!"

@app.route('/welcome/<name>/<int:num>')
def welcome(name,num):
    return f"<h2>Hi, {name.title()} welcome to my course.<br>Your age is {num}"

if(__name__ == '__main__'):
    app.run(debug=True)