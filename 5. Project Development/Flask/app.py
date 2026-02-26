# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 19:12:30 2026

@author: sujan
"""

from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)    