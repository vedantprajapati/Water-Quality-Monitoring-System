# Readme

This code is used to monitor the water quality by reading data from an arduino connected to sensors that measure temperature, turbidity, and dissolved solids. The data is then visualized using either Octave or Matplotlib. The user can choose to draw a square in Octave or visualize the data in Matplotlib or octave after logging the data.

## Prerequisites

- Python 3.x
- Matplotlib
- Octave

## Installation

1. Clone the repository
2. Install the required Python modules: `python -m pip install -r requirements.txt`.
3. Install Octave

## Usage

The script can be executed with the following arguments, note: you can only run one of these arguments at a time:

- `-test`: test the script without reading from the arduino.
- `-live`: draw the square in octave.
- `-vo`: draw a visualization of the data in octave.
- `-vm`: draw a visualization of the data in matplotlib.

Example usage: `python monitor.py --live`.

## Functions

The code consists of the following functions:

### `vis_octave()`

This function is used to visualize the data in Octave.

### `vis_matplotlib()`

This function is used to visualize the data in Matplotlib. It reads data from a CSV file, gets the temperature, turbidity, and dissolved solids data and color data from the file, and creates a 3D plot of the data using Matplotlib.

### `draw_octave(temperature, turbidity, dissolved_solids, r, g, b, test_mode=test_mode)`

This function draws a square with color based on average readings in Octave. It takes in six arguments:

- `temperature`: temperature of the water ranging from 0 to 30 degrees C.
- `turbidity`: turbidity of the water ranging from 0 to 1.
- `dissolved_solids`: amount of dissolved solids in the water ranging from 0 to 3000 mg/L.
- `r`: integer from 0 to 255 representing the red value of the color.
- `g`: integer from 0 to 255 representing the green value of the color.
- `b`: integer from 0 to 255 representing the blue value of the color.
- `test_mode`: determines whether to read from the arduino or not.

### `main(test_mode=test_mode, live_mode=live_mode)`

This function is the main function of the script. It runs for 5 minutes and gets the average of the last 5 readings. It then draws a square with color based on the average readings in Octave or visualizes the data in Matplotlib.

### `get_average_readings(test_mode)`

This function gets the average of the last 5 readings from the arduino.

## Running the Code

To run the code, navigate to the directory where the code is located and execute the following command in the terminal: `python monitor.py`.

This will run the script with default settings. To run the script with different settings, use the following command:

`python monitor.py --[MODE]`.

The script will output the number of readings and the number of draws over 5 minutes.

```bash 
#runs the program with the AR HUD enabled. A CSV file named monitor_data.csv will be populated with data
python monitor.py --live 

#runs the program in open brush visualization mode. The data from monitor_data.csv will be plotted in Openbrush
python monitor.py --vo 

#runs the program in matplotlib visualization mode. The data from monitor_data.csv will be plotted in Matplotlib on the connected display
python monitor.py --vm 

#runs the program with imitation values from the arduino
python monitor.py --test 
```

## Testing

To run the test suite, call `python -m pytest` from the meta_quest_scripts directory
