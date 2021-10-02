from flask import Flask,render_template,request
from os import link
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import csv
from itertools import zip_longest
from selenium import webdriver
from selenium.webdriver.common import keys 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from pytube import YouTube
from pytube import Playlist
import datetime 
url = ""




app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download" ,methods=['GET', 'POST'] )
def download():
    if request.method == 'POST':
        url = request.form["address"]
        # typ = request.form["ty"]
        video = YouTube(url)
        mp3 = video.streams.get_audio_only()
        high = video.streams.get_highest_resolution()
        low = video.streams.get_lowest_resolution()
        if request.form["ty"] == "high":
            high.download()
        elif request.form["ty"] == "low":
            low.download()
        elif request.form["ty"] == "mp3":
            mp3.download()
        return render_template("index.html")
    else:
        return render_template("index.html")


@app.route("/clac", methods=['GET', 'POST'])
def clac():
    if request.method == 'POST':
        url = request.form["address"]
        p = Playlist(url)
        t = 0 
        for video in p.videos:
            t += video.length
        convert = datetime.timedelta(seconds=t)
        
        return render_template("result.html",convert=convert)
    else:
        return render_template("index.html")


@app.route('/back',methods=['GET', 'POST'] )
def back():
    if request.method == 'POST':
        return render_template("index.html")
    render_template("index.html")




if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")

