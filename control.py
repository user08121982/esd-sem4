from flask import Flask, render_template
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
    return render_template('index.html',st1=s1,st2=s2,st3=s3)

@app.route("/a")
def d1Tog():
    global s1
    s1=not s1
    # GPIO.output(d1,s1)
    return render_template('index.html',st1=s1,st2=s2,st3=s3)

@app.route("/b")
def d2Tog():
    global s2
    s2=not s2
    # GPIO.output(d2,s2)
    return render_template('index.html',st1=s1,st2=s2,st3=s3)

@app.route("/c")
def d3Tog():
    global s3
    s3=not s3
    # GPIO.output(d3,s3)
    return render_template('index.html',st1=s1,st2=s2,st3=s3)

if __name__=="__main__":
    print("Start")
    app.run(host='192.168.43.189',port=5010)