import serial
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
    if test_read:
        # return a dictionary of random data for testing
        return {
            "time": datetime.now(),
            "temperature": random.randint(0, 30),
            "turbidity": random.randint(0, 1000) / 1000,
            "dissolved solids": random.randint(0, 3000),
        }
    else:
        ser = serial.Serial(
            "/dev/ttyACM0", 9600
        )  # Establish the connection on a specific port
        ser.flushInput()

        # Read data from the Arduino
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes.decode("utf-8").rstrip()

        # Parse the data and return a dictionary
        values = decoded_bytes.split(",")
        reading = {
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": float(values[0]),
            "turbidity": float(values[1]),
            "dissolved solids": float(values[2]),
        }

        return reading


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
    return [{**data[i], 'colour': colours[i]} for i in range(5)]
