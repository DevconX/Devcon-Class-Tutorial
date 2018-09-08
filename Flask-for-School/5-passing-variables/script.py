from flask import Flask, flash, redirect, render_template, request, session, abort
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/hello/<string:name>/")
def hello(name):
    quotes = [ "Ilmu itu patut dikongsi",
               "Jangan kedekut ilmu",
               "Sentiasalah rendahkan diri",
               "Husein itu comel",
               "Anda sudah pun luar biasa!",
               "Jangan merungut, fikir positif"]
    randomNumber = random.randint(0,len(quotes)-1)
    quote = quotes[randomNumber]
    # or, return render_template('header.html',**locals()) passing all local variables in this script
    return render_template('header.html',name=name,quote=quote)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
