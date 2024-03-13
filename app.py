from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

# Set up GPIO
GPIO.setmode(GPIO.BCM)
LED_PIN = 17  # GPIO pin number where LED is connected
GPIO.setup(LED_PIN, GPIO.OUT)

# Function to turn the LED on
def turn_on_led():
    GPIO.output(LED_PIN, GPIO.HIGH)

# Function to turn the LED off
def turn_off_led():
    GPIO.output(LED_PIN, GPIO.LOW)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/turn_on')
def turn_on():
    turn_on_led()
    return 'LED turned on'

@app.route('/turn_off')
def turn_off():
    turn_off_led()
    return 'LED turned off'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
