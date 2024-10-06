from flask import Flask, request,render_template,redirect
from db import db
app=Flask(__name__)


@app.route('/')
def index():
    return redirect('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        user=db.get(username)
        if user and password ==user['password']:
            return render_template('profile.html',name=user['name'])
        else:
            return render_template('login.html',error_msg='invalid username or password')    

    else:
        return render_template('login.html')