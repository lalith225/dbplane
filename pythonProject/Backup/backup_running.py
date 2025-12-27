#python backup_running.py DEVICE_GROUP EXPORTTYPE EXPORTLOCATION FTP_IP FTPUSER FTPPASSWORD FTP_PORT DRFTP_IP DRFTPUSER DRFTPPASSWORD DRFTP_PORT FTP_LOCATION ZIP SFTP DAILY
# <TYPE 1/RUNNING  2/VERSION  3 VERSION/RUNNING> 172.16.253.13 ftpnoc ftpnoc
# DAILY/WEEKLy

#python backup_running.py NA 3 /opt/ConfigBackup 172.16.253.13 ftpnoc ftpnoc 21 ConfigBackup 1
#python backup_running.py NA 3 /opt/ConfigBackup NA NA ftpnoc 21 ConfigBackup 0

from unmsutil import *
import gzip
import zipfile
import sys
from datetime import datetime, timedelta

error=0
def constructDeviceGroupFilter(filter_name):
	val = ''
	try:
		sql_stmt = "select * from tblfilter_config where name = '%s'"%(filter_name)
		objs = DatabaseServer.executeSQLStatement(sql_stmt)
		if objs and objs != -1:
			actual_request_data = objs[0].get('filterconfigs','')
			val = getNodeFilter(actual_request_data)
	except:pass
	return val
print sys.argv
	
try:device_group = sys.argv[1].strip()
except:device_group = 'NA'
print "Device group %s\n"%device_group

# 1 Running & Startup, 2 Running & Inventory, 3 Running & Startup & Inventory, 4 Startup & Inventory
try:export_type = sys.argv[2].strip()
except:export_type = '3'
print "export_type %s\n"%export_type

try:export_location = sys.argv[3].strip()
except:export_location = "NA"
print "export_location %s\n"%export_location
	
try:ftp_ip = sys.argv[4].strip()
except:ftp_ip = "NA"
print "ftp_ip %s\n"%ftp_ip

try:ftp_user = sys.argv[5].strip()
except:ftp_user = "NA"
print "ftp_user %s\n"%ftp_user
	
try:ftp_password = sys.argv[6].strip()
except:ftp_password = "NA"
# print "ftp_password %s\n"%ftp_password

try:ftp_port = sys.argv[7].strip()
except:ftp_port = 21
print "ftp_port %s\n"%ftp_port

try:drftp_ip = sys.argv[8].strip()
except:drftp_ip = "NA"
print "drftp_ip %s\n"%drftp_ip

try:drftp_user = sys.argv[9].strip()
except:drftp_user = "NA"
print "drftp_user %s\n"%drftp_user
	
try:drftp_password = sys.argv[10].strip()
except:drftp_password = "NA"
# print "drftp_password %s\n"%drftp_password

try:drftp_port = sys.argv[11].strip()
except:drftp_port = 21
print "drftp_port %s\n"%drftp_port

try:ftp_location = sys.argv[12].strip()
except:ftp_location = 'NA'
print "ftp_location %s\n"%ftp_location

try:zip_content = sys.argv[13].strip()
except:zip_content = "1"
print "zip_content %s\n"%zip_content

try:ftp_or_sftp = sys.argv[14].strip()
except:ftp_or_sftp = "FTP"
print "ftp_or_sftp %s\n"%ftp_or_sftp

try:period = sys.argv[15].strip()
except:period = "DAILY"
print "period %s\n"%period

if device_group != 'NA':
	device_group_filter = constructDeviceGroupFilter(device_group)
	if not device_group_filter:
		error = 1
		print "Error in Device Group %s"%device_group
	
date = getLastDay()[0].split(' ')[0]
yesterday_start_time = timeStrTotimeInt(date + " 00:00:00")

if device_group == 'NA':
	sql_stmt = "select n.location, c.nodeid, r.confdataid, c.ipaddress, c.last_success_downloadtime, c.last_success_startup_downloadid, c.last_success_startup_downloadtime from tblNodeInfo n,tblconfmconfig c, tblconfmresult r where n.nodeid = c.nodeid and c.nodeid in (select nodeid from tblnodeinfo where isdeleted = 0) and download_status = 1 and last_success_downloadid = r.id and c.last_success_downloadtime >= %s"%yesterday_start_time
else:
	sql_stmt = "select n.location, c.nodeid, r.confdataid, c.ipaddress, c.last_success_downloadtime, c.last_success_startup_downloadid, c.last_success_startup_downloadtime from tblNodeInfo n, tblconfmconfig c, tblconfmresult r where n.nodeid = c.nodeid and c.nodeid in (%s) and download_status = 1 and last_success_downloadid = r.id and c.last_success_downloadtime >= %s"%(device_group_filter, yesterday_start_time)
print sql_stmt
objs = DatabaseServer.executeSQLStatement(sql_stmt)
if type(objs) != type([]):
	error = 1
	objs = []
print "Number of IPS to export  %s\n"%len(objs)

