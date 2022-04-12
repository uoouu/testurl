import time
from flask import Flask,redirect


app = Flask(__name__)

@app.route('/')
def red():
    return(redirect('/get-time'))


@app.route("/get-time", methods=['GET'])

def tt():
    timeo = '4:09'
    timenh = time.strftime('%I')
    timenh = int(timenh)+3
    timenm = time.strftime('%M')
    ttt = f'{timenh}:{timenm}'
    return('Bot start at '+timeo+'<br/><br/>'+'time now is '+ttt)

if __name__ == '__main__':
	app.run()
