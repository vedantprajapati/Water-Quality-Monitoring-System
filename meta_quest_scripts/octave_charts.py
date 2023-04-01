from utils import timeit
import subprocess

@timeit
def draw_octave(temperature, turbidity, dissolved_solids, r, g, b, test_mode):
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

    ret = subprocess.run(
        draw_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    
    # print(ret.stdout.decode())
    # print(ret.stderr.decode())p
    return draw_command

def vis_octave():
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

    draw_octave = "octave-cli octave_scripts/plot_vis_graph.m"
    draw_command = (
        draw_octave
    )
    print(f"Command Run: {draw_command}")
    #if not test_mode:
    ret = subprocess.run(
        draw_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    print(ret.stdout.decode())
    print(ret.stderr.decode())
    return draw_command
