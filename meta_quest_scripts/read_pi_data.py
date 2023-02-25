import serial
from datetime import datetime
import numpy as np
import time

# ser = serial.Serial(
#     "/dev/ttyACM0", 9600
# )  # Replace '/dev/ttyACM0' with the port where your Arduino is connected
# ser.flushInput()

def calculate_temperature_rating(temperature):
    # Calculate a rating for the temperature of the water
    # The rating is a number from 0 to 100 representing the quality of the water with 100 being the best
    return 100 * np.exp(-1 * ((temperature - 25) ** 2) / 100)


def calculate_turbidity_rating(turbidity):
    # Calculate a rating for the turbidity of the water
    # The rating is a number from 0 to 100 representing the quality of the water with 100 being the best
    # 0.5 NTU is the maximum amount of turbidity allowed in drinking water
    if turbidity < 0:
        return 0
    return turbidity / 0.5 * 100


def calculate_dissolved_solids_rating(dissolved_solids):
    # Calculate a rating for the dissolved solids of the water
    # The rating is a number from 0 to 100 representing the quality of the water with 100 being the best
    # 1500-2000 mg/L is the maximum amount of dissolved solids allowed in drinking water
    if dissolved_solids < 0:
        return 0
    return dissolved_solids / 2000 * 100


def evaluate_reading(reading):
    # Evaluate a reading and return a dictionary of the evaluation results
    # The dictionary keys are "time", "temperature", "turbidity", and "dissolved solids"

    # TODO: replace with actual code to evaluate the reading and return a color for the quality of the water (gradient from green to red)
    evaluation = 0
    print(reading)
    for key in reading.keys():
        if key == "time":
            continue
        elif key == "temperature":
            evaluation += calculate_temperature_rating(reading[key])
        elif key == "turbidity":
            evaluation += calculate_turbidity_rating(reading[key])
        elif key == "dissolved solids":
            evaluation += calculate_dissolved_solids_rating(reading[key])

    # a number from 0 to 100 representing the quality of the water with 100 being the best
    evaluated_rating = 100

    # generate a color based on the rating
    rgb = [
        int(255 * (1 - evaluated_rating / 100)),
        int(255 * (evaluated_rating / 100)),
        0,
    ]
    print(rgb)
    return rgb

def read_arduino_data():
    # Read data from the Arduino and return a dictionary of the latest readings
    # The dictionary keys are "time", "temperature", "turbidity", and "dissolved solids"

    # Read data from the Arduino
    # ser_bytes = ser.readline()
    # decoded_bytes = ser_bytes.decode("utf-8").rstrip()

    # Parse the data and return a dictionary
    # values = decoded_bytes.split(",")
    # reading = {
    #     "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    #     "temperature": float(values[0]),
    #     "turbidity": float(values[1]),
    #     "dissolved solids": float(values[2]),
    # }

    # return
    
    return {
            "time": datetime.now(),
            "temperature": 0,
            "turbidity": 0.3,
            "dissolved solids": 1500,
        }


def read_pi_data():
    # Read data from the PI server and return a list of dictionaries of the last 5 readings
    # The dictionary keys are "time", "temperature", "turbidity", and "dissolved solids"

    # TODO: replace with actual code to read data from the PI server
    data = []
    for i in range(5):
        data.append(read_arduino_data())
        time.sleep(0.25)
    colours = [evaluate_reading(reading) for reading in data]
    for i in range(5):
        data[i]["colour"] = colours[i]
    return data


