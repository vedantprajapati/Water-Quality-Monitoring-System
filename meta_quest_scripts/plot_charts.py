import matplotlib.pyplot as plt
import numpy as np
import csv
import ast

def draw_scatter(
    x_label, y_label, z_label, x_data, y_data, z_data, colour, title, fig, index
):
    ax = fig.add_subplot(2, 2, index, projection="3d")
    ax.scatter(xs=x_data, ys=y_data, zs=z_data, c=colour)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    ax.set_title(title)


def vis_matplotlib():
    # read the csv file
    try:
        with open("monitor_data.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
    except FileNotFoundError:
        print("File not found")
        return
    
    # get the data
    temperature_data = np.array([float(row["temperature"]) for row in data])
    turbidity_data = np.array([float(row["turbidity"]) for row in data])
    dissolved_solids_data = np.array([float(row["dissolved solids"]) for row in data])
    colour = [ast.literal_eval(row["colour"]) for row in data]
    red = np.array([c[1] / 255 * 100 for c in colour])

    # draw the graphs
    fig = plt.figure(figsize=(12, 8))
    draw_scatter(
        "Temperature (C)",
        "Turbidity (NTU)",
        "Dissolved Solids ppm",
        temperature_data,
        turbidity_data,
        dissolved_solids_data,
        "m",
        "Temperature vs Turbidity vs Dissolved Solids",
        fig,
        1,
    )
    draw_scatter(
        "Temperature (C)",
        "Turbidity (NTU)",
        "Water Safety Rating",
        temperature_data,
        turbidity_data,
        red,
        "r",
        "Temperature vs Turbidity vs Water Safety Rating",
        fig,
        2,
    )
    draw_scatter(
        "Temperature (C)",
        "Dissolved Solids (ppm)",
        "Water Safety Rating",
        temperature_data,
        dissolved_solids_data,
        red,
        "g",
        "Temperature vs Dissolved Solids vs Water Safety Rating",
        fig,
        3,
    )
    draw_scatter(
        "Turbidity (NTU)",
        "Dissolved Solids (ppm)",
        "Water Safety Rating",
        turbidity_data,
        dissolved_solids_data,
        red,
        "b",
        "Turbidity vs Dissolved Solids vs Water Safety Rating",
        fig,
        4,
    )

    plt.tight_layout()
    plt.show()

def vis_octave():
    pass
