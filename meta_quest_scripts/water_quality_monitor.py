import read_pi_data as rpd
import time
import subprocess
import argparse
from utils import timeit

parser = argparse.ArgumentParser()
parser.add_argument(
    "--test",
    help="test the script without reading from the arduino",
    action="store_true",
)
args = parser.parse_args()
test_mode = args.test


@timeit
def draw_octave(temperature, turbidity, dissolved_solids, r, g, b, test_mode=test_mode):
    """_summary_

    Args:
        temperature (_type_): temperature of the water ranging from 0 to 30 degrees C
        turbidity (_type_): turbidity of the water ranging from 0 to 1
        dissolved_solids (_type_): amount of dissolved solids in the water ranging from 0 to 3000 mg/L
        r (_type_): integer from 0 to 255 representing the red value of the color
        g (_type_): integer from 0 to 255 representing the green value of the color
        b (_type_): integer from 0 to 255 representing the blue value of the color
        test_mode (_type_, optional): Defaults to test_mode.
    """
    draw_octave = "octave-cli octave_scripts/plot_pad.m"
    draw_command = (
        draw_octave + f" {temperature} {turbidity} {dissolved_solids} {r} {g} {b}"
    )
    print(f"Command Run: {draw_command}")
    if not test_mode:
        ret = subprocess.run(
            draw_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        print(ret.stdout.decode())
        print(ret.stderr.decode())


def main(test_mode=test_mode):
    """
    Main function to run the water quality monitor

    Args:
        test_mode (_type_, optional): _description_. Defaults to False.
    """
    draw_count = 0
    start_time, loop_time = time.time(), time.time()
    while time.time() - start_time < 300:  # run for 5 minutes
        average_readings = get_average_readings(test_mode)

        # call bash script to draw square with color based on average_readings in octave underneath the user's feet
        if time.time() - loop_time > 5:
            print(f"draw_iteration {draw_count}")
            print(average_readings)
            draw_octave(
                temperature=average_readings["temperature"],
                turbidity=average_readings["turbidity"],
                dissolved_solids=average_readings["dissolved solids"],
                r=average_readings["colour"][0],
                g=average_readings["colour"][1],
                b=average_readings["colour"][2],
                test_mode=test_mode,
            )
            draw_count += 1
            loop_time = time.time()

    print(f"Total number of readings over 5 minutes: {draw_count * 5}")
    print(f"Total number of draws over 5 minutes: {draw_count}")


def get_average_readings(test_mode):
    """
    get the average of the last 5 readings

    Args:
        test_mode (_type_): Determines whether to read from the arduino or not

    Returns:
        _type_: a dictionary of the average readings
    """
    readings = rpd.read_pi_data(test_mode)
    average_readings = {
        key: sum(r[key] for r in readings) / 5
        for key in ["temperature", "turbidity", "dissolved solids"]
    }
    average_rgb = [
        int(sum(int(r["colour"][i]) for r in readings) / 25) for i in range(3)
    ]
    average_readings.update({"colour": average_rgb, "time": readings[0]["time"]})
    return average_readings


main(test_mode)
