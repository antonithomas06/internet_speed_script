import csv
import os
from datetime import datetime 
import time
import speedtest
import schedule

month = datetime.now().month
year = datetime.now().year
csv_name = str(year) + "_" + str(month) + "_InetSpeedTests.csv"

def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)


def check_file():
    month = datetime.now().month
    year = datetime.now().year
    global csv_name
    csv_name = str(year) + "_" + str(month) + "_InetSpeedTests.csv"

    if os.path.isfile(csv_name):
        print("File already exists")
    else:
        print("file does not exists")
        file= open(csv_name, 'a', newline="")
        write = csv.writer(file)
        write.writerow(["Upload_Speed" ,"Download_Speed" ,"Datum"])
        file.close()


def internet_test(file):
    print (datetime.now())
    st = speedtest.Speedtest()
    fileo= open(file,'a', newline="")
    write = csv.writer(fileo)
    write.writerow([bytes_to_mb(st.upload()),bytes_to_mb(st.download()),datetime.now(),])
    fileo.close()

# Task scheduling
# After every 5mins internet_test() is called. 
schedule.every(1).minutes.do(check_file)
schedule.every(2).minutes.do(internet_test, csv_name)

# schedule.every().day.at("00:00").do(check_file)

while(True):
    schedule.run_pending()
    time.sleep(1)


