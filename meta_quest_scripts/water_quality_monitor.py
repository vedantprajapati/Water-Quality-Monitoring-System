import read_pi_data as rpd
import time
import subprocess

x = subprocess.run("ls", capture_output=True, shell=True)
print(x.stdout.decode("utf-8"))


def main():
    draw_octave = "octave-cli octave_scripts/plot_pad.m"

    # test the draw_octave function outside the loop
    start_test = time.time()
    test_time = time.time() - start_test
    print(f"draw_octave test time: {test_time:.2f} seconds")
    draw_count = 0
    start_time = time.time()
    while time.time() - start_time < 300:  # run for 5 minutes
        # [{"time":"", "temperature": 0,"turbidity": 0, "dissolved solids": 0}}]
        # sorted by most recent first
        last_5_readings = rpd.read_pi_data()
        average_readings = {
            key: sum([reading[key] for reading in last_5_readings]) / 5
            for key in ["temperature", "turbidity", "dissolved solids"]
        }

        rgb = [0, 0, 0]
        for i in range(5):
            for j, elem in enumerate(last_5_readings[i]["colour"]):
                rgb[j] += int(elem)
        rgb = [elem / 5 for elem in rgb]

        average_readings["colour"] = rgb
        average_readings["time"] = last_5_readings[0]["time"]
        print(average_readings)

        # call bash script to draw square with color based on average_readings in octave underneath the user's feet
        if 5 - (time.time() - start_time) > 0:
            sleep = time.sleep(5 - (time.time() - start_time))
        print(average_readings)

        draw_command = (
            draw_octave
            + f' {int(average_readings["temperature"])} {int(average_readings["turbidity"])} {int(average_readings["dissolved solids"])} {int(average_readings["colour"][0])} {int(average_readings["colour"][1])} {int(average_readings["colour"][2])}'
        )
        print(draw_command)
        ret = subprocess.run(draw_command, capture_output=True, shell=True)
        print("yoooo")
        print(ret.stdout)
        draw_count += 1

    average_draws = draw_count / 300
    print(f"Average number of draws over 5 minutes: {average_draws:.2f}")


main()
