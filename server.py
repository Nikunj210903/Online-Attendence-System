import readandwrite
from flask_socketio import SocketIO
from flask import Flask,render_template,request,redirect,url_for
import json


app = Flask(__name__)
app.config['SECRET_KEY']="hhkjh"
socketio=SocketIO(app)
li=list()


al={"CP":{"year-1":{},"year-3":{"Sem=5":{},"Sem-6":{"C":[],"Java":[]}}},"ME":{"year-1":{},"year-3":{"Sem=5":{},"Sem-6":{"S1":[],"S2":[]}}}}
sub={"CP":{"year-1":{},"year-3":{"Sem=5":{},"Sem-6":{"C":False,"Java":False}}},"ME":{"year-1":{},"year-3":{"Sem=5":{},"Sem-6":{"S1":False,"S2":False}}}}
cur_sub={"CP":{"year-1":{},"year-3":{"Sem-5":{},"Sem-6":{"subject":"C"}}},"ME":{"year-1":{},"year-3":{"Sem=5":{},"Sem-6":{"subject":"S1"}}}}

@app.route('/login' , methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        print("hello")
        username = request.form['uname']
        password = request.form['password']
        if username == "admin" and password == "admin":
            return render_template("after_login.html")  
        else:
            return render_template("login.html")

        
@app.route('/')
def result():
        return render_template('login.html')


@app.route('/store' ,methods = ['POST','GET'])
def store():
    print("worked")
    dic={}
    total={}
    dic['branch'] = request.args.get('branch')
    dic['year'] = request.args.get('year')
    dic['sem'] = request.args.get('sem')
    dic['subject'] = request.args.get('subject')
    dic['date'] = request.args.get('date')
    dic['time'] = request.args.get('time')
    print(dic)
    readandwrite.fun(dic,{'attendence':al[request.args.get('branch')][request.args.get('year')][request.args.get('sem')][request.args.get('subject')]})
    total["total"]=len(al[request.args.get('branch')][request.args.get('year')][request.args.get('sem')][request.args.get('subject')])
    print(total)
    print(len(total))
    al[request.args.get('branch')][request.args.get('year')][request.args.get('sem')][request.args.get('subject')].clear()
    sub[request.args.get('branch')][request.args.get('year')][request.args.get('sem')][request.args.get('subject')]=False
    return render_template('store.html',values=total)

 
@app.route('/attendence',methods=["POST","GET"])
def attendence():
    if request.method=="POST":
        global li
        b=request.args.get('branch')
        y=request.args.get('year')
        s=request.args.get('sem')
        #su=request.args.get('subject')
        su=cur_sub[b][y][s]["subject"]
        id_no=request.args.get('id_no')
        dd=sub[b][y][s]
    
        print("dd..................",dd)
        print(b,y,s,su)
        dic={"branch":b,"year":y,"sem":s,"subject":su}
        if dd[su]:
            
            li=al[b][y][s][su]
            li.append(id_no)
            socketio.emit("update",json.dumps({"to":dic,"id_no":li[-1]}))
            print(li)
        else:
            return "Subject is currently unavailable"
        return "You gave attendence"


@app.route('/after_login',methods = ['POST' , 'GET'])
def after_login():
    if request.method == 'POST':
        dic={}
        print("hello")
        dic['branch'] = request.form['branch']
        dic['year'] = request.form['year']
        dic['sem'] = request.form['sem']
        dic['subject_name'] = request.form['subject']
        dic['date'] = request.form['date']
        dic['time'] = request.form['time']
        dd=sub[request.form['branch']][request.form['year']][request.form['sem']]
        for k,v in dd.items():
            if v==True:
                return render_template("notable.html")
        sub[request.form['branch']][request.form['year']][request.form['sem']][request.form['subject']]=True
        print(dic)
        return render_template("store_into.html",values = dic)


if __name__ == '__main__':
     #socketio.run(app,host="0.0.0.0",debug = True)
    app.run(host="0.0.0.0",debug=True)
#result()
