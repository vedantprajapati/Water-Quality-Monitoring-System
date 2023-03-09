import read_pi_data as rpd
import time
import subprocess
import argparse
from utils import timeit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.tri import Triangulation
import csv
import ast

parser = argparse.ArgumentParser()
parser.add_argument(
    "--test",
    help="test the script without reading from the arduino",
    action="store_true",
)
parser.add_argument(
    "--live",
    help="draw the square in octave",
    action="store_true",
)
parser.add_argument(
    "--vo",
    help="draw a visualization of the data in octave",
    action="store_true",
)
parser.add_argument(
    "--vm",
    help="draw a visualization of the data in matplotlib",
    action="store_true",
)

args = parser.parse_args()
test_mode = args.test
live_mode = args.live
visualize_octave = args.vo
visualize_matplotlib = args.vm

def vis_octave():
    pass
def vis_matplotlib():
    #read the csv file
    try:
        with open('monitor_data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
    except FileNotFoundError:
        print('File not found')
        return
    #get the data
    print(reader)
    temperature = [float(row['temperature']) for row in data]
    turbidity = [float(row['turbidity']) for row in data]
    dissolved_solids = [float(row['dissolved solids']) for row in data]
    
    colour = [ast.literal_eval(row['colour']) for row in data]

    # Create a triangulation of the data points
    tri = Triangulation(temperature, turbidity)

    # Create a 3D figure and axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Normalize the color values
    normalized_colors = [[c[0]/255, c[1]/255, c[2]/255] for c in colour]
    # Flatten the color values
    flat_colors = [c for sublist in normalized_colors for c in sublist]

    # Plot the surface
    surf = ax.plot_trisurf(temperature, turbidity, dissolved_solids, triangles=tri.triangles, cmap='coolwarm')
    surf.set_array(flat_colors)
    # Set labels for the axes
    ax.set_xlabel('Temperature')
    ax.set_ylabel('Turbidity')
    ax.set_zlabel('Dissolved Solids')

    # Add a color bar
    fig.colorbar(surf).set_label('cleanliness')
    

    # Show the plot
    plt.show()
    print("Done")


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


def main(test_mode=test_mode, live_mode=live_mode):
    """
    Main function to run the water quality monitor

    Args:
        test_mode (_type_, optional): _description_. Defaults to False.
    """
    draw_count = 0
    start_time, loop_time = time.time(), time.time()
    
    if visualize_octave:
        vis_octave()
    elif visualize_matplotlib:
        vis_matplotlib()
    else:       
        while time.time() - start_time < 300:  # run for 5 minutes
            average_readings = get_average_readings(test_mode)

            # call bash script to draw square with color based on average_readings in octave underneath the user's feet
            if live_mode and time.time() - loop_time > 5:
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
