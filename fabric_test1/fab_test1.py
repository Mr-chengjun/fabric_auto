#!/usr/bin/env python
#_*_coding:utf-8_*_
from fabric_test1.main1 import main1
from fabric.api import execute
from flask import Flask,render_template,request
from fabric_test1.piliang import host_type


app = Flask(__name__)
@app.route('/')
def login():
    return render_template('index.html')
@app.route('/',methods=['POST'])
def lo():
    ml = request.form['ml']
    # result = main1(ml).decode()
    a = execute(host_type,ml)

    return render_template('index.html',result=a.values())

if __name__ == '__main__':
    app.run(debug=True)






