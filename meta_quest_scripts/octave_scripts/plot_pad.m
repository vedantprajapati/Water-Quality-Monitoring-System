system("sendcom new")

% example command
% octave-cli plot_pad.m 1 2 3 255 255 255
temperature = argv(){1}
turbidity = argv(){2}
dissolved_solids = argv(){3}
r = argv(){4}
g = argv(){5}
b = argv(){6}

system(sprintf("sendcom color.set.rgb=""%d,%d,%d""",r,g,b))
system(sprintf("sendcom draw.polygon=""4,0.5,0.0"""))
system("sendcom color.set.rgb=""255,255,255""")
system(sprintf("sendcom draw.text=""Temp: %s, Turb: %s, DS: %s""",temperature,turbidity,dissolved_solids))
