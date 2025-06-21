import schedule
import time

def task1():
    print("Lunch Time!")

def task2():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(task1)

    schedule.every().day.at("16:00").do(task2)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
