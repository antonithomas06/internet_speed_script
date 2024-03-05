import csv
import os
from datetime import datetime 
import time
import speedtest
import schedule




if os.path.isfile("logfile.csv"):
    print("File already exists")
else:
    print("file does not exists")
    file= open('logfile.csv', 'a', newline="")
    write = csv.writer(file)
    write.writerow(["Datum" ,"Upload_Speed" ,"Download_Speed"])
    file.close()

def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)

st = speedtest.Speedtest()
up = bytes_to_mb(st.upload())
down = bytes_to_mb(st.download())
file= open('logfile.csv', 'a', newline="")
write = csv.writer(file)
write.writerow([datetime.now() , up + "MB" , down + "MB"])
file.close()

# def internet_test():

#     st = speedtest.Speedtest()
#     file= open('logfile.csv','a', newline="")
#     write = csv.writer(file)
#     write.writerow([datetime.now(),st.Upload_Speed(),st.Download_Speed()])
#     file.close()

# # Task scheduling
# # After every 5mins internet_test() is called. 
# schedule.every(5).minutes.do(internet_test)

# while(True):
#     schedule.run_pending()
#     time.sleep(1)

