import schedule
import time
from datetime import datetime


def display():
    current_datetime = datetime.now()
    print(current_datetime)

def main():
    schedule.every(1).minutes.do(display)
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
