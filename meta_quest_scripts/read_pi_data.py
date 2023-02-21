import serial
import datetime

ser = serial.Serial('/dev/ttyACM0', 9600)  # Replace '/dev/ttyACM0' with the port where your Arduino is connected
ser.flushInput()

def read_arduino_data():
    # Read data from the Arduino and return a dictionary of the latest readings
    # The dictionary keys are "time", "temperature", "turbidity", and "dissolved solids"
    
    # Read data from the Arduino
    ser_bytes = ser.readline()
    decoded_bytes = ser_bytes.decode("utf-8").rstrip()
    
    # Parse the data and return a dictionary
    values = decoded_bytes.split(",")
    reading = {
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": float(values[0]),
        "turbidity": float(values[1]),
        "dissolved solids": float(values[2])
    }
    
    return reading

def read_pi_data():
    # Read data from the PI server and return a list of dictionaries of the last 5 readings
    # The dictionary keys are "time", "temperature", "turbidity", and "dissolved solids"

    
    #TODO: replace with actual code to read data from the PI server
    # return [read_arduino_data() for i in range(5)]
    return [{"time":datetime.now(), "temperature": 0,"turbidity": 0, "dissolved solids": 0},
            {"time":datetime.now(), "temperature": 0,"turbidity": 0, "dissolved solids": 0},
            {"time":datetime.now(), "temperature": 0,"turbidity": 0, "dissolved solids": 0},
            {"time":datetime.now(), "temperature": 0,"turbidity": 0, "dissolved solids": 0},
            {"time":datetime.now(), "temperature": 0,"turbidity": 0, "dissolved solids": 0}
            ]

def evaluate_reading(reading):
    # Evaluate a reading and return a dictionary of the evaluation results
    # The dictionary keys are "time", "temperature", "turbidity", and "dissolved solids"
    
    #TODO: replace with actual code to evaluate the reading and return a color for the quality of the water (gradient from green to red)
    
    #a number from 0 to 100 representing the quality of the water with 100 being the best
    evaluated_rating = 100
    
    #generate a color based on the rating
    rgb =  [str(int(255 * (1 - evaluated_rating / 100))), str(int(255 * (evaluated_rating / 100))), "0"]
    return rgb