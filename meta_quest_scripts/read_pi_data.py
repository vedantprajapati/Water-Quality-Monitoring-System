import serial
import csv
import time
import os
from utils import timeit
import random
from datetime import datetime
from evaluate_readings import evaluate_reading

def read_arduino_data(test_read: bool):
    """read data from the arduino

    Args:
        test_read (bool): Determines whether to read from the arduino or not

    Returns:
        _type_: a dictionary of the data read from the arduino
    """
    
    ser = serial.Serial(
            "/dev/ttyACM0", 115200
        )  # Establish the connection on a specific port
        
    if test_read:
        # return a dictionary of random data for testing
        time.sleep(0.3)
        return {
            "time": datetime.now(),
            "temperature": random.randint(0, 30),
            "turbidity": random.randint(0, 1000) / 1000,
            "dissolved solids": random.randint(0, 3000),
        }
    else:
        while (ser.in_waiting <= 0):
            time.sleep(0.03)
        
        ser.flushInput()

        # Read data from the Arduino
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes.decode("utf-8").rstrip()

        # Parse the data and return a dictionary
        values = decoded_bytes.split(",")
        print(values)
        reading = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": float(values[0]),
            "turbidity": float(values[1]),
            "dissolved solids": float(values[2]),
        }

        return reading


def append_to_csv(file_path, data):
    """Append data to a csv file
    
    Args:
        file_path (str): the path to the csv file
        data (list): a list of dictionaries of the data to append
    
    Returns:
        a csv file with the data appended
    """

    if os.path.isfile(file_path) and os.stat(file_path).st_size > 0:
        # File exists and has data, so just append the new rows
        with open(file_path, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writerows(data)
    else:
        # File does not exist or is empty, so write the header row and data
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


def read_pi_data(test_mode):
    """   
    Read data from the PI server and return a list of dictionaries of the last 5 readings
    The dictionary keys are "time", "temperature", "turbidity", and "dissolved solids"

    Args:
        test_mode (_type_): whether to read real data or generate random data for testing

    Returns:
        _type_: a list of dictionaries of the last 5 readings
    """

    data = [read_arduino_data(test_mode) for i in range(5)]
    colours = [evaluate_reading(reading) for reading in data]
    output = [{**data[i], 'colour': colours[i]} for i in range(5)]
    append_to_csv('monitor_data.csv', output)
    return output



def get_average_readings(test_mode):
    """
    get the average of the last 5 readings

    Args:
        test_mode (_type_): Determines whether to read from the arduino or not

    Returns:
        _type_: a dictionary of the average readings
    """
    readings = read_pi_data(test_mode)
    average_readings = {
        key: sum(r[key] for r in readings) / 5
        for key in ["temperature", "turbidity", "dissolved solids"]
    }
    average_rgb = [
        int(sum(int(r["colour"][i]) for r in readings) / 25) for i in range(3)
    ]
    average_readings.update({"colour": average_rgb, "time": readings[0]["time"]})
    return average_readings