counter = 0
for obj in objs:
	try:
		counter += 1
		if counter % 500 == 0:
			print "Completed ", counter
		poll_addr = obj["ipaddress"].strip()
		nodeid = obj["nodeid"]
		location = obj["location"].strip().replace('/', '')
		if not location:
			location = "Unknown"
		
		if period == "DAILY":
			date = getLastDay()[0].split(' ')[0]
		else:
			date = getLastDay()[0].split(' ')[0]
			dt = datetime.strptime(date, '%Y-%m-%d')
			start = dt - timedelta(days=dt.weekday())
			end = start + timedelta(days=6)
			date = start.strftime("%Y_%m_%d") + "_" + end.strftime("%Y_%m_%d")

		folder_location = export_location + '/' + date + '/' + location
		ftp_folder_location = ftp_location + '/' + date + '/' + location
		# print "folder_location",folder_location 
		
		if not os.path.exists(folder_location):
			os.makedirs(folder_location)
		if zip_content == "1":
			dump_file = folder_location + '/' + poll_addr + '.zip'
			dump_file_1 = folder_location + '/' + poll_addr + '_configuration.txt'
			dump_file_2 = folder_location + '/' + poll_addr + '_inventory.txt'
			f = zipfile.ZipFile(dump_file, 'w', zipfile.ZIP_DEFLATED)
			t1 = open(dump_file_1, 'w')
			t2 = open(dump_file_2, 'w')
			# print "dump_file",dump_file 
			# f = gzip.open(dump_file , 'wb')
		else:	
			dump_file = folder_location + '/' + poll_addr + '.txt'
			# print "dump_file",dump_file 
			f = open(dump_file , 'w')
		
		#Inventory
		if export_type in ['2','3', '4']:
			sql_stmt = "select component, command from tblnodecomponentinfocli where nodeid = %s"%nodeid
			# sql_stmt = "select component from tblnodecomponentinfocli where command = 'Version' and nodeid = %s"%nodeid
			result_objs = DatabaseServer.executeSQLStatement(sql_stmt)
			# print sql_stmt

			if result_objs and type(result_objs) == type([]):
				for result_obj in result_objs:
					try:
						component = decompressMsg(decryptConfig(result_obj.get('component','')))
					except Exception, msg:
						print "Exception in componenet export : ", msg
						component = ""
					
					if component:
						# f.write("\n\nVersion output:\n\n")
						if zip_content == "1":
							t2.write("\n\n%s output:\n\n"%result_obj.get("command","N/A"))
							t2.write(component)
							t2.write("\n\n")
						else:
							f.write("\n\n%s output:\n\n"%result_obj.get("command","N/A"))
							f.write(component)
							f.write("\n\n")
		# else:
			# print "export_type",export_type

		#Running Configuration
		if export_type in ['1', '2', '3']:
			last_success_downloadtime = obj["last_success_downloadtime"]
			if last_success_downloadtime >= safe_int(time.time()) - (2 * 86400):
				confdataid = obj["confdataid"]
				sql_stmt = "select configdata from tblconfmconfigdata where confdataid = %s"%confdataid
				result_objs = DatabaseServer.executeSQLStatement(sql_stmt)
				if result_objs and type(result_objs) == type([]):
					configdata = decompressMsg(decryptConfig(result_objs[0].get('configdata','')))
					if zip_content == "1":
						t1.write("\n\nRunning Configuration:\n\n")
						t1.write(configdata)
						t1.write("\n\n")
					else:
						f.write("\n\nRunning Configuration:\n\n")
						f.write(configdata)
						f.write("\n\n")
			# else:
				# print "OLD FILE", last_success_downloadtime, safe_int(time.time()) - (2 * 86400)

		#Startup Configuration
		if export_type in ['1', '3', '4']:
			last_success_downloadtime = safe_int(obj["last_success_startup_downloadtime"])
			last_success_startup_downloadid = safe_int(obj["last_success_startup_downloadid"])
			if last_success_startup_downloadid and last_success_downloadtime >= safe_int(time.time()) - (2 * 86400):
				sql_stmt = "select configdata from tblconfmconfigdata d, tblconfmresult r where r.id = %s and d.confdataid = r.confdataid"%last_success_startup_downloadid
				result_objs = DatabaseServer.executeSQLStatement(sql_stmt)
				if result_objs and type(result_objs) == type([]):
					configdata = decompressMsg(decryptConfig(result_objs[0].get('configdata','')))
					if zip_content == "1":
						t1.write("\n\Startup Configuration:\n\n")
						t1.write(configdata)
						t1.write("\n\n")
					else:
						f.write("\n\Startup Configuration:\n\n")
						f.write(configdata)
						f.write("\n\n")

		if zip_content == "1":
			try:t1.close()
			except:pass
			try:t2.close()
			except:pass
			try:f.write(dump_file_1, "%s_configuration.txt"%poll_addr)
			except:pass
			try:f.write(dump_file_2, "%s_inventory.txt"%poll_addr)
			except:pass
		try:f.close()
		except:pass
		if zip_content == "1":
			try:os.system("rm -f %s"%dump_file_1)
			except:pass
			try:os.system("rm -f %s"%dump_file_2)
			except:pass

		if ftp_ip != 'NA' and ftp_user != 'NA':
			if ftp_or_sftp == "SFTP":
				sftpUpload(ftp_ip,  safe_int(ftp_port),  ftp_user, ftp_password, ftp_folder_location, dump_file)
			else:
				ftpUpload(ftp_ip,  safe_int(ftp_port),  ftp_user, ftp_password, ftp_folder_location, dump_file)

		if drftp_ip != 'NA' and drftp_user != 'NA':
			if ftp_or_sftp == "SFTP":
				sftpUpload(drftp_ip,  safe_int(drftp_port),  drftp_user, drftp_password, ftp_folder_location, dump_file)
			else:
				ftpUpload(drftp_ip,  safe_int(drftp_port),  drftp_user, drftp_password, ftp_folder_location, dump_file)
	except Exception, msg:
		print "Exception : ", msg
		try:f.close()
		except:pass

if error == 0:
	print "\nCompleted Successfully"
else:
	print "\nCompleted Error"