from flask import Flask
from flask_ask import Ask, question
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launched():
    return question('高さを調節します')

@ask.intent('upIntent')
def up():
    ser.write(b'u')
    return question('高さを高くしました')

@ask.intent('downIntent')
def down():
    ser.write(b'd')
    return question('高さを低くしました')

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
