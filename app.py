import re
from flask import Flask,render_template
import speech_recognition as sr
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")
