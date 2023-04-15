from flask import Flask, render_template, request
import socket
#import RPi.GPIO as GPIO

app=Flask(__name__)

d1,d2,d3=2,3,4
s1,s2,s3=False,False,False

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(d1,GPIO.OUT)
# GPIO.setup(d2,GPIO.OUT)
# GPIO.setup(d3,GPIO.OUT)
# GPIO.output(d1,0)
# GPIO.output(d2,0)
# GPIO.output(d3,0)
print("Done")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/b1",methods=['GET','POST'])
def d1Tog():
    global s1
    if request.method=='POST':
        s1=not s1
        # GPIO.output(d1,s1)
    return str(s1)

@app.route("/b2",methods=['GET','POST'])
def d2Tog():
    global s2
    if request.method=='POST':
        s2=not s2
        # GPIO.output(d2,s2)
    return str(s2)

@app.route("/b3",methods=['GET','POST'])
def d3Tog():
    global s3
    if request.method=='POST':
        s3=not s3
        # GPIO.output(d3,s3)
    return str(s3)

if __name__=="__main__":
    print("Start")
    app.run(host=socket.gethostbyname(socket.gethostname()),port=5010)