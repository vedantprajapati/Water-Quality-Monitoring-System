system("sendcom new")

M = dlmread('swim_v10.csv');
len_M = length(M);

%%%%%%%%%%%%%%%%%%%%
% USED TO MOVE THE ENTIRE PLOT AROUND
%%%%%%%%%%%%%%%%%%%%
X_OFFSET=0.5;
Y_OFFSET=1.5;

system("sendcom new");
system("sendcom brush.move.to=0,0,0");
system("sendcom brush.size.set=0.1")
system("sendcom brush.type=Light"); % http://localhost:40074/help/brushes
system("sendcom color.rgb=1.0,0.0,0.5");

% FOR PUTTING THE "DRAWING" INTO CENTER IN MONOSCOPIC MODE
system("sendcom user.move.to=-7,10,10")

for i = 1:len_M
  system(sprintf("sendcom draw.path=[%d,%d,0],[%d,%d,0]",i*0.1+X_OFFSET,M(i)-865,i*0.1+X_OFFSET+0.1, M(i)-865));
end
