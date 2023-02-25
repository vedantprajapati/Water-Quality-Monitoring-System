import subprocess

x = subprocess.run("ls", capture_output=True,shell=True)
print(x.stdout.decode("utf-8"))

x = subprocess.run("octave-cli octave_scripts/plot_pad.m", capture_output=True,shell=True)
print(x.stdout.decode("utf-8"))