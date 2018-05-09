from flask import *
import sys
import os
import glob
import time
app= Flask(__name__)
globalvidnumber=len(glob.glob("static/*.mp4"))   #two variables to take care of looping part.
globalvideocount=0

#use raspberrypi gpio setup and detection here. callback->bottleinterrupt()
@app.route("/")
def home():    #main homepage where looping takes place
    global globalvideocount
    global globalvidnumber

    #return redirect(url_for('bottleinterrupt'))
    globalvideocount+=1
    if globalvideocount==globalvidnumber:
        globalvideocount=0
    return render_template("home.html",filenameargument=glob.glob("static/*.mp4")[globalvideocount].split("/")[1])
@app.route("/bottleinterrupt")
def bottleinterrupt():    #this gets called whenever bottle is put in
    return render_template("bottle.html")
@app.route("/submit",methods=["GET","POST"])
def submit():
    return render_template("submit.html",mobile=request.args.get('mobile'))
if __name__ == '__main__':
   app.run(host='0.0.0.0')
