import serial as ArduinoSerial #import
import time

Arduino = ArduinoSerial.Serial('COM5', '9600')  # setup serial communication

while True: #remove if you want process to only happen once
    prompt = Arduino.readline().decode()  # Read string from port

    #Getting and validating user input
    while True:
        time_input = input(prompt)  #pormpt user for input

        try:
            float(time_input) #check if input is number
        except:
            print("Input invalid, enter again") #if not integer prompt again
            continue
        else:
            Arduino.write(time_input.encode()) #if integer send to arduino (as string)
            time.sleep(0.1) #wait a bit to make sure data gets sent
            break



#Arduino.close() #close serial communication



# time.sleep(0.5)
