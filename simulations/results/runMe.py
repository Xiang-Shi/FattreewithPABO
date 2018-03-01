#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import os
import csv
import sys

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
csvfile1='PABO_PkDelayOutsplit.csv'
csvfile2='PABO_RDOutsplit.csv'
csvfile3='PABO_PkDelayOutsplit2.csv'
csvfile4='PABO_RDOutsplit2.csv'
csvfile5='noPABO_PkDelayOutsplit.csv'
csvfile6='noPABO_RDOutsplit.csv'
csvfile7='noPABO_PkDelayOutsplit2.csv'
csvfile8='noPABO_RDOutsplit2.csv'
######  backup sourcefile
os.system('cp '+sourcefile+' '+bkfile)
		

exam_num = 1
######  start loop
######  change A in a loop ...
######  change Threshold in a loop ...
for A in range(50,51,1):
	for Threshold in range(500,1000,50):
	
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

		###############################  PABO  ############################
		######  compile both inet and FattreewithPABO
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/inet')
		os.system('make MODE=debug CONFIGNAME=gcc-debug -j3 all')
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO') 
		os.system('make MODE=debug CONFIGNAME=gcc-debug -j3 all') 

		######  set ini file and run 
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO/simulations')
		os.system('../src/FattreewithPABO -r 0 -u Cmdenv -n ../src:.:../../inet/examples:../../inet/src:../../inet/tutorials -l ../../inet/src/INET omnetpp_manytomany_PABO.ini')
		
		######  saving result data
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO/simulations/results')
		os.system('mkdir Theta_Study')
		
		os.system('scavetool scalar -p \'module(FattreewithPABO.host1.eth[0].encap) AND ("reversePassback:histogram:count")\' -O Theta_Study/reversePassback1.csv -F csv General-0.sca')
		os.system('scavetool scalar -p \'module(FattreewithPABO.host5.eth[0].encap) AND ("reversePassback:histogram:count")\' -O Theta_Study/reversePassback2.csv -F csv General-0.sca')
		os.system('scavetool scalar -p \'module(FattreewithPABO.host13.eth[0].encap) AND ("reversePassback:histogram:count")\' -O Theta_Study/reversePassback3.csv -F csv General-0.sca')
		os.system('scavetool scalar -p \'module(FattreewithPABO.host4.eth[0].encap) AND ("reversePassback:histogram:count")\' -O Theta_Study/reversePassback4.csv -F csv General-0.sca')
		os.system('scavetool scalar -p \'module(FattreewithPABO.host8.eth[0].encap) AND ("reversePassback:histogram:count")\' -O Theta_Study/reversePassback5.csv -F csv General-0.sca')
		os.system('scavetool scalar -p \'module(FattreewithPABO.host16.eth[0].encap) AND ("reversePassback:histogram:count")\' -O Theta_Study/reversePassback6.csv -F csv General-0.sca')
		
		os.system('scavetool vector -p \'module(FattreewithPABO.host9.tcp) AND ("SHI: reordering density")\' -O Theta_Study/PABO_RDOutsplit.csv -F splitcsv General-0.vec')
		os.system('scavetool vector -p \'module(FattreewithPABO.host9.tcp) AND ("SHI: packet delay")\' -O Theta_Study/PABO_PkDelayOutsplit.csv -F splitcsv General-0.vec')
		os.system('scavetool scalar -p \'module(FattreewithPABO.host9.*) AND ("endToEndDelay:histogram:mean")\' -O Theta_Study/PABO_endToEndDelay.csv -F csv General-0.sca')
		os.system('scavetool vector -p \'module(FattreewithPABO.host12.tcp) AND ("SHI: reordering density")\' -O Theta_Study/PABO_RDOutsplit2.csv -F splitcsv General-0.vec')
		os.system('scavetool vector -p \'module(FattreewithPABO.host12.tcp) AND ("SHI: packet delay")\' -O Theta_Study/PABO_PkDelayOutsplit2.csv -F splitcsv General-0.vec')
		os.system('scavetool scalar -p \'module(FattreewithPABO.host12.*) AND ("endToEndDelay:histogram:mean")\' -O Theta_Study/PABO_endToEndDelay2.csv -F csv General-0.sca')
						
		###### please make sure the data files and matlab code file are in '/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO/simulations/results/Theta_Study'
		###### split the dumped outsplit csvfiles into several files : 1_xxx.csv , 2_xxx.csv , 3_xxx.csv ...
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO/simulations/results/Theta_Study')	
		csv_data = csv.reader(open(csvfile1,'r'))
		part = 1
		fcsv = open('%d_'%part+csvfile1,'w+')
		for row in csv_data:
			if row[0] == 'time':
				fcsv.close()
				fcsv = open('%d_'%part+csvfile1,'w+')
				csv_writer = csv.writer(fcsv)
				csv_writer.writerow(row)
				part = part+1
			else:
				csv_writer.writerow(row)
		fcsv.close()

		csv_data = csv.reader(open(csvfile2,'r'))
		part = 1
		fcsv = open('%d_'%part+csvfile2,'w+')
		for row in csv_data:
			if row[0] == 'time':
				fcsv.close()
				fcsv = open('%d_'%part+csvfile2,'w+')
				csv_writer = csv.writer(fcsv)
				csv_writer.writerow(row)
				part = part+1
			else:
				csv_writer.writerow(row)
		fcsv.close()

		csv_data = csv.reader(open(csvfile3,'r'))
		part = 1
		fcsv = open('%d_'%part+csvfile3,'w+')
		for row in csv_data:
			if row[0] == 'time':
				fcsv.close()
				fcsv = open('%d_'%part+csvfile3,'w+')
				csv_writer = csv.writer(fcsv)
				csv_writer.writerow(row)
				part = part+1
			else:
				csv_writer.writerow(row)
		fcsv.close()
		
		csv_data = csv.reader(open(csvfile4,'r'))
		part = 1
		fcsv = open('%d_'%part+csvfile4,'w+')
		for row in csv_data:
			if row[0] == 'time':
				fcsv.close()
				fcsv = open('%d_'%part+csvfile4,'w+')
				csv_writer = csv.writer(fcsv)
				csv_writer.writerow(row)
				part = part+1
			else:
				csv_writer.writerow(row)
		fcsv.close()


		############################### no PABO ############################
		######  compile both inet and FattreewithPABO
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/inet')
		os.system('make MODE=debug CONFIGNAME=gcc-debug -j3 all')
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO') 
		os.system('make MODE=debug CONFIGNAME=gcc-debug -j3 all') 

		###### set ini file and run 
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO/simulations')
		os.system('../src/FattreewithPABO -r 0 -u Cmdenv -n ../src:.:../../inet/examples:../../inet/src:../../inet/tutorials -l ../../inet/src/INET omnetpp_manytomany_noPABO.ini')
		
		######  saving result data
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO/simulations/results')
		os.system('scavetool vector -p \'module(FattreewithPABO.host9.tcp) AND ("SHI: reordering density")\' -O Theta_Study/noPABO_RDOutsplit.csv -F splitcsv General-0.vec')
		os.system('scavetool vector -p \'module(FattreewithPABO.host9.tcp) AND ("SHI: packet delay")\' -O Theta_Study/noPABO_PkDelayOutsplit.csv -F splitcsv General-0.vec')
		os.system('scavetool scalar -p \'module(FattreewithPABO.host9.*) AND ("endToEndDelay:histogram:mean")\' -O Theta_Study/noPABO_endToEndDelay.csv -F csv General-0.sca')
		os.system('scavetool vector -p \'module(FattreewithPABO.host12.tcp) AND ("SHI: reordering density")\' -O Theta_Study/noPABO_RDOutsplit2.csv -F splitcsv General-0.vec')
		os.system('scavetool vector -p \'module(FattreewithPABO.host12.tcp) AND ("SHI: packet delay")\' -O Theta_Study/noPABO_PkDelayOutsplit2.csv -F splitcsv General-0.vec')
		os.system('scavetool scalar -p \'module(FattreewithPABO.host12.*) AND ("endToEndDelay:histogram:mean")\' -O Theta_Study/noPABO_endToEndDelay2.csv -F csv General-0.sca')
		
		###### please make sure the data files and matlab code file are in '/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO/simulations/results/Theta_Study'
		###### split the dumped outsplit csvfiles into several files : 1_xxx.csv , 2_xxx.csv , 3_xxx.csv ...
		os.chdir('/Users/shixiang/Documents/omnetpp-4.6/samples/FattreewithPABO/simulations/results/Theta_Study')	
		csv_data = csv.reader(open(csvfile5,'r'))
		part = 1
		fcsv = open('%d_'%part+csvfile5,'w+')
		for row in csv_data:
			if row[0] == 'time':
				fcsv.close()
				fcsv = open('%d_'%part+csvfile5,'w+')
				csv_writer = csv.writer(fcsv)
				csv_writer.writerow(row)
				part = part+1
			else:
				csv_writer.writerow(row)
		fcsv.close()

		csv_data = csv.reader(open(csvfile6,'r'))
		part = 1
		fcsv = open('%d_'%part+csvfile6,'w+')
		for row in csv_data:
			if row[0] == 'time':
				fcsv.close()
				fcsv = open('%d_'%part+csvfile6,'w+')
				csv_writer = csv.writer(fcsv)
				csv_writer.writerow(row)
				part = part+1
			else:
				csv_writer.writerow(row)
		fcsv.close()

		csv_data = csv.reader(open(csvfile7,'r'))
		part = 1
		fcsv = open('%d_'%part+csvfile7,'w+')
		for row in csv_data:
			if row[0] == 'time':
				fcsv.close()
				fcsv = open('%d_'%part+csvfile7,'w+')
				csv_writer = csv.writer(fcsv)
				csv_writer.writerow(row)
				part = part+1
			else:
				csv_writer.writerow(row)
		fcsv.close()
		
		csv_data = csv.reader(open(csvfile8,'r'))
		part = 1
		fcsv = open('%d_'%part+csvfile8,'w+')
		for row in csv_data:
			if row[0] == 'time':
				fcsv.close()
				fcsv = open('%d_'%part+csvfile8,'w+')
				csv_writer = csv.writer(fcsv)
				csv_writer.writerow(row)
				part = part+1
			else:
				csv_writer.writerow(row)
		fcsv.close()

		###### deal with data using matlab
		###### for example. we need to run test.m, then write "test;quit". Notice: test.m should not contain any gui-relative operations, such as 'plot','bar','figure'.... 
 
                cmd='matlab -nodesktop -nosplash -nojvm -r "thetaStudyDumpResults(%f'%Thresholdf + ',' + '%d,\'finalRecord.csv\','%A+'%d);quit;"'%exam_num
                print(os.path.exists('thetaStudyDumpResults.m'))
                print(sys.argv[0])
                os.system(cmd)
    		exam_num = exam_num+1;