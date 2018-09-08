from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
    return "muka depan!"
 
@app.route("/hello")
def hello():
    return "Hello World!"
 
@app.route("/members")
def members():
    return "tahu kah anda boleh letak apa sahaja nama selepas /members/"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return name
 
if __name__ == "__main__":
    app.run()

