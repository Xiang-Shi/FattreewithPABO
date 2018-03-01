#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import os
import csv

######  the line to be changed for Threshold
line_Threshold_Num=33
######  the line to be changed for A
line_A_Num=34

######  source file
sourcefile='/Users/shixiang/Documents/omnetpp-4.6/samples/inet/src/inet/linklayer/ethernet/switch/MACRelayUnit.cc'
######backup source file
bkfile=sourcefile+'_bk'
######  temporary file
tmpfile='tmp.cpp'
######  csv file
csvfile='outsplit.csv'

######  backup sourcefile
os.system('cp '+sourcefile+' '+bkfile)
		

exam_num = 1
######  start loop
######  change A in a loop 1-50
######  change Threshold in a loop 0, 0.05, ...0.95, 
for A in range(1,25,2):
	for Threshold in range(0,1000,100):
	
		######  for loop must be int
		Thresholdf = Threshold/1000.0

		######  read from sourcefile and write to tmpfile
		fr = open(sourcefile,'r')
		fw = open(tmpfile,'w+')
		lines = fr.readlines()

		counter = 1
		for line in lines:
			if counter == line_A_Num:
				fw.write('#define A %d\n'%A)
			else:
				if counter == line_Threshold_Num:
					fw.write('#define Threshold %f\n'%Thresholdf)  
				else:
					fw.write(line)
			counter = counter+1

		fr.close()
		fw.close()

		######  replace sourcefile
		os.system('cp '+tmpfile+' '+sourcefile)

		######  compile both inet and FattreewithPABO
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/inet')
		os.system('make MODE=debug CONFIGNAME=gcc-debug -j3 all')
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO') 
		os.system('make MODE=debug CONFIGNAME=gcc-debug -j3 all') 

		######  run & saving data
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO/simulations')
		os.system('../src/FattreewithPABO -r 0 -u Cmdenv -n ../src:.:../../inet/examples:../../inet/src:../../inet/tutorials -l ../../inet/src/INET omnetpp.ini')
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO/simulations/results')
		os.system('scavetool vector -p \'module(FattreewithPABO.host9.tcp) AND ("SHI: packet delay")\' -O outsplit.csv -F splitcsv General-0.vec')
		os.system('scavetool scalar -p \'module(FattreewithPABO.host1.eth[0].encap) AND ("reversePassback:histogram:count")\' -O reversePassback1.csv -F csv General-0.sca')
		os.system('scavetool scalar -p \'module(FattreewithPABO.host5.eth[0].encap) AND ("reversePassback:histogram:count")\' -O reversePassback2.csv -F csv General-0.sca')
		os.system('scavetool scalar -p \'module(FattreewithPABO.host13.eth[0].encap) AND ("reversePassback:histogram:count")\' -O reversePassback3.csv -F csv General-0.sca')
		
		
		###### please make sure the data files and matlab code file are in '/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO/simulations/results'
		###### split csvfile into 3 files : 1_xxx.csv , 2_xxx.csv , 3_xxx.csv
		csv_data = csv.reader(open(csvfile,'r'))
		part = 1
		fcsv = open('%d_'%part+csvfile,'w+')
		for row in csv_data:
			if row[0] == 'time':
				fcsv.close()
				fcsv = open('%d_'%part+csvfile,'w+')
				csv_writer = csv.writer(fcsv)
				csv_writer.writerow(row)
				part = part+1
			else:
				csv_writer.writerow(row)
		fcsv.close()

		###### deal with data using matlab
		###### for example. we need to run test.m, then write "test;quit". Notice: test.m should not contain any gui-relative operations, such as 'plot','bar','figure'.... 
 
        	cmd='matlab -nodesktop -nosplash -nojvm -r "PABOParamaterandPacketDelay(%f'%Thresholdf + ',' + '%d,\'finalRecord.csv\','%A+'%d);quit;"'%exam_num
        	os.system(cmd)
    		exam_num = exam_num+1;