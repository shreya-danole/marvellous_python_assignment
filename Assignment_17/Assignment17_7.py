import schedule
import time

def CreateLog():
    timestamp = time.ctime()

    filename ="backup_log.txt"

    fobj = open(filename,"w")

    Border = "-"*54

    fobj.write(Border+"\n")
    fobj.write("this is log file of marvellous automation script\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("This is created at: \n"+timestamp+"\n")
    fobj.write(Border+"\n")

    
def main():
    schedule.every(1).minutes.do(CreateLog)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
