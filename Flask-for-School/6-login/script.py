from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('beautiful-login.html')
    else:
        return "Boss sudah login!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Password salah!')
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12) #to make sure the session is belong to you only
    app.run(debug=True,host='0.0.0.0', port=81)
