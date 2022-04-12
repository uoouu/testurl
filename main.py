import time,requests


timeo = '7:40'
timenh = time.strftime('%I')
timenh = int(timenh)+3
timenm = time.strftime('%M')
ttt = f'{timenh}:{timenm}'
def  rer():
    gg = requests.post(f"https://api.telegram.org/bot5200214331:AAGBoBxoxS9IQVO24rI0ZK-REvsd_IpnDOo/editmessagetext?chat_id=1110953194&message_id=271&text="'Bot start at '+timeo+'\n'+'time now is '+ttt)
    print(gg.text)
gad = 0
while True:
    time.sleep(1)
    gad +=1
    print("BOT IS RUNNNN")
    if gad == 60:
        rer()
        gad = 0
    else:
        pass

    
