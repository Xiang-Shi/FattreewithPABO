function PABOParamaterandPacketDelay(Threshold,A,finalfile,num)

queueCapacity = 100;

%======================= average packet delay ========================

filename1 = '1_outsplit.csv';
filename2 = '2_outsplit.csv';
filename3 = '3_outsplit.csv';

data_1 = csvread(filename1,1,1);
data_2 = csvread(filename2,1,1);
data_3 = csvread(filename3,1,1);

pkDelay1 = mean(data_1(:));
pkDelay2 = mean(data_2(:));
pkDelay3 = mean(data_3(:));
%======================= average packet delay ========================

%======================= exclude reverse passback data  ==============
filename4 = 'reversePassback1.csv';
filename5 = 'reversePassback2.csv';
filename6 = 'reversePassback3.csv';

data_4 = csvread(filename4,1,4);
data_5 = csvread(filename5,1,4);
data_6 = csvread(filename6,1,4);

total = data_4 + data_5 + data_6;


if(total ~= 0)   %bidirectional pass back error
    pkDelay = -1;
else
    pkDelay =  (pkDelay1 + pkDelay2 + pkDelay3)/3;
end



f = fopen('finalPKDelayRecord.txt','a+');
fprintf(f,'%f %d %f\n',Threshold,A,pkDelay);
fclose(f);
end