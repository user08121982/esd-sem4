from flask import Flask, render_template, request
# import RPi.GPIO as GPIO

app=Flask(__name__)

d=(2,3,4)
s=[False]*len(d)

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# for i in range(len(d)):
#     GPIO.setup(d[i],GPIO.OUT)
#     GPIO.output(d[i],0)
print("Done")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<int:b>",methods=['GET','POST'])
def d1Tog(b):
    global s
    if request.method=='POST':
        s[b]=not s[b]
        # GPIO.output(d[b],s[b])I
    return str(s[b])

if __name__=="__main__":
    print("Start")
    app.run(host='192.168.105.203',port=5010)