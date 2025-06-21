import schedule
import time

def Check_email():
    print("Checking mail...")

    
def main():
    schedule.every(10).seconds.do(Check_email)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
