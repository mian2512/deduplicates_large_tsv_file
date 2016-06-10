"""
This script removes duplicate rows in a large csv file 

Created 06.10.2016 by Paul Sirma 
"""


#Necessary packages to run this script 
import csv
import os.path, sys
import zipfile , pprint 

path = 'C:\Users\psirma\Desktop\HM'.replace('\\' , '/')  #path to the data

file = zipfile.ZipFile(path + "/patent_data_FS_with_cats.zip", "r")   #loading the Zipfile
#Getting the file names in file
file_name = ''
for name in file.namelist():
	file_name = name
print file_name


outp = csv.writer(open(path+'/final_unique_output.csv','wb'))  #final output file
f = file.open(file_name)


seen = set() # Creating a varioable seen which is a set to missing for now. 
#The loop below populate the variable seen with a set of unique rows in the file "patent_data_FS_with_cats"
for line in f :  #read line by line to save memory 
 	data = ''
	if line in seen: #check if the curernt line we are reading is in seen. 
		#print "Warning! we have a duplciates"
		continue  #if the line is in seen ==> we have a duplicates, skip that line
	else:  #if the line is not in variable seen 
		seen.add(line) #we first add the line to variable seen 
		data = line.split('\t')
		print line
	outp.writerow(data) #then write the unique line into our output file  "final_unique_output"

print "****** The End ********"		