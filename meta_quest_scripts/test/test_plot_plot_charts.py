from plot_charts import vis_matplotlib, draw_scatter
import numpy as np

def get_random_data(size=100):
    temperature_data = np.random.randing(0,100,size=100)
    turbidity_data =  np.random.randing(0,100,size=100)
    dissolved_solids_data = np.random.randing(0,100,size=100)
    red = np.random.randint(0, 255, size=100)
    return temperature_data, turbidity_data, dissolved_solids_data, red

def test_draw_scatter():
    temperature_data, turbidity_data, dissolved_solids_data, red = get_random_data()
    fig = plt.figure(figsize=(12, 8))
    draw_scatter(
        "Temperature",
        "Turbidity",
        "Dissolved Solids",
        temperature_data,
        turbidity_data,
        dissolved_solids_data,
        "m",
        "Temperature vs Turbidity vs Dissolved Solids",
        fig,
        1,
    )
    draw_scatter(
        "Temperature",
        "Turbidity",
        "Red",
        temperature_data,
        turbidity_data,
        red,
        "r",
        "Temperature vs Turbidity vs Red",
        fig,
        2,
    )
