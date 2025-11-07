from flask import Flask, redirect, url_for #type:ignore


app=Flask(__name__)
@app.route('/')
def Home():
    return "<h1>this is the home function</h1>"


@app.route('/failed/<int:marks>')
def failed(marks):
    return f"<h1>you are failed whith {marks}, sorry...</h1>"

@app.route('/passed/<int:marks>')
def passed(marks):
    return f"<h1>you are passed whith {marks}, congratulations...</h1>"

@app.route('/result/<int:num>')
def Result(num):
    if(num<50):
        return redirect(url_for('failed',marks=num))

    else:
       return  redirect(url_for('passed',marks=num))




if(__name__=='__main__'):
    app.run(debug=True)