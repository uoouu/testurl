import flask
from flask import Flask,request,jsoify

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def index():
    if (request.method == "POST"):
        some_json = request.get_json()
        return jsoify({"you sent":some_json}),201

    else:
        return ('Welcome to Short website API.<br/><br/>Use this link For cut your url => https://meroforshorturl.pythonanywhere.com/url=YOUR URL')

if __name__ == "__main__":
    app.run()
