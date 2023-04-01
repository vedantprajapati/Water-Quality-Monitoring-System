from read_pi_data import get_average_readings
import time
import subprocess
import argparse
from plot_charts import vis_matplotlib
from octave_charts import vis_octave, draw_octave
from utils import setup_parser

parser = argparse.ArgumentParser()
setup_parser(parser)

def main(test_mode, live_mode):
    """
    Main function to run the water quality monitor

    Args:
        test_mode (_type_, optional): _description_. Defaults to False.
    """
    draw_count = 0
    start_time, loop_time = time.time(), time.time()

    if parser.parse_args().vo:
        vis_octave()
    elif parser.parse_args().vm:
        vis_matplotlib()
    elif parser.parse_args().testdraw:
        print('hi')
    else:
        while time.time() - start_time < 300:  # run for 5 minutes

            # call bash script to draw square with color based on average_readings in octave underneath the user's feet
            if live_mode and time.time() - loop_time > 5:
                average_readings = get_average_readings(test_mode)
                print(f"draw_iteration {draw_count}")
                print(average_readings)
                draw_octave(
                    temperature=average_readings["temperature"],
                    turbidity=average_readings["turbidity"],
                    dissolved_solids=average_readings["dissolved solids"],
                    r=average_readings["colour"][0],
                    g=average_readings["colour"][1],
                    b=average_readings["colour"][2],
                    test_mode= False,
                )
                draw_count += 1
                loop_time = time.time()
            elif test_mode and time.time() - loop_time > 5:
                print(f"draw_iteration {draw_count}")
                print(average_readings)
                draw_octave(
                    temperature=average_readings["temperature"],
                    turbidity=average_readings["turbidity"],
                    dissolved_solids=average_readings["dissolved solids"],
                    r=average_readings["colour"][0],
                    g=average_readings["colour"][1],
                    b=average_readings["colour"][2],
                    test_mode= True,
                )
                draw_count += 1
                loop_time = time.time()
            elif not test_mode and not live_mode:
                raise Exception("Please specify a mode: --live or --test")

        print(f"Total number of readings over 5 minutes: {draw_count * 5}")
        print(f"Total number of draws over 5 minutes: {draw_count}")



main(parser.parse_args().test,live_mode=parser.parse_args().live)
