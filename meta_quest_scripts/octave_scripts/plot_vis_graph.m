system("sendcom new")

filename = 'monitor_data.csv';
M = csvread(filename);
%mean = mean(M)
% example command
% octave-cli plot_pad.m 1 2 3 255 255 255
%temperature = regexprep(argv(){1}, '[^0-9.]', '')

%temp = num2str(mean(2))
%ds = num2str(mean(3))
%turb = num2str(mean(4))


system(sprintf("sendcom color.set.rgb=""%s,%s,%s"""))
system(sprintf("sendcom brush.move.to=""0,18,12"""))

% system("sendcom color.set.rgb=""0,255,0""")
% system(sprintf("sendcom draw.polygon=""4,10,45"""))
system("sendcom color.set.rgb=""255,255,255""")
system(sprintf("sendcom draw.path=[0,0,0],[0,0,100]"));
system(sprintf("sendcom draw.path=[0,0,0],[0,100,0]"));
system(sprintf("sendcom draw.path=[0,0,0],[100,0,0]"));
for i = 1:rows(M) 
    %system(sprintf("sendcom draw.path=[%s,%s,%s],[%s,%s,%s]", num2str(i), num2str(i), num2str(i), num2str(i) + 0.1, num2str(i) + 0.1, num2str(i) + 0.1));
    system(sprintf("sendcom draw.path=[%s,%s,%s],[%s,%s,%s]", num2str(M(i,2)) *2, num2str(M(i,3))*100, num2str(M(i,4))/100, num2str(M(i,2)) * 3 + 0.1, num2str(M(i,3)) * 100 + 0.1, num2str(M(i,4)) / 100 + 0.1));
    disp(M(i, 2))
endfor

