from flask import Flask

app=Flask(__name__)

a=10
b=20

@app.route('/',methods=['GET'])
def welcome():
    return 'i can perform math ops'

@app.route('/add',methods=['GET'])
def addition():
    return f"addition of {a} and {b} is {a+b}"

@app.route('/sub',methods=['GET'])
def subtract():
    return f"subtract of {a} and {b} is {a-b}"

@app.route('/mul',methods=['GET'])
def multiplication():
    return f"multiplication of {a} and {b} is {a*b}"

@app.route('/div',methods=['GET'])
def division():
    return f"division of {a} and {b} is {a/b}"

app.run()