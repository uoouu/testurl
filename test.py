import time
from flask import Flask,redirect


app = Flask(__name__)

@app.route('/')
def red():
    return(redirect('/get-time'))


@app.route("/get-time", methods=['GET'])

def tt():
    timeo = '03:15'
    timen = time.strftime('%I:%M')
    return('Bot start at '+timeo+'<br/><br/>'+'time now is '+timen)

if __name__ == '__main__':
	app.run()
