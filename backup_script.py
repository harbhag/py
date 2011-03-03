import os, platform, logging, logging.handlers, glob
from time import *
import tarfile
import zipfile, zlib

class backup:
	source_s = ''
	destination_d = ''
	
	def __init__(self):
		
		if strftime("%p") == 'AM':
			if strftime("%I") in ['12', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']:
				time_d = 'Morning'
			else:
				pass 
		if strftime("%p") == 'PM':
			if strftime("%I") in ['12', '01', '02', '03']:
				time_d = 'Afternoon'
			elif strftime("%I") in ['04', '05', '06', '07', '08']:
				time_d = 'Evening'
			elif strftime("%I") in ['09', '10', '11']:
				time_d = 'Night'
			else:
				pass 
		
		print "Date:",strftime("%d %b %Y")
		print "Hi There, Today is ",strftime("%A")," And time is ", strftime("%I:%M:%S:%P"),  ", So on this beautiful ",strftime("%A"),"", time_d," I welcome you to this Backup program."
		
		
	def source_destination(self):
		w_s = True
		w_ss = True
		while w_s:
			source = raw_input('Please Enter The Complete Path of Source Directory: ')
			if source == '':
				print "***You have not Specified Anything***"
				print "***Source Directory is required in Order to make backup***"
				continue
			elif os.path.exists(source) == False:
				print "***Source Path Does not Exists***"
				print "***Please check source path and Try Again***"
				continue
			else:
				print "***Specified source path is ACCEPTED***"
				w_s = False
				backup.source_s = source
				

 
		while w_ss:
			destination = raw_input('Please Enter Complete Path of Destination Directory:')
			destination = destination.replace(' ','_')
			
			if destination == '':
				print "***You have not Specified Anything***"
				print "***Destination Directory is required to store the backup files***"
		
				continue
			elif os.path.exists(destination) == False:
				print "***Destination Path Does not Exists***"
				decision = raw_input('Do you Want me to Create Destination For you (yes or no or just hit enter for yes):')
				if decision == 'yes':
					print "***Destination Path Will now be created***"
					os.mkdir(destination)
					print "***Directory has been created now***"
					print "***Program will now continue***"
					backup.destination_d = destination
					w_ss = False
				elif decision == 'no':
					print "***As You Wish, because Your wish is my Command***"
					print "***Program will now Terminate***"
					print "Bye !!!"
					exit()
				elif decision == '':
					print "***Destination Path Will now be created***"
					mk_d = 'mkdir {0}'.format(destination)
					os.system(mk_d)
					print "***Directory has been created now***"
					print "***Program will now continue***"
					backup.destination_d = destination
					w_ss = False
				elif decision not in ['yes','no','']:
					print "***What you think you are doing, you just have to choose yes or no, is it that HARD?***"
					print "***Try again now***"
					continue
			elif os.path.exists(destination) == True:
				if os.path.isdir(destination)== False:
					print "***Specified location is a file and not a directory, so try again and enter path of a directory***"
					continue
				else:
					print "***Specified destination path is ACCEPTED***"
					w_ss = False
					backup.destination_d = destination

			else:
				print "***Specified destination path is ACCEPTED***"
				w_ss = False
				backup.destination_d = destination
		
	def compress(self):
		source = backup.source_s
		destination = backup.destination_d
		
		w_sss = True
		f_name = raw_input('Please Enter The Desired name for output file(without extension):')
		
		if f_name == '':
			print "***You have not specified any name so DEFAULT will be used.(i.e 'untitled')***"
			f_name = 'untitled'
		else:
			pass

		while w_sss:
			c_method = raw_input('How you want your backup file to be compressed ?(tar, tar.gz, tar.bz2, or zip):')	
	
			if c_method == 'tar':
				ff_name = f_name.replace(' ', '_') + '.tar'
				w_sss = False
			elif c_method == 'tar.gz':
				ff_name = f_name.replace(' ', '_') + '.tar.gz'
				w_sss = False
			elif c_method == 'tar.bz2':
				ff_name = f_name.replace(' ', '_') + '.tar.bz2'
				w_sss = False
			elif c_method == 'zip':
				ff_name = f_name.replace(' ', '_') + '.zip'
				
				w_sss = False
	
			elif c_method == '':
				print "***You have not selected any method of compression***"
				print "***Please select atleast one method of compression***"
		
				continue
			else:
				print "***Sorry, The method you specified is not supported yet***"
				print "Please choose from the given options i.e tar, tar.gz, tar.bz2 or zip "
		
				continue

		suffix = ("/")
		if source.endswith(suffix) == True:
			pass 
		else:
			source = source + os.sep
		if destination.endswith(suffix) == True:
			pass 
		else:
			destination = destination + os.sep

		values = [source, destination, ff_name]

		if c_method == 'tar':
			print "***Compression can take sometime depending upon method you selected and the size of the source, so please be patient***"
			tar = tarfile.open(destination+ff_name, 'w')
			for item in os.listdir(source):
				print "Adding",item,"to archive"
				tar.add(os.path.join(source,item))
				
			
			tar.close()
			print "Operation successful"
			exit()
		elif c_method == 'tar.gz':
			print "***Compression can take sometime depending upon method you selected and the size of the source, so please be patient***"
			tar = tarfile.open(destination+ff_name, 'w:gz')
			for item in os.listdir(source):
				print "Adding",item,"to archive"
				tar.add(os.path.join(source,item))
				
			
			tar.close()
			print "Operation successful"
			exit()
		elif c_method == 'tar.bz2':
			print "***Compression can take sometime depending upon method you selected and the size of the source, so please be patient***"
			tar = tarfile.open(destination+ff_name, 'w:bz2')
			for item in os.listdir(source):
				print "Adding",item,"to archive"
				tar.add(os.path.join(source,item))
			
			tar.close()
			print "Operation successful"
			exit()
		else:
			print "***Compression can take sometime depending upon method you selected and the size of the source, so please be patient***"
			zipf = zipfile.ZipFile(destination+ff_name,"w", compression=zipfile.ZIP_DEFLATED)
			def recursive_zip(a, b):
				for item in os.listdir(b):
					if os.path.isfile(os.path.join(b, item)):
						print "Adding",item,"to archive"
						a.write(os.path.join(b, item))
					elif os.path.isdir(os.path.join(b, item)):
						recursive_zip(a, os.path.join(b, item))
 
			
			
			recursive_zip(zipf, source)
			zipf.close()
			print "Operation successful"
			exit()


		
		
try:
	p = backup()
	p.source_destination()
	p.compress()
except KeyboardInterrupt:
	print "Why are you leaving me "
	reason = raw_input("1. Your program is not good enough 2. I will be back (1 or 2):")
	if(reason == '1'):
		print "Thanks for using my program, I will try to Improve it, so till then, Good Bye !"
		exit();
	elif(reason == '2'):
		print "OK then, See you Soon"
		exit()
	else:
		print "Invalid Input !!!"
		exit()
		
except EOFError:
	print "Why are you leaving me "
	reason = raw_input("1. Your program is not good enough 2. I will be back (1 or 2):")
	if(reason == '1'):
		print "Thanks for using my program, I will try to Improve it, so till then, Good Bye !"
		exit();
	elif(reason == '2'):
		print "OK then, See you Soon"
		exit()
	else:
		print "Invalid Input !!!"
		exit()
	
