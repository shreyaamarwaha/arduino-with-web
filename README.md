LED Control Web Application with Flask and Arduino

Description:
This repository contains code for a web application built using Flask and Arduino, allowing users to control an LED remotely via a web interface. The application utilizes Flask, a Python web framework, to create a server-side application that communicates with an Arduino microcontroller connected to an LED.

Components:
Arduino board (such as Arduino Uno)
LED (any color)
Resistor (220 ohms is commonly used for LEDs)
Breadboard
Jumper wires

Instructions:
Connect the long leg (anode) of the LED to digital pin 13 on the Arduino.
Connect one end of the resistor to the short leg (cathode) of the LED.
Connect the other end of the resistor to the GND (ground) pin on the Arduino.
Ensure the Arduino is properly powered via USB or an external power source.

Features:
- Flask Server: The Flask server acts as the backend of the web application, handling HTTP requests from the frontend interface and communicating with the Arduino.
- Arduino Code: The Arduino code listens for incoming commands from the Flask server via serial communication and controls the LED accordingly.
- Web Interface: The web interface provides users with buttons to turn the LED on and off remotely. The interface is styled using HTML, CSS, and JavaScript to enhance user experience and visual appeal.
- Responsive Design: The web application is designed to be responsive and compatible with various devices and screen sizes.


Instructions:
1. Clone the repository to your local machine.
2. Set up the Arduino with the LED connected to a GPIO pin.
3. Install the necessary libraries and dependencies for Flask and Arduino, if required.
4. Run the Flask server locally and ensure that it is listening for incoming requests.
5. Open the web interface in a web browser and use the buttons to control the LED remotely.

This repository serves as a practical example of integrating web technologies with microcontrollers to create IoT applications. It can be used for educational purposes, prototyping projects, or as a basis for developing more complex IoT solutions. Contributions and feedback are welcome to enhance the functionality and usability of the application.

![image](https://github.com/shreyaamarwaha/arduino-with-web/assets/113081204/d8896e28-b852-41a6-a2b9-3fe10a123b9d)

PS: a picture of the circuit has been added for the reference as well:)
