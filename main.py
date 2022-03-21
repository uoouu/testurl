from flask import Flask,jsonify,request
import pyshorteners,random

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def index():
    if (request.method == "POST"):
        some_json = request.get_json()
        return jsoify({"you sent":some_json}),201

    else:
        return ('Welcome to Short website API.<br/><br/>Use this link For cut your url => https://meroforshorturl.pythonanywhere.com/url=YOUR URL')

@app.route("/url=<urs>", methods=['GET'])

def get_url(urs):
    url = urs.replace('&','/')
    s = pyshorteners.Shortener()
    no = '123'
    n = random.choice(no)

    if n == '1':
        tt = 0
        for i in range(15):
            tt+=1
            try:
                ur = s.clckru.short(url)
                st_u = True
                break
            except:
                if tt == 15:
                    st_u = False
                    break
                else:
                    pass


    if n == '2':
        tt = 0
        for i in range(15):
            tt+=1
            try:
                ur = s.isgd.short(url)
                st_u = True
                break
            except:
                if tt == 15:
                    st_u = False
                    break
                else:
                    pass


    if n == '3':
        tt = 0
        for i in range(15):
            tt+=1
            try:
                ur = s.tinyurl.short(url)
                st_u = True
                break
            except:
                if tt == 15:
                    st_u = False
                    break
                else:
                    pass
    

    if st_u == True:
        return jsonify({"API FOR":"Tele @ooo1e / insta @uoouu","ShortURL":ur})

    if st_u == False:
        return jsonify({"API FOR":"Tele @ooo1e / insta @uoouu","ShortURL":"Was a problem"})

if __name__ == "__main__":
    app.run(debug=True)