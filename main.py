import time,requests


timeo = '7:40'
timenh = time.strftime('%I')
timenh = int(timenh)+3
timenm = time.strftime('%M')
ttt = f'{timenh}:{timenm}'
gad = 0

def  rer():
    gg = requests.post(f"https://api.telegram.org/bot5200214331:AAGBoBxoxS9IQVO24rI0ZK-REvsd_IpnDOo/editmessagetext?chat_id=1110953194&message_id=271&text="'Bot start at '+timeo+'\n'+'time now is '+ttt)
    print(gg.text)

while True:
    print("BOT IS RUNNNN ")
    rer()

