import math

def calculate_temperature_rating(temperature):
    """Calculate a rating for the temperature of the water.

    The rating is a number from 0 to 100 representing the quality of the water with 100 being the best.

    Args:
        temperature (float): The temperature of the water, in degrees Celsius.

    Returns:
        float: The temperature rating, from 0 to 100.
    """
    return min(abs(20 * math.exp(-1 * ((temperature - 25) ** 2) / 100)),20)


def calculate_turbidity_rating(turbidity):
    """
    Calculate a rating for the turbidity of the water.

    The rating is a number from 0 to 100 representing the quality of the water with 100 being the best.
    The maximum amount of turbidity allowed in drinking water is 0.5 NTU.

    Args:
        turbidity (float): The turbidity of the water, in NTU.

    Returns:
        float: The turbidity rating, from 0 to 100.
    """
    if turbidity < 0:
        return 0
    return min(abs(turbidity / 0.5 * 40), 40)


def calculate_dissolved_solids_rating(dissolved_solids):
    """
    Calculate a rating for the dissolved solids of the water.

    The rating is a number from 0 to 100 representing the quality of the water with 100 being the best.
    The maximum amount of dissolved solids allowed in drinking water is 1500-2000 mg/L.

    Args:
        dissolved_solids (float): The amount of dissolved solids in the water, in mg/L.

    Returns:
        float: The dissolved solids rating, from 0 to 100.
    """
    if dissolved_solids < 0:
        return 0
    return min(abs(dissolved_solids / 2000 * 40), 40)


def evaluate_reading(reading):
    """    
    Evaluate a reading and return a dictionary of the evaluation results
    The dictionary keys are "time", "temperature", "turbidity", and "dissolved solids"

    Args:
        reading (_type_): a dictionary of the data read from the arduino

    Returns:
        _type_: a dictionary of the evaluation results mapped to an rgb color
    """

    evaluation = 0
    for key in reading.keys():
        if key == "temperature":
            evaluation += calculate_temperature_rating(reading[key])
        elif key == "turbidity":
            evaluation += calculate_turbidity_rating(reading[key])
        elif key == "dissolved solids":
            evaluation += calculate_dissolved_solids_rating(reading[key])
        evaluation=abs(evaluation) 
    # generate a color based on the rating
    rgb = [
        int(255 * (1 - evaluation / 100)),
        int(255 * (evaluation / 100)),
        0,
    ]

    return rgb
