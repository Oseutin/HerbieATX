import serial
with serial.Serial('/dev/ttyACM0', 9600, timeout=10) as ser:  # open serial port
    while True:
        lightData = open("lightSense.txt", "w")
        lightData.write(ser.readline())
        lightData.close()
        # print(ser.readline())
