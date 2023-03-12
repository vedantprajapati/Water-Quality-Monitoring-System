from ..evaluate_readings import evaluate_reading
import random
import datetime

def get_random_reading():
        return {
            "time": datetime.now(),
            "temperature": random.randint(0, 30),
            "turbidity": random.randint(0, 1000) / 1000,
            "dissolved solids": random.randint(0, 3000),
        }

def test_evaluate_reading():
    readings = [get_random_reading() for _ in range(10)]
    evaluation = [evaluate_reading(reading) for reading in readings]
    assert all([type(evaluate_reading(reading)) == list for reading in readings])
    assert all([all([0 <= color <= 255 for color in rgb]) for rgb in evaluation])
    assert all([len(rgb) == 3 for rgb in evaluation])
    