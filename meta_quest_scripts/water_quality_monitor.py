import read_pi_data as rpd
import time
import subprocess

def main():
    cd_octave = "cd ./meta_quest_scripts/octave_scripts"
    draw_octave = "octave-cli plot_pad.m"

    # test the draw_octave function outside the loop
    start_test = time.time()
    subprocess.run(draw_octave, capture_output=True, shell=True)
    test_time = time.time() - start_test
    print(f"draw_octave test time: {test_time:.2f} seconds")

    draw_count = 0
    start_time = time.time()
    while time.time() - start_time < 300:  # run for 5 minutes
        #[{"time":"", "temperature": 0,"turbidity": 0, "dissolved solids": 0}}]
        #sorted by most recent first
        last_5_readings = rpd.read_pi_data()
        average_readings = {key: sum([reading[key] for reading in last_5_readings])/5 for key in last_5_readings[0].keys()}
        average_readings["time"] = last_5_readings[0]["time"]
        
        #call bash script to draw square with color based on average_readings in octave underneath the user's feet
        if 5 - (time.time() - start_time) > 0:
            sleep = time.sleep(5 - (time.time() - start_time))
        ret = subprocess.run(draw_octave, capture_output=True, shell=True)
        draw_count += 1
    
    average_draws = draw_count / 300
    print(f"Average number of draws over 5 minutes: {average_draws:.2f}")

main()