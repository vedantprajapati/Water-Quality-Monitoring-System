system("sendcom new")

% example command
% octave-cli plot_pad.m 1 2 3 255 255 255
temp = argv(){1}
ds = argv(){3}
turb = argv(){2}
system(sprintf("sendcom color.set.rgb=""%s,%s,%s"""))
system("sendcom color.set.rgb=""255,255,255""")
system(sprintf("sendcom brush.move.to=""0,18,12"""))

% system("sendcom color.set.rgb=""0,255,0""")
% system(sprintf("sendcom draw.polygon=""4,10,45"""))
system(sprintf("sendcom draw.text=""Average Readings\n"""))


system(sprintf("sendcom draw.text=""\n \n Temp: %s \n \n DS: %s \n \n Turb:   %s \n \n""",temp,ds,turb))

if (str2num(temp) < 30 && str2num(ds) < 0.5 && str2num(turb) < 3000)
    system("sendcom color.set.rgb=""0,255,0""")
    system(sprintf("sendcom draw.path=[0.5,-0.5,0],[12,-0.5,0]"));
    system(sprintf("sendcom draw.text=""\n \n \n \n \n \n \n \n Status: SAFE"""))
else
    system("sendcom color.set.rgb=""255,0,0""")
    system(sprintf("sendcom draw.path=[0.5,-0.5,0],[12,-0.5,0]"));
    system(sprintf("sendcom draw.text=""\n \n \n \n \n \n \n \n Status: UNSAFE"""))
endif