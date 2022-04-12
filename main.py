from flask import Flask,redirect,request
import time,requests


timeo = '4:10'
timenh = time.strftime('%I')
timenh = int(timenh)+3
timenm = time.strftime('%M')
ttt = f'{timenh}:{timenm}'
requests.post(f"https://api.telegram.org/bot5200214331:AAGBoBxoxS9IQVO24rI0ZK-REvsd_IpnDOo/editmessagetext?chat_id=1110953194&message_id=271&text="'Bot start at '+timeo+'\n'+'time now is '+ttt)

app = Flask(__name__)

@app.route('/')
def red():
    return(redirect('/get-time'))

@app.route("/get-time", methods=['GET'])

def tt():
    return('Bot start at '+timeo+'<br/><br/>'+'time now is '+ttt)


app.run()
