function thetaStudyDumpResults(Threshold,A,finalfile,num)

serverNumOfOneIncast = 3;  
totalServerNum = 6; 


%=======================check PABO bi-directional passback ====================
total = 0;
for i=1:totalServerNum
    PABO_filename = sprintf('Theta_Study/reversePassback%d.csv',i);
    PABO_data = csvread(PABO_filename,1,4);
    total = total + PABO_data;
end
if (total >0)
    biPassBack = 1;
else
    biPassBack = 0;
end

%======================= average packet delay ========================
PABO_PkDelay1 = 0;
noPABO_PkDelay1 = 0;

for i=1:serverNumOfOneIncast
    PABO_filename = sprintf('Theta_Study/%d_PABO_PkDelayOutsplit.csv',i);
    PABO_data = csvread(PABO_filename,1,1);
    PABO_pkDelay = mean(PABO_data(:));
    PABO_PkDelay1 = PABO_PkDelay1 + PABO_pkDelay;
    
    noPABO_filename = sprintf('Theta_Study/%d_noPABO_PkDelayOutsplit.csv',i);
    noPABO_data = csvread(noPABO_filename,1,1);
    noPABO_pkDelay = mean(noPABO_data(:));
    noPABO_PkDelay1 = noPABO_PkDelay1 + noPABO_pkDelay;

end

PABO_PkDelay2 = 0;
noPABO_PkDelay2 = 0;

for i=1:serverNumOfOneIncast
    PABO_filename = sprintf('Theta_Study/%d_PABO_PkDelayOutsplit2.csv',i);
    PABO_data = csvread(PABO_filename,1,1);
    PABO_pkDelay = mean(PABO_data(:));
    PABO_PkDelay2 = PABO_PkDelay2 + PABO_pkDelay;
    
    noPABO_filename = sprintf('Theta_Study/%d_noPABO_PkDelayOutsplit2.csv',i);
    noPABO_data = csvread(noPABO_filename,1,1);
    noPABO_pkDelay = mean(noPABO_data(:));
    noPABO_PkDelay2 = noPABO_PkDelay2 + noPABO_pkDelay;
end
PABO_avgPkDelay = (PABO_PkDelay1 + PABO_PkDelay2)/totalServerNum;
noPABO_avgPkDelay = (noPABO_PkDelay1 + noPABO_PkDelay2)/totalServerNum;

%=======================PABO: reorder entopy ========================

PABO_ER1 = 0;
noPABO_ER1 = 0;

for i=1:serverNumOfOneIncast
    PABO_filename = sprintf('Theta_Study/%d_PABO_RDOutsplit.csv',i);
    PABO_data = csvread(PABO_filename,1,1);
    PABO_RD = tabulate(PABO_data(:));
    PABO_RD(:,3) = PABO_RD(:,3)/100; 
    PABO_ER = -1*sum(PABO_RD(:,3).*log(PABO_RD(:,3)));
    PABO_ER1 = PABO_ER1 + PABO_ER;
    
    noPABO_filename = sprintf('Theta_Study/%d_noPABO_RDOutsplit.csv',i);
    noPABO_data = csvread(noPABO_filename,1,1);
    noPABO_RD = tabulate(noPABO_data(:));
    noPABO_RD(:,3) = noPABO_RD(:,3)/100; 
    noPABO_ER = -1*sum(noPABO_RD(:,3).*log(noPABO_RD(:,3)));
    noPABO_ER1 = noPABO_ER1 + noPABO_ER;

end

PABO_ER2 = 0;
noPABO_ER2 = 0;

for i=1:serverNumOfOneIncast
    PABO_filename = sprintf('Theta_Study/%d_PABO_RDOutsplit2.csv',i);
    PABO_data = csvread(PABO_filename,1,1);
    PABO_RD = tabulate(PABO_data(:));
    PABO_RD(:,3) = PABO_RD(:,3)/100; 
    PABO_ER = -1*sum(PABO_RD(:,3).*log(PABO_RD(:,3)));
    PABO_ER2 = PABO_ER2 + PABO_ER;
    
    
    noPABO_filename = sprintf('Theta_Study/%d_noPABO_RDOutsplit2.csv',i);
    noPABO_data = csvread(noPABO_filename,1,1);
    noPABO_RD = tabulate(noPABO_data(:));
    noPABO_RD(:,3) = noPABO_RD(:,3)/100; 
    noPABO_ER = -1*sum(noPABO_RD(:,3).*log(noPABO_RD(:,3)));
    noPABO_ER2 = noPABO_ER2 + noPABO_ER;
   
end
PABO_avgER = (PABO_ER1 + PABO_ER2)/totalServerNum;
noPABO_avgER = (noPABO_ER1 + noPABO_ER2)/totalServerNum;


%======================= end to end delay ========================
PABO_endToEndFile1 = 'Theta_Study/PABO_endToEndDelay.csv';
PABO_endtoend_data1 = csvread(PABO_endToEndFile1,1,4);
PABO_EndtoEndDelay1 = mean(PABO_endtoend_data1);

PABO_endToEndFile2 = 'Theta_Study/PABO_endToEndDelay2.csv';
PABO_endtoend_data2 = csvread(PABO_endToEndFile2,1,4);
PABO_EndtoEndDelay2 = mean(PABO_endtoend_data2);

PABO_avgEndtoEndDelay = (PABO_EndtoEndDelay1 + PABO_EndtoEndDelay2)/2;


noPABO_endToEndFile1 = 'Theta_Study/noPABO_endToEndDelay.csv';
noPABO_endtoend_data1 = csvread(noPABO_endToEndFile1,1,4);
noPABO_EndtoEndDelay1 = mean(noPABO_endtoend_data1);

noPABO_endToEndFile2 = 'Theta_Study/noPABO_endToEndDelay2.csv';
noPABO_endtoend_data2 = csvread(noPABO_endToEndFile2,1,4);
noPABO_EndtoEndDelay2 = mean(noPABO_endtoend_data2);

noPABO_avgEndtoEndDelay = (noPABO_EndtoEndDelay1 + noPABO_EndtoEndDelay2)/2;


f = fopen('ThetaStudyResults.txt','a+');
fprintf(f,'%f %d %f %f %f %f %f %f\n',Threshold, A, PABO_avgER, noPABO_avgER, PABO_avgPkDelay, noPABO_avgPkDelay, PABO_avgEndtoEndDelay, noPABO_avgEndtoEndDelay);
fclose(f);
end

