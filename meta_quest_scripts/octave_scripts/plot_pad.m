system("sendcom new")

% example command
% octave-cli plot_pad.m 1 2 3 255 255 255
temperature = argv(){1}
turbidity = argv(){2}
dissolved_solids = argv(){3}
r = argv(){4}
g = argv(){5}
b = argv(){6}

system(sprintf("sendcom color.set.rgb=""%s,%s,%s""",r,g,b))
system(sprintf("sendcom brush.move.to=""0,18,12"""))

% system("sendcom color.set.rgb=""0,255,0""")
% system(sprintf("sendcom draw.polygon=""4,10,45"""))
system(sprintf("sendcom draw.path=[0,-4,0],[8,-4,0],[8,1,0],[0,1,0],[0,-4,0]"));

system("sendcom color.set.rgb=""255,255,255""")

system(sprintf("sendcom draw.text=""\n Temp: %s \n \n Turb: %s \n DS: %s""",temperature,turbidity,dissolved_solids))
