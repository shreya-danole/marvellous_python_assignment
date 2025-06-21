import schedule
import time
from datetime import datetime

def Create_log():
    fobj = open("Marvellous.txt",'w')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    fobj.write(current_time)

def main():
    schedule.every(5).minutes.do(Create_log)
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
