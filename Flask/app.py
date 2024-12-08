from flask import Flask, render_template, jsonify, make_response, request
import time
import board
from adafruit_motorkit import MotorKit
from picamera2 import Picamera2

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("HomePage.html")

@app.route('/HomePage', methods=['GET'])
def HomePage():
    return render_template("HomePage.html")

@app.route('/ConveyorBelt', methods=['GET'])
def ConveyorBelt():
    return render_template("ConveyorBelt.html")

@app.route('/conveyor_on', methods=["POST"])
def click_button():
    kit = MotorKit(i2c=board.I2C())
    kit.motor1.throttle = -1
    time.sleep(2)
    kit.motor1.throttle = 0
    return "Conveyor activated" 

@app.route('/OctoPrint', methods=["GET"])
def OctoPrint():
    return render_template("OctoPrint.html")

picam2 = Picamera2()
def take_photos():
    picam2.start()
    photo = picam2.capture_file("static/image.jpg")
    picam2.stop()
    return photo

@app.route('/FailureDetection', methods=["GET"])
def FailureDetection():
    response = make_response(take_photos())
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return render_template("FailureDetection.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
