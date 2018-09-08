from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Flask App!"
 
@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('header.html',name=name)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
