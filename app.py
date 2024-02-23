from flask import Flask, render_template, request
import serial

app = Flask(__name__)
ser = serial.Serial('COM4', 9600, timeout=1)

def send_command(command):
    ser.write(command.encode())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.form.get('input_data')
    # Process the data and return a response
    return 'Received: ' + data

@app.route('/control', methods=['POST'])
def control_led():
    command = request.form['command']
    if command == 'on':
        send_command('1')
        return 'LED turned on'
    elif command == 'off':
        send_command('0')
        return 'LED turned off'
    else:
        return 'Invalid command'

if __name__ == '__main__':
    app.run(debug=True)
