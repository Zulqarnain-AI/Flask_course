from flask import Flask

app=Flask(__name__)

@app.route('/')
def Home():
    return 'hello world'

@app.route('/about')
def about():
    return 'this is about page'



if(__name__ == '__main__'):
    app.run(debug=True)