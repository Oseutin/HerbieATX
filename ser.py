# Currently unused by HerbieATX due to Jetson's inability to process serial data from Arduino-based sensors in real-time
# Created by Austin Fang and Amulya Bhattaram

import serial
with serial.Serial('/dev/ttyACM0', 9600, timeout=10) as ser:  # open serial port
    while True:
        light_data = open("lightSense.txt", "w")
        decoded_string = ser.readline().decode("utf-8")
        light_data.write(decoded_string)
        light_data.close()
        # print(ser.readline())
